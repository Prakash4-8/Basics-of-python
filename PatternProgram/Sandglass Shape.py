class SandglassShape:
    def sandGlassShape(n):
        for i in range(n * 2):
            if i < n:
                for j in range(i):
                    print(' ', end='')
                for j in range(n - i):
                    print('* ', end='')
                print('')
            else:
                for j in range(2 * n - i - 1):
                    print(' ', end='')
                for j in range(i % n + 1):
                    print('* ', end='')
                print('')


SandglassShape.sandGlassShape(5)
