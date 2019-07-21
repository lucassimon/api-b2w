

from marshmallow import Schema
from marshmallow.fields import Str

# -*- coding: utf-8 -*-

# importar nossas CONSTANTES
from apps.messages import MSG_FIELD_REQUIRED

class PlanetRegistrationSchema(Schema):
    name = Str(required=True, error_messages={MSG_FIELD_REQUIRED})
    climate = Str()
    terrain = Str()


class PlanetSchema(Schema):
    name = Str(required=True, error_messages={MSG_FIELD_REQUIRED})
    climate = Str()
    terrain = Str()
    # cpf_cnpj = Str()
    # active = Boolean()