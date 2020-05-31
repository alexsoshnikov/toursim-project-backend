from flask_pymongo import pymongo  # pip install Flask-PyMongo
import json


CONNECTION_STRING = "mongodb+srv://Alex:init1234567890@cluster0-hmzhr.mongodb.net/test?retryWrites=true&w=majority"

client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('tourism')
DATA = pymongo.collection.Collection(db, 'places_information')

# result = []

# for field in DATA.find():
#     result.append({
#         "place_id": field['place_id'],
#         "name": field['name'],
#         "rating": field['rating'],
#         "formatted_address": field['formatted_address'],
#         "location": field['location'],
#         "price_level": field['price_level'],
#         "international_phone_number": field['international_phone_number']
#     })


# with open("data_places.json", "w", encoding="utf-8") as write_file:
#     json.dump(result, write_file)
