
digits = []

with open("/home/itisntme1/Documents/coding/projects/advent-of-code-2025/3/input.txt", "r") as file:
    for line in file:
        line = str(line)
        first = [0,0]
        second = 0

        for i in range(len(line) - 2):
            if int(line[i]) > first[0]:
                first = [int(line[i]), i]

        print(first, line, )

        for i in range(first[1] + 1, len(line) - 1):
            print(line[i], line)
            if int(line[i]) > second:
                second = int(line[i])

        digits.append(int(f"{first[0]}{second}"))

print(sum(digits), digits)