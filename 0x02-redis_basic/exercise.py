#!/usr/bin/env python3
""" create a Cache class with a private redis instance """
import redis
import uuid
from typing import Union

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
