def solve(numheads, numlegs):
    num_rabbits = (numlegs - 2 * numheads) / 2
    num_chickens = numheads - num_rabbits

    return int(num_chickens), int(num_rabbits)


numheads = 35
numlegs = 94
chickens, rabbits = solve(numheads, numlegs)
print("Number of chickens:", chickens)
print("Number of rabbits:", rabbits)
