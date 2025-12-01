
curr_num: int = 50
count: int = 0

def move(line: str, curr_num):
    direction: str = line[0].lower()
    distance: int = int(line[1::])

    if direction == "r":
        curr_num += distance
    elif direction == "l":
        curr_num -= distance

    curr_num %= 100

    return curr_num

with open("input.txt", "r") as file:
    for line in file:
        curr_num = move(line.strip(), curr_num)

        if curr_num == 0:
            count += 1
        
print(count)