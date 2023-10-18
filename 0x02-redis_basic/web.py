#!/usr/bin/env python3
""" implementing an expiring web cache tracker """
from functools import wraps
import requests
import redis
from typing import Callable


cache = redis.Redis()


def counter(method: Callable) -> Callable:
    """ count how many times a url is read """
    @wraps(method)
    def wrapper(*args, **kwargs) -> str:
        """ the wrapper """
        url_key = 'count:{}'.format(url)

        cache.incr(url_key)
        cached_html = cache.get(url_key)
        if cached_html:
            return cached_html.decode('utf-8')
        result = method(url)
        cache.setex(url_key, 10, value=result)

        return result

    return wrapper


@counter
def get_page(url: str) -> str:
    """ get HTTP content of URL and return it """
    req = results.get(url)
    return req.text
