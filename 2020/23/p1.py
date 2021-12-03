data = "952316487"
# data = "389125467" # sample

LOG = False
p = print
if not LOG:
    def print(*a):
        pass

class Cup:
    def __init__(self, val, nxt=None):
        self.val = val
        self.nxt = nxt

    def __repr__(self):
        return f"{self.val}"

def print_cups(current):
    s = []
    s.append(f"({current.val})")
    for i in range(8):
        current = current.nxt
        s.append(str(current.val))
    print(' '.join(s))

lookup = {}
prev = None
current = None
for v in data:
    c = Cup(int(v))
    lookup[int(v)] = c
    if prev:
        prev.nxt = c
    else:
        current = c
    prev = c
c.nxt = current

print(lookup)

removed = []
for i in range(100):
    print(f"--- move {i+1} ---")
    print_cups(current)
    removed = [current.nxt, current.nxt.nxt, current.nxt.nxt.nxt]
    print(f"pick up {removed}")
    current.nxt = removed[-1].nxt
    destination = current.val - 1 if current.val > 1 else 9
    while destination in [r.val for r in removed]:
        destination -= 1
        if destination == 0:
            destination = 9
    print(f"destination: {destination}")
    dcup = lookup[destination]
    after = dcup.nxt
    dcup.nxt = removed[0]
    removed[-1].nxt = after
    current = current.nxt

cup = lookup[1].nxt
s = []
for i in range(8):
    s.append(str(cup.val))
    cup = cup.nxt

p("".join(s))
