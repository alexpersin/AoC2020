import re

def make_addresses(mask):
    out = [[], []]
    done = False
    for c in mask:
        if c == 'X' and not done:
            out[0].append('0')
            out[1].append('1')
            done = True
        else:
            out[0].append(c)
            out[1].append(c)
    if not done:
        return [out[0]]
    else:
        return make_addresses(out[0]) + make_addresses(out[1])

with open("inputs/14", "r") as f:
    data = f.read().split('\n')

memr = re.compile(r"mem\[(\d+)\] = (\d+)")

mem = {}
for line in data:
    if not line:
        continue
    if line.startswith('mask'):
        mask = line.strip().split(' = ')[-1]
    else:
        m = memr.match(line)
        addr = bin(int(m.group(1)))[2:]
        data = int(m.group(2))

        padding = 36 - len(addr)
        addr = '0' * padding + addr
        out = []
        for a, b in zip(mask, addr):
            out.append(b if a == '0' else a)
        addresses = make_addresses(out)
        for a in addresses:
            a = ''.join(a)
            mem[a] = data

# 3705162613854
print(sum(mem.values()))
