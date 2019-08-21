
# file = open('hello.txt', 'r')
# lines = file.readlines()
# print(lines)
# file.close()

with open('hello.txt', 'r') as file:
    lines = file.readlines()
    print(lines)


