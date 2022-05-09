#!/usr/bin/env python3
'''T12. Log stats.
'''
from pymongo import MongoClient


def print_nginx_logs():
    '''Provides some stats about Nginx logs stored in MongoDB.
    '''
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    print('{} logs'.format(nginx_collection.count_documents({})))
    print('Methods:')
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        method_count = len(list(nginx_collection.find({'method': method})))
        print('\tmethod {}: {}'.format(method, method_count))
    statusChecks_count = len(list(
        nginx_collection.find({'method': 'GET', 'path': '/status'})
    ))
    print('{} status check'.format(statusChecks_count))
    print("IPs:")
    sorted_ips = nginx_collection.aggregate(
        [
            {
                '$group': {'_id': "$ip", 'totalRequests': {'$sum': 1}}
            },
            {
                '$sort': {'totalRequests': -1}
            },
            {
                '$limit': 10
            },
        ])
    for sorted_ip in sorted_ips:
        print(f"\t{sorted_ip.get('_id')}: {sorted_ip.get('count')}")

if __name__ == '__main__':
    print_nginx_logs()
