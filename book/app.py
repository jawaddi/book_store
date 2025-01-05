from flask import Flask
from routes import book_blueprint
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
from models import db,Book,init_app

load_dotenv()
file_path = os.path.abspath(os.getcwd())+r"\database\book.db"
app = Flask(__name__)

app.config['SECRECT_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{file_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.register_blueprint(book_blueprint)

init_app(app)

migrate = Migrate(app,db)
if __name__ == '__main__':
    app.run(debug=True,port=5003)
