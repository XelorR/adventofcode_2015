INPUT = [c.rstrip() for c in open("input.txt").readlines()]


def additions_calc(dimensions: str) -> int:
    l, w, h = dimensions.split("x")
    l = int(l)
    w = int(w)
    h = int(h)
    ribbon = min([(l + w) * 2, (w + h) * 2, (h + l) * 2])
    bow = l * w * h
    return ribbon + bow


assert additions_calc("2x3x4") == 34
assert additions_calc("1x1x10") == 14

print(sum([additions_calc(b) for b in INPUT]))
