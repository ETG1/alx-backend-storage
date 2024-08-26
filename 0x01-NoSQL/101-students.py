#!/usr/bin/env python3
"""
Function returns all students sorted by average score from a MongoDB collection.
"""

from pymongo import MongoClient

def top_students(mongo_collection):
    """Return a list of students sorted by average score."""
    students = mongo_collection.find()
    
    student_scores = []
    for student in students:
        scores = student.get('topics', [])
        if scores:
            total_score = sum(topic.get('score', 0) for topic in scores)
            average_score = total_score / len(scores)
        else:
            average_score = 0

        student_scores.append({
            '_id': student.get('_id'),
            'name': student.get('name'),
            'topics': scores,
            'averageScore': average_score
        })
    
    sorted_students = sorted(student_scores, key=lambda x: x['averageScore'], reverse=True)
    
    return sorted_students

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.school
    collection = db.students

    top_students_list = top_students(collection)
    for student in top_students_list:
        print(f"[{student['_id']}] {student['name']} - {student['topics']}")
        print(f"[{student['_id']}] {student['name']} => {student['averageScore']}")

