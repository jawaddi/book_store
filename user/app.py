from flask import Flask
from flask_login import LoginManager 
from routes import user_Blueprint
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
import models
import base64



load_dotenv()

file_path = os.path.abspath(os.getcwd())+r"\database\user.db"
print(file_path)
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SQLALCHEMY_DATABASE_URI'] =f'sqlite:///{file_path}'
#os.getenv('SQLALCHEMY_DATABASE_URI')


models.init_app(app)
app.register_blueprint(user_Blueprint)
login_manager = LoginManager(app)
migrate = Migrate(app,models.db) 

@login_manager.request_loader
def load_user_from_request(request):

    # first, try to login using the api_key url arg
    api_key = request.args.get('api_key')
    if api_key:
        user = models.User.query.filter_by(api_key=api_key).first()
        if user:
            return user

    # next, try to login using Basic Auth
    api_key = request.headers.get('Authorization')
    if api_key:
        api_key = api_key.replace('Basic ', '', 1)
        try:
            api_key = base64.b64decode(api_key)
        except TypeError:
            pass
        user = models.User.query.filter_by(api_key=api_key).first()
        if user:
            return user

    # finally, return None if both methods did not login the user
    return None

if __name__ == '__main__':
    app.run(debug=True)

