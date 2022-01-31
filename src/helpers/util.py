import logging
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


def repeat_prompt(prompt, fn):
    transient_failures = 0
    transient_falure_threshold = 5
    count = int(input(prompt))
    results = []

    for _ in range(count):
        try:
            result = fn()
            results.append(result)
            transient_failures = 0
        except HTTPError as e:
            if transient_failures >= transient_falure_threshold:
                logging.error("Too many transient errors. Exiting repeat loop")
                raise e

            logging.info("Transient error. Retrying request")
            transient_failures += 1
            count += 1

    return results
