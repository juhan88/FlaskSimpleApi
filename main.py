from flask import Flask, jsonify, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class LoggedIn(Resource):
    def get(self):
        return {'loggedIn': True}

class SubmitSession(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        user = json_data['username']
        password = json_data['password']
        return jsonify(u=user,p=password)


api.add_resource(HelloWorld, '/')
api.add_resource(LoggedIn, '/loggedIn')
api.add_resource(SubmitSession, '/submitSession')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9191, debug=True)
