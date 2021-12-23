import json
import os
import random

from functional import seq


def _get_env(env):
    result = os.getenv(env)

    if result is None:
        raise Exception(f"Environment variable '{env}' has no value")

    return result


def to_json(input):
    # TODO: Turn into decorator
    return json.dumps(input)


def full_url(base_url, endpoint):
    f"{base_url}/{endpoint}"


def base_from_env(domain_env, port_env):
    domain = _get_env(domain_env)
    port = _get_env(port_env)
    return f"{domain}:{port}"


def random_ints(length):
    #TODO: Remove
    return seq.range(length)\
        .map(lambda _: str(random.randrange(9)))


def phone_number():
    #TODO: Remove
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
    #TODO: Remove
    return random_ints(12)\
        .map(str)\
        .reduce(lambda acc, val: acc + val, "")
