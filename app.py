from flask import Flask, render_template
from controllers import users

app = Flask(__name__, template_folder="views")
app.secret_key = "earglass"

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

app.register_blueprint(users.controller, url_prefix="/users")

app.run(port=8080, host="0.0.0.0", debug=True)
