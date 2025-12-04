grid = []

# Populate grid
with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()

        grid.append(line)

accesible = 0
cords = []

# Find the number of neighbors
for i in range(len(grid)):
    for j in range(len(grid[i])):
        count = 0
        if grid[i][j] != '@':
            continue

        for k in range(3):
            for l in range(3):
                x = (i-1) + k
                y = (j-1) + l

                if not(0 <= y < len(grid[i])) or not(0 <= x < len(grid)):
                    continue

                if grid[x][y] == '@':
                    count += 1

        if count <= 4:
            accesible += 1

print(accesible)
