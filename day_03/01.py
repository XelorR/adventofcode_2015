INPUT = open("input.txt").read()


def visit_houses(directions: str) -> int:
    visited = set()
    visited.add((0, 0))

    current_coords = {"santa": [0, 0], "robosanta": [0, 0]}

    for iter, direction in enumerate(directions):
        if iter % 2 == 0:
            who = "santa"
        else:
            who = "robosanta"

        if direction == "^":
            current_coords[who][-1] += 1
        elif direction == "v":
            current_coords[who][-1] -= 1
        elif direction == ">":
            current_coords[who][0] += 1
        elif direction == "<":
            current_coords[who][0] -= 1

        visited.add((current_coords[who][0], current_coords[who][-1]))

    return len(visited)


assert visit_houses("^v") == 3, f'Error!!! {visit_houses("^v")} instead of 3'
assert visit_houses("^>v<") == 3, f'Error!!! {visit_houses("^>v<")} instead of 3'
assert visit_houses("^v^v^v^v^v") == 11, f'Error!!! {visit_houses("^v^v^v^v^v")} instead of 11'

print(visit_houses(INPUT))
