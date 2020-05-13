import googlemaps
import json
from properties import GOOGLE_API_KEY

gmaps = googlemaps.Client(key=GOOGLE_API_KEY)

# https://developers.google.com/maps/documentation/javascript/examples/places-placeid-finder?hl=ru
# https://developers.google.com/places/web-service/details

# place = gmaps.place('ChIJv21XTFtKtUYR8ikdmhgpqJM',
#                     fields=['price_level', 'rating'], language='ru-RU')


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


# query = {
#     'query': 'Музей Пушкина'
# }

# print(return_place_info(query))
