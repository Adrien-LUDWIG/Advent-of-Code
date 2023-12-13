# Solved from a smartphone using Pydroid

input = """Time:        49     78     79     80
Distance:   298   1185   1066   1181"""

times, distances = input.split("\n")

times = map(int, times.split()[1:])
distances = map(int, distances.split()[1:])

possibilities_product = 1

for time, distance in zip(times, distances):
    wait = 0
    while wait * (time - wait) < distance:
        wait += 1

    possibilities_product *= time - wait * 2

print(possibilities_product)
