INPUT = open("input.txt").read()


def visit_houses(directions):
    visited = set()

    x = 0
    y = 0
    for direction in directions:
        if direction == "^":
            y += 1
        elif direction == "<":
            x -= 1
        elif direction == ">":
            x += 1
        elif direction == "v":
            y -= 1
        visited.add((x, y))
    return visited


print(len(visit_houses(INPUT)))
