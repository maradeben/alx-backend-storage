#!/usr/bin/env python3
""" insert a new document in a collection based on kwargs
    return the new _id
"""


def insert_school(mongo_collection, **kwargs):
    """ insert kwargs into collection """
    result = mongo_collection.insert_one(kwargs)

    return result.inserted_id
