class RightAngleShape:
    def rightangleShape(n):
        for i in range(n):
            for j in range(i + 1):
                print('* ', end= '')
            print('')

RightAngleShape.rightangleShape(5)