def get_csv_number_of_rows(csv_path: str) -> int:
    """
    :param csv_path: Path of the csv file of which you want to know the total of rows.
    :return: The total of rows in the specified csv file.
    """
    row_count = -1

    for row in open(csv_path):
        row_count += 1

    return row_count
