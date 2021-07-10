from flask import Flask,request,jsonify
from method.blurp import blp

app=Flask(__name__)
app.register_blueprint(blp)

def create_app():
    return app