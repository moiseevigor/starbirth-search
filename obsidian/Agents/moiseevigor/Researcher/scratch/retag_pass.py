"""Add registered topic tags (substance-tested by hand, 2026-09-26 connection pass). Usage: retag_pass.py [--write]"""
import sys, re
from vaultlib import *

ADD = {
 'molinari-2016': ['survey-completeness-reliability', 'survey-artefacts-and-contamination'],
 'mainzer-2014': ['survey-completeness-reliability', 'survey-artefacts-and-contamination'],
 'meisner-2023': ['survey-completeness-reliability', 'survey-artefacts-and-contamination'],
 'robitaille-2017': ['radiative-transfer'],
 'konyves-2015': ['core-mass-function', 'herschel-protostar-surveys'],
 'kuhn-2021': ['survey-completeness-reliability', 'survey-artefacts-and-contamination'],
 'furlan-2016': ['radiative-transfer', 'herschel-protostar-surveys', 'accretion-luminosity'],
 'elia-2017': ['clump-evolutionary-stages', 'survey-completeness-reliability'],
 'elia-2021': ['clump-evolutionary-stages', 'survey-completeness-reliability'],
 'elia-2022': ['clump-evolutionary-stages', 'survey-completeness-reliability'],
 'battersby-2017': ['clump-evolutionary-stages', 'methanol-masers'],
 'svoboda-2016': ['clump-evolutionary-stages', 'methanol-masers'],
 'enoch-2008': ['core-mass-function'],
 'evans-2009': ['accretion-luminosity'],
 'contreras-pena-2019': ['outburst-recurrence-rate'],
 'contreras-pena-2024': ['outburst-recurrence-rate', 'survey-completeness-reliability', 'survey-artefacts-and-contamination'],
 'fischer-2019': ['outburst-recurrence-rate', 'herschel-protostar-surveys', 'accretion-luminosity'],
 'lee-2021': ['outburst-recurrence-rate', 'survey-artefacts-and-contamination'],
 'lu-2024': ['clump-evolutionary-stages', 'methanol-masers'],
 'lucas-2024': ['survey-artefacts-and-contamination'],
 'park-2021': ['outburst-recurrence-rate'],
 'safron-2015': ['accretion-luminosity', 'herschel-protostar-surveys'],
 'zakri-2022': ['outburst-recurrence-rate', 'accretion-luminosity', 'herschel-protostar-surveys'],
 'dunham-2008': ['accretion-luminosity', 'radiative-transfer', 'survey-completeness-reliability'],
 'dunham-2014': ['accretion-luminosity', 'herschel-protostar-surveys'],
 'enoch-2010': ['radiative-transfer', 'protostellar-outflows'],
 'pineda-2011': ['protostellar-outflows', 'radiative-transfer', 'accretion-luminosity'],
 'stutz-2013': ['herschel-protostar-surveys', 'survey-artefacts-and-contamination', 'radiative-transfer'],
 'bhandare-2020': ['accretion-luminosity'],
 'larson-1969': ['accretion-luminosity'],
 'masunaga-inutsuka-2000': ['accretion-luminosity', 'radiative-transfer'],
 'tomida-2013': ['protostellar-outflows'],
 'young-2023': ['protostellar-outflows', 'accretion-luminosity'],
}
REG = set(re.findall(r'`#topic/([a-z0-9-]+)`', open(f'{VAULT}/_meta/tags.md').read()))
P = papers()
for n, add in ADD.items():
    assert set(add) <= REG, (n, set(add) - REG)
    t, d = load(P[n])
    have = [x for x in d['tags'] if x.startswith('topic/')]
    new = [a for a in add if f'topic/{a}' not in have]
    if not new: continue
    last = re.findall(r'^  - topic/.*$', t, re.M)[-1]
    t = t.replace(last + '\n', last + '\n' + ''.join(f'  - topic/{a}\n' for a in new), 1)
    print(f'{n}: {len(have)} -> {len(have)+len(new)} topics; +{new}')
    if '--write' in sys.argv: open(P[n], 'w').write(t)
for n, f in P.items():
    d = load(f)[1]; assert d['status'] == 'draft'
