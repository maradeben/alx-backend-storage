#!/usr/bin/env python3
""" create a Cache class with a private redis instance """
import redis
import uuid
from typing import Union, Callable


class Cache:
    """ the Cache class """

    def __init__(self) -> None:
        """ initialize with a redis instance """
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    def store(self, data: Union[bytes, str, int, float]) -> str:
        """ store data in redis instance """
        key = str(uuid.uuid4())
        self._redis.set(key, data)

        return key

    def get(self, key: str, fn: Callable = None) -> \
            Union[str, bytes, float, int]:
        """ get value associated with key """
        value = self._redis.get(key)

        if fn is None:
            return value
        else:
            return fn(value)

    def get_str(self, key: str) -> str:
        """ returns value as a str """
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """ returns value as an int """
        return self.get(key, lambda x: int(x))
