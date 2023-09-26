import random
from datetime import datetime

import psycopg2
import os
import dotenv

dotenv.load_dotenv()


def save(filename, name, date):
    conn = psycopg2.connect(
        host=os.getenv('DB_HOST'),
        database=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD')
    )
    cur = conn.cursor()
    date = datetime.strptime(date, "%d.%m.%Y")
    date = date.strftime("%Y-%m-%d")
    cur.execute(
        "INSERT INTO stories(filename, name, date) VALUES (%s, %s, %s)",
        (filename, name, date,))
    conn.commit()
    conn.close()


def get_story():
    stories = get_all_stories()
    return random.choice(stories)


def get_all_stories():
    conn = psycopg2.connect(
        host=os.getenv('DB_HOST'),
        database=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD')
    )
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM stories;")
    elms = cur.fetchall()
    conn.close()
    return elms


def delete_story(story):
    conn = psycopg2.connect(
        host=os.getenv('DB_HOST'),
        database=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD')
    )
    cur = conn.cursor()
    story = story.replace('delete-', '')
    print(story)
    cur.execute(
        "DELETE FROM stories WHERE name=%s;", (story, ))
    conn.commit()
    conn.close()
