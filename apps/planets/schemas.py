

from marshmallow import Schema, post_load
from marshmallow.fields import Str

# -*- coding: utf-8 -*-

# importar nossas CONSTANTES
from apps.messages import MSG_FIELD_REQUIRED


class PlanetRegistrationSchema(Schema):
    name = Str(required=True, error_messages={"required": MSG_FIELD_REQUIRED})
    climate = Str()
    terrain = Str()

    @post_load
    def lowerstrip(self, item, **kwargs):
        item["name"] = item["name"].lower().strip()

        if "climante" in item:
            item["climate"] = item["climate"].lower().strip()

        if "terrain" in item:
            item["terrain"] = item["terrain"].lower().strip()
        return item


class PlanetSchema(Schema):
    name = Str(required=True, error_messages={"required": MSG_FIELD_REQUIRED})
    climate = Str()
    terrain = Str()
