#!/usr/bin/env python3
"""
Function to find all schools by a specific topic.

:param mongo_collection: The pymongo collection object.
:param topic: The topic to search for in the school documents.
:return: A list of documents that contain the specified topic.
"""

def schools_by_topic(mongo_collection, topic):
    """
    Find all schools that have the specified topic.

    :param mongo_collection: The pymongo collection object.
    :param topic: The topic to search for in the school documents.
    :return: A list of documents that contain the specified topic.
    """
    return list(mongo_collection.find({"topics": topic}))

