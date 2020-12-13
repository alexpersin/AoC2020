data = open('inputs/7', 'r').readlines()

# for each bag map to each parent
# for the gold bag count the children
from collections import defaultdict

mapp = defaultdict(list)

for line in data:
    parent, child = line.split(" contain ", 1)
    parent = parent.replace(" bags", "")
    children = [" ".join(a.split(' ')[:3]) for a in child.split(', ')]
    mapp[parent] = children


def count(bag):
    s = 1
    children = mapp[bag]
    for c in children:
        num, key = c.split(' ', 1)
        if num == "no":
            print(bag, children, 1)
            return 1
        n = count(key)
        s += int(num) * n
    print(bag, children, s)
    return s

print(count('shiny gold'))
