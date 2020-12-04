from hashlib import md5

INPUT = "yzbqklnj"


md5("abcdef609043".encode()).hexdigest()


def mine_it(key: str) -> int:
    second_part = 0
    while True:
        if md5(f"{key}{second_part}".encode()).hexdigest().startswith("00000"):
            return second_part
        second_part += 1


assert mine_it("abcdef") == 609043
assert mine_it("pqrstuv") == 1048970

print(mine_it(INPUT))
