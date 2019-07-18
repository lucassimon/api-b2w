from mongoengine import (
    BooleanField,
    StringField,
)

# Apps

from apps.planets.models import Planet


class TestPlanet:
    def setup_method(self):
        self.data = {
            'name': 'teste', 'climate': 'abc123',
            'terrain': 'bca321'

        }
        # create instance object planet
        self.model = Planet(**self.data)

    def test_name_field_exists(self):
        """
        Verifico se o campo name existe
        """
        assert 'name' in self.model._fields

# https://lucassimon.com.br/2018/10/serie-api-em-flask---parte-6---criando-e-testando-nosso-modelo-de-usuarios/
