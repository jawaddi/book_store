from flask import Blueprint,render_template,session,redirect,request,flash,url_for
from API.book_client import BookClient
from flask_login import current_user
from API.order_client import OrderClient
from API.user_api import UserClient
import forms
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

@blueprint.route('/register',methods=['POST','GET'])
def register():
    form = forms.RegistrationForm(request.form)
    if request.method=='POST':
        if form.validate_on_submit():
            username = form.username.data 
            
            if UserClient.user_exists(username):
                flash("Please try another user name")
                return render_template("register.html",form=form)
            else:
                user = UserClient.create_user(form)
                if user:
                    flash('Registred.Please Login.')
                    return redirect(url_for("frontend.index"))
        else:
            flash("Errors")
    
    return render_template("register.html",form = form)

@blueprint.route('/login',methods=['GET','POST'])

def login():
    form = forms.LoginForm()
    if request.method=='POST':
        if form.validate_on_submit():
            api_key = UserClient.login(form)
            if api_key:
                session['user_api_key']=api_key
                user=UserClient.get_user()
                session['user']=user['user']
                flash("Welcome back")
                return redirect(url_for('frontend.index'))
            else:
                flash("Cannot login")
        else:
            flash("cannot login")
        
    return render_template('login.html',form=form)

@blueprint.route('/logout',methods=['GET'])
def logout():
    session.clear()
    flash('Logged out')
    return redirect(url_for("frontend.index"))
