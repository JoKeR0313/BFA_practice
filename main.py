from flask import *
import requests


app = Flask(__name__)
app.secret_key = 'development key'


class Address:

    def __init__(self, address, ):
        pass


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
