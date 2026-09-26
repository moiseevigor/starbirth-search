"""Helpers for connection passes over Research/ paper notes (frontmatter = source of truth)."""
import glob, json, os, re, yaml

VAULT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..'))
FM = re.compile(r'^---\n(.*?)\n---\n', re.S)
WL = re.compile(r'\[\[([^\]|#]+)')

def papers():
    out = {}
    for f in sorted(glob.glob(f'{VAULT}/Research/**/*.md', recursive=True)):
        if os.path.basename(f).startswith('_'):
            continue
        out[os.path.basename(f)[:-3]] = f
    return out

def load(f):
    t = open(f).read()
    return t, yaml.safe_load(FM.match(t).group(1))

def names(lst):
    return [WL.search(x).group(1).strip() for x in (lst or []) if WL.search(x)]

def set_fm_list(text, field, items):
    """Rewrite a single-line flow-list field in the frontmatter block only."""
    head, sep, body = text.partition('\n---\n')
    new = f'{field}: ' + json.dumps([f'[[{n}]]' for n in items], ensure_ascii=False)
    head, k = re.subn(rf'^{field}: \[.*\]$', new, head, count=1, flags=re.M)
    assert k == 1, field
    return head + sep + body

def related_line(text, label):
    m = re.search(rf'^- {re.escape(label)}:.*$', text, re.M)
    return m

EMPTY = re.compile(r'^(—|-|none.*)$', re.I)

def add_to_related(text, label, add):
    """Append missing wikilinks to a '- <label>: ...' bullet, keeping annotations."""
    m = related_line(text, label)
    if not m or not add:
        return text, bool(add) and not m
    line = m.group(0)
    prefix = f'- {label}: '
    rest = line[len(prefix):]
    have = set(n.strip() for n in WL.findall(rest))
    missing = [a for a in add if a not in have]
    if not missing:
        return text, False
    links = ', '.join(f'[[{a}]]' for a in missing)
    rest = links if EMPTY.match(rest.strip()) else rest + ', ' + links
    return text[:m.start()] + prefix + rest + text[m.end():], False
