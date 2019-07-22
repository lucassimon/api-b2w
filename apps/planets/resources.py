from flask import request
# Third
from flask_restful import Resource
from mongoengine.errors import NotUniqueError, ValidationError

# Apps
from apps.responses import (
    resp_already_exists,
    resp_exception,
    resp_data_invalid,
    resp_ok
)
from apps.messages import MSG_INVALID_DATA, MSG_RESOURCE_CREATED

# Local
from .models import Planet
from .schemas import PlanetRegistrationSchema, PlanetSchema


class PlanetsResource(Resource):
    def post(self, *args, **kwargs):
        # Inicializo todas as variaveis utilizadas
        req_data = request.get_json() or None
        data, errors, result = None, None, None
        # password, confirm_password = None, None
        schema = PlanetRegistrationSchema()

        # Se meus dados postados forem Nulos retorno uma respota inválida
        if req_data is None:
            return resp_data_invalid('Planets', [], msg=MSG_INVALID_DATA)

        # Desserialização os dados postados ou melhor meu payload
        data, errors = schema.load(req_data)

        # Se houver erros retorno uma resposta inválida
        if errors:
            return resp_data_invalid('Planets', errors)

        try:
            model = Planet(**data)
            model.save()

        except NotUniqueError:
            return resp_already_exists('Planets', 'local')

        except ValidationError as e:
            return resp_exception('Planets', msg=MSG_INVALID_DATA, description=e.__str__())

        except Exception as e:
            return resp_exception('Planets', description=e.__str__())

        # Realizo um dump dos dados de acordo com o modelo salvo
        schema = PlanetSchema()
        result = schema.dump(model)

        # Retorno 200 o meu endpoint
        return resp_ok(
            'Planets', MSG_RESOURCE_CREATED.format('Planet'),  data=result.data
        )
