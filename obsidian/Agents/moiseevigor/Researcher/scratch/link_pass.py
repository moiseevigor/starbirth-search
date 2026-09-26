"""Make cites <-> cited_by symmetric (extends/replicates/contradicts imply cites). Usage: link_pass.py [--write]"""
import sys, re
from vaultlib import *

P = papers()
data = {n: load(f) for n, f in P.items()}
edges = set()  # (citing, cited)
for n, (t, d) in data.items():
    for fld in ('cites', 'extends', 'replicates', 'contradicts'):
        edges |= {(n, b) for b in names(d.get(fld))}
    edges |= {(a, n) for a in names(d.get('cited_by'))}
    for lab, rev in (('Cites', False), ('Cited by (in this vault)', True)):
        m = related_line(t, lab)
        if m:
            for x in WL.findall(m.group(0)):
                edges.add((x, n) if rev else (n, x))
unknown = {x for e in edges for x in e if x not in P}
if unknown: print('UNKNOWN targets (skipped):', unknown)
edges = {e for e in edges if e[0] in P and e[1] in P and e[0] != e[1]}

added = 0; log = []
for n, (t, d) in data.items():
    cites = names(d.get('cites')); cb = names(d.get('cited_by'))
    nc = [b for a, b in sorted(edges) if a == n and b not in cites]
    ncb = [a for a, b in sorted(edges) if b == n and a not in cb]
    if not (nc or ncb): continue
    added += len(nc) + len(ncb)
    log.append(f'{n}: cites +{nc} cited_by +{ncb}')
    if nc: t = set_fm_list(t, 'cites', cites + nc)
    if ncb: t = set_fm_list(t, 'cited_by', cb + ncb)
    t, miss1 = add_to_related(t, 'Cites', nc)
    t, miss2 = add_to_related(t, 'Cited by (in this vault)', ncb)
    if miss1 or miss2: print('WARN no Related line in', n)
    if '--write' in sys.argv: open(P[n], 'w').write(t)
print('\n'.join(log)); print('links added:', added)
# verify
for n, f in P.items():
    load(f)
