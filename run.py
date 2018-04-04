import os

from api import create_app

config_name = os.getenv('FLASK_CONFIG')
app = create_app(config_name)
# Blueprint names
from app.books import book
from app.users import user


from api import app


# Register the blueprints
app.register_blueprint(book)
app.register_blueprint(user)



if __name__ == '__main__':
    app.run()