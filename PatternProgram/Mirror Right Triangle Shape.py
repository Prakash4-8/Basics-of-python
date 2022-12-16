class MirroredRightAngleShape:
    def mirrorRightangleShape(n):
        for i in range(n):
            for j in range(n - i - 1):
                print(' ', end='')
            for j in range(i + 1):
                print('*', end='')
            print('')
MirroredRightAngleShape.mirrorRightangleShape(5)