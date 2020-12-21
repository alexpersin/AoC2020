"""
If an allergen appears in more than one line then items that are not
in the intersection of all those lines cannot contain that allergen.

Ingredients that are not in a line that contains an allergen cannot
contain that allergen.

Union the list of safe ingredients for each allerged from those two methods
then find the intersection of those lists.s"""
import re
from collections import defaultdict

r = re.compile(r"(.*)\((.*)\)")
lines = []
all_ings = set()
with open("inputs/21", 'r') as f:
    for line in f.readlines():
        if line:
            m = r.match(line)
            ing = set(m.group(1).strip().split(" "))
            allergens = set(m.group(2).replace('contains ', '').split(', '))
            lines.append((ing, allergens))
            all_ings.update(ing)

al_to_ing = defaultdict(list)
for ings, als in lines:
    for al in als:
        al_to_ing[al].append(ings)

i = {}
for al, ings in al_to_ing.items():
    not_present_in_all = set.union(*ings) - set.intersection(*ings)
    i[al] = not_present_in_all

# Ingredients not in a line that contains an allergen cannot contain that
# allergen
for al, ings in al_to_ing.items():
    for ing in ings:
        i[al].update(all_ings - ing)

no_allergens = set.intersection(*i.values())

count = 0
for ings, _ in lines:
    for ing in ings:
        if ing in no_allergens:
            count += 1
print(f"Part 1: {count}")

resolved = set()
added = True
answer = []
while added:
    added = False
    for al, ing in i.items():
        m = all_ings - ing - resolved
        if len(m) == 1:
            v = list(m)[0]
            # print(f"{v}: {al}")
            answer.append((v, al))
            resolved.add(v)
            added = True
print("Part 2: " + ','.join([s[0] for s in sorted(answer, key = lambda x: x[1])]))
