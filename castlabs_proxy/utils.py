import os
import secrets


def get_secret(secret_name: str, testing: bool = False):
    """
    It gets a secret configured with Docker, and defaults to a random value if we are
    on a testing phase.
    """
    secret_path = f'/run/secrets/{secret_name}'
    if os.path.exists(secret_path):
        with open(secret_path) as f:
            return f.read()
    elif testing:
        return secrets.token_hex()
    else:
        raise RuntimeError(f'{secret_name} not found')
