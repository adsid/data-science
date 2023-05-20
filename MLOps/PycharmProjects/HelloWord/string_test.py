str_single_quote = "This string has 'single' quote"
str_double_quote = 'This string has "double" quote'
str_multi_line = ''' This is 
a multi-line
string, as you can
see'''

str_single_quoted ='This string has \'single\' quote'

print(str_single_quote)
print(str_double_quote)
print(str_multi_line)
print(str_single_quoted)

print(str_single_quote[0])
print(str_single_quote[-1])
print(str_single_quote[0:5])
print(str_single_quote[0:])
print(str_single_quote[:5])
print(str_single_quote[:])

print(str_double_quote[1:-1])

# formatted string
first = 'Adnan'
last = 'Siddiqui'
msg = first + '[' + last + '] is a coder'
msg1 = f'{first} [{last}] is a coder'
print(msg)
print(msg1)
print(len(msg))

print(msg.upper())
print(msg.upper().isupper())
print(msg.lower())
print(msg.find('q'))
print(msg.find('z'))

print(msg.find('coder'))

print(msg.replace('coder', 'developer'))
print(msg)

print('coder' in msg)
print('dog' in msg)

print(msg.title());