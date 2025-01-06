from flask import Flask
from routes import order_Blueprint
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
from models import db,init_app





load_dotenv()

file_path = os.path.abspath(os.getcwd())+r"\database\order.db"
print(file_path)
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] =f'sqlite:///{file_path}'
app.register_blueprint(order_Blueprint)
init_app(app)
migrate = Migrate(app,db)


if __name__ == '__main__':
    app.run(debug=True,port=5004)