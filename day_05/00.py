INPUT = [s.rstrip() for s in open("input.txt").readlines()]


def check_vowels(string: str) -> bool:
    if sum([string.count(l) for l in "aeiou"]) >= 3:
        return True
    else:
        return False


def check_doubles(string: str) -> bool:
    if sum([(l + l) in string for l in string]) > 0:
        return True
    else:
        return False


def check_exlusion(string: str) -> str:
    if sum([sh in string for sh in ["ab", "cd", "pq", "xy"]]) == 0:
        return True
    else:
        return False


def mastercheck_once(string: str) -> str:
    if check_vowels(string) and check_doubles(string) and check_exlusion(string):
        return "nice"
    else:
        return "naughty"


assert mastercheck_once("ugknbfddgicrmopn") == "nice"
assert mastercheck_once("aaa") == "nice"
assert mastercheck_once("jchzalrnumimnmhp") == "naughty"
assert mastercheck_once("haegwjzuvuyypxyu") == "naughty"
assert mastercheck_once("dvszwmarrgswjxmb") == "naughty"

print(sum([mastercheck_once(string) == "nice" for string in INPUT]))
