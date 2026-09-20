from pathlib import Path
import hashlib, sys
root=Path(__file__).resolve().parents[1]
web=root/'web'
assets=root/'android/app/src/main/assets/www'
ignore={'README.md','CHANGELOG.md','VALIDATION.md','SOURCE_MAPPING.md','DATA_DICTIONARY.md','PAGE4_FAILURE_WORKFLOW.md'}
def files(base):
    return sorted(p.relative_to(base) for p in base.rglob('*') if p.is_file() and 'tests' not in p.parts and p.name not in ignore)
def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()
wf=files(web); af=files(assets)
if wf!=af:
    print('SYNC FAIL: file lists differ')
    print('web only:',sorted(set(wf)-set(af)))
    print('android only:',sorted(set(af)-set(wf)))
    sys.exit(1)
for rel in wf:
    if digest(web/rel)!=digest(assets/rel):
        print('SYNC FAIL:',rel)
        sys.exit(1)
print(f'SYNC PASS: {len(wf)} runtime file(s) are byte-identical between web and Android assets.')
