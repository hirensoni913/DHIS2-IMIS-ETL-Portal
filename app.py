import os
import json
from dataclasses import dataclass
from flask import Flask
from flask import render_template
from markupsafe import escape

from utils import load_json

app = Flask(__name__)


@dataclass
class Row:
    category: str
    month: str
    value: str

@app.route("/info")
def info():
    data = load_json(os.path.join('data', 'info.json'))
    return render_template('info.html', info=data)


@app.route("/premium_collected")
def premium_collected():

    data = load_json(os.path.join('data', 'premium_collected.json'))
    rows = [
        Row(category=row[0], month=row[1], value=row[2])
        for row in data.get('rows')
    ]
    bank_data = [float(escape(r.value)) for r in rows if r.category == 'Bank']
    cash_data = [float(escape(r.value)) for r in rows if r.category == 'Cash']
    mobile_data = [float(escape(r.value)) for r in rows if r.category == 'Mobile']
    print(bank_data)
    print(type(bank_data))
    j = json.dumps(bank_data)
    print(j)
    print(type(j))
    return render_template('premium_collected.html', bank_data=json.dumps(bank_data), cash_data=json.dumps(cash_data), mobile_data=json.dumps(mobile_data))


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080, passthrough_errors=True)
