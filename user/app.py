from flask import Flask
from routes import user_Blueprint
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
import models

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

migrate = Migrate(app,models.db) 

if __name__ == '__main__':
    app.run(debug=True)

