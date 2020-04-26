import googlemaps
import json

gmaps = googlemaps.Client(key='AIzaSyC2jeSpDJbj4ueR6ey8Lovbejfg4m3QxR8')

# directions_result = gmaps.directions(
#     newport_ri, cleveland_oh, mode="transit", departure_time=now)

# https://developers.google.com/maps/documentation/javascript/examples/places-placeid-finder?hl=ru
# https://developers.google.com/places/web-service/details

raiting = []
places = ['ChIJ24qgza1LtUYR0WNYdcqSsVI', 'ChIJh43O9AhLtUYR6Lh-M6hB2jU']

for i in range(0, len(places)):
    place = gmaps.place(places[i],
                        fields=['place_id', 'rating'], language='ru-RU')
    raiting.append(place)

print(raiting)

# def optimal_directions(len):
#     directions = []
#     for i in range(0, len - 1):
#         for j in range(i + 1, len):
#             directions.append((i, j))
#     return directions


# def correct_direction(matrix):
#     result = []
#     optimal = optimal_directions(len(matrix['destination_addresses']))
#     rows = matrix['rows']
#     for i in range(0, len(optimal)):
#         direction = rows[optimal[i][0]]['elements'][optimal[i][1]]
#         result.append({
#             'start': optimal[i][0],
#             'end': optimal[i][1],
#             'direction': direction
#         })

#     return result


# def return_directions_result(data, mode):
#     matrix = gmaps.distance_matrix(
#         data, data, mode=mode, language="ru-RU", units="metric")
#     return correct_direction(matrix)
