from flask import Blueprint

user_Blueprint = Blueprint("user_api_routes",__name__,url_prefix="/api/user")

@user_Blueprint.route("/")
def index():
    return "hello"