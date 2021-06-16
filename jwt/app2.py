from flask import Flask,render_template,request,session,url_for,redirect,flash,session
from auth import auth
from models import Log
from db_connect import sess
from flask_login import LoginManager,login_required,current_user

app=Flask(__name__)

app.register_blueprint(auth)

login_manager=LoginManager()
login_manager.login_view='auth.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    return sess.query(Log).filter_by(id=id).first()

@app.route('/')
def home():
    return "Hello"

@app.route('/home/<int:id>',methods=['GET', 'POST'])
@login_required
def index(id):
    name=current_user.name
    return render_template('home.html',id=str(id)+"  "+name)


if __name__ == '__main__':
    app.secret_key="1234567890asdfg;lkjhj"
    app.run(debug=True)
