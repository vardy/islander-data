from flask import Flask, request
from flask_restful import Api, Resource
from pathlib import Path
import tarfile
import shutil

app = Flask(__name__)
api = Api(app)

class Inbound(Resource):
    def get(self):
        return "Hello world"

    def post(self):
        json = request.get_json(force=True)
        data = json["data"]
        id = json["id"]
        Path("data/temp").mkdir(parents=True, exist_ok=True)
        with open("data/temp/" + id, 'w') as file:
            file.write(data)
        return 200

api.add_resource(Inbound, "/")

app.run(host="0.0.0.0", port=3000, debug=True)