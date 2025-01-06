from flask import Blueprint,jsonify,request,make_response

order_Blueprint = Blueprint("order_api_routes",__name__,url_prefix="/api/order")
USER_API_URL = 'http://127.0.0.1:5001/api/user'
# get all the users
@order_Blueprint.route("/all",methods=['GET'])
def get_order():
    return "Open Order"

@order_Blueprint.route("/all",methods=['GET'])
def all_orders():
    return "all orders"

@order_Blueprint.route("/add-item",methods=['POST'])
def add_order_item():
    return "adding item"


@order_Blueprint.route("/checkout",methods=["POST"])

def checkout():
    return "checkout"


    

#create new user
