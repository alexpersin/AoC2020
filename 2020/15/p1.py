"""
store map of number to most recent turn
look at the last number, compare its val to current turn number
say that number:
    update the number you say with the current turn
"""

starters = [8,11,0,19,1,2]
# starters = [0,6,3]
cur_turn = 1
mem = {}

for s in starters:
    # print(f'say {s} on turn {cur_turn}')
    mem[s] = cur_turn
    first_time_spoken = True
    last_said = s
    cur_turn += 1

while cur_turn < 30000001:
    if first_time_spoken:
        say = 0
        # print(f'say {say} on turn {cur_turn}, previous value {last_said} has not been spoken before')
    else:
        m = mem.get(last_said)
        say = cur_turn - m - 1
        # print(f'say {say} on turn {cur_turn}, last value {last_said} was last said on turn {m}')
    first_time_spoken = say not in mem
    mem[last_said] = cur_turn - 1

    last_said = say
    cur_turn += 1

print(f'Say {last_said} on turn {cur_turn-1}')

