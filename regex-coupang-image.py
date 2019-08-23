import requests
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
}
res = requests.get('https://www.coupang.com/np/campaigns/82/components/178155', headers=headers)

# 정규식을 통해서 해당되는 텍스트를 모두 가져온다.
img_regex = re.compile(r'''
src="\/\/         #
.*                #
\/thumbnails\/    #
[^"]+             #
\.jpg"            #
''', re.VERBOSE)

pattern_matched = img_regex.findall(res.text)

img_customed = []
for pattern in pattern_matched:
    img_customed.append('http:' + (pattern.strip()[5:-1]))

for img in img_customed:
    res = requests.get(img)
    with open('./images/' + img[img.rindex('/'):], 'wb') as file:
        file.write(res.content)
        print(img + ' saved..')

