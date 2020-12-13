data = open('inputs/7', 'r').readlines()

# for each bag map to each parent
# for the gold bag count the children
from collections import defaultdict

mapp = defaultdict(list)

for line in data:
    parent, child = line.split(" contain ", 1)
    parent = parent.replace(" bags", "")
    children = [" ".join(a.split(' ')[:3]) for a in child.split(', ')]
    print(parent, "_", children)
    mapp[parent] = children


def contains(key):
    if mapp[key][0] == "other bags.\n":
        return False
    elif any(i == "shiny gold" for i in mapp[key]):
        return True
    else:
        return any(contains(k) for k in mapp[key])

s=0
for k, v in mapp.items():
    if contains(k):
        s+=1
print(s)
