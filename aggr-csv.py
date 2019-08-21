import os
import glob
import csv


SALES_FILE_PATH = 'C:\\Users\\KITRI\\PycharmProjects\\hello-python\\examples\\05\\csv_files'


def get_sales_files():
    return glob.glob(os.path.join(SALES_FILE_PATH, '*.csv'))


def calc_total_sale(file_month):
    with open(os.path.join(SALES_FILE_PATH, file_month), 'r', encoding='utf-8') as file:
        sum_sales = 0
        for line in file.readlines()[1:]:
            sum_sales += int(line.split(',')[1])

        return sum_sales


def create_year_csv_from_result_data(result_data):
    with open('year_month_sales.csv', 'w', newline='', encoding='utf-8') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(['년', '월', '매출'])
        for index, month_data in enumerate(result_data):
            csv_writer.writerow(['2017', index + 1, month_data])


def main():
    result_data = []
    files = get_sales_files()
    for file_month in files:
        sum_sales_month = calc_total_sale(file_month)
        result_data.append(sum_sales_month)

    create_year_csv_from_result_data(result_data)
    print('job completed..')


main()
