#!/usr/bin/env python3
""" create a Cache class with a private redis instance """
import redis
import uuid
from typing import Any, Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ decorator to count how many times Cache methods
        are called
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        """ increment the counter for the method on call """
        if isinstance(self._redis, redis.Redis):
            self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """ decorator to keep track of inputs and outputs """
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        if isinstance(self._redis, redis.Redis):
            self._redis.rpush('{}:inputs'.format(method.__qualname__),
                              str(args))
            data = method(self, *args, **kwargs)
            self._redis.rpush('{}:outputs'.format(method.__qualname__),
                              str(data))
            return data
    return wrapper


def replay(fn: Callable) -> None:
    """ display call history of function """
    key = method.__qualname__
    cache = redis.Redis()
    calls = cache.get(key).decode("utf-8")
    inputs = cachel.lrange('{}:inputs'.format(key), 0, -1)
    ouputs = cache.lrange('{}:outputs'.format(key), 0, -1)
    print("{} was called {} times:".format(key, calls))
    for i, o in zip(inputs, outputs):
        print("{}(*{}) -> {}".format(name, i.decode('utf-8'),
                                     o.decode('utf-8')))


class Cache:
    """ the Cache class """

    def __init__(self) -> None:
        """ initialize with a redis instance """
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    @call_history
    @count_calls
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
