import os

try:
    os.mkdir('c:\\work-for-python')
except:
    print('디렉토리 있으므로 만들지 않습니다.')

os.chdir('c:\\work-for-python')
print(os.getcwd())

for i in range(200):
    file = open('scan-000' + str(i) + '-sdfsdf.pdf', 'w')
    print(file.name + ' created..')
    file.close()

print('job completed..')
