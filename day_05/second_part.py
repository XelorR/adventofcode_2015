INPUT = [s.rstrip() for s in open("input.txt").readlines()]


def check_pairs(string: str) -> bool:
    for iter, letter in enumerate(string):
        try:
            if string.count(letter + string[iter + 1]) > 1:
                return True
        except IndexError:
            pass
    return False


def check_over_one(string: str) -> bool:
    for iter, letter in enumerate(string):
        try:
            if letter == string[iter + 2]:
                return True
        except IndexError:
            pass
    return False


def mastercheck_once(string: str) -> str:
    if check_pairs(string) and check_over_one(string):
        return "nice"
    else:
        return "naughty"


assert mastercheck_once("qjhvhtzxzqqjkmpb") == "nice"
assert mastercheck_once("xxyxx") == "nice"
assert mastercheck_once("uurcxstgmygtbstg") == "naughty"
assert mastercheck_once("ieodomkazucvgmuy") == "naughty"

print(sum([mastercheck_once(string) == "nice" for string in INPUT]))
