import re

with open('inputs/19', 'r') as f:
    rules_str, data = f.read().split('\n\n')


rules = {}
for rule in rules_str.split('\n'):
    key, expr = rule.split(':')
    rules[key] = expr.strip()

data = data.strip().split('\n')

def expand(key, capture=False):
    r = rules[key]

    if 'a' in r or 'b' in r:
        return r.strip('"')
    if key == '8':
        # Rule 8 matches 42 1 or more times
        e = expand('42')
        return f"{e}+"
    if key == '11':
        # Rule 11 matches rule 42 * i then rule 31 * i for i>=1
        e1 = expand('42')
        e2 = expand('31')
        e = "("
        for i in range(1,10):
            e += e1 * i
            e += e2 * i
            e += "|"
        e = e[:-1]
        e += ")"
        return e

    items = r.split(' ')
    output = []
    for item in items:
        if item.isnumeric():
            output.append(expand(item))
        elif item == '|':
            output.append(item)
    m = "" if capture else  "?:"
    if '|' in items:
        output = [f'({m}'] + output + [')']
    return ''.join(output)

r = re.compile('^' + expand('0') + '$')

count = 0
for line in data:
    m = r.match(line)
    if m:
        count +=1
print(count)
