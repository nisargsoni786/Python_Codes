from flask import Blueprint,url_for,render_template,redirect,request,flash,session
from db_connect import sess
from models import Log
from flask_login import login_user,logout_user,login_required
from werkzeug.security import generate_password_hash,check_password_hash
# from passlib.hash import sha256_crypt

auth=Blueprint('auth',__name__)

@auth.route('/register',methods=['POST',"GET"])
def register():
    if request.method=="POST":
        name=request.form.get("name")
        username=request.form.get("username")
        password=request.form.get("password")
        confirm_password=request.form.get("confirm")
        if password!=confirm_password:
            flash("Password Doesn't match Confirm password","danger")
            return render_template('register.html') 
        # secure_password=sha256_crypt.encrypt(str(password))
        secure_password=generate_password_hash(password,method='sha256')
        log=Log(name=name,username=username,password=secure_password)
        sess.add(log)
        sess.commit()
        return redirect(url_for('auth.login'))
    return render_template('register.html')

@auth.route('/login',methods=['POST','GET' ])
def login():
    if request.method=="POST":
        username=request.form.get('username')
        password=request.form.get('password')
        user=sess.query(Log).filter_by(username=username).first()

        print('n\n\n\n',check_password_hash(password,user.password),'\n\n\n\n')

        if user==None and not check_password_hash(password,user.password):
            flash("invalid username or password","danger")
            return redirect(url_for('auth.login'))

        login_user(user)
        
        flash("You are logged in...","success")
        return redirect('/home/'+str(user.id))

    return render_template('login.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))