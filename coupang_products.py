import requests
from bs4 import BeautifulSoup
import pprint


PRODUCT_URL = 'https://www.coupang.com/np/campaigns/82/components/178155'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
}
products = []
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

        download_image(li.find('dl').find('dt').find('img')['src'])

def main():
    for page in range(1, 1000):
        res = requests.get(PRODUCT_URL + '?page=' + str(page), headers=HEADERS)
        soup = BeautifulSoup(res.text, 'html.parser')

        ul_tag = soup.select_one('#productList')
        try:
            li_list = ul_tag.find_all('li')
            generate_contents_with_list_tag(li_list)
            print(str(page) + '페이지 작업 완료..')
        except AttributeError:
            break


    save_to_excel(products)
    send_email_for_report()

    print('작업 끝났어요..')
    pprint.pprint(products)
    print(len(products))


main()