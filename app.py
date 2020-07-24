#para instalar todos os pacotes usar o comando "pip install -r requirements.txt"
from flask import Flask,request,jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class Desenvolvedor(Resource):
    def get(self):
        return {"hello":"world"}
    def get(self):
        return {"hello":"world"}
    def get(self):
        return {"hello":"world"}
    def get(self):
        return {"hello":"world"}

api.add_resource(Desenvolvedor, '/')

if __name__ == '__main__':
    app.run(debug=True)