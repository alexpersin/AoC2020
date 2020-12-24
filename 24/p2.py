"""
Hexagonal grid:
\ /\ /\ /\ /\
 |  |  |  |  |
/ \/ \/ \/ \/
|  |  |  |  |
 \/ \/ \/ \/ \
One axis is E-W and one is NE-SW
"""
from collections import defaultdict, namedtuple

Tile = namedtuple('Tile', ['isblack', 'bnc'])

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

grid = defaultdict(lambda: Tile(False, 0))

for line in data:
    pos = 0,0
    for direction in iter_line(line):
        pos = move[direction](*pos)
    g = grid[pos]
    grid[pos] = Tile(not g[0], 0)

for i in range(100):
    for (e, ne), tile in list(grid.items()):
        if tile.isblack:
            for coord in ((e+1, ne), (e-1, ne), (e, ne+1), (e, ne-1), (e-1, ne+1), (e+1, ne-1)):
                isblack, bnc = grid[coord]
                grid[coord] = Tile(isblack, bnc+1)

    for pos in list(grid.keys()):
        tile = grid[pos]
        if tile.isblack and (tile.bnc == 0 or tile.bnc > 2):
            grid[pos] = Tile(not tile.isblack, 0)
        elif (not tile.isblack) and tile.bnc == 2:
            grid[pos] = Tile(not tile.isblack, 0)
        else:
            grid[pos] = Tile(tile.isblack, 0)

print(sum(x[0] for x in grid.values()))
