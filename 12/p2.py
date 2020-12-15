import math

E = 0
N = 0

WE = 10
WN = 1


with open("inputs/12", "r") as f:
    for instruction in f.readlines():
        direc, mag = instruction[0], instruction[1:-1]
        mag = int(mag)
        if direc == "N":
            WN += mag
        elif direc == "S":
            WN -= mag
        elif direc == "E":
            WE += mag
        elif direc == "W":
            WE -= mag
        elif direc == "L":
            angle = math.radians(mag)
            sin = math.sin(angle)
            cos = math.cos(angle)
            ne = (WE-E)*cos - (WN-N)*sin
            nn = (WE-E)*sin + (WN-N)*cos
            WE = ne + E
            WN = nn + N
        elif direc == "R":
            angle = math.radians(mag)
            sin = math.sin(angle)
            cos = math.cos(angle)
            ne = (WE-E)*cos + (WN-N)*sin
            nn = -(WE-E)*sin + (WN-N)*cos
            WE = ne + E
            WN = nn + N
        elif direc == "F":
            DE = WE - E
            DN = WN - N
            E = E + (DE*mag)
            N = N + (DN*mag)
            WE = E + DE
            WN = N + DN
        print(f"({E}, {N}) ({WE}, {WN})")

print(abs(E) + abs(N))
