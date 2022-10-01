from motor import Arduino
from time import sleep
from flask import Flask
from flask_restful import Resource
from flask_restful import Api
from flask_restful import reqparse
from datetime import datetime as dt

arduino = Arduino()
app = Flask(__name__)
api = Api(app)


class motor_control(Resource):
    def get(self):
        return {"status": "alive", "dt": str(dt.now())}

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("controle")
        data = parser.parse_args()
        arduino.controle(bytes(data["controle"], "utf-8"))
        return {"status": "work_motor", "data": data}


api.add_resource(motor_control, "/api/arduino/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
