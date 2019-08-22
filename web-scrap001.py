# 0. 대상 페이지를 설정한다.
# 1. 페이지의 소스를 가져온다.
# 2. 소스(HTML) 내에 데이터를 파싱해서
# 3. 파이썬 데이터로 만든다. (list, dict.. 즉, 메모리로 올린다)
# 4. 메모리에 있는 데이터를 저장(공유)한다.

# 1. requests 모듈을 설치해서 사용한다.

import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
}
res = requests.get('https://www.coupang.com/np/campaigns/82/components/178155',
                   headers=headers)

soup = BeautifulSoup(res.text, 'html.parser')
tag = soup.select_one('#\\31 37145559 > a > dl > dd > div.name')

print(tag.text.strip())








