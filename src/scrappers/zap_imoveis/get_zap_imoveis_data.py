import csv
import datetime
import os

from selenium import webdriver
from selenium.webdriver.common.by import By


def get_csv_number_of_rows(csv_path):
    row_count = -1

    for row in open(csv_path):
        row_count += 1

    return row_count


def save_to_csv(adress, price, csv_path):
    headers = ["address", "price", "date"]
    open_mode = "w"

    if os.path.isfile(csv_path):
        open_mode = "a"

    with open(csv_path, open_mode) as imoveis_web_csv:
        writer = csv.DictWriter(imoveis_web_csv, headers)

        if get_csv_number_of_rows(csv_path) > 0:
            writer.writerow({headers[0]: adress, headers[1]: price, headers[2]: datetime.date.today()})
            return

        writer.writeheader()
        writer.writerow({headers[0]: adress, headers[1]: price, headers[2]: datetime.date.today()})


# Link to the first page of the website, with the filter set to look for houses in São Paulo, SP, Brazil
zap_imoveis_url = "https://www.zapimoveis.com.br/venda/imoveis/sp+sao-paulo/"
csv_path = "../../../data/raw/real_state/zap_imoveis/{date}_zap_imoveis_data.csv".format(date=datetime.date.today())

browser = webdriver.Chrome()
browser.get(zap_imoveis_url)

parent_element = browser.find_elements(By.XPATH, r'/html/body/main/section/div[1]/div[3]/div[2]/div')[0]
elements = parent_element.find_elements(By.CLASS_NAME, "card-container")

for element in elements:
    price: str = element.find_elements(By.CLASS_NAME, "simple-card__price")[0].text
    address: str = element.find_elements(By.CLASS_NAME, "simple-card__address")[0].text
    save_to_csv(address, price, csv_path)
