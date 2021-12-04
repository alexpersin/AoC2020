data = "952316487"
# data = "389125467" # sample

MAX = 1_000_000
ROUNDS = 10_000_000

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
    for i in range(20):
        current = current.nxt
        s.append(str(current.val))
    p(' '.join(s))

lookup = {}
prev = None
first = None
for v in data:
    c = Cup(int(v))
    lookup[int(v)] = c
    if prev:
        prev.nxt = c
    else:
        first = c
    prev = c

for i in range(10, MAX+1):
    c = Cup(i)
    prev.nxt = c
    lookup[i] = c
    prev = c
c.nxt = first
current = first

removed = []
for i in range(ROUNDS):
    if i % 100000 == 0:
        p(i)
    print(f"--- move {i+1} ---")
    # print_cups(current)
    removed = [current.nxt, current.nxt.nxt, current.nxt.nxt.nxt]
    print(f"pick up {removed}")
    current.nxt = removed[-1].nxt
    destination = current.val - 1 if current.val > 1 else MAX
    while destination in [r.val for r in removed]:
        destination -= 1
        if destination == 0:
            destination = MAX
    print(f"destination: {destination}")
    dcup = lookup[destination]
    after = dcup.nxt
    dcup.nxt = removed[0]
    removed[-1].nxt = after
    current = current.nxt

a, b = lookup[1].nxt.val, lookup[1].nxt.nxt.val

p(a * b)
