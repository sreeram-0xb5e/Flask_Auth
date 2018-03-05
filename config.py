from pymongo import MongoClient


WTF_CSRF_ENABLED = True
SECRET_KEY = 'A_Secret_Key'

DB_NAME = 'washi'

DATABASE = MongoClient()[DB_NAME]
POSTS_COLLECTION = DATABASE.history
USERS_COLLECTION = DATABASE.users
SETTINGS_COLLECTION = DATABASE.settings

DEBUG = True
