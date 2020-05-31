import googlemaps
import json
from properties import GOOGLE_API_KEY

gmaps = googlemaps.Client(key=GOOGLE_API_KEY)

# directions_result = gmaps.directions(
#     newport_ri, cleveland_oh, mode="transit", departure_time=now)


def optimal_directions(len):
    directions = []
    for i in range(0, len):
        for j in range(0, len):
            directions.append((i, j))
    return directions


# работает неверно
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


def correct_matrix(matrix):
    order = matrix[1][0]
    list_of_coord = matrix[1][1]
    order_result = []
    final_result = []

    for i in range(0, len(order)):
        origin_order = order[i][0]
        destination_order = order[i][1]
        for origin in range(0, len(list_of_coord[origin_order])):
            for destination in range(0, len(list_of_coord[destination_order])):
                order_result.append(
                    (list_of_coord[origin_order][origin], list_of_coord[destination_order][destination]))

    for j in range(0, len(matrix[0])):
        final_result.append({
            'start': order_result[j][0],
            'end': order_result[j][1],
            'direction': matrix[0][j]
        })

    return final_result


def return_directions_result(data, mode):
    matrix = gmaps.distance_matrix(
        data, data, mode=mode, language="ru-RU", units="metric")
    return correct_direction(matrix)


def optimal_matrix(coordinates):
    requests = []
    divided_arr = [coordinates[d:d+10] for d in range(0, len(coordinates), 10)]

    for i in range(0, len(divided_arr)):
        for j in range(0, len(divided_arr)):   # range(i, lem()) - если убираем повтор
            requests.append((i, j))
    return requests, divided_arr


def optimal_request(points_list):
    directions_matrix = []
    correct_matrix = optimal_matrix(points_list)
    for i in range(0, len(correct_matrix[0])):
        idx = correct_matrix[0][i]
        result = gmaps.distance_matrix(
            correct_matrix[1][idx[0]], correct_matrix[1][idx[1]], mode='transit', language="ru-RU", units="metric")
        # directions_matrix.append(result)
        for row in range(0, len(result['rows'])):
            for el in range(0, len(result['rows'][row]['elements'])):
                directions_matrix.append(result['rows'][row]['elements'][el])

    return directions_matrix, correct_matrix


def return_connection(coordinates):
    response = optimal_request(coordinates)
    return correct_matrix(response)

