import utils.csv_utils

from selenium import webdriver
from selenium.webdriver.common.by import By

# Link to the first page of the website, with the filter set to look for houses in São Paulo, SP, Brazil
imoveis_web_url = "https://www.imovelweb.com.br/imoveis-venda-sao-paulo-sp.html?iv_=__iv_p_1_a_14183648872_g_131270747251_w_kwd-320060452994_h_1001566_ii__d_c_v__n_g_c_537751034622_k_imovelweb_m_e_l__t__e__r__vi__&gclid=Cj0KCQjw2v-gBhC1ARIsAOQdKY1y8mXhbQGbaj3mFfLv2-Wh7lRkQ-v63JxJQnSpZUJhxE0Dh547e0gaAmxpEALw_wcB"
csv_path = "../../../data/raw/real_state/imovel_web/imoveis_web_data.csv"
csv_headers = ["address", "price"]

browser = webdriver.Chrome()
browser.get(imoveis_web_url)

parent_element = browser.find_elements(By.XPATH, r'/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div[2]')[0]
elements = parent_element.find_elements(By.CLASS_NAME, r'sc-i1odl-2')

for element in elements:
    price = element.find_elements(By.CLASS_NAME, r'sc-12dh9kl-4')
    address = element.find_elements(By.CLASS_NAME, r'sc-ge2uzh-1')

    if len(price) > 0:
        price = price[0].text

    if len(address) > 0:
        address = address[0].text

    if len(price) > 0 and len(address) > 0:
        utils.csv_utils.save_to_csv(address, price, csv_path, csv_headers)
