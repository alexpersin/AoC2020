"""
modulo the start time by each id
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
"""
with open("inputs/13", "r") as f:
    data = f.read()

start, ids = data.split("\n", 1)
start = int(start)
ids = [int(i.strip()) for i in ids.split(",") if i != "x"]

m = 1000000
s = None
for i in ids:
    d = i - ( start % i )
    if d < m:
        m = d
        s = i
    print(d, i)

print(m * s)
