acc = 0
s = set()
with open("inputs/6", "r") as f:
    data = f.read()
    a = sum([len(set(d.replace('\n', ''))) for d in data.split("\n\n")])
    print(a)

acc = 0
for group in data.split("\n\n"):
    s = None
    sets = [set(l.strip()) for l in group.split("\n")]
    print(sets)
    s = sets[0].intersection(*sets[1:])
    acc += len(s)
    print(s)
print(acc)