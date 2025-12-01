curr_num = 50
count = 0

with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()

        direction = line[0].lower()
        distance = int(line[1:])
        
        if direction == "r":
            for position in range(distance):
                curr_num += 1
                curr_num %= 100

                if curr_num == 0:
                     count += 1

                print(curr_num)
        elif direction == "l":
            for position in range(distance):
                curr_num -= 1
                curr_num %= 100

                if curr_num == 0:
                     count += 1

                print(curr_num)

print(count)