ClientID = 'D27XOJWmhRiNEgPtei5H'
ClientSecret = 'Dis2xjQawO'

import requests

headers = {
    'X-Naver-Client-Id': ClientID,
    'X-Naver-Client-Secret': ClientSecret
}
payload = {
    'source': 'en',
    'target': 'ko',
    'text': '''I was able to mitigate the issues by reinstalling the package/library
    as another user pointed out before me. I am using Python 3.8.2 in conjunction with pandas 1.0.1 without hiccup now.
    '''
}
res = requests.post('https://openapi.naver.com/v1/papago/n2mt',
              headers=headers, data=payload)
import pprint
# pprint.pprint(res.json())

print(res.json()['message']['result']['translatedText'])
