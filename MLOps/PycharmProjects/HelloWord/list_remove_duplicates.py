numbers = [2, 2, 5, 6, 6, 5, 2, 10, 9, 2, 11, 9, 8]
unique_list = []

for number in numbers:
    if number not in unique_list:
        unique_list.append(number)

print(f'unique_list: {unique_list}')