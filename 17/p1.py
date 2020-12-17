from itertools import product

class Cube:
    def __init__(self, state="."):
        self.active_neighbours = 0
        self.active = state == "#"

    def signal(self):
        """Tell this cube that it has an active neighbour"""
        self.active_neighbours += 1
    
    def cycle(self):
        """Cycle the cube to the next state"""
        if self.active and self.active_neighbours not in (2,3):
                self.active = False
        elif self.active_neighbours == 3:
            self.active = True
        self.active_neighbours = 0
    
    def __repr__(self):
        return "#" if self.active else "."


def expand_space(space):
    coords = space.keys()
    xmn = min(c[0] for c in coords)
    ymn = min(c[1] for c in coords)
    zmn = min(c[2] for c in coords)
    xmx = max(c[0] for c in coords)
    ymx = max(c[1] for c in coords)
    zmx = max(c[2] for c in coords)

    for x, y, z in product(range(xmn-1, xmx+2), range(ymn-1, ymx+2), range(zmn-1, zmx+2)):
        if (x,y,z) not in space:
            space[(x,y,z)] = Cube()


def print_space(space):
    row = []
    for x, y, z in sorted(space):
        print(space[(x,y,z)])


# Read input
with open("inputs/17", "r") as f:
    start = f.read().split("\n")


# Create initial space
space = {}
for x, row in enumerate(start):
    for y, state in enumerate(row):
        space[(x,y,0)] = Cube(state)


# Create the neighbouring cubes first so we don't modify the dict in place
expand_space(space)


for cycle in range(6):
    # Iterate over the space sending a signal to each neighbour
    for (x,y,z), cube in space.items():
        if cube.active:
            for xo, yo, zo in product(*[(-1,0,1)]*3):
                if xo == 0 and yo == 0 and zo ==0:
                    continue
                space[(x+xo, y+yo, z+zo)].signal()

    # Cycle the space, activating or deactivating
    for (x,y,z), cube in space.items():
        cube.cycle()
    expand_space(space)

print(sum(cube.active for cube in space.values()))
