matrix = [
    [0, 1, 3],
    [5, 7, 8],
    [12, 34, 56]
]
print(f'Print first list {matrix[0]}')
print(f'Print Second list {matrix[1]}')
print(f'3rd list, 2nd item {matrix[2][1]}')

print("PRINT FULL LIST:")
print(len(matrix[0]))

for row in matrix:
    for item in row:
        print(item)
    print('\n')

