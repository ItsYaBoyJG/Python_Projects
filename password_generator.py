"""

"""

import random
import string

file = open("pass.txt", "a")
ch = (input("Enter how strong you want your password to be "
            "'1 for Weak' "
            "'2 for Average' "
            "'3 for Strong' "))

n = input("What will the password be used for? ")

weak = range(5)
med = range(8)
strong = range(15)
lv1 = string.ascii_letters
lv2 = string.ascii_letters + string.digits
lv3 = string.ascii_letters + string.digits + string.punctuation


# print(f'The password, {pass_strength(ch)} will be used for {n}, make sure to write it down')


def pass_strength(x):
    if x == '1':
        return ''.join(random.choice(lv1) for _ in weak)
    elif x == '2':
        return ''.join(random.choice(lv2) for _ in med)
    elif x == '3':
        return ''.join(random.choice(lv3) for _ in strong)
    return x


wrd = pass_strength(ch)

print(f'The password, {wrd}, will be used for {n}')

file.write("Password: " + wrd)
file.write("               Website: " + n), '\n'

if __name__ == "__main__":
    pass_strength(ch)
