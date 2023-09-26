import yadisk
import os
import dotenv

dotenv.load_dotenv()
y = yadisk.YaDisk(token=os.getenv('YANDEX_TOKEN'))


def upload_file(filename):
    y.upload(filename, f"/juicy_and_seekness/{filename}")


upload_file('3943698.mp4')
