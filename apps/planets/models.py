from datetime import datetime
# Third
from mongoengine import (
    BooleanField,
    DateTimeField,
    DictField,
    EmailField,
    EmbeddedDocument,
    EmbeddedDocumentField,
    StringField,
    URLField
)

# Apps
from apps.db import db


class Mixin(db.Document):
    """
    Default implementation for Planet fields
    """
    meta = {
        'abstract': True,
        'ordering': ['created']
    }

    created = DateTimeField(default=datetime.now)
    update = DateTimeField(default=datetime.utcnow)

# Abaixo fica o código para a classe Adress

# Abaixo fica o código para a classe User


class Planet(Mixin):
    '''
    Plantes
    '''
    meta = {'collection': 'planets'}

    name = StringField(max_length=200, required=True)
    terrain = StringField(max_length=200, default='unknown')
    climate = StringField(max_length=200, default='unknown')
