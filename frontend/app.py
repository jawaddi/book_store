from flask import Flask
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

from routes import blueprint

app = Flask(__name__,static_folder='static/images')

app.config["SECRET_KEY"] = 'Q7R8S9T0U1V2W3X4Y5Z6A7B8C9D0E1F2'
app.config["WTF_CSRF_SECRET_KEY"] = 'A1B2C3D4E5F6G7H8I9J0K1L2M3N4O5P6'
app.config["UPLOAD_FOLDER"] = 'static/images'
app.register_blueprint(blueprint)

login_manager=LoginManager(app)
login_manager.init_app(app)
login_manager.login_message='Please login.'
login_manager.login_view='frontend.login'

bootstrap = Bootstrap(app)

@login_manager.user_loader
def load_user(user_id):
    return None

if __name__=='__main__':
    app.run(debug=True,port=3000)
