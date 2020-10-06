lines = int(input('How many star line in Star Pattern # 6 ?:'))
print('The required star pattern is:')

for i in range(lines, 0, -1):
    for k in range(lines, i, -1):
        print(' ', end='')
    for j in range(1, i * 2):
        print('*', end='')
    print()
