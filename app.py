from flask import Flask, render_template, request
from controllers import users, admin, task, submitter, estimator
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
    user_id = request.cookies.get("user_id")
    user = users.get_user_by_id(user_id)
    if user:
        # admin:
        if user["Role"] == "관리자":
            pass

        # submitter:
        if user["Role"] == "제출자":
            pass

        # estimator:
        if user["Role"] == "평가자":
            pass

    return render_template("index.html")

# Blueprint(Routers)
app.register_blueprint(users.controller, url_prefix="/users")
app.register_blueprint(admin.controller, url_prefix="/admin")
app.register_blueprint(task.controller, url_prefix="/task")
app.register_blueprint(submitter.controller, url_prefix="/submitter")
app.register_blueprint(estimator.controller, url_prefix="/estimator")


# run
app.run(port=8080, host="0.0.0.0", debug=True)
