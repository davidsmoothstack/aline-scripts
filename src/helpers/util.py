import random
from functional import seq


def random_ints(length):
    return seq.range(length)\
        .map(lambda _: str(random.randrange(9)))


def phone_number():
    def to_phone_number(acc, tup):
        special_index = [2, 5]
        (index, val) = tup

        if index in special_index:
            return f"{acc}{val}-"

        return f"{acc}{val}"

    return random_ints(10)\
        .map(str)\
        .enumerate()\
        .reduce(to_phone_number, "")


def drivers_liscense():
    return random_ints(12)\
        .map(str)\
        .reduce(lambda acc, val: acc + val, "")
