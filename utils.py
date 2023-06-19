from passlib.hash import pdkdf2_sha256
from config import Config


# 1. 원문 비밀번호를, 단방향으로 암호화하는 함수 
def hash_password(original_password) : 
    password = pdkdf2_sha256.hash(original_password + Config.SALT)
    return password


