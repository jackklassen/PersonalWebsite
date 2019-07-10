from flask import Flask, render_template


app = Flask(__name__)


@app.route("/.html")
@app.route("/home.html")
@app.route("/index.html")
def home():
    return render_template('home.html')


if __name__ == '__main__':
   
    app.run(debug=True)
    