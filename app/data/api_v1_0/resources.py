from flask import request, Blueprint
from flask_restful import Api, Resource

from .schemas import PlacaSchema, BlackSchema, ComunicationSchema, AlertSchema, UserSchema
from ..models import Placa, Black, Comunication, Alert, User
from app.data.api_v1_0.decorador import token_required

data_v1_0_bp = Blueprint('data_v1_0_bp', __name__)

placa_schema = PlacaSchema()
black_schema = BlackSchema()
comunication_schema = ComunicationSchema()
alert_schema = AlertSchema()
user_schema = UserSchema()

class PlacaListResource(Resource):
    @token_required
    def get(self):
        placas = Placa.get_all()
        result = placa_schema.dump(placas, many=True)
        return result

    def post(self):
        data = request.get_json()
        data_dict = placa_schema.load(data)
        plate = Placa(placa=data_dict['placa'],
                    fecha=data_dict['fecha'],
                    posicion=data_dict['posicion'],
                    tipo=data_dict['tipo'],
                    match=data_dict['match']
        )

        plate.save()
        resp = placa_schema.dump(plate)
        return resp, 201

class BlackListResource(Resource):
    def get(self):
        blacks = Black.get_all()
        result = black_schema.dump(blacks, many=True)
        return result
    
    @token_required
    def post(self):
        data = request.get_json()
        black_dict = black_schema.load(data)
        black = Black(placanegra=black_dict['placanegra'],
                    fechanegra=black_dict['fechanegra'],
                    status=black_dict['status'],
        )

        black.save()
        resp = black_schema.dump(black)
        return resp, 201

class ComunicationListResource(Resource):
    def get(self):
        comunications = Comunication.get_all()
        result = comunication_schema.dump(comunications, many=True)
        return result
    
    @token_required
    def post(self):
        data = request.get_json()
        comunication_dict = comunication_schema.load(data)
        comunication = Comunication(selector=comunication_dict['selector'],
                    flag=comunication_dict['flag'],
        )

        comunication.save()
        resp = comunication_schema.dump(comunication)
        return resp, 201

class AlertListResource(Resource):
    @token_required
    def get(self):
        alerts = Alert.get_all()
        result = alert_schema.dump(alerts, many=True)
        return result

    def post(self):
        data = request.get_json()
        alert_dict = alert_schema.load(data)
        alert = Alert(alertaplaca=alert_dict['alertaplaca'],
                    alertaselector=alert_dict['alertaselector'],
        )

        alert.save()
        resp = alert_schema.dump(alert)
        return resp, 201
    
class UserListResource(Resource):
    @token_required
    def get(self):
        users = User.get_all()
        result = user_schema.dump(users, many=True)
        return result
    @token_required
    def post(self):
        data = request.get_json()
        user_dict = user_schema.load(data)
        user = User(usuario=user_dict['usuario'],
                    key=user_dict['key'],
        )

        user.save()
        resp = user_schema.dump(user)
        return resp, 201


api = Api(data_v1_0_bp)

api.add_resource(PlacaListResource, '/api/v1.0/placa/', endpoint='placa_list_resource')
api.add_resource(BlackListResource, '/api/v1.0/black/', endpoint='black_list_resource')
api.add_resource(ComunicationListResource, '/api/v1.0/comunication/', endpoint='comunication_list_resource')
api.add_resource(AlertListResource, '/api/v1.0/alert/', endpoint='alert_list_resource')
api.add_resource(UserListResource, '/api/v1.0/user/', endpoint='user_list_resource')


