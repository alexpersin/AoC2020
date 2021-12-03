from itertools import product

COL = 90
ROW = 91

# For sample
# COL = 10
# ROW = 10

class Square:
    def __init__(self, state="."):
        self.occupied_neighbours = 0
        self.occupied = state == "#"
        self.floor = state == "."

    def signal(self):
        """Tell this square that it has an occupied neighbour"""
        self.occupied_neighbours += 1

    def cycle(self):
        """Cycle the square to the next state"""
        changed = False
        if not self.floor:
            if not self.occupied and self.occupied_neighbours == 0:
                self.occupied = True
                changed = True
            elif self.occupied and self.occupied_neighbours >= 5:
                self.occupied = False
                changed = True
        self.occupied_neighbours = 0
        return changed

    def __repr__(self):
        return "#" if self.occupied else ("." if self.floor else 'L')


def print_space(space):
    row = []
    for i in range(-1,ROW+1):
        row = []
        for j in range(-1,COL+1):
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

for i in range(-1,COL+1):
    space[(-1,i)] = Square()
    space[(ROW,i)] = Square()
for i in range(-1,ROW+1):
    space[(i,-1)] = Square()
    space[(i,COL)] = Square()

print_space(space)

changed = True
while changed:
    changed = False
    # Iterate over the space sending a signal to each neighbour
    for (x,y), square in space.items():
        if not square.occupied:
            continue
        for xo, yo in product((-1,0,1),(-1,0,1)):
            if xo == 0 and yo == 0:
                continue
            m = 1
            cx = x + (m*xo)
            cy = y + (m*yo)
            los = space[(cx,cy)]
            while los.floor and cx >= 0 and cx < ROW and cy >= 0 and cy < COL:
                m += 1
                cx = x + (m*xo)
                cy = y + (m*yo)
                los = space[(cx,cy)]
            los.signal()

    # Cycle the space, activating or deactivating
    for (x,y), square in space.items():
        changed = square.cycle() or changed
    print_space(space)

print(sum(s.occupied for s in space.values()))
