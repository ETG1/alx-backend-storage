#!/usr/bin/env python3
"""
Function to insert a new document into a MongoDB collection.

:param mongo_collection: The pymongo collection object.
:param kwargs: Key-value pairs to be included in the document.
:return: The _id of the newly inserted document.
"""

import pymongo

def insert_school(mongo_collection, **kwargs):
    """
    Insert a new document into the MongoDB collection.

    :param mongo_collection: The pymongo collection object.
    :param kwargs: Key-value pairs to be included in the document.
    :return: The _id of the newly inserted document.
    """
    result = mongo_collection.insert_one(kwargs)
    return str(result.inserted_id)

