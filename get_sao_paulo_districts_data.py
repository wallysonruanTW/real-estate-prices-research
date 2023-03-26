from array import array

import requests, json, csv

# Documentation: https://servicodados.ibge.gov.br/api/docs/localidades#api-Distritos-municipiosMunicipioDistritosGet
api_url = "https://servicodados.ibge.gov.br/api/v1/localidades/municipios/3550308/distritos"
csv_path = "csv_files/sao_paulo_districts_names.csv"

def getDistrictsNames(api_url: str):
    response = requests.get(api_url)
    if response.status_code is not 200:
        return
    districts = json.loads(response.text)
    data = []

    for district in districts:
        data.append(district["nome"])

    return data

def addToCsv(districts:array, csv_path:str, headers:array):
    with open(csv_path, "w") as district_csv:
        writer = csv.DictWriter(district_csv, headers)
        writer.writeheader()
        for district in districts:
            writer.writerow({headers[0]: district})

data = getDistrictsNames(api_url)
addToCsv(data, csv_path, ["district_name"])