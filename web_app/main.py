from flask import Flask, render_template
from writeinfotojson import check_data_and_write
import datetime

app = Flask(__name__)


@app.route("/")
def birdnest():
    return render_template('data.html')


@app.route('/data')
def data():
    # Sends an HTML table containing the information of pilots who violated the NDZ.
    table = check_data_and_write()
    return table


if __name__ == "__main__":
    app.run(debug=True)
