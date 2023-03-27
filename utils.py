import csv

def get_csv_number_of_rows(csv_path):
    row_count = -1

    for row in open(csv_path):
        row_count += 1

    return row_count

def save_to_csv(adress, price, csv_path, arr_headers):
    with open(csv_path, "a") as imoveis_web_csv:
        writer = csv.DictWriter(imoveis_web_csv, arr_headers)

        if get_csv_number_of_rows(csv_path) > 0:
            writer.writerow({arr_headers[0]: adress, arr_headers[1]: price})
            return

        writer.writeheader()
        writer.writerow({arr_headers[0]: adress, arr_headers[1]: price})