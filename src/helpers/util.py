import json
import os
from requests.models import HTTPError


def get_env(env):
    result = os.getenv(env)

    if result is None:
        raise Exception(f"Environment variable '{env}' has no value")

    return result


def to_json(input):
    return json.dumps(input)


def base_from_env(domain_env, port_env):
    domain = get_env(domain_env)
    port = get_env(port_env)
    return f"{domain}:{port}"


def repeat(prompt, fn):
    transient_failures = 0
    transient_falure_threshold = 5
    count = int(input(prompt))
    results = []

    for i in range(count):
        try:
            results.append(fn())
            transient_failures = 0
        except HTTPError as e:
            if transient_failures >= transient_falure_threshold:
                raise e

            transient_failures += 1
            i -= 1

    return results
