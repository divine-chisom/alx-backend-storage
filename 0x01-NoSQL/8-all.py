#!/usr/bin/env python3
'''8. List all documents in Python.
'''


def list_all(mongo_collection):
    '''Lists all documents in a collection.
    '''
    docs = mongo_collection.find()
    return [i for i in docs]
