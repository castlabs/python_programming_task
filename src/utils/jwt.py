import jwt as _jwt


def generate_jwt(claims: dict, secret: str, algorithm: str) -> str:
    return _jwt.encode(
        payload=claims,
        key=secret,
        algorithm=algorithm,
    )
