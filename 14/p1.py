import re

with open("inputs/14", "r") as f:
    data = f.read().split('\n')

memr = re.compile(r"mem\[(\d+)\] = (\d+)")

mask = None
mem = {}
for line in data:
    if line.startswith('mask') or not line:
        mask = line.strip().split(' = ')[-1]
        print(f'mask: {mask}')
    else:
        m = memr.match(line)
        addr = m.group(1)
        data = bin(int(m.group(2), 10))
        padding = 36 - (len(data) - 2)
        data = '0' * padding + data[2:]
        out = []
        for a, b in zip(mask, data):
            out.append(b if a == 'X' else a)
        data = ''.join(out)
        print(f'{addr=}, {data=}')
        mem[addr] = int(data, 2)

print(sum(mem.values()))
