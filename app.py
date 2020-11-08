from flask import Flask, render_template, request
from controllers import users, admin
from werkzeug.wrappers import Request
import services

app = Flask(__name__, template_folder="views")
app.secret_key = "earglass"

@app.context_processor
def inject_user():
    def is_logged_in():
        user_id = request.cookies.get("user_id")
        user = services.users.get_user_by_id(user_id)
        if user: return user
        else: return False
    return dict(is_logged_in=is_logged_in)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

# Blueprint(Routers)
app.register_blueprint(users.controller, url_prefix="/users")
app.register_blueprint(admin.controller, url_prefix="/admin")


# run
app.run(port=8080, host="0.0.0.0", debug=True)
