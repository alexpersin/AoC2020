from collections import defaultdict
from itertools import combinations
from functools import reduce

class Tile:
    flip = {}

    def __init__(self, ID, image):
        self.ID = ID
        self.edges = self.process_image(image)
        self.orientation = 0
        self.flip = False
        self.possible_neighbours = set()

    def process_image(self, image):
        top = self.process_edge([i for i in image[0]])
        bottom = self.process_edge([i for i in image[-1]])
        left = self.process_edge([i[0] for i in image])
        right = self.process_edge([i[-1] for i in image])
        return [top, right, bottom, left]

    def process_edge(self, edge):
        bin_str = ''.join('1' if i == '#' else '0' for i in edge)
        edge = int(bin_str, 2)
        return edge

    def orientations(self):
        """
        Yields self in every orientation
        """
        for i in range(4):
            yield self
            self.rotate()
        self.rotate()

        self.flip_horizontal()
        for i in range(4):
            yield self
            self.rotate()
        self.rotate()
        self.flip_horizontal()

        self.flip_vertical()
        for i in range(4):
            yield self
            self.rotate()
        self.rotate()
        self.flip_vertical()

    def flip_horizontal(self):
        self.edges[1], self.edges[3] = self.edges[3], self.edges[1]
        self.edges[2] = self.reflect(self.edges[2])
        self.edges[0] = self.reflect(self.edges[0])

    def flip_vertical(self):
        self.edges[0], self.edges[2] = self.edges[2], self.edges[0]
        self.edges[3] = self.reflect(self.edges[3])
        self.edges[1] = self.reflect(self.edges[1])

    def rotate(self):
        self.edges.append(self.edges.pop(0))

    def reflect(self, edge: int) -> int:
        edge = int(''.join(reversed(f"{edge:b}")),2)
        return edge

    def all_edges(self):
        """Not needed"""
        return self.edges + [self.reflect(edge) for edge in self.edges]


    def __str__(self):
        return f"<Tile {self.ID}: {self.edges} orient: {self.orientation} flip: {int(self.flip)}>"

    def __repr__(self):
        return f"<{self.ID}>"

class Board:
    """
    provides get_neighbour_edges and place_tile methods for each square
    """
    def __init__(self):
        self.placed = set()
        self._board = []
        for i in range(12):
            row = []
            for j in range(12):
                row.append(None)
            self._board.append(row)

    def __iter__(self):
        for row in self._board:
            for square in row:
                yield square

    def on_board(self, tile):
        return tile.ID in self.placed

    def place(self, square, tile) -> bool:
        """
        Places the tile in the square in a correct orientation if possible
        otherwise returns False
        """
        neighbours = list(self.get_neighbour_edges(square))
        for t in tile.orientations():
            for a, b in zip(neighbours, t.edges):
                if a and (a!=b):
                    continue
            else:
                new = Board()
                new._board = self._board.copy()
                new.placed = self.placed.copy()
                new._board[square//12][square % 12] = tile
                new.placed.add(tile.ID)
                return new
        return False

    def get_neighbour_edges(self, i):
        """
        Yields all the neighbouring edges of tile i
        """
        row = i//12
        col = i % 12
        if row > 0:
            n = self._board[row-1][col]
            if n:
                yield n.edges[0] or None
        if col < 11:
            n = self._board[row][col+1]
            if n:
                yield n.edges[1] or None
        if row < 11:
            n = self._board[row+1][col]
            if n:
                yield n.edges[2] or None
        if col > 0:
            n = self._board[row][col-1]
            if n:
                yield n.edges[3] or None

    def __str__(self):
        o = []
        for row in self._board:
            o.append(''.join(str(row)))
        return '\n'.join(o)


# Parse input
with open("inputs/20", 'r') as f:
    data = f.read().split("\n\n")

edges = defaultdict(list)

tiles = []
for item in data:
    item = item.strip().split('\n')
    id_str = item[0]
    _id = int(id_str.split(' ')[-1][:-1])
    image = item[1:]
    tile = Tile(_id, image)
    tiles.append(tile)
    for edge in tile.all_edges():
        edges[edge].append(tile)

for k, v in edges.items():
    for t1 in v:
        for t2 in v:
            if t1.ID == t2.ID:
                continue
            t1.possible_neighbours.add(t2)

board = Board()

# Set the corner tile
start = 1021
s = None
for t in tiles:
    if t.ID == start:
        t.flip_vertical()
        n = list(t.possible_neighbours)
        s = t
board._board[0][0] = s
board.placed.add(s)

def get_possible_tiles(board, square):
    # Possible tiles have an edge that matches a neighbour
    neighbour_edges = list(board.get_neighbour_edges(square))
    print("Neighbour edges:", neighbour_edges)
    for edge in neighbour_edges:
        for tile in edges[edge]:
            if not board.on_board(tile):
                yield tile

# Fit the other tiles

def fit(board, square):
    print(board)
    tiles = list(get_possible_tiles(board, square))
    if not tiles:
        return False
    if square == 144:
        return board
    for tile in tiles:
        new = board.place(square, tile)
        if new:
            return fit(new, square+1)
        return False

# fit(board, square=1)

print(board)
print(s)
print(list(get_possible_tiles(board, 12)))

"""
a tile can only be valid if there are possible tiles to place next to it
fit returns true if placing that tile there results in a complete image
fit:
    if no fits:
        return false
    for tile in possible tiles for square:
        if last_square:
            return True or print board
        place tile
        fit(next_square)

While there are remaining tiles try and fit a tile onto the board
if there are no fits remove the last tile from the board
fit(): given a position, find a tile that fits in that place. if no fits return false
when a tile is found, call fit on the next place
if that returns false, return false
if it returns true then the board will contain the pieces all fitted
"""
