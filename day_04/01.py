from hashlib import md5

INPUT = "yzbqklnj"


md5("abcdef609043".encode()).hexdigest()


def mine_it(key: str) -> int:
    second_part = 0
    while True:
        if md5(f"{key}{second_part}".encode()).hexdigest().startswith("000000"):
            return second_part
        second_part += 1


print(mine_it(INPUT))
