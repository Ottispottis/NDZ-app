from flask import Flask, render_template
from writeinfotojson import check
import datetime

app = Flask(__name__)


@app.route("/")
def birdnest():
    return render_template('data.html')


@app.route('/data')
def data():
    """send current content"""
    table = check()
    return table


if __name__ == "__main__":
    app.run(debug=False)
