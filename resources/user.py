from flask_restful import Resource
from flask import request
import mysql.connector
from mysql.connector import Error

from mysql_connection import get_connection
from email_validator import validate_email, EmailNotValidError
from utils import hash_password


class UserRegisterResource(Resource):
    # 플라스크의 리소스를 상속받아서 http 메소드들을 사용하겠다. 
    # 클래스는 변수와 함수의 묶음!
    def post(self): 
        # 이게 아래의 data임.
        # {
        #     "username": "홍길동",
        #     "email": "abc@naver.com",
        #     "password": "1234"
        # }
        # 1. 클라이언트가 보낸 데이터를 받아준다. 
        # body 부분의 json
        data = request.get_json() #함수 동작은 매뉴얼에 들어있다. 
        # 인간의 요청은 대체로 두루뭉술함 컴퓨터 입장에서 절차와 방법을 만들어주세요.
        # 2. 이메일 주소 형식이 올바른지 확인한다. 이메일 체크하는 라이브러리가 엄청 많다. 찾아서 쓰면 됨 email-validator
        try : 
            validate_email( data['email'] )
        except EmailNotValidError as e :
            print(e) # 디버깅할 때 필요하니까 넣어두세요
            return {'result':'fail', 'error':str(e)}, 400 # 400:bad request
        
        # 3. 비밀번호 길이가 유효한지 체크한다. 
        # 만약 비번이 4자리 이상, 12자리 이하라고 한다면, 
        if len( data['password'] ) < 4 or len( data['password'] ) > 12 : # 비정상이면 체크하고 리턴하고 끝내는 것이 맞음 그래서 비정상 체크 
            return {'result':'fail', 'error':'비번 길이 에러'}, 400
            # 클라이언트 개발자도 데이터 제대로 들어가는지 체크한다. 데이터무결성과 보안이 중요하니까. 해킹 요청 시도 : d-dos 공격 서버에 요청이 많아서 다운시킴. 

        # 4. 비밀번호를 암호화한다. 보안 때문에 중요하다. 
        hashed_password = hash_password( data['password'] )
        print(hashed_password)

        # 5. DB에 이미 있는지 확인한다. 
        try : 
            connection = get_connection()
            query = """select * from user
                    where email = '%s';"""
            record = ( data['email'], )

        except Error as e:
            pass



        return 