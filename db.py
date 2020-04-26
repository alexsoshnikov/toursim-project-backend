from flask import Flask
from flask_pymongo import pymongo  # pip install Flask-PyMongo

CONNECTION_STRING = "mongodb+srv://Alex:init1234567890@cluster0-hmzhr.mongodb.net/test?retryWrites=true&w=majority"

client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('tourism')
data = pymongo.collection.Collection(db, 'data')
