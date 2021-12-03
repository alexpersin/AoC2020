"""
Each Row starts off with all possible field names.
If one is invalid for a ticket then it is removed
"""
from collections import defaultdict
from copy import deepcopy

with open("inputs/16", 'r') as f:
    data = f.read()

fields, ticket, nearby = data.split("\n\n")

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
    for tkt in nearby.split("\n")[1:] + [ticket.split('\n')[-1]]:
        for field in tkt.split(","):
            f = int(field)
            if f >= len(valid) or not valid[f]:
                break
        else:
            valid_tkts.append(sorted([int(f) for f in tkt.split(",")]))

    return valid_tkts

tickets = get_valid_tickets()

print(fields)

# field_values = [[]] * len(valid_tkts[0])
# for tkt in valid_tkts:
#     for i, f in enumerate(tkt):
#         field_values[i].append(f)

tkt_fields = {}
names = set()
for field in fields.split("\n"):
    name, a, _, b = field.rsplit(' ', 3)
    names.add(name[:-1])
    tkt_fields[name[:-1]] = [[int(x) for x in a.split('-')], [int(x) for x in b.split('-')]]

print(names)
possible_fields = [deepcopy(names)] * len(tickets[0])

for j, ticket in enumerate(tickets):
    for i, val in enumerate(ticket):
        # check each constraint for the remaining fields for that row, if it fails remove it
        to_remove = set()
        for field in possible_fields[i]:
            c1, c2 = tkt_fields[field]
            if  val < c1[0] or (val > c1[1] and val < c2[0]) or val > c2[1]:
                print(f"Ticket {j}: value {val} for row {i} is invalid with constaints {c1} {c2}")
                to_remove.add(field)
        if to_remove and i == 6:
            print(f"Removing {to_remove} from {possible_fields[i]}")
        possible_fields[i] = possible_fields[i] - to_remove

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



# print(tkt_fields)
# possible_fields = []

# for j, l in enumerate(field_values):
#     p = []
#     for field in tkt_fields:
#         for mn, mx in field[1:]:
#             print(mn, mx)
#             if not all(x>=mn and x<=mx for x in l):
#                 print(f"Field {field[0]} not valid for row {j}")
#                 break
#         else:
#             p.append(tkt_fields[0])
#     possible_fields.append(p)

# print(possible_fields)
# """
# get range for each row
# get possible fields for each row
# """
