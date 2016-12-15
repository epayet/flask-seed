from flask import Blueprint, jsonify

from app.app_context import home_controller

main = Blueprint('main', __name__)


# TODO this does not work
@main.route('/', methods=['GET'])
def home():
    model = home_controller.model()
    return jsonify(model)
