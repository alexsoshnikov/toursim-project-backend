from flask import Flask, jsonify, request  # pip install -U Flask
from bson.objectid import ObjectId
from flask_cors import CORS  # pip install -U flask-cors
import db

app = Flask(__name__)

CORS(app)


def get_data_db():
    result = []

    for field in db.data.find():
        result.append({'_id': str(field['_id']), 'name': field['name']})
    return result


@app.route('/api/data', methods=['GET'])
def get_client():
    result = get_data_db()
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
