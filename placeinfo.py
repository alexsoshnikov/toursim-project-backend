import googlemaps
from flask import jsonify
import time
import calendar
import numpy as np
from properties import GOOGLE_API_KEY
from db import DATA
import json

gmaps = googlemaps.Client(key=GOOGLE_API_KEY)


# https://developers.google.com/maps/documentation/javascript/examples/places-placeid-finder?hl=ru
# https://developers.google.com/places/web-service/details


def return_places_rating(places):
    raiting = []
    for i in range(0, len(places)):
        place = gmaps.place(places[i], fields=[
                            'place_id', 'rating'], language='ru-RU')
        raiting.append({
            'rating': place['result']['rating'],
            'place_id': place['result']['place_id']
        })
    return raiting


def return_place_info(query):
    places = []
    info = gmaps.find_place(
        query['text'], input_type='textquery', language='ru-RU')

    for i in range(0, len(info['candidates'])):
        place = gmaps.place(info['candidates'][i]['place_id'], fields=[
                            'place_id', 'rating', 'formatted_address', 'geometry/location'], language='ru-RU')
        places.append({
            'rating': place['result']['rating'],
            'place_id': place['result']['place_id'],
            'address': place['result']['formatted_address'],
            'location': place['result']['geometry']['location'],
        })

    return places


def return_place_full_info(query):
    places = []
    info = gmaps.find_place(
        query['name'], input_type='textquery', language='ru-RU')

    for i in range(0, len(info['candidates'])):
        place = gmaps.place(info['candidates'][i]['place_id'], fields=[
                            'place_id', 'rating', 'name', 'formatted_address', 'review', 'geometry/location', 'international_phone_number'], language='ru-RU')

        places.append({
            'place_id': place['result']['place_id'] if 'place_id' in place['result'] else None,
            'name': place['result']['name'] if 'name' in place['result'] else None,
            'rating': place['result']['rating'] if 'rating' in place['result'] else None,
            'formatted_address': place['result']['formatted_address'] if 'formatted_address' in place['result'] else None,
            'location': place['result']['geometry']['location'] if 'geometry' in place['result'] else None,
            'international_phone_number': place['result']['international_phone_number'] if 'international_phone_number' in place['result'] else None,
            'category': query['class']
        })

    if len(places) != 0:
        DATA.insert_many(places)


with open('names.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# for i in range(0, len(data['places'])):
#     return_place_full_info(data['places'][i])
