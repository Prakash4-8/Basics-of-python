s_size = int(input('Enter the size of shape: '))
def alphabetA(size):
    for i in range(size+1):
        for j in range((size//2)+1):
            if ((j ==0 or j == size//2) and i != 0) or (i == 0 and j != size//2) or (i == size//2 and (j != 0 and j!= size//2)) :
                print('*', end='')
            else:
                print(' ', end='')
        print('')
alphabetA(s_size)