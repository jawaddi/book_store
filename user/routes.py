from flask import Blueprint,jsonify
from models import db,User
user_Blueprint = Blueprint("user_api_routes",__name__,url_prefix="/api/user")

@user_Blueprint.route("/all",methods=['GET'])
def get_all_users():
    all_user = User.query.all()
    users = [user.serialize() for user in all_user]
    response = {
        "message":"get all the users",
        "users":users
    }

    return jsonify(response)