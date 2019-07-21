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
from apps.messages import MSG_NO_DATA, MSG_PASSWORD_WRONG, MSG_INVALID_DATA
from apps.messages import MSG_RESOURCE_CREATED

# Local
from .models import Planet
from .schemas import PlanetRegistrationSchema, PlanetSchema


class SignUp(Resource):
    def post(self, *args, **kwargs):
        # Inicializo todas as variaveis utilizadas
        req_data = request.get_json() or None
        data, errors, result = None, None, None
        # password, confirm_password = None, None
        schema = PlanetRegistrationSchema()

        # Se meus dados postados forem Nulos retorno uma respota inválida
        if req_data is None:
            return resp_data_invalid('Planets', [], msg=MSG_NO_DATA)

        # password = req_data.get('password', None)
        # confirm_password = req_data.pop('confirm_password', None)

        # verifico através de uma função a senha e a confirmação da senha
        # Se as senhas não são iguais retorno uma respota inválida
        # if not check_password_in_signup(password, confirm_password):
        #     errors = {'password': MSG_PASSWORD_WRONG}
        #     return resp_data_invalid('Users', errors)

        # Desserialização os dados postados ou melhor meu payload
        data, errors = schema.load(req_data)

        # Se houver erros retorno uma resposta inválida
        if errors:
            return resp_data_invalid('Planets', errors)

        # Crio um hash da minha senha
        # hashed = hashpw(password.encode('utf-8'), gensalt(12))

        # Salvo meu modelo de usuário com a senha criptografada e email em lower case
        # Qualquer exceção ao salvar o modelo retorno uma resposta em JSON
        # ao invés de levantar uma exception no servidor
        try:
            # data['password'] = hashed
            data['name'] = data['name'].lower()
            data['climate'] = data['climate'].lower()
            data['terrain'] = data['terrain'].lower()
            model = Planet(**data)
            model.save()

        except NotUniqueError:
            return resp_already_exists('Planets', 'local')

        except ValidationError as e:
            return resp_exception('Planets', msg=MSG_INVALID_DATA, description=e)

        except Exception as e:
            return resp_exception('Users', description=e)

        # Realizo um dump dos dados de acordo com o modelo salvo
        schema = PlanetSchema()
        result = schema.dump(model)

        # Retorno 200 o meu endpoint
        return resp_ok(
            'Planets', MSG_RESOURCE_CREATED.format('Planet'),  data=result.data,
        )
