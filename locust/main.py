from flask import Flask 

app=Flask(__name__)

@app.route('/')
def index():
    return "index page"

@app.route('/a')
def indexa():
    return "index page a"

@app.route('/b')
def indexb():
    return "index page b"

@app.route('/c')
def indexc():
    return "index page c"

if __name__=='__main__':
    app.run(debug=True)