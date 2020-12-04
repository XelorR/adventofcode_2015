INPUT = open("input.txt").read()

current_floor = 0

for command in INPUT:
    if command == "(":
        current_floor += 1
    elif command == ")":
        current_floor -= 1

print(current_floor)
