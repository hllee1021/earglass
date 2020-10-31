from flask import Blueprint, render_template
import json


users_router = Blueprint("users_router", __name__)

@users_router.route("/", methods=["GET"])
def get_as_text_route():
  return render_template('index.html')