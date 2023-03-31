import datetime
import pandas

from src.entities.RealStateClean import RealStateClean


def get_street_without_door_number(address: str):
    full_address = address.split(",")
    street = "".join((letter for letter in full_address[0] if not letter.isdigit()))
    return street


def get_district(address: str):
    full_address = address.split(",")
    return full_address[-1]


def get_only_the_numbers_from_price(price: str):
    return price.replace("R$", "").replace(" ", "")


raw_data_csv_path = "../../../data/raw/real_state/imovel_web/{date}_imoveis_web_data.csv".format(
    date=datetime.date.today())
clean_data_csv_path = "../../../data/clean/real_state/imovel_web/{date}_imoveis_web_data.csv".format(
    date=datetime.date.today())

csv_file = pandas.read_csv(raw_data_csv_path)
addresses = csv_file["address"].tolist()
prices = csv_file["price"].tolist()
dates = csv_file["dateOfCreation"].tolist()

real_states_clean = []
i = 0
while i < len(addresses):
    price = get_only_the_numbers_from_price(prices[i])
    street = get_street_without_door_number(addresses[i])
    district = get_district(addresses[1])

    real_states_clean.append(RealStateClean(street, district, price, dates[i]))
    i += 1

real_states_data_frame = pandas.DataFrame(real_state.__dict__ for real_state in real_states_clean)
real_states_data_frame.to_csv(clean_data_csv_path)