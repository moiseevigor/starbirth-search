"""Verify: YAML parses, cites/cited_by symmetric, hub appears_in == key_concepts back-links, all wikilinks resolve."""
import glob, os
from vaultlib import *

P = papers()
H = {os.path.basename(f)[:-3]: f for f in glob.glob(f'{VAULT}/Concepts/*.md')}
allnotes = {os.path.basename(f)[:-3] for f in glob.glob(f'{VAULT}/**/*.md', recursive=True)}
bad = 0
D = {n: load(f)[1] for n, f in {**P, **H}.items()}
for a, d in ((n, D[n]) for n in P):
    for b in names(d.get('cites')):
        if a not in names(D[b].get('cited_by')): print('asym', a, '->', b); bad += 1
    for b in names(d.get('cited_by')):
        if b not in names(D[a].get('cites')) and a not in names(D[b].get('cites')): print('asym cb', a, b); bad += 1
    for c in names(d.get('key_concepts')):
        if c not in H: print('missing hub', c); bad += 1
back = {}
for n in P:
    for c in names(D[n].get('key_concepts')): back.setdefault(c, set()).add(n)
for h in H:
    if set(names(D[h].get('appears_in'))) != back.get(h, set()): print('appears_in mismatch', h); bad += 1
for f in [*P.values(), *H.values()]:
    for l in set(WL.findall(open(f).read())):
        if l.strip() not in allnotes: print('dangling', os.path.basename(f), l); bad += 1
print('notes', len(P), 'hubs', len(H), 'problems', bad)
