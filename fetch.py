import os
from datetime import datetime

import requests

from utils import save_json

BASE_URL = 'https://dhis-imis.swisstph-mis.ch'
charts = {
    'premium_collected': '/api/analytics?dimension=bOCrZguqyBl:trJaHzeHYnM;y0wlxDf8qDR;yP3GrmbXDRC&dimension=pe:LAST_12_MONTHS&showHierarchy=false&hierarchyMeta=false&includeMetadataDetails=true&includeNumDen=true&skipRounding=false&completedOnly=false&outputIdScheme=NAME&filter=ou:USER_ORGUNIT,dx:dQxo7a1fQNL'
}


def run():
    for name, query in charts.items():
        data = requests.get(f"{BASE_URL}{query}").json()
        file_path = os.path.join('data', f"{name}.json")
        save_json(filepath=file_path, data=data)
        print(file_path)
    info = {'lastUpdated': str(datetime.now())}
    file_path = os.path.join('data', "info.json")
    save_json(filepath=file_path, data=info)


if __name__ == '__main__':
    run()
