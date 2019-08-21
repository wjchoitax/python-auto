favorite_colors = ['red', 'orange', 'white', 'blue']

new_colors = []
for color in favorite_colors:
    new_colors.append(color + '\n')

file = open('hello.txt', 'w', encoding='utf-8')

file.writelines(new_colors)
file.close()

print('file operation ok..')
