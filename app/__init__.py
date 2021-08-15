from flask import Flask

from app.exts import init_ext
from app.views import init_view
#

def create_app(config_filename='development'):
    app = Flask(__name__)
    app.config.from_object(config_filename)
    init_ext(app)
    init_view(app)
    return app