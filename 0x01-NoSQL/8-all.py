#!/usr/bin/env python3
""" list all documents in a mongodb collection """


def list_all(collection):
    """ list all docs in collection """
    docs = collection.find()

    if docs:
        return docs
    else:
        return []
