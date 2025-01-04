from flask import Blueprint,jsonify,request,make_response
from flask_login import login_user
from models import db,User
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_user, current_user, logout_user

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
        return make_response(jsonify(response), 400)  # 400 Bad Request

    return jsonify(response)

#create  login endpoint

@user_Blueprint.route("/login",methods=['POST'])

def login():
    username = request.form['username']
    password = request.form['password']

    user = User.query.filter_by(username=username).first()

    if not user:
        response =  {
                "message":f'{username} is not exists! :( )'
            }
        return make_response(jsonify(response),401)
    if check_password_hash(user.password,password) :
        user.update_api_key()
        db.session.commit()

        login_user(user)

        response = {
            "message":"logged in",
            "api_key":user.api_key
        }
        return make_response(jsonify(response),200)
    
    
    response = {"message":"access denied"}

    return make_response(jsonify(response),401)


# log out

@user_Blueprint.route("/logout",methods=['POST'])

def logout():
    if current_user.is_authenticated:
        logout_user()
        response = {"message":"logged out"}
        return make_response(jsonify(response),200)

    return make_response(jsonify({"message":"No user logged out"}),401)

@user_Blueprint.route("/<username>/exists",methods=['GET'])
def user_exists(username):
    user = User.query.filter_by(username=username).first()
    response = {"message":"user not found"}
    if not user:
        return make_response(jsonify(response),404)
    
    response = {"message":"user exists","user":user}
    return make_response(jsonify(response),200)

@user_Blueprint.route("/",methods=["GET"])
def get_current_user():
    # print(current_user)
    # print(current_user.is_authenticated)
    # print(current_user.serialize())
    if current_user.is_authenticated:
        return make_response(jsonify({"user":current_user.serialize()}),200)
    else:
        return make_response(jsonify({"message":"no user logged in "}),200)
