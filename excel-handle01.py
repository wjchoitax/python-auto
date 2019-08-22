import openpyxl


def main():
    wb = openpyxl.load_workbook('C:\\Users\\KITRI\\Desktop\\examples\\06\\2017.12.1.xlsx')
    sheet = wb['Sheet']

    for cell in sheet['C']:
        print(cell.value)


main()
