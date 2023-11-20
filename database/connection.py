from pymongo import MongoClient

from configs.database_configs import database_configs


MONGODB_CONNECTION_STRING = database_configs.MONGODB_CONNECTION_STRING
DB_NAME = database_configs.DB_NAME
USERS_COLLECTION = database_configs.USERS_COLLECTION


client = MongoClient(MONGODB_CONNECTION_STRING)
database = client[DB_NAME]
users_collection = database[USERS_COLLECTION]
