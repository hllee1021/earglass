from flask import Flask, render_template
from controllers import users, admin
from werkzeug.wrappers import Request
import services

app = Flask(__name__, template_folder="views")
app.secret_key = "earglass"

class UserPopulateMiddleware(object):
    def __init__(self, app):
        self.app = app
    def __call__(self, environ, start_response):
        req = Request(environ, shallow=True)
        return self.app(environ, start_response)

app.wsgi_app = UserPopulateMiddleware(app.wsgi_app)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

# Blueprint(Routers)
app.register_blueprint(users.controller, url_prefix="/users")
app.register_blueprint(admin.controller, url_prefix="/admin")


# run
app.run(port=8080, host="0.0.0.0", debug=True)
