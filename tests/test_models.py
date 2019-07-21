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

    def test_name_field_is_required(self):
        """
        verifica se o campo nome é requirido
        """
        assert self.model._fields['name'].required is True

    def test_name_field_is_unique(self):
        """
        Verifico se o campo email é unico
        """
        assert self.model._fields['name'].required is True

    def test_name_field_is_str(self):
        """
        Verifico se o campo email é do tipo string
        """
        assert isinstance(self.model._fields['name'], StringField)

    def test_active_field_exists(self):
        assert 'active' in self.model._fields

    def test_all_fields_in_model(self):
        """
        Verifico se todos os campos estão de fato no meu modelo
        """
        fields = [
            'name', 'climate', 'terrain', 'created_at',  'updated_at'
        ]

        model_keys = [i for i in self.model._fields.keys()]

        fields.sort()
        model_keys.sort()

        assert fields == model_keys

# https://lucassimon.com.br/2018/10/serie-api-em-flask---parte-6---criando-e-testando-nosso-modelo-de-usuarios/
