ranges = []
ids = []

# Parse ranges and id's
with open("input.txt", "r") as file:

    for line in file:
        line = line.strip()

        if '-' in line:
            ranges.append(line.split('-'))
        elif len(line) != 0:
            ids.append(int(line))

# Convert ranges to ints
ranges = [[int(item) for item in rng] for rng in ranges]

# Check for fresh id's
fresh = 0

for id in ids:
    for rng in ranges:
        if rng[0] <= id <= rng[1]:
            fresh += 1
            
            break

print(fresh)