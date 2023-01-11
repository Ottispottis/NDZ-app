from flask import Flask, render_template
from writeinfotojson import write_to_file, check
import datetime

app = Flask(__name__)


@app.route("/")
def birdnest():
    return render_template('data.html')


@app.route('/data')
def data():
    """send current content"""
    check()
    return "names[0], emails[0]"


if __name__ == "__main__":
    app.run(debug=False)
