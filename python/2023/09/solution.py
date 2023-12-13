# Solved on smartphone using Pydroid

# TODO: Replace copy/paste input string here
input = <input_str>

input = [list(map(int, line.split())) for line in input.split("\n")]

def find_next(seq):
    stack = [seq]
    
    while any(seq):
        stack.append([rhs - lhs for lhs, rhs in zip(seq[:-1], seq[1:])])
        seq = stack[-1]

    prediction = 0
    
    while stack:
        seq = stack.pop()
        prediction = seq[0] - prediction
        
    return prediction
        
    
print(sum(find_next(seq) for seq in input))