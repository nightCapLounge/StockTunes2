from flask import Flask, request, Blueprint, render_template
from models.logging import logger
from time import strftime
import traceback

from flask_restplus import Resource, Api
from api.api_config import api

# Grab namespaces
from api.stock.endpoints.endpoints import _namespace as stock_current_endpoints
from api.core.endpoints.endpoints import _namespace as midi_endpoints

# Make us that good app
app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(error):
	app.logger.error('Page not found: %s', (request.path))
	return '404', 404

@app.errorhandler(Exception)
def unhandled_exception(error):
    app.logger.error(traceback.format_exc())
    return '500', 500


@app.after_request
def after_request(response):
    timestamp = strftime('[%Y-%b-%d %H:%M]')
    app.logger.info('%s - %s - %s - %s - %s - %s', 
        timestamp, request.remote_addr,request.method, 
        request.scheme, request.full_path, response.status)
    return response

@app.route("/")
def index():
    return render_template('index.html')


def initialize(flask_app):
    # Load up the configuration
    flask_app.config.from_object('config')
    flask_app.logger.addHandler(logger.GetLogHandler(flask_app.config["LOG_DIR"], flask_app.config["DEBUG_LOG_LEVEL"], flask_app.config["PROD_LOG_LEVEL"]))

    # Set blueprints and namespaces
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)

    api.add_namespace(stock_current_endpoints)
    api.add_namespace(midi_endpoints)

    # Register Blueprints
    flask_app.register_blueprint(blueprint)



if __name__ == '__main__':
    initialize(app)
    app.logger.info("\t> Application launching just fine.")
    app.run()


