"""
Developer: Sam Skywalker
Purpose: Learning
Date: 12022.05.09.03:32 to 12022.05.19.15:29
"""

import requests
import hashlib
import sys


def requestapi_data(query):
    url = 'https://api.pwnedpasswords.com/range/' + query
    response = requests.get(url)
    print(response)
    # if response.status_code != 200:
    #     raise RuntimeError(f'Error: {response.status_code}, Check the API & Try Again :(')
    return response


def read_response(response):
    print(response.text)


def leakedpass_count(hashes, hash_candidate):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_candidate:
            return count
    return 0


def passwordsec_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    # print(sha1password)
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = requestapi_data(first5_char)
    # print(response)
    return leakedpass_count(response, tail)


def main(args):
    for password in args:
        count = passwordsec_check(password)
        if count:
            print(f'\n Your password was leaked {count} times. You should consider changing it... \n')
        else:
            print("\n All good! No leaks found for your password :) \n")
    return "\t\n Done...\n"


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))






