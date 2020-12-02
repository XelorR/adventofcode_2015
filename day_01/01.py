INPUT = open("input.txt").read()

current_floor = 0

for position, command in enumerate(INPUT):
    if command == "(":
        current_floor += 1
    elif command == ")":
        current_floor -= 1
        if current_floor == -1:
            print(position + 1)
