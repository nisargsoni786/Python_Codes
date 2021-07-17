import os
from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)
    
    import bot
    app.register_blueprint(bot.bp)    
    app.add_url_rule('/', endpoint='index')

    return app

if __name__ == '__main__':
    app=create_app()
    app.run(debug=True)