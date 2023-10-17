#!/usr/bin/env python3
""" get all schools having a specific topic """


def schools_by_topic(mongo_collection, topic):
    """ return list of schools having matching topic """
    query = {'topics': {'$elemMatch': {'$eq': topic}}}
    result = mongo_collection.find(query)

    return (list(result))
