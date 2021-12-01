with open("inputs/16", 'r') as f:
    data = f.read()

fields, ticket, nearby = data.split("\n\n")

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
for tkt in nearby.split("\n")[1:]:
    for field in tkt.split(","):
        f = int(field)
        if f >= len(valid) or not valid[f]:
            break
    else:
        valid_tkts.append([int(f) for f in tkt.split(",")])

field_values = [[]] * len(valid_tkts[0])
for tkt in valid_tkts:
    for i, f in enumerate(tkt):
        field_values[i].append(f)

tkt_fields = []
for field in fields.split("\n"):
    name, a, _, b = field.rsplit(' ', 3)
    tkt_fields.append([name[:-1],[int(x) for x in a.split('-')], [int(x) for x in b.split('-')]])

print(tkt_fields)
possible_fields = []

for j, l in enumerate(field_values):
    p = []
    for field in tkt_fields:
        for mn, mx in field[1:]:
            print(mn, mx)
            if not all(x>=mn and x<=mx for x in l):
                print(f"Field {field[0]} not valid for row {j}")
                break
        else:
            p.append(tkt_fields[0])
    possible_fields.append(p)

print(possible_fields)
"""
get range for each row
get possible fields for each row
"""
