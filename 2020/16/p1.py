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

invalid = []
for tkt in nearby.split("\n")[1:]:
    for field in tkt.split(","):
        f = int(field)
        if f >= len(valid) or not valid[f]:
            invalid.append(f)

print(sum(invalid))
