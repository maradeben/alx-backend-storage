#!/usr/bin/env python3
""" parse mongo db database and extract stats """
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    coll = client.logs.nginx

    logs_count = coll.count_documents({})
    get_methods = coll.count_documents({'method':'GET'})
    post_methods = coll.count_documents({'method':'POST'})
    put_methods = coll.count_documents({'method':'PUT'})
    patch_methods = coll.count_documents({'method':'PATCH'})
    delete_methods = coll.count_documents({'method':'DELETE'})
    status_check = coll.count_documents({'method':'GET', 'path':'/status'})

    # print results
    print("{} logs".format(logs_count))
    print("Methods:")
    print("\tmethod GET: {}".format(get_methods))
    print("\tmethod POST: {}".format(post_methods))
    print("\tmethod PUT: {}".format(put_methods))
    print("\tmethod PATCH: {}".format(patch_methods))
    print("\tmethod DELETE: {}".format(delete_methods))
    print("{} status check".format(status_check))
