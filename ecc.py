from requests import get, post
from pprint import pprint
import json

baseUrl = 'http://localhost:8083'


def isAlive():
    headers = {
        "Content-Type": "application/json",
    }

    try:
        r = get(baseUrl+'/isalive/', headers=headers)

        res = json.loads(r.content)

        return res["text"]
    except Exception as e:
        return False


def add(a, b):
    headers = {
        'Content-Type': 'application/json',
    }
    body = {"a": a, "b": b}

    r = post(baseUrl+'/ec/add/', headers=headers, data=json.dumps(body))

    res = json.loads(r.content)

    return res


if __name__ == "__main__":
    isAlive = isAlive()

    if not isAlive:
        print("ECC API Server not running")
        print("exiting...")
        exit(0)

    print(isAlive)

    input = {
        "a": {
            "x": "0x030644e72e131a029b85045b68181585d97816a916871ca8d3c208c16d87cfd3",
            "y": "0x1a76dae6d3272396d0cbe61fced2bc532edac647851e3ac53ce1cc9c7e645a83"
        },
        "b": {
            "x": "0x0000000000000000000000000000000000000000000000000000000000000001",
            "y": "0x30644e72e131a029b85045b68181585d97816a916871ca8d3c208c16d87cfd45"
        }
    }

    pprint(add(**input))

