"""
Module to run the Flask server and start the background fetch
"""

import os
from datetime import datetime
from operator import attrgetter
from dataclasses import dataclass

from flask import Flask
from flask import render_template
from markupsafe import escape
from apscheduler.schedulers.background import BackgroundScheduler

from utils import load_json
from background import download_data

app = Flask(__name__)

scheduler = BackgroundScheduler(daemon=True)
scheduler.add_job(download_data, 'interval', minutes=5, next_run_time=datetime.now())
scheduler.start()


@dataclass
class Row:
    category: str
    month: str
    value: str
    period: str


@dataclass
class PremiumCollected:
    bank: list
    cash: list
    mobile: list


@app.route("/info")
def info():
    data = load_json(os.path.join('data', 'info.json'))
    return render_template('info.html', info=data)


@app.route("/")
def main():
    # loading data
    data = load_json(os.path.join('data', 'premium_collected.json'))

    # get the periods, e.g. 202011
    periods = data['metaData']['dimensions']['pe']

    # map the periods to what we find in the data rows, e.g. 'June 2022' -> '202206'
    period_map = {value['name']: key for key, value in data['metaData']['items'].items()}

    # parse the rows and assign the numeric period
    rows = [
        Row(category=row[0], month=row[1], value=row[2], period=period_map[row[1]])
        for row in data.get('rows')
    ]

    # sort by period
    data_sorted = sorted(rows, key=attrgetter('period'))

    # extract category values
    bank_data = [float(escape(r.value)) for r in data_sorted if r.category == 'Bank']
    cash_data = [float(escape(r.value)) for r in data_sorted if r.category == 'Cash']
    mobile_data = [float(escape(r.value)) for r in data_sorted if r.category == 'Mobile']

    # pass object and periods to template
    pc = PremiumCollected(bank=bank_data, cash=cash_data, mobile=mobile_data)
    return render_template('index.html', premium_collected=pc, periods=periods)


if __name__ == "__main__":
    # debug server
    # app.run(debug=True, host='0.0.0.0', port=80, passthrough_errors=True)

    # prod server
    app.run(host='0.0.0.0', port=80)
