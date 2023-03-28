import csv
import datetime
import os.path
import pandas

from selenium import webdriver
from selenium.webdriver.common.by import By


def get_csv_number_of_rows(csv_path):
    row_count = -1

    for row in open(csv_path):
        row_count += 1

    return row_count


def save_raw_data_to_csv(adress, price, date, csv_path):
    headers = ["address", "price", "date"]

    open_mode = "a"

    if os.path.isfile(csv_path) is False:
        open_mode = "x"

    with open(csv_path, open_mode) as imovel_web_csv:
        writer = csv.DictWriter(imovel_web_csv, headers)

        if get_csv_number_of_rows(csv_path) > 0:
            writer.writerow({headers[0]: adress, headers[1]: price, headers[2]: date})
            return

        writer.writeheader()
        writer.writerow({headers[0]: adress, headers[1]: price, headers[2]: date})


def save_clean_data_to_csv(street, district, price, date, csv_path):
    headers = ["street", "district", "price", "date"]

    open_mode = "a"

    if os.path.isfile(csv_path) is False:
        open_mode = "x"

    with open(csv_path, open_mode) as imovel_web_csv:
        writer = csv.DictWriter(imovel_web_csv, headers)

        if get_csv_number_of_rows(csv_path) > 0:
            writer.writerow({headers[0]: street, headers[1]: district, headers[2]: price, headers[3]: date})
            return

        writer.writeheader()
        writer.writerow({headers[0]: street, headers[1]: district, headers[2]: price, headers[3]: date})


def get_street_and_district_from_address_column(address: str):
    full_address = address.split(",")
    separated_address = {
        "street": full_address[0],
        "district": full_address[-1]
    }
    return separated_address


def get_only_the_numbers_from_price_column(price:str):
    return price.replace("R$", "")


def clean_imovel_web_data(raw_data_csv_path:str, path_to_store_the_cleaned_data:str):
    csv_file = pandas.read_csv(raw_data_csv_path)
    addresses = csv_file["address"].tolist()
    prices = csv_file["price"].tolist()
    dates = csv_file["date"].tolist()

    i = 0

    while i < len(addresses):
        price = get_only_the_numbers_from_price_column(prices[i])
        address = get_street_and_district_from_address_column(addresses[i])
        street = address["street"].strip()
        district = address["district"].strip()

        save_clean_data_to_csv(street, district, price, dates[i], path_to_store_the_cleaned_data)
        i += 1

# Link to the first page of the website, with the filter set to look for houses in São Paulo, SP, Brazil
imoveis_web_url = "https://www.imovelweb.com.br/imoveis-venda-sao-paulo-sp.html?iv_" \
                  "=__iv_p_1_a_14183648872_g_131270747251_w_kwd" \
                  "-320060452994_h_1001566_ii__d_c_v__n_g_c_537751034622_k_imovelweb_m_e_l__t__e__r__vi__&gclid" \
                  "=Cj0KCQjw2v-gBhC1ARIsAOQdKY1y8mXhbQGbaj3mFfLv2-Wh7lRkQ-v63JxJQnSpZUJhxE0Dh547e0gaAmxpEALw_wcB "
raw_data_csv_path = "../../../data/raw/real_state/imovel_web/{date}_imoveis_web_data.csv".format(date=datetime.date.today())
clean_data_csv_path = "../../../data/clean/real_state/imovel_web/{date}_imoveis_web_data.csv".format(date=datetime.date.today())

browser = webdriver.Chrome()
browser.get(imoveis_web_url)

parent_element = browser.find_elements(By.XPATH, r'/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div[2]')[0]
elements = parent_element.find_elements(By.CLASS_NAME, r'sc-i1odl-2')

for element in elements:
    price = element.find_elements(By.CLASS_NAME, r'sc-12dh9kl-4')
    street_and_door_number = element.find_elements(By.CLASS_NAME, r'sc-ge2uzh-0')
    district_and_city = element.find_elements(By.CLASS_NAME, r'sc-ge2uzh-2')

    if len(price) > 0:
        price = price[0].text

    if len(street_and_door_number) > 0:
        street_and_door_number = street_and_door_number[0].text.split(",")[0]

    if len(district_and_city) > 0:
        district_and_city = district_and_city[0].text.split(",")[0]

    if len(street_and_door_number) > 0 and len(district_and_city) > 0:
        address = street_and_door_number + ", " + district_and_city

    save_raw_data_to_csv(address, price, datetime.date.today(), raw_data_csv_path)

clean_imovel_web_data(raw_data_csv_path, clean_data_csv_path)