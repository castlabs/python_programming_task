from datetime import datetime

import tests.utils.jwt as jwt_utils
from src.buissness_logic import generate_datetime_value
from src.buissness_logic import generate_jwt
from src.buissness_logic import generate_unique_value


def test_generate_unique_value():
    NUMBER_OF_TESTS = 100000

    # test optimized for efficiency
    unique_values = set()
    for _ in range(NUMBER_OF_TESTS):
        potentially_unique_value = generate_unique_value()

        before_add_size = len(unique_values)

        unique_values.add(potentially_unique_value)

        after_add_size = len(unique_values)

        assert before_add_size != after_add_size


def test_generate_datetime_value_is_not_from_future():
    datetime_value = generate_datetime_value()

    assert datetime_value < datetime.now()


def test_generate_jwt():
    expected_claims = {"name": "Kuba", "strength": "Code Quality +3"}

    jwt = generate_jwt(expected_claims)

    received_claims = jwt_utils.decode(jwt)

    assert received_claims == expected_claims
