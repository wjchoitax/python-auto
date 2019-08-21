
try:
    with open('hell.txt', 'r') as file:
        lines = file.readlines()
        print(lines)
except FileNotFoundError as fne:
    print(fne)

print('the end..')
