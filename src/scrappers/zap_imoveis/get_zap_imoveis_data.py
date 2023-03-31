import datetime

import pandas
from selenium import webdriver
from selenium.webdriver.common.by import By

from src.entities.RealState import RealState

# Link to the first page of the website, with the filter set to look for houses in São Paulo, SP, Brazil
zap_imoveis_url = "https://www.zapimoveis.com.br/venda/imoveis/sp+sao-paulo/"
raw_data_csv_path = "../../../data/raw/real_state/zap_imoveis/{date}_zap_imoveis_data.csv".format(
    date=datetime.date.today())

browser = webdriver.Chrome()
browser.get(zap_imoveis_url)

parent_element = browser.find_elements(By.XPATH, r'/html/body/main/section/div[1]/div[3]/div[2]/div')[0]
elements = parent_element.find_elements(By.CLASS_NAME, "card-container")
real_states = []

for element in elements:
    price: str = element.find_elements(By.CLASS_NAME, "simple-card__price")[0].text
    address: str = element.find_elements(By.CLASS_NAME, "simple-card__address")[0].text
    real_states.append(RealState(address, price))

real_states_dataFrame = pandas.DataFrame(real_state.__dict__ for real_state in real_states)
real_states_dataFrame.to_csv(raw_data_csv_path)
