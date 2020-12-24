"""
Hexagonal grid:
\ /\ /\ /\ /\
 |  |  |  |  |
/ \/ \/ \/ \/
|  |  |  |  |
 \/ \/ \/ \/ \
One axis is E-W and one is NE-SW
"""
from collections import defaultdict

def iter_line(line):
    prev = None
    for c in line:
        if c in 'ew' and not prev:
            yield c
        elif c in 'ew' and prev:
            yield prev + c
            prev = None
        elif c in 'ns' and not prev:
            prev = c
        else:
            raise Exception("Unparsable input")

move = {
    'e': lambda e, ne: (e+1, ne),
    'w': lambda e, ne: (e-1, ne),
    'ne': lambda e, ne: (e, ne+1),
    'sw': lambda e, ne: (e, ne-1),
    'nw': lambda e, ne: (e-1, ne+1),
    'se': lambda e, ne: (e+1, ne-1),
}

with open("inputs/24", "r") as f:
    data = f.read().strip().split('\n')

grid = defaultdict(lambda: False)

for line in data:
    pos = 0,0
    for direction in iter_line(line):
        pos = move[direction](*pos)
    grid[pos] = not grid[pos]

print(sum(grid.values()))
