from flask import Blueprint, render_template, redirect, request, make_response, flash

# writed by seungsu

demo_bp = Blueprint("demo", __name__)

@demo_bp.route("/signup", methods=["GET"])
def get_main_admin():
    return render_template("signup.html")