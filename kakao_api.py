import requests

headers = {
    'Authorization': 'KakaoAK 1285fd0d562b79b87e0605bdbf27bfa6'
}
params = {
    'query': '이효리'
}
res = requests.get('https://dapi.kakao.com/v2/search/web',
             headers=headers, params=params)

import pprint
pprint.pprint(res.json())
