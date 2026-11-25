"""Recompute registered numerical claims and their source evidence, offline."""
import argparse
import hashlib
from collections import Counter
import json
from pathlib import Path
import sys

import pandas as pd

try:
    from .analyze import HERE, ROOT, OUTPUT, run, write_json
    from .claim_engine import load_registry, evaluate
    from .reporting import reporting_findings
except ImportError:
    from analyze import HERE, ROOT, OUTPUT, run, write_json
    from claim_engine import load_registry, evaluate
    from reporting import reporting_findings


def verify(output=OUTPUT, registry=HERE/'claims.json', claim_id=None):
    tables,audit=run(output)
    audit['claim_registry']={'filename':str(registry),'sha256':hashlib.sha256(registry.read_bytes()).hexdigest()}
    write_json(output/'source-reconciliation.json',audit)
    claims=load_registry(registry)
    if claim_id:
        claims=[c for c in claims if c['id']==claim_id]
        if not claims:
            raise ValueError(f'Unknown claim: {claim_id}')
    (output/'evidence').mkdir(exist_ok=True)
    results=[]
    for claim in claims:
        source_ok=audit['reconciliation_status']=='PASS'
        validation=json.loads((ROOT/'cleaned/2026/general/validation.json').read_text())
        if 2026 in claim['years'] and (validation['missing_exports'] or validation['download_failures'] or not validation['precinct_coverage_complete']):
            source_ok=False
        result,evidence,selected,denominator=evaluate(claim,tables,source_ok)
        write_json(output/result['evidence_file'],evidence)
        results.append(result)
        if claim_id:
            print(json.dumps(result,indent=2,default=str))
            print('\nUnderlying calculation rows (full vote counts and identifiers):')
            print(selected.to_csv(index=False))
            print('\nEligible denominator rows:')
            cols=[c for c in ['race','county','precinct','precinct_2024','precinct_2026','match_status','geographically_verified','total_votes','total_votes_2024','total_votes_2026'] if c in denominator]
            print(denominator[cols].to_csv(index=False) if cols else denominator.to_csv(index=False))
            print('\nMatch coverage:')
            print(tables['match-coverage'][tables['match-coverage'].race.eq(claim['race'])].to_csv(index=False))
    if claim_id:
        # Keep the complete report intact when inspecting one claim.
        write_json(output/f'{claim_id}.json',results[0])
    else:
        write_json(output/'story-claims.json',{'claims':results,'status_counts':dict(Counter(r['verification_status'] for r in results))})
        flattened=[]
        for r in results:
            flattened.append({k:json.dumps(v,ensure_ascii=False) if isinstance(v,(dict,list)) else v for k,v in r.items()})
        pd.DataFrame(flattened).to_csv(output/'story-claims.csv',index=False)
        lines=['# Story fact-check', '', 'PASS verifies arithmetic in the retained snapshot. It does not certify final results.',
               'The 2026 headers report 727/728 precincts, one partial; write-ins are excluded. 2024 retained headers also say unofficial.',
               'Claims without expected values are recomputed calculations, not comparisons against a draft assertion.',
               'Differences report after and before operands; their numerator/denominator fields are not a vote ratio.',
               '', 'Status totals: '+json.dumps(dict(Counter(r['verification_status'] for r in results))), '']
        for r in results:
            lines += [f"## {r['id']}: {r['verification_status']}", '',r['description'],'',
                      f"Expected: {r.get('expected_value')} | Calculated: {r['calculated_value']} | Display: {r['display_value']}",
                      f"Numerator / after operand: {r['numerator']} | Denominator / before operand: {r['denominator']} ({r['denominator_meaning']})",'',
                      f"Calculation: `{r['calculation']}`",'',f"Sources: {', '.join(r['source_files'])}",
                      f"Evidence: [{r['evidence_file']}]({r['evidence_file']})",'', 'Caveats: '+' '.join(r['caveats']), '']
        (output/'story-fact-check.md').write_text('\n'.join(lines))
        (output/'reporting-findings.md').write_text(reporting_findings(results,tables,audit))
        inventory=['# Generated files','', 'CSV sorting is deterministic: source-records follow source file order (2024, then 2026). Other groups sort by race/year/county/precinct; county tables follow race/county; candidate columns preserve source names. Rankings sort ascending Republican share change, then county and 2024 precinct. Claims follow registry order. Crosswalks include unpaired rows.','',
                   'Fractions use `_share`, margins use `_margin`, percentage-point changes use `_change_pp`; no CSV share or margin values are display-rounded. `winning_margin_pp` is winner minus runner-up as a share of all candidate votes, multiplied by 100. `votes__NAME` and `share__NAME` identify candidates exactly. Source keys and election labels are retained in source-records.csv and precinct-results.csv.','',
                   'The audit transition matrix contains unverified and changed-boundary proposed pairs; only the explicitly labeled verified sample is geography-checked. Provisional means the original normalized-name sample (including its independently reviewed subset). Independently verified renames can lie outside that sample.','']
        for path in sorted(output.glob('*')):
            if path.is_file():
                inventory.append(f'- [{path.name}]({path.name})')
        (output/'README.md').write_text('\n'.join(inventory)+'\n')
    print('Claim statuses:',dict(Counter(r['verification_status'] for r in results)))
    print('Source reconciliation:',audit['reconciliation_status'],f"({len(audit['checks'])} candidate/geography checks)")
    print('Reports:',output)
    return results


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--claim',help='Stable claim ID; prints underlying records and coverage')
    parser.add_argument('--registry',type=Path,default=HERE/'claims.json')
    parser.add_argument('--output',type=Path,default=OUTPUT)
    args=parser.parse_args()
    try:
        results=verify(args.output,args.registry,args.claim)
    except (ValueError,KeyError) as error:
        parser.exit(2,str(error)+'\n')
    sys.exit(1 if any(r['verification_status'] in ['FAIL','SOURCE_INCOMPLETE'] for r in results) else 0)
