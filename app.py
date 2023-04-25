from flask import Flask, render_template
from routes.search import search
from routes.add import add_rout
from routes.remove import remove
app = Flask(__name__)

app.register_blueprint(search)
app.register_blueprint(add_rout)
app.register_blueprint(remove)

@app.route("/")
def index():
    # Return the HTML templates named "index.html" in the "templates" directory
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
