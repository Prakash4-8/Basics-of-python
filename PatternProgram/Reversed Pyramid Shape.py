class ReversedPyramidShape:
    def reversedPyramidShape(n):
        for i in range(n):
            for j in range(i):
                print(' ', end= '')
            for j in range(n - i):
                print('* ', end='')
            print('')
ReversedPyramidShape.reversedPyramidShape(5)