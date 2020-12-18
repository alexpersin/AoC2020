with open("inputs/18", "r") as f:
    inputs = f.readlines()

"""
send characters into the coroutine
coroutine evaluates expression

loop over characters
if number, apply operator to accumulator and number
if operator, set operator
if open bracket send characters into evaluate until bracket count is 0 
receive result as number
"""

class GetVal(Exception):
    pass

def maths(line):
    print(f"Evaluating {line}")
    def evaluate():
        accumulator = 0
        open_brackets = 0
        operator = "+"
        subgroup_evaluate = evaluate()
        expr = ''
        s = False
        while True:
            try:
                token = yield
                expr += token
                if token == ' ':
                    continue
                print(token)

                if token == ')':
                    open_brackets -= 1
                if token == '(':
                    open_brackets += 1
                if open_brackets > 0:
                    print(f"Depth {open_brackets} sending {token} to subroutine")
                    if not s:
                        next(subgroup_evaluate)
                        s = True
                    subgroup_evaluate.send(token)
                elif token == ')':
                    open_brackets -= 1
                    if open_brackets == 0:
                        subresult = subgroup_evaluate.throw(GetVal)
                        print(f"Got subresult {subresult}")
                        print(f"acc: {accumulator} {operator} {subresult}")
                        accumulator = eval(f"{accumulator} {operator} {subresult}")
                    print(f"{open_brackets} open brackets")
                elif token.isnumeric():
                    print(f"acc: {accumulator} {operator} {token}")
                    accumulator = eval(f"{accumulator} {operator} {token}")
                elif token == '(':
                    open_brackets += 1
                    print(f"{open_brackets} open brackets")
                elif token in ("-+*/"):
                    operator = token
            except GetVal:
                print(f"Exiting {expr} subroutine with val {accumulator} and token {token}")
                yield accumulator
        
        return

    ev = evaluate()
    next(ev)
    for token in line:
        ev.send(token)
    return int(ev.throw(GetVal))

print(maths("1 + (2 * 3) + (4 * (5 + 6))"))
# print(sum(maths(line) for line in inputs))