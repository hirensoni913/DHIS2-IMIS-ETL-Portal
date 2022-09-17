"""
This script is to pull the public analytics data
and store it in a file locally.
"""

import os
from datetime import datetime

import requests

from utils import save_json

BASE_URL = 'https://dhis-imis.swisstph-mis.ch'

# Add more charts here
# Make sure the query is URL decoded
charts = {
    'premium_collected': '/api/analytics?dimension=bOCrZguqyBl:trJaHzeHYnM;y0wlxDf8qDR;yP3GrmbXDRC&dimension=pe:LAST_12_MONTHS&showHierarchy=false&hierarchyMeta=false&includeMetadataDetails=true&includeNumDen=true&skipRounding=false&completedOnly=false&outputIdScheme=NAME&filter=ou:USER_ORGUNIT,dx:dQxo7a1fQNL'
}


def run():
    # get all charts into json files
    for name, query in charts.items():
        print(f"Downloading data: {name}")
        data = requests.get(f"{BASE_URL}{query}").json()
        file_path = os.path.join('data', f"{name}.json")
        save_json(filepath=file_path, data=data)
        print(f"Saved file at {file_path}")

    # print some stats and info to info.json file
    info = {
        'lastUpdated': str(datetime.now()),
        'charts': list(charts.keys())
    }
    file_path = os.path.join('data', "info.json")
    save_json(filepath=file_path, data=info)
    print(info)


if __name__ == '__main__':
    run()
