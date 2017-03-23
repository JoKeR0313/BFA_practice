from flask import *


app = Flask(__name__)
app.secret_key = 'development key'


class Address:

    def __init__(self, country, address, zip_code):
        self.country = country
        self.address = address
        self.zip_code = zip_code

    def log_address(self):
        print("Address:", self.country, self.address, self.zip_code)

    def check_budapest(self):
        zip_code_str = str(self.zip_code)
        if zip_code_str[0] == "1":
            print("Your district is: {}".format(zip_code_str[1:3]))


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        country = request.form["country"]
        address = request.form["address"]
        zip_code = request.form["zip_code"]
        address1 = Address(country, address, zip_code)
        address1.log_address()
        address1.check_budapest()
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
