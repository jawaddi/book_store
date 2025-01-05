from flask import Blueprint ,request,jsonify

book_blueprint = Blueprint('book_api_routes',__name__,url_prefix="/api/book")

@book_blueprint.route("/all",methods=['GET'])
def get_all_books():
    return "all books"


@book_blueprint.route("/create",methods=['POST'])
def create_books():
    return "create book"

@book_blueprint.route("/<slug>",methods=['GET'])
def book_details():
    return "book details"

@book_blueprint.route("/",methods=['GET'])
def index():
    return "hello"
