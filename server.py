from flask import Flask, request
from flask_restful import Api, Resource
from flask_cors import CORS, cross_origin
from pathlib import Path
import tarfile
import shutil

app = Flask(__name__)
api = Api(app)

cors = CORS(app)

class Inbound(Resource):
    @cross_origin()
    def get(self):
        return "Hello world"

    @cross_origin()
    def post(self):
        json = request.get_json(force=True)
        data = json["data"]
        id = json["id"]
        Path("data/temp").mkdir(parents=True, exist_ok=True)
        with open("data/temp/" + id, 'w') as file:
            file.write(data)
        return id, 200

api.add_resource(Inbound, "/")

app.run(host="0.0.0.0", port=3000, debug=True)