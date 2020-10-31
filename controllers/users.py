from flask import Blueprint, render_template, redirect
import json


users_router = Blueprint("users_router", __name__)

@users_router.route("/login", methods=["GET"])
def get_login_page():
  return render_template('login.html')

@users_router.route("/login", methods=["POST"])
def post_login_data():
  return redirect("my")

@users_router.route("/my", methods=["GET"])
def get_my_page():
  return "성공적으로 로그인이 완료되었습니다."