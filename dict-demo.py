post = {
    'title': '오늘은 좋은날',
    'content': '조아요',
    'tag': ['good', 'python', 'pycharm'],
    'replies': [
        {
            'author': 'iu',
            'content': 'good'
        },
        {
            'author': 'kim',
            'content': 'bad'
        }
    ]
}
print(post.get('replies')[0].get('author'))

print(post['replies'][0]['author'])




