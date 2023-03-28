import csv
import datetime
import os
import pandas

from utils import csv_utils


def save_clean_data_to_csv(street, district, price, date, csv_path):
    headers = ["street", "district", "price", "date"]

    open_mode = "a"

    if os.path.isfile(csv_path) is False:
        open_mode = "x"

    with open(csv_path, open_mode) as zap_imoveis_csv:
        writer = csv.DictWriter(zap_imoveis_csv, headers)

        if csv_utils.get_csv_number_of_rows(csv_path) > 0:
            writer.writerow({headers[0]: street, headers[1]: district, headers[2]: price, headers[3]: date})
            return

        writer.writeheader()
        writer.writerow({headers[0]: street, headers[1]: district, headers[2]: price, headers[3]: date})


def get_street_and_district_from_address_column(address: str):
    full_address = address.split(",")
    separated_address = {
        "street": full_address[0],
        "district": full_address[1]
    }
    return separated_address


def get_only_the_numbers_from_price_column(price:str):
    return price.replace("R$", "")


def clean_zap_imoveis_data(raw_data_csv_path:str, path_to_store_the_cleaned_data:str):
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


raw_data_csv_path: str = "../../../data/raw/real_state/zap_imoveis/{date}_zap_imoveis_data.csv".format(
    date=datetime.date.today())
cleaned_data_csv_path: str = "../../../data/clean/real_state/zap_imoveis/{date}_zap_imoveis_data.csv".format(
    date=datetime.date.today())

clean_zap_imoveis_data(raw_data_csv_path, cleaned_data_csv_path)