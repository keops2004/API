from marshmallow import fields

from app.ext import ma


class PlacaSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    placa = fields.String()
    fecha = fields.String()
    posicion = fields.String()
    tipo = fields.String()
    match = fields.Integer()

class BlackSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    placanegra = fields.String()
    fechanegra = fields.String()
    status = fields.String()

class ComunicationSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    selector = fields.String()
    flag = fields.String()

class AlertSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    alertaplaca = fields.String()
    alertaselector = fields.String()
    
class UserSchema(ma.Schema):
    id_usu = fields.Integer(dump_only=True)
    usuario = fields.String()
    key = fields.String()

# crear las clases de COMUNICACIONES y ALERTAS
# Comunicaciones se encargara de generar los protocolos de acciones ante X situaciones en funcion de status definidos ejem: protocolo 101 >> actualizacion automatica de lista negra, protocolo 202 >> envio de base de placas almacenadas.....
# Alertas se encargara de gestionar y almacenar los match detectados por el sistema. Se trabajaran en una lista aparte para mayor velocidad deprocesamiento.



