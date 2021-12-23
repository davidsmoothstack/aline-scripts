import random
import json
import os
from functional import seq

# TODO: Turn into decorator
def to_json(input):
    return json.dumps(input)

def full_url(base_url, endpoint):
    f"{base_url}/{endpoint}"

def base_from_env(domain_env, port_env):
    domain = os.getenv(domain_env)
    port = os.getenv(port_env)    
    return f"{domain}:{port}"


#TODO: Remove
def random_ints(length):
    return seq.range(length)\
        .map(lambda _: str(random.randrange(9)))

#TODO: Remove
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

#TODO: Remove
def drivers_liscense():
    return random_ints(12)\
        .map(str)\
        .reduce(lambda acc, val: acc + val, "")
