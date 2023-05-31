from flask_restful import Resource

class SmokeApi(Resource):
    def get(self):
        return {'message': 'OK'}, 200