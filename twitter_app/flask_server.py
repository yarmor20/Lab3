from flask import Flask, render_template, request
from friends_location import main
from urllib.error import HTTPError

app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    return render_template("web-try.html")


@app.route("/register", methods=['POST'])
def register():
    name = str(request.form['username'])
    if name == '':
        return render_template("page_not_found.html")

    try:
        contex = {"map_location": main(name)}
    except HTTPError:
        return render_template("page_not_found.html")
    return render_template("friends_map.html", **contex)


if __name__ == '__main__':
    app.run(debug=True, port=5003)
