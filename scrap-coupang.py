import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
}
res = requests.get('https://www.coupang.com/np/campaigns/82/components/178155',
                   headers=headers)

soup = BeautifulSoup(res.text, 'html.parser')

# 2. 데이터를 수집하여 list of list 로 만든다.
product_list = []

for li_tag in soup.select('#productList > li'):
    likes = 0
    try:
       likes = int(li_tag.select_one('a > dl > dd > div.other-info > div.rating-star > span.rating-total-count')
            .text.strip()[1:-1])
    except:
       pass

    product_list.append([
        li_tag.select_one('a > dl > dd > div.name').text.strip(),
        int(li_tag.select_one('a > dl > dd > div.price-area > div.price-wrap > div.price > em > strong')
              .text.strip().replace(',', '')),
        likes,
        'http:' + li_tag.select_one('a > dl > dt > img')['src']
    ])

print(product_list)
# 3. 엑셀로 저장한다.
# pandas 를 사용해서 엑셀로 저장한다. 코드는 단 세줄정도..
