
import json


def getJsonData(city):

    city += ".csv"

    with open('Data/csv-metadata.json') as f:
        data = json.load(f)

    numberRowstoSkip = data['skipRows']

    for url in data['tables']:
        if url['url'] == city:
            headers = [str(header['name']).strip(' ').replace("'","") for header in url['tableSchema']['columns']]
            return headers, numberRowstoSkip
    