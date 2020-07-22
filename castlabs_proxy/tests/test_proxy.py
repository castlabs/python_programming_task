from datetime import datetime

import jwt


class TestProxy:
    def test_post_must_contain_a_json_payload(self, client):
        response = client.post('/')
        assert response.status_code == 400
        assert 'errors' in response.json.keys()
        assert 'Missing payload' in response.json['errors']

    def test_post_must_contain_a_user_key(self, client):
        current = datetime.now()
        current_str = current.strftime('%Y-%m-%d')

        data = {
            'date': current_str,
        }
        response = client.post('/', json=data)

        assert response.status_code == 400
        assert 'errors' in response.json.keys()
        assert 'Missing user' in response.json['errors']

    def test_post_must_contain_a_date_key(self, client):
        data = {
            'user': 'foo',
        }
        response = client.post('/', json=data)

        assert response.status_code == 400
        assert 'errors' in response.json.keys()
        assert 'Missing date' in response.json['errors']

    def test_post_date_must_be_in_YYYYMMDDHHMMSS(self, client):
        data = {
            'user': 'foo',
            'date': '20200801123000',
        }
        response = client.post('/', json=data)

        assert response.status_code == 200

        data['date'] = '2020-08-01 12:30:00'
        response = client.post('/', json=data)

        assert response.status_code == 400
        assert 'errors' in response.json.keys()
        assert 'Not a valid datetime value' in response.json['errors']

    def test_response_contains_a_jwt(self, client):
        data = {
            'user': 'foo',
            'date': '20200801123000',
        }
        response = client.post('/', json=data)

        assert response.status_code == 200
        assert 'x-my-jwt' in response.json['headers'].keys()

    def test_jwt_contains_iat_field(self, client):
        token = client.application.config['JWT_TOKEN']
        algorithm = client.application.config['JWT_ALGORITHM']
        data = {
            'user': 'foo',
            'date': '20200801123000',
        }
        response = client.post('/', json=data)
        encoded_jwt = response.json['headers']['x-my-jwt']
        decoded_jwt = jwt.decode(encoded_jwt, token, algorithms=algorithm)

        assert 'iat' in decoded_jwt.keys()

    def test_jwt_contains_jwt(self, client):
        token = client.application.config['JWT_TOKEN']
        algorithm = client.application.config['JWT_ALGORITHM']
        data = {
            'user': 'foo',
            'date': '20200801123000',
        }
        response = client.post('/', json=data)
        encoded_jwt = response.json['headers']['x-my-jwt']
        decoded_jwt = jwt.decode(encoded_jwt, token, algorithms=algorithm)

        assert 'jti' in decoded_jwt.keys()

    def test_jwt_contains_payload(self, client):
        token = client.application.config['JWT_TOKEN']
        algorithm = client.application.config['JWT_ALGORITHM']
        data = {
            'user': 'foo',
            'date': '20200801123000',
        }
        response = client.post('/', json=data)
        encoded_jwt = response.json['headers']['x-my-jwt']
        decoded_jwt = jwt.decode(encoded_jwt, token, algorithms=algorithm)

        assert 'payload' in decoded_jwt.keys()

    def test_payload_contains_username_and_date_fields(self, client):
        token = client.application.config['JWT_TOKEN']
        algorithm = client.application.config['JWT_ALGORITHM']
        data = {
            'user': 'foo',
            'date': '20200801123000',
        }
        response = client.post('/', json=data)
        encoded_jwt = response.json['headers']['x-my-jwt']
        decoded_jwt = jwt.decode(encoded_jwt, token, algorithms=algorithm)

        assert 'payload' in decoded_jwt.keys()
        assert 'username' in decoded_jwt['payload'].keys()
        assert 'date' in decoded_jwt['payload'].keys()

    def test_user_can_be_retreived_from_jwt(self, client):
        token = client.application.config['JWT_TOKEN']
        algorithm = client.application.config['JWT_ALGORITHM']
        data = {
            'user': 'foo',
            'date': '20200801123000',
        }
        response = client.post('/', json=data)
        encoded_jwt = response.json['headers']['x-my-jwt']
        decoded_jwt = jwt.decode(encoded_jwt, token, algorithms=algorithm)

        assert 'payload' in decoded_jwt.keys()
        assert 'username' in decoded_jwt['payload'].keys()
        assert 'foo' == decoded_jwt['payload']['username']

