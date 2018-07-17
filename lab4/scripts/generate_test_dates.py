import os 
import json
from random import randint
from faker import Faker
from simpledu.models import db, User, Course, Chapter
from sqlalchemy.orm import sessionmaker

fake = Faker()

def iter_users():
    yield User(
            username='Jack Lee',
            email='jacklee@example.com',
            password='zxcvbnm',
            job='developer'
    )

def iter_courses():
    author = User.query.filter_by(username='Jack Lee').first()
    with open('/home/shiyanlou/lab4/datas/courses.json') as f:
        courses = json.loads(f.read())
        print(courses)
    for course in courses:
        yield Course(
                name=course['name'],
                description=course['description'],
                image_url=course['image_url'],
                author=author
        )

def iter_chapters():
    for course in Course.query:
        for i in range(randint(3, 10)):
            yield Chapter(
                    name=fake.sentence(),
                    course=course,
                    vedio_url='https://labfile.oss.aliyuncs.com/courses/923/week2_mp4/2-1-1-mac.mp4',
                    vedio_duration='{}:{}'.format(randint(10, 30), randint(10,59))
            )

def run():
    for user in iter_users():
        db.session.add(user)

    for course in iter_courses():
        db.session.add(course)

    for chapter in iter_chapters():
        db.session.add(chapter)

    try:
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()
