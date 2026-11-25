"""Declarative numerical checks. No eval, prose interpretation, or stored results."""
from decimal import Decimal, localcontext
import math

import pandas as pd

try:
    from .core import display
except ImportError:
    from core import display


def select(frame, filters):
    mask = pd.Series(True,index=frame.index)
    operators = {'eq':lambda a,b:a.eq(b),'ne':lambda a,b:a.ne(b),
                 'gt':lambda a,b:a.gt(b),'lt':lambda a,b:a.lt(b),
                 'ge':lambda a,b:a.ge(b),'le':lambda a,b:a.le(b),
                 'in':lambda a,b:a.isin(b)}
    for rule in filters:
        column=rule['column']
        other=frame[rule['right_column']] if 'right_column' in rule else rule.get('value')
        mask &= operators[rule.get('op','eq')](frame[column],other).fillna(False)
    return frame[mask]


def expected_matches(value, claim):
    expected=claim.get('expected_value')
    if expected is None:
        return None
    if value is None:
        return False
    if claim.get('expected_rounding') is not None:
        return display(value,claim['expected_rounding']) == display(expected,claim['expected_rounding'])
    return abs(Decimal(str(value))-Decimal(str(expected))) <= Decimal(str(claim.get('absolute_tolerance',0)))


def evaluate(claim, tables, source_ok=True):
    frame=tables[claim['table']]
    selected=select(frame,claim.get('filters',[]))
    denominator_rows=select(frame,claim.get('denominator_filters',claim.get('filters',[])))
    operation=claim['operation']
    scale=claim.get('scale',1)
    numerator=denominator=None
    value=None
    if operation=='count':
        if not selected.index.isin(denominator_rows.index).all():
            raise ValueError('Count numerator must be a subset of denominator')
        numerator=len(selected);denominator=len(denominator_rows);value=numerator
    elif operation=='sum':
        numerator=selected[claim['column']].sum(min_count=1) if len(selected) else None
        denominator=selected[claim['denominator_column']].sum(min_count=1) if claim.get('denominator_column') and len(selected) else len(denominator_rows)
        value=numerator*scale if numerator is not None else None
    elif operation=='minimum':
        numerator=selected[claim['column']].min() if len(selected) else None
        denominator=len(denominator_rows)
        value=numerator*scale if numerator is not None else None
    elif operation=='ratio':
        numerator=selected[claim['numerator_column']].sum(min_count=1)
        denominator=selected[claim['denominator_column']].sum(min_count=1)
        value=numerator/denominator*scale if denominator else None
    elif operation=='difference':
        if len(selected)!=1:
            raise ValueError(f"{claim['id']}: difference requires exactly one row")
        row=selected.iloc[0]
        numerator=row[claim['after_column']];denominator=row[claim['before_column']]
        value=(numerator-denominator)*scale
    else:
        raise ValueError(f'Unknown operation {operation}')
    clean=lambda x: None if x is None or pd.isna(x) else x.item() if hasattr(x,'item') else x
    value,numerator,denominator=map(clean,(value,numerator,denominator))
    if value is not None and not math.isfinite(value):
        value=None
    exact_value = value
    if operation=='ratio' and value is not None:
        with localcontext() as context:
            context.prec=50
            exact_value=Decimal(str(numerator))/Decimal(str(denominator))*Decimal(str(scale))
    matches=expected_matches(exact_value,claim)
    # A mismatch is visible even if geography/source also needs review.
    status='PASS'
    if value is None or (claim.get('sample')=='verified' and len(denominator_rows)==0):
        status='NOT_COMPARABLE'
    comparison_table = {'status_2024','status_2026','geographically_verified'}.issubset(frame.columns)
    geography_pending = comparison_table and len(selected)>0 and not selected.geographically_verified.all()
    if claim.get('sample')=='verified' and geography_pending:
        raise ValueError(f"{claim['id']}: verified claim includes unverified selected records")
    if claim.get('sample')=='provisional' or geography_pending:
        status='NEEDS_GEOGRAPHIC_REVIEW'
    if not source_ok or claim.get('requires_final_results',False):
        status='SOURCE_INCOMPLETE'
    if matches is False:
        status='FAIL'
    result=dict(claim,calculated_value=value,numerator=numerator,denominator=denominator,
                denominator_meaning='before value' if operation=='difference' else claim.get('denominator_meaning','eligible rows or contest votes'),
                display_value=display(exact_value,claim.get('display_rounding',1)),
                rounding_verified=display(value,claim.get('display_rounding',1))==display(exact_value,claim.get('display_rounding',1)),
                exact_ratio_decimal=str(exact_value) if operation=='ratio' else None,expected_matches=matches,
                verification_status=status,evidence_file=f"evidence/{claim['id']}.json")
    evidence=dict(table=claim['table']+'.csv',selected_csv_rows=[int(i)+2 for i in selected.index],
                  denominator_csv_rows=[int(i)+2 for i in denominator_rows.index],
                  source_files=claim['source_files'],calculation=claim['calculation'],
                  note='CSV row numbers include header; open the derived rows and follow source keys to source-records.csv, which retains original source_file/source_row. Shares are calculated from unrounded counts.')
    return result,evidence,selected,denominator_rows


def load_registry(path):
    import json
    claims=json.loads(path.read_text())['claims']
    ids=[c['id'] for c in claims]
    if len(ids)!=len(set(ids)):
        raise ValueError('Duplicate claim IDs')
    required={'id','description','years','race','geographic_scope','candidate_or_party','calculation','source_files','display_rounding','caveats','table','operation'}
    for c in claims:
        if required-set(c):
            raise ValueError(f"{c.get('id')}: missing {sorted(required-set(c))}")
    return claims
