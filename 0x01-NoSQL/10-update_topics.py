#!/usr/bin/env python3
"""
This module contains the function update_topics.
"""

def update_topics(mongo_collection, name, topics):
    """
    Update all topics of the school document with the given name.

    Parameters:
    - mongo_collection: pymongo collection object
    - name (string): the school name to update
    - topics (list of strings): the list of topics approached in the school

    The function updates the documents that match the name with the new topics list.
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )

