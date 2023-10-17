#!/usr/bin/env python3
""" change all topics of a school document based one name """


def update_topics(mongo_collection, name, topics):
    """ update school topics """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
