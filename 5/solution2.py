ranges = []

# Parse ranges
with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()

        if '-' in line:
            start, end = map(int, line.split('-'))
            ranges.append([min(start, end), max(start, end)])

# Count fresh id's
ranges.sort()
merged = [ranges[0]]

for start, end in ranges[1:]:
    last_start, last_end = merged[-1]
    if start <= last_end + 1:
        merged[-1][1] = max(last_end, end)
    else:
        merged.append([start, end])

count = sum(end - start + 1 for start, end in merged)
print(count)