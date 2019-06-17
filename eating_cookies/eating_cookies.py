#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


def eating_cookies(n, cache=None):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)


print(eating_cookies(1))
print(eating_cookies(3))

cookie_cache = {}


def eating_cookies_cached(n, cookie_cache):
    if n in cookie_cache:
        return cookie_cache[n]
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        number_cookies = eating_cookies_cached(
            n-1, cookie_cache) + eating_cookies_cached(n-2, cookie_cache) + eating_cookies_cached(n-3, cookie_cache)
    cookie_cache[n] = number_cookies
    return number_cookies


print(eating_cookies_cached(1, cookie_cache))
print(eating_cookies_cached(3, cookie_cache))
print(eating_cookies_cached(10, cookie_cache))
print(eating_cookies_cached(50, cookie_cache))
# if __name__ == "__main__":
#     if len(sys.argv) > 1:
#         num_cookies = int(sys.argv[1])
#         print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
#             ways=eating_cookies(num_cookies), n=num_cookies))
#     else:
#         print('Usage: eating_cookies.py [num_cookies]')
