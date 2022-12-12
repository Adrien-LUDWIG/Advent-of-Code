input = """noop
noop
noop
addx 6
addx -1
addx 5
noop
noop
noop
addx 5
addx 11
addx -10
addx 4
noop
addx 5
noop
noop
noop
addx 1
noop
addx 4
addx 5
noop
noop
noop
addx -35
addx -2
addx 5
addx 2
addx 3
addx -2
addx 2
addx 5
addx 2
addx 3
addx -2
addx 2
addx 5
addx 2
addx 3
addx -28
addx 28
addx 5
addx 2
addx -9
addx 10
addx -38
noop
addx 3
addx 2
addx 7
noop
noop
addx -9
addx 10
addx 4
addx 2
addx 3
noop
noop
addx -2
addx 7
noop
noop
noop
addx 3
addx 5
addx 2
noop
noop
noop
addx -35
noop
noop
noop
addx 5
addx 2
noop
addx 3
noop
noop
noop
addx 5
addx 3
addx -2
addx 2
addx 5
addx 2
addx -25
noop
addx 30
noop
addx 1
noop
addx 2
noop
addx 3
addx -38
noop
addx 7
addx -2
addx 5
addx 2
addx -8
addx 13
addx -2
noop
addx 3
addx 2
addx 5
addx 2
addx -15
noop
addx 20
addx 3
noop
addx 2
addx -4
addx 5
addx -38
addx 8
noop
noop
noop
noop
noop
noop
addx 2
addx 17
addx -10
addx 3
noop
addx 2
addx 1
addx -16
addx 19
addx 2
noop
addx 2
addx 5
addx 2
noop
noop
noop
noop
noop
noop"""

input = input.split('\n')

X = 1

ticks = []

for line in input:
    cmd = line[:4]
    
    ticks.append(X)
    if cmd == "addx":
        ticks.append(X)
        arg = int(line[5:])
        X += arg

print(ticks)
        
signal = 0 

for i in range(20, 221, 40):
    print(i, ticks[i])
    signal += i * ticks[i - 1]
    
print(signal)