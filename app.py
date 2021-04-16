from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/play")
def block():
    return render_template('index.html')

@app.route("/play/<number>")
def block_number(number):
    return render_template('index2.html', repeat=int(number))

@app.route("/play/<number>/<color>")
def block_color(number, color):
    return render_template('index3.html', repeat=int(number), block_color=color)


if __name__ == "__main__":
    app.run(debug=True)