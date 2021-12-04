import math

E = 0
N = 0
D = 0


with open("inputs/12", "r") as f:
    for instruction in f.readlines():
        direc, mag = instruction[0], instruction[1:-1]
        mag = int(mag)
        if direc == "N":
            N += mag
        elif direc == "S":
            N -= mag
        elif direc == "E":
            E += mag
        elif direc == "W":
            E -= mag
        elif direc == "L":
            D  = (D + mag) % 360
        elif direc == "R":
            D = (D - mag) % 360
        elif direc == "F":
            d = D * math.pi / 180
            E += round(math.cos(d)) * mag
            N += round(math.sin(d)) * mag
        print(f"({E}, {N}) {D}")

print(abs(E) + abs(N))
