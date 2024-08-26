#!/usr/bin/env python3
"""
Function provides statistics about Nginx logs stored in MongoDB, including top IPs.
"""

from pymongo import MongoClient

def get_nginx_stats():
    """Fetches and prints statistics from the Nginx logs collection."""
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx

    total_logs = collection.count_documents({})

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {method: collection.count_documents({"method": method}) for method in methods}

    status_check_count = collection.count_documents({"method": "GET", "path": "/status"})

    ip_counts = collection.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])
    
    ip_counts_list = list(ip_counts)

    print(f"{total_logs} logs")
    print("Methods:")
    for method in methods:
        print(f"\tmethod {method}: {method_counts[method]}")
    print(f"{status_check_count} status check")
    
    print("IPs:")
    for ip in ip_counts_list:
        print(f"\t{ip['_id']}: {ip['count']}")

if __name__ == "__main__":
    get_nginx_stats()

