from flask import Blueprint,render_template,session,redirect
from API.book_client import BookClient
from flask_login import current_user
from API.order_client import OrderClient

blueprint = Blueprint('frontend',__name__)

@blueprint.route('/',methods=['GET'])

def index():

    if current_user.is_authenticated:
        session['order']=OrderClient.get_order_from_session()
    
    try:
        print(f"1 {BookClient.get_books()}")
        books={'results':BookClient.get_books()['books']}
       # print(f"jawad {books['results']}")
        
    except:
        books={'results':[]}

    # books=BookClient.get_book()
    return render_template('index.html',books=books)