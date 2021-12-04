"""
If an allergen is listed in more than one line then items that are not
in the intersection of all the lines containing the allergen cannot
contain that allergen

Ingredients that are not in a line that contains an allergen cannot
contain that allergen
"""
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
print(count)
