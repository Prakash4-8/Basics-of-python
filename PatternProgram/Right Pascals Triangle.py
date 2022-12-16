class RightPascalsTriangle:
    def rightpascalsTriangle(n):
        for i in range(2*n - 1):
            if i < n:
                for j in range(i + 1):
                    print('* ', end='')
                print('')
            else:
                for j in range(2 * n - i - 1):
                    print('* ', end='')
                print('')
RightPascalsTriangle.rightpascalsTriangle(5)