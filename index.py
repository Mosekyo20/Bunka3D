from flask import Flask, render_template

Flask(__name__)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/modelos')
def modelos():
    return render_template('modelos.html')




if __name__ == "__main__":
    app.run(debug=True)

