"""
time   bus 7   bus 13  bus 59  bus 31  bus 19
929      .       .       .       .       .
930      .       .       .       D       .
931      D       .       .       .       D
932      .       .       .       .       .
933      .       .       .       .       .
934      .       .       .       .       .
935      .       .       .       .       .
936      .       D       .       .       .
937      .       .       .       .       .
938      D       .       .       .       .
939      .       .       .       .       .
940      .       .       .       .       .
941      .       .       .       .       .
942      .       .       .       .       .
943      .       .       .       .       .
944      .       .       D       .       .
945      D       .       .       .       .
946      .       .       .       .       .
947      .       .       .       .       .
948      .       .       .       .       .
949      .       D       .       .       .

t is the current time being checked
p is the current period being incremented
np is the period of the next bus being checked
o is the required offset

t starts at start
p starts as 1
np starts as id[0]
o starts at 0

check multiples of p until offset is o
p = np * p
np = next bus
o = next bus offset
"""
with open("inputs/13", "r") as f:
    data = f.read()

start, ids = data.split("\n", 1)
start = int(start)
ids = [(i, int(v.strip())) for i, v in enumerate(ids.split(",")) if v != "x"]

t = start
p = 1
for o, np in ids:
    o = o % np
    print(f'{t=} {p=} {o=} {np=}')
    while t % np != (np - o) % np :
        t+=p
    p *= np
print(t)
