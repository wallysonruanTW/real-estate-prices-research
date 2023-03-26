import csv

from selenium import webdriver
from selenium.webdriver.common.by import By

def getCsvNumberOfRows(csv_path):
    row_count = -1

    for row in open(csv_path):
        row_count += 1

    return row_count

def saveToCsv(adress, price):
    csv_path = "csv_files/zap_imoveis_data.csv"
    headers = ["address", "price"]

    with open(csv_path, "a") as zapimoveis_csv:
        writer = csv.DictWriter(zapimoveis_csv, headers)

        if getCsvNumberOfRows(csv_path) > 0:
            writer.writerow({headers[0]: adress, headers[1]: price})
            return

        writer.writeheader()
        writer.writerow({headers[0]: adress, headers[1]: price})

# Link to the first page of the website, with the filter set to look for houses in São Paulo, SP, Brazil
zap_imoveis_url = "https://www.zapimoveis.com.br/venda/imoveis/sp+sao-paulo/"

browser = webdriver.Chrome()
browser.get(zap_imoveis_url)

parent_element = browser.find_elements(By.XPATH, r'/html/body/main/section/div[1]/div[3]/div[2]/div')[0]
elements = parent_element.find_elements(By.CLASS_NAME, "card-container")

for element in elements:
    price: str = element.find_elements(By.CLASS_NAME, "simple-card__price")[0].text
    address: str = element.find_elements(By.CLASS_NAME, "simple-card__address")[0].text
    saveToCsv(address, price)
