from flask import Blueprint

api = Blueprint('api', __name__)

from . import property_management, register, server, user
