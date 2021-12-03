from itertools import product

class Square:
    def __init__(self, state="."):
        self.occupied_neighbours = 0
        self.occupied = state == "#"
        self.floor = state == "."

    def signal(self):
        """Tell this cube that it has an active neighbour"""
        self.occupied_neighbours += 1

    def cycle(self):
        """Cycle the cube to the next state"""
        changed = False
        if not self.floor:
            if not self.occupied and self.occupied_neighbours == 0:
                    self.occupied = True
                    changed = True
            elif self.occupied and self.occupied_neighbours >= 4:
                self.occupied = False
                changed = True
        self.occupied_neighbours = 0
        return changed

    def __repr__(self):
        return "#" if self.occupied else ("." if self.floor else 'L')


def print_space(space):
    row = []
    for i in range(-1,92):
        row = []
        for j in range(-1,91):
            row.append(space[(i,j)])
        print(''.join(str(s) for s in row))


# Read input
with open("inputs/11", "r") as f:
    data = f.read().split("\n")


# Create initial space
space = {}
for x, row in enumerate(data):
    for y, state in enumerate(row):
        space[(x,y)] = Square(state)

for i in range(-1,91):
    space[(-1,i)] = Square()
    space[(91,i)] = Square()
for i in range(-1,92):
    space[(i,-1)] = Square()
    space[(i,90)] = Square()

print_space(space)


changed = True
while changed:
    changed = False
    # Iterate over the space sending a signal to each neighbour
    for (x,y), square in space.items():
        if x in (-1,91) or y in (-1,90):
            continue
        if square.occupied:
            for xo, yo in product(*[(-1,0,1)]*2):
                if xo == 0 and yo == 0:
                    continue
                space[(x+xo, y+yo)].signal()

    # Cycle the space, activating or deactivating
    for (x,y), square in space.items():
        changed = square.cycle() or changed
    print_space(space)

print(sum(s.occupied for s in space.values()))
