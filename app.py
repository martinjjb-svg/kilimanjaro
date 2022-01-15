from flask import Flask, render_template, url_for


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/training_target")
def training_target():
    return render_template("training_target.html")


@app.route("/events")
def events():
    return render_template("events.html")


@app.route("/calendar")
def calendar():
    return render_template("calendar.html")


@app.route("/fund_raising")
def fund_raising():
    return render_template("fund_raising.html")


if __name__ == '__main__':
    app.run()
