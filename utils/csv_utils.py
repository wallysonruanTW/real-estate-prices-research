def get_csv_number_of_rows(csv_path):
    row_count = -1

    for row in open(csv_path):
        row_count += 1

    return row_count