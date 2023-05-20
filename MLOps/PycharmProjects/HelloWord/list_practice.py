names = ['Adnan', 'Abdul', 'Shameem', 'Ali', 'Fazal', 'Shahzad']
count_phrase = ''
for name_index in range(len(names)):
    if name_index==0:
        count_phrase = 'First'
    elif name_index==1:
        count_phrase = 'Second'
    elif name_index==2:
        count_phrase = 'Third'
    elif name_index==3:
        count_phrase='Fourth'
    else:
        count_phrase = 'Other'
    print(f'Name of my {count_phrase} friend is: "{names[name_index]}"')

print(names[2])
print(names[0:3])
print(names[-1])
print(names[-3:-1])
print(names[3:])
print(names[:4])
print(f'names[:]\t\t{names[:]}')
print(f'names\t\t\t{names}')

# Modify a list
names[1]='Afif'
print(names)

# List Exercise
# Write a program to find the largest number in a list
list_of_numbers=[3, 10, 5, 34, 99, 2, 43, 83]

largest_number = list_of_numbers[0];
for iNumber in list_of_numbers:
    if largest_number<iNumber:
        largest_number=iNumber
print(f'Largest number in the list is {largest_number}')


#List Operations
list_of_numbers=[3, 10, 5, 34, 99, 2, 10, 2, 43, 83]
list_of_numbers.append(90)
print(list_of_numbers)
list_of_numbers.insert(0, 59)
print(list_of_numbers)
list_of_numbers.remove(5)
print(list_of_numbers)
print(list_of_numbers.pop())
print(list_of_numbers.pop())
print(list_of_numbers)
print(f'Index of item 43 is: {list_of_numbers.index(43)}')
print(f'Does 50 exists in the list:  {50 in list_of_numbers}')
print(f'How many 10s in the list: {list_of_numbers.count(10)}')
print(f'How many 2s in the list: {list_of_numbers.count(2)}')
list_of_numbers.sort()
print(f'Print sorted list: {list_of_numbers}')
list_of_numbers.reverse()
print(f'Print reversed list: {list_of_numbers}')
second_list = list_of_numbers.copy()
second_list.append(39)
print(f'list_of_numbers: {list_of_numbers}')
print(f'second_list: {second_list}')



list_of_numbers.clear()
print(list_of_numbers)