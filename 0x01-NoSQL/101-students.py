#!/usr/bin/env python3
'''Task 14's module.
'''


def top_students(mongo_collection):
    '''Prints all students in a collection sorted by average score.
    '''
    return mongo_collection.aggregate([
        {
            "$project": {
                '_id': 1,
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ])
