"""
Each Row starts off with all possible field names.
If one is invalid for a ticket then it is removed
"""
from collections import defaultdict
from copy import deepcopy

with open("inputs/16", 'r') as f:
    data = f.read().strip()

fields, TICKET, nearby = data.split("\n\n")

def get_valid_tickets():
    pairs = []
    maxval = 0
    for field in fields.split("\n"):
        _, a, _, b = field.rsplit(' ', 3)
        for i in (a,b):
            x, y = i.split("-")
            x, y = int(x), int(y)
            pairs.append((x, y))
            maxval = max(maxval, x, y)

    valid = [0]*(maxval+1)

    for mn, mx in pairs:
        for i in range(mn, mx+1):
            valid[i] = 1

    valid_tkts = []
    for tkt in nearby.split("\n")[1:]: # + [ticket.split('\n')[-1]]:
        for field in tkt.split(","):
            f = int(field)
            if f >= len(valid) or not valid[f]:
                break
        else:
            valid_tkts.append([int(f) for f in tkt.split(",")])

    return valid_tkts

tickets = get_valid_tickets()
print("Valid tickets:")
for t in tickets:
    print(t)

tkt_fields = {}
names = set()
for field in fields.split("\n"):
    name, a, _, b = field.rsplit(' ', 3)
    names.add(name[:-1])
    tkt_fields[name[:-1]] = [[int(x) for x in a.split('-')], [int(x) for x in b.split('-')]]
print("Contstraints:")
for i in tkt_fields.items():
    print(i)

values = []
possible_fields = []
for i in range(len(tickets[0])):
    possible_fields.append(deepcopy(names))
    values.append([])

for j, ticket in enumerate(tickets):
    for i, val in enumerate(ticket):
        values[i].append(val)

print(values)

for i, vals in enumerate(values):
    for val in vals:
        # check each constraint for the remaining fields for that row, if it fails remove it
        for field in list(possible_fields[i]):
            c1, c2 = tkt_fields[field]
            if not ((val >= c1[0] and val <= c1[1]) or (val >= c2[0] and val <= c2[1])):
                print(f"{val} is invalid with {c1} {c2}. Position {i} cannot be {field}")
                possible_fields[i].remove(field)

csp = defaultdict(set)
for i, v in enumerate(possible_fields):
    print(f"row {i} could be {v}")
    for field in v:
        csp[field].add(i)

for k, v in csp.items():
    a = []
    for i in range(20):
        if i in v:
            a.append('0')
        else:
            a.append(' ')
    print(f"{k[:16]:16} {''.join(a)}")

answer = {}
changed = True
while changed:
    changed = False
    for pos, fields in list(enumerate(possible_fields)):
        if pos in answer:
            continue
        if len(fields) == 1:
            changed = True
            field = list(fields)[0]
            print(f"pos {pos} is {field}")
            answer[pos] = field
            for a, b in list(enumerate(possible_fields)):
                if a != pos:
                    b.discard(field)

TICKET = [int(t.strip()) for t in TICKET.replace('your ticket:\n', '').strip().split(',')]
res = 1
for k, v in answer.items():
    if v.startswith('departure'):
        val = TICKET[k]
        print(k, v, val)
        res *= val
print(res)
print(TICKET)
# 6320160
