"""
Start by placing the corner tile in the corner
for each possible tile
    place a tile by placing it on a sqaure neighbouring a tile
    and joining it with the exposed edges
    if the board is complete, finish
    else recurse
    if there are no tiles that can be placed, return False

need a list of available tiles
need a list of exposed edges
need a dict of edge to tile
"""

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
        self._board = []
        self.exposed_edges = defaultdict(lambda: 0)
        for i in range(12):
            row = []
            for j in range(12):
                row.append(None)
            self._board.append(row)

    def __iter__(self):
        for row in self._board:
            for square in row:
                yield square

    def place(self, tile, row, col) -> bool:
        # Check place is not filled
        if self._board[row][col]:
            print("Position already filled!")
            return False
        # Check edges line up with neighbours
        for neighbour_edge, edge in zip(self.get_neighbour_edges(row, col), tile.edges):
            if neighbour_edge and neighbour_edge != 'EDGE' and neighbour_edge != edge:
                print(f"Edge {edge} on tile {tile.ID} does not match neighbour, cannot place")
                return False
        # Place tile
        self._board[row][col] = tile
        # Update list of exposed edges
        for neighbour_edge, edge in zip(self.get_neighbour_edges(row, col), tile.edges):
            if neighbour_edge and neighbour_edge != 'EDGE':
                self.exposed_edges[neighbour_edge] = self.exposed_edges[neighbour_edge] - 1
            elif neighbour_edge != 'EDGE':
                self.exposed_edges[edge] += 1
        print(list(self.get_neighbour_edges(row, col)))
        print(f"Placed tile {tile.ID} at ({row}, {col})")
        print(f"Exposed edges are now {self.exposed_edges}")
        return True

    def get_neighbour_edges(self, row, col):
        """
        Yields all the neighbouring edges of square
        """
        if row > 0:
            n = self._board[row-1][col]
            if n:
                yield n.edges[0] or None
            else:
                yield None
        else:
            yield 'EDGE'
        if col < 11:
            n = self._board[row][col+1]
            if n:
                yield n.edges[1] or None
            else:
                yield None
        else:
            yield 'EDGE'
        if row < 11:
            n = self._board[row+1][col]
            if n:
                yield n.edges[2] or None
            else:
                yield None
        else:
            yield 'EDGE'
        if col > 0:
            n = self._board[row][col-1]
            if n:
                yield n.edges[3] or None
            else:
                yield None
        else:
            yield 'EDGE'

    def __str__(self):
        o = []
        for row in self._board:
            o.append(''.join(str(row)))
        return '\n'.join(o)


# Parse input
with open("inputs/20", 'r') as f:
    data = f.read().split("\n\n")

available_edges = defaultdict(list)
available_tiles = {}
for item in data:
    item = item.strip().split('\n')
    id_str = item[0]
    _id = int(id_str.split(' ')[-1][:-1])
    image = item[1:]
    tile = Tile(_id, image)
    available_tiles[_id] = tile
    for edge in tile.all_edges():
        available_edges[edge].append(tile)

board = Board()

# Set the corner tile
start = available_tiles[1021]
start.flip_vertical()
ok = board.place(start, 0, 0)
if ok:
    del available_tiles[1021]
    for edge in tile.all_edges():
        available_edges[edge].remove(tile)

# def place():



# def get_possible_tiles(board, square):
#     # Possible tiles have an edge that matches a neighbour
#     neighbour_edges = list(board.get_neighbour_edges(square))
#     print("Neighbour edges:", neighbour_edges)
#     for edge in neighbour_edges:
#         for tile in edges[edge]:
#             if not board.on_board(tile):
#                 yield tile

# # Fit the other tiles

# def fit(board, square):
#     print(board)
#     tiles = list(get_possible_tiles(board, square))
#     if not tiles:
#         return False
#     if square == 144:
#         return board
#     for tile in tiles:
#         new = board.place(square, tile)
#         if new:
#             return fit(new, square+1)
#         return False

# # fit(board, square=1)

# print(board)
# print(s)
# print(list(get_possible_tiles(board, 12)))
