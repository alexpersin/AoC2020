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
    """Add the neighbouring cubes to the space so we don't modify the dict while iterating over it"""
    dims = []
    for d in range(4):
        dims.append([f(c[d] for c in space.keys()) for f in (min, max)])

    for x, y, z, w in product(*[range(d[0]-1, d[1]+2) for d in dims]):
        if (x,y,z,w) not in space:
            space[(x,y,z,w)] = Cube()


with open("inputs/17", "r") as f:
    start = f.read().split("\n")

# Create initial space
space = {}
for x, row in enumerate(start):
    for y, state in enumerate(row):
        space[(x,y,0,0)] = Cube(state)
expand_space(space)


for cycle in range(6):
    # Iterate over the space sending a signal to each neighbour
    for (x,y,z,w), cube in space.items():
        if cube.active:
            for xo, yo, zo, wo in product(*[(-1,0,1)]*4):
                if xo == 0 and yo == 0 and zo == 0 and wo == 0:
                    continue
                space[(x+xo, y+yo, z+zo, w+wo)].signal()

    # Cycle the space, activating or deactivating
    for cube in space.values():
        cube.cycle()
    expand_space(space)

print(sum(cube.active for cube in space.values()))
