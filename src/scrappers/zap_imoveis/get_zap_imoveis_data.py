import csv
import datetime
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from utils import csv_utils


def save_raw_data_to_csv(adress: str, price: str, date: datetime.date, csv_path: str) -> None:
    """Create a csv file if none exists, and name it accordingly to the following format:
    [date_of_execution]_zap_imoveis_data.csv

    :param adress:
    :param price:
    :param date:
    :param csv_path:
    :return: None
    """

    headers = ["address", "price", "date"]
    open_mode = "a"

    if os.path.isfile(csv_path) is False:
        open_mode = "x"

    with open(csv_path, open_mode) as zap_imoveis_csv:
        writer = csv.DictWriter(zap_imoveis_csv, headers)

        if csv_utils.get_csv_number_of_rows(csv_path) > 0:
            writer.writerow({headers[0]: adress, headers[1]: price, headers[2]: date})
            return

        writer.writeheader()
        writer.writerow({headers[0]: adress, headers[1]: price, headers[2]: date})


# Link to the first page of the website, with the filter set to look for houses in São Paulo, SP, Brazil
zap_imoveis_url = "https://www.zapimoveis.com.br/venda/imoveis/sp+sao-paulo/"
raw_data_csv_path = "../../../data/raw/real_state/zap_imoveis/{date}_zap_imoveis_data.csv".format(
    date=datetime.date.today())

browser = webdriver.Chrome()
browser.get(zap_imoveis_url)

parent_element = browser.find_elements(By.XPATH, r'/html/body/main/section/div[1]/div[3]/div[2]/div')[0]
elements = parent_element.find_elements(By.CLASS_NAME, "card-container")

for element in elements:
    price: str = element.find_elements(By.CLASS_NAME, "simple-card__price")[0].text
    address: str = element.find_elements(By.CLASS_NAME, "simple-card__address")[0].text
    save_raw_data_to_csv(address, price, datetime.date.today(), raw_data_csv_path)