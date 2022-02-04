"""
prints a N x M door mat where N is odd and M is 3 x N



"""

n = input()
m = input()


def doormat(n, m):
    s = '.|.'
    for i in range(1, n + 1):
        if not i > int(n / 2):
            print(((s * i) + (s * (i - 1))).center(m, '-'))
        else:
            if i == int(n / 2) + 1:
                print('WELCOME'.center(m, '-'))
            else:
                print(((s * (n - i + 1)) + (s * (n - i))).center(m, '-'))


if __name__ == '__main__':
    doormat(int(n), int(m))
