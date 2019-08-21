
favorite_colors = ['red', 'blue', 'pink', 'brown']
print(favorite_colors)

result_list = []
for color in favorite_colors:
    if len(color) >= 5:
        result_list.append(color)

print(result_list)


# create.. add item
favorite_colors.append('white')

print(favorite_colors)

# update item
favorite_colors.insert(2, 'black')
print(favorite_colors)

# delete item with content
favorite_colors.remove('black')
print(favorite_colors)

del favorite_colors[1]
print(favorite_colors)

# search item(s)
print(favorite_colors[1:3])
