n = 4
for j in range(1, n * 2):
    if j % 2 == 0:
        continue
    else:
        for i in range(1, n * 2 - j):
            print('  ', end='')
        for i in range(j * 2 - 1):
            print('* ', end='')
    print('')
