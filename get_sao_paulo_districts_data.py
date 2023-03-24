import requests, json, csv

# Documentation: https://servicodados.ibge.gov.br/api/docs/localidades#api-Distritos-municipiosMunicipioDistritosGet
api_url = "https://servicodados.ibge.gov.br/api/v1/localidades/municipios/3550308/distritos"
csv_path = "csv_files/sao_paulo_districts_names.csv"

def getDistrictsNames(api_url):
    response = requests.get(api_url)
    if response.status_code != 200:
        return
    districts = json.loads(response.text)
    data = []

    for district in districts:
        data.append(district["nome"])

    return data

def addToCsv(arr_districts, csv_path, arr_headers):
    with open(csv_path, "w") as district_csv:
        writer = csv.DictWriter(district_csv, arr_headers)
        writer.writeheader()
        for district in arr_districts:
            writer.writerow({arr_headers[0]: district})

data = getDistrictsNames(api_url)
addToCsv(data, csv_path, ["district_name"])