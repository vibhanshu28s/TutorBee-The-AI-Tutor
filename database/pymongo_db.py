import pymongo 
import os
from dotenv import load_dotenv

load_dotenv()

mongo_db = os.getenv("mongo_connector")


def create_database(): #name of user(child)

    myclient = pymongo.MongoClient(mongo_db)
    mydb = myclient["mydatabase"]   #name will be taken from form which is fill by user on home screen
