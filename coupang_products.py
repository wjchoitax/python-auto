import requests
from bs4 import BeautifulSoup

EMAIL_USER = 'soongon@gmail.com'
EMAIL_PASSWD = 'tnsrhsl30#)'

PRODUCT_URL = 'https://www.coupang.com/np/campaigns/82/components/178155'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
}
products = []

def send_email_for_report():
    import smtplib
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()
            smtp.login(EMAIL_USER, EMAIL_PASSWD)
            smtp.sendmail('alert@gmail.com', 'ssgoni@naver.com',
                          'coupang ok..')
            print('email sending ok..')
    except:
        print('mail sending fail..')

def save_to_excel(data, file_name):
    import pandas as pd
    df = pd.DataFrame(data)
    df.to_excel(file_name)
    print('save to excel..')


def download_image(img_url):
    import os
    try:
        os.mkdir('./images')
    except FileExistsError:
        pass

    file_name = './images/' + img_url[img_url.rindex('/')+1:]
    res = requests.get(img_url)

    with open(file_name, 'wb') as file:
        file.write(res.content)
        print(file_name + ' 파일 저장 완료..')


def generate_contents_with_list_tag(li_list):
    for li in li_list:
        try:
            products.append([
                li.find('dl').find('dd').find('div', {'class': 'name'}).text.strip(),
                int(li.find('dl').find('dd').find('div', {'class': 'price-area'}) \
                    .find('div').find('div', {'class': 'price'}).find('em').find('strong') \
                    .text.replace(',', '')),
                li.find('dl').find('dt').find('img')['src'],
                int(li.find('dl').find('dd').find('div', {'class': 'other-info'}) \
                    .find('div').find('span', {'class': 'rating-total-count'}).text[1:-1])
            ])
        except AttributeError as ae:
            print(ae, '파싱 에러 발생')
            continue

        download_image('https:' + li.find('dl').find('dt').find('img')['src'])

def main():
    for page in range(1, 1000):
        res = requests.get(PRODUCT_URL + '?page=' + str(page), headers=HEADERS)
        soup = BeautifulSoup(res.text, 'lxml')

        ul_tag = soup.select_one('#productList')
        try:
            li_list = ul_tag.find_all('li')
            generate_contents_with_list_tag(li_list)
            print(str(page) + '페이지 작업 완료..')
        except AttributeError:
            break


    save_to_excel(products, 'coupang-products.xlsx')
    send_email_for_report()


main()