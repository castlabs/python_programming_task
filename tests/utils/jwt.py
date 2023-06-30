import jwt as _jwt

from src._constants import HEX_STRING_SECRET
from src._constants import SIGNATURE_ALGHORITM


def decode(jwt_value):
    return _jwt.decode(
        jwt=jwt_value, key=HEX_STRING_SECRET, algorithms=[SIGNATURE_ALGHORITM]
    )
