from flask import Flask, render_template, request
from routes.search import search
app = Flask(__name__)

app.register_blueprint(search)


@app.route("/")
def index():
    # Return the HTML templates named "index.html" in the "templates" directory
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
