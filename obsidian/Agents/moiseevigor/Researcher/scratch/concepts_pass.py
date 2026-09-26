"""Add new concept hubs to key_concepts (+ Related 'Concepts' bullet) and print concept -> appears_in map.
Usage: concepts_pass.py [--write]"""
import sys
from vaultlib import *

ADD = {
 'bolometric-temperature': ['masunaga-inutsuka-2000', 'evans-2009', 'dunham-2008', 'dunham-2014', 'furlan-2016', 'stutz-2013', 'pineda-2011'],
 'accretion-luminosity': ['larson-1969', 'masunaga-inutsuka-2000', 'bhandare-2020', 'dunham-2008', 'dunham-2014', 'evans-2009', 'pineda-2011', 'fischer-2019', 'young-2023'],
 'outburst-recurrence-time': ['fischer-2019', 'zakri-2022', 'park-2021', 'contreras-pena-2019', 'contreras-pena-2024'],
 'pacs-bright-red-source': ['stutz-2013', 'furlan-2016', 'dunham-2014'],
 'vello': ['dunham-2008', 'dunham-2014', 'pineda-2011', 'enoch-2010', 'park-2021'],
 'free-fall-time': ['enoch-2008', 'konyves-2015', 'battersby-2017', 'svoboda-2016', 'larson-1969', 'masunaga-inutsuka-2000', 'tomida-2013'],
}
P = papers()
per = {}
for c, ns in ADD.items():
    for n in ns: per.setdefault(n, []).append(c)
for n, cs in per.items():
    t, d = load(P[n]); kc = names(d.get('key_concepts'))
    new = [c for c in cs if c not in kc]
    if not new: continue
    t = set_fm_list(t, 'key_concepts', kc + new)
    t, miss = add_to_related(t, 'Concepts introduced/used', new)
    assert not miss, n
    print(n, '+', new)
    if '--write' in sys.argv: open(P[n], 'w').write(t)
m = {}
for n, f in P.items():
    for c in names(load(f)[1].get('key_concepts')): m.setdefault(c, []).append(n)
for c in sorted(m): print(f'{c} ({len(m[c])}):', ', '.join(m[c]))
