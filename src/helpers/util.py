import json
import os
import helpers.store as store


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
    count = int(input(prompt))
    results = []

    for _ in range(count):
        try:
            results.append(fn())
        except:
            print("Error processing results")

    return results
