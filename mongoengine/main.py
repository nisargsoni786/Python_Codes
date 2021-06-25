from flask import Flask,jsonify,request
from app.database.connect import connect_db
from app.controller.book_controller import bp as book_bp

app = Flask(__name__)
app.register_blueprint(book_bp)


@app.route('/')
def index():
    return "Home"

if __name__ == '__main__':
    connect_db()
    app.run(debug=True)