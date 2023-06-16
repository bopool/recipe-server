# conda create -n lambda_app python=3.10
# conda env remove -n lambda_app
# lambda_app 가상환경에서 작업. 

from flask import Flask
from flask_restful import Api
from resources.recipe import RecipeListResource, RecipeResource 

app = Flask(__name__)
api = Api(app)
# app을 플라스크 api에 넣어서 사용하겠어. 

# 경로(path)와 API동작코드(resource)를 연결한다. flask의 문법대로. flask에게 알려주기. 
api.add_resource( RecipeListResource, '/recipes' )
api.add_resource( RecipeResource, '/recipes/<int:recipe_id_abc>' )

if __name__ == '__main__' : 
    app.run()

