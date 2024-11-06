import unittest
from settings.flask_app import create_app


class FlaskTestClass(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        app = create_app()
        app.config['TESTING'] = True
        cls.client = app.test_client()
        cls.token = cls.get_token()

    @classmethod
    def get_token(cls):
        payload = {'user': 'flask', 'pwd': 'flask123'}
        response = cls.client.post('/login', json=payload)
        data = response.get_json()
        return data.get('access_token')


    def test_base_incidencia_duplicate_delete_route(self):
        methods = ['duplicated', 'deleted']
        header = dict(Authorization=f'Bearer {self.token}')

        for method in methods:
            response = self.client.patch(
                f'/base-incidencia?id=1&metodo={method}', headers=header)
            data = response.get_json()

            self.assertEqual(response.status_code, 200)
            print(data)


    def test_tributo_competencia_duplicate_delete_route(self):
        methods = ['duplicated', 'deleted']
        header = dict(Authorization=f'Bearer {self.token}')

        for method in methods:
            response = self.client.patch(
                f'/tributo-competencia?id=1&metodo={method}', headers=header)
            data = response.get_json()

            self.assertEqual(response.status_code, 200)
            print(data)