class DownTriangleShape:
    def downtriangleShape(n):
        for i in range(n):
            for j in range(n - i):
                print('* ', end='')
            print('')
DownTriangleShape.downtriangleShape(5)