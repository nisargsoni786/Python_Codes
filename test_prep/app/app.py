from flask import Flask,request,jsonify,Blueprint

bp=Blueprint('bp',__name__)

@bp.route('/')
def index():
    return {"xyz":"Home page"}

@bp.route('/a')
def indexa():
    return "a page"

@bp.route('/b')
def indexb():
    return "b page"

@bp.route('/c',methods=['POST'])
def indexc():
    data=request.get_json()
    name=data['name']
    return {"name":name}

@bp.route('/d')
def indexd():
    return "d page"

@bp.route('/e')
def indexe():
    return "e page"
