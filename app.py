from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/how/")
def how():
    return render_template("how.html")

@app.route("/locations")
def locations():
    return render_template("locations.html")

@app.route("/area/<state>/<location>/")
def area(state,location):
    return render_template(f"area/{state}/{location}.html")

if __name__ == "__main__":
    app.run(debug=True)