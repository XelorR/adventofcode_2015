INPUT = [c.rstrip() for c in open("input.txt").readlines()]


def surface_calc(dimensions: str) -> int:
    l, w, h = dimensions.split("x")
    side1 = 2 * int(l) * int(w)
    side2 = 2 * int(w) * int(h)
    side3 = 2 * int(h) * int(l)
    return int(sum([side1, side2, side3]) + min([side1, side2, side3]) / 2)


assert surface_calc("2x3x4") == 58
assert surface_calc("1x1x10") == 42

print(sum([surface_calc(b) for b in INPUT]))
