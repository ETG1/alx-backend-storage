#!/usr/bin/env python3
"""
Script to list all documents in a MongoDB collection.

:param mongo_collection: The pymongo collection object.
:return: A list of documents in the collection. Returns an empty list if no documents are found.
"""

def list_all(mongo_collection):
    """
    Lists all documents in the given MongoDB collection.

    :param mongo_collection: The pymongo collection object.
    :return: A list of documents. Returns an empty list if no documents are present.
    """
    return list(mongo_collection.find())

