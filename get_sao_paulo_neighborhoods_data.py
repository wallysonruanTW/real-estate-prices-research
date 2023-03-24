import requests, json


api_url = "https://servicodados.ibge.gov.br/api/v1/localidades/municipios/3550308/distritos"
response = requests.get(api_url)
teste = json.loads(response.text)

print(teste)