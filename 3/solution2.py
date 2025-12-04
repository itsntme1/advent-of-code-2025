
highest_digits = []

with open("/home/itisntme1/Documents/coding/projects/advent-of-code-2025/3/input2.txt", "r") as file:
    for line in file:
        line = str(line)
        digits = [[0,0] for _ in range(12)]
        highest_digit = ""
        start = 0

        for count in range(12):
            for pos in range(start, 100 - (11 - count)):
                if int(line[pos]) > digits[count][0]:
                    digits[count][0], digits[count][1] = int(line[pos]), int(pos)
                    start = int(pos) + 1

            highest_digit += str(digits[count][0])

        highest_digits.append(int(highest_digit))

print(sum(highest_digits), highest_digits)

#FIXME Wrong pos range beginning -> leaves out the first num