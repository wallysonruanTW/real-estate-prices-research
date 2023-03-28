import utils.csv_utils

from selenium import webdriver
from selenium.webdriver.common.by import By

# Link to the first page of the website, with the filter set to look for houses in São Paulo, SP, Brazil
zap_imoveis_url = "https://www.zapimoveis.com.br/venda/imoveis/sp+sao-paulo/"
csv_path = "../../../data/raw/real_state/zap_imoveis/zap_imoveis_data.csv"
csv_headers = ["address", "price"]

browser = webdriver.Chrome()
browser.get(zap_imoveis_url)

parent_element = browser.find_elements(By.XPATH, r'/html/body/main/section/div[1]/div[3]/div[2]/div')[0]
elements = parent_element.find_elements(By.CLASS_NAME, "card-container")

for element in elements:
    price: str = element.find_elements(By.CLASS_NAME, "simple-card__price")[0].text
    address: str = element.find_elements(By.CLASS_NAME, "simple-card__address")[0].text
    utils.csv_utils.save_to_csv(address, price, csv_path, csv_headers)
