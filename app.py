from flask import Flask, jsonify, request  # pip install -U Flask
from bson.objectid import ObjectId
from flask_cors import CORS  # pip install -U flask-cors
from db import DATA
from directions import return_directions_result
from placeinfo import return_places_rating, return_place_info

app = Flask(__name__)

CORS(app)


def get_coordinates_from_db():
    result = []
    for field in DATA.find():
        result.append(field['coordinates'])
    return result


def get_places_from_db():
    result = []
    for field in DATA.find():
        result.append(field['place_id'])
    return result


@app.route('/api/directions', methods=['GET'])
def get_directions():
    result = return_directions_result(get_coordinates_from_db(), 'transit')
    return jsonify(result)


@app.route('/api/rating', methods=['GET'])
def get_rating():
    result = return_places_rating(get_places_from_db())
    return jsonify(result)


@app.route('/api/query', methods=['POST'])
def post_query():
    result = return_place_info(request.json)
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
