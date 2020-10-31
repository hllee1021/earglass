from flask import Flask, render_template
from controllers import users

app = Flask(__name__, template_folder="views")

@app.route("/", methods=["GET"])
def index():
    return "<h1>This is the index page</h1>"

app.register_blueprint(users.users_router, url_prefix="/users")

app.run(port=8080, host="0.0.0.0", debug=True)
