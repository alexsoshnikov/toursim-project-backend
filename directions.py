import googlemaps
import json
from properties import GOOGLE_API_KEY

gmaps = googlemaps.Client(key=GOOGLE_API_KEY)

# directions_result = gmaps.directions(
#     newport_ri, cleveland_oh, mode="transit", departure_time=now)


def optimal_directions(len):
    directions = []
    for i in range(0, len - 1):
        for j in range(i + 1, len):
            directions.append((i, j))
    return directions


def correct_direction(matrix):
    result = []
    optimal = optimal_directions(len(matrix['destination_addresses']))
    rows = matrix['rows']
    for i in range(0, len(optimal)):
        direction = rows[optimal[i][0]]['elements'][optimal[i][1]]
        result.append({
            'start': optimal[i][0],
            'end': optimal[i][1],
            'direction': direction
        })

    return result


def return_directions_result(data, mode):
    matrix = gmaps.distance_matrix(
        data, data, mode=mode, language="ru-RU", units="metric")
    return correct_direction(matrix)
