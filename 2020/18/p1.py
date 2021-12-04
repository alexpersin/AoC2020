with open("inputs/18", "r") as f:
    inputs = f.readlines()


def tokenize(line):
    for char in line:
        if char != " ":
            yield char

def parse(tokenizer):
    children = []
    try:
        while True:
            token = next(tokenizer)
            if token == '(':
                children.append(parse(tokenizer))
            elif token == ')':
                return children
            else:
                children.append(token)
    except StopIteration:
        return children

def evaluate(expr):
    acc = 0
    op = "+"
    for token in expr:
        if isinstance(token, list):
            val = evaluate(token)
            acc = eval(f"{acc} {op} {val}")
        elif token in "+*":
            op = token
        else:
            acc = eval(f"{acc} {op} {token}")
    return acc

def evaluate_2(expr):
    expr = iter(expr)
    output = [next(expr)]
    for item in expr:
        try:
            item = int(item)
        except:
            pass

        if output[-1] == '+':
            # Add the current item to the last value
            if isinstance(item, int):
                output.pop()
                last_val = output.pop()
                output.append(last_val + item)
            else:
                output.pop()
                last_val = output.pop()
                output.append(last_val + evaluate_2(item))
        else:
            output.append(item)

    expr = iter(expr)
    output = [next(expr)]
    for item in expr:
        try:
            item = int(item)
        except:
            pass

        if output[-1] == '+':
            # Add the current item to the last value
            if isinstance(item, int):
                output.pop()
                last_val = output.pop()
                output.append(last_val + item)
            else:
                output.pop()
                last_val = output.pop()
                output.append(last_val + evaluate_2(item))
        else:
            output.append(item)

    print(output)

"""
For item in list
if int, add to output
if item is a list, evaluate it and add to list
if item is a plus, set last item to this plus that
if item is a mult, ignore

rerun
"""


for line in inputs:
    print(line.strip())
    print(parse(tokenize(line.strip())))
    print(evaluate_2(parse(tokenize(line.strip()))))
    print()

"""
if token is int and next token is op, int goes to left of op, op becomes current
if token is op with no r and next is int, int goes to right
if token is mult and next token is plus, right becomes right of plus, mult becomes left of plus
"""


print(sum(evaluate(parse(tokenize(line.strip()))) for line in inputs))
