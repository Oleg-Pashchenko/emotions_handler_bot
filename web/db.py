import random
from datetime import datetime

import psycopg2
import os
import dotenv

dotenv.load_dotenv()


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
        "SELECT * FROM stories ORDER BY date;")
    elms = cur.fetchall()
    d = []
    for e in elms:
        d.append({
            'content_type': e[0].split('.')[-1],
            'content_paths': [e[0].split('/')[-1]],
            'title': e[1],
            'date': e[2]
        })
    conn.close()
    return elms

