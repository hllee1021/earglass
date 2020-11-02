from flask import Blueprint, render_template, redirect, request, make_response, flash

# writed by seungsu

pages_bp = Blueprint("pages", __name__)

@pages_bp.route("/signup", methods=["GET"])
def get_main_admin():
    return render_template("signup.html")
    # /pages/signup