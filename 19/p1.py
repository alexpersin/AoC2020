"""
read each rule map

call repr(0)
look up in map what the rule string is
rule 0 repr calls its sub rules reprs
"""
import re

with open('inputs/19', 'r') as f:
    rules_str, data = f.read().split('\n\n')


rules = {}
for rule in rules_str.split('\n'):
    key, expr = rule.split(':')
    rules[key] = expr.strip()

data = data.strip().split('\n')

def expand(r):
    if 'a' in r or 'b' in r:
        return r.strip('"')
    items = r.split(' ')
    output = []
    for item in items:
        if item.isnumeric():
            output.append(expand(rules[item]))
        elif item == '|':
            output.append(item)
    if '|' in items:
        output = ['('] + output + [')']
    return ''.join(output)

# print(re.match(r"(aa|bb)(bb)", "aabb")[0])
r = re.compile('^' + expand(rules['0']) + '$')

print(r)

count = 0
for line in data:
    if r.match(line):
        print(line)
        count +=1
print(count)
