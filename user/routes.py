from flask import Blueprint,jsonify,request
from models import db,User
from werkzeug.security import generate_password_hash,check_password_hash

user_Blueprint = Blueprint("user_api_routes",__name__,url_prefix="/api/user")

# get all the users
@user_Blueprint.route("/all",methods=['GET'])
def get_all_users():
    all_user = User.query.all()
    users = [user.serialize() for user in all_user]
    response = {
        "message":"get all the users",
        "users":users
    }

    return jsonify(response)


#create new user

@user_Blueprint.route("/create",methods=['POST'])

def create_user():
    try:
        print('jawad',request.form)
        user = User()
        user.username = request.form["username"]
        user.password = generate_password_hash(request.form["password"],method='pbkdf2:sha256')
        user.is_admin = True

        db.session.add(user)
        db.session.commit()

        response = {
            "message":"User has been created successfully",
            "user":user.serialize()
        }
    except Exception as e:
        print(str(e))
        response = {

            "message":"something went wrong while creating user "
        }

    return jsonify(response)




