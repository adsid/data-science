for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')

# nested loop exercise
numbers = [5, 2, 5, 2, 2]

for item in numbers:
    print('*' * item)

for item in numbers:
    output = ''
    for count in range(item):
        output += 'x'
    print (output)

numbers = [2, 2, 10]

for item in numbers:
    output = ''
    for count in range(item):
        output += 'x'
    print (output)