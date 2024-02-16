from flask import Blueprint

bp = Blueprint("pages", __name__)


@bp.route("/")
def home():
    return "Hello, from Home!"


@bp.route("/about")
def about():
    return "Hello, from about"
