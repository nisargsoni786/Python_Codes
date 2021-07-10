from flask import Blueprint,request

blp=Blueprint('blp',__name__)

@blp.route('/gett')
def a():
    return "Hello"

@blp.route('/postt',methods=['POST'])
def postt():
    data=request.get_json()
    data['surname']='soni'
    return data