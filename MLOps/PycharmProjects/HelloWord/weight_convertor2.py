weight = input('Weight: ')
weight_unit = input("(L)bs or (K)g: ")

if weight_unit.upper()=='L':
    print('You chose L')
    final_weight = float(weight) * 0.453592
elif weight_unit.upper()=='K':
    print('You chose K')
    final_weight = float(weight) / 0.453592

print(f'Your weight is {final_weight}')