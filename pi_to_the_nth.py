"""

Chudnovsky Algorithm
Find Pi to the Nth Digit
User enters Pi
prints Pi to the 'n'th

"""

import math


def square_root(number, one):
    """
    Calculate the square root of an integer, with the precision passed in as
    one.
    second order Newton-Raphson convergence.
    """
    floating_point_precision = 10 ** 16
    number_float = float((number * floating_point_precision) // one) / \
                   floating_point_precision
    num_x = (int(floating_point_precision * math.sqrt(number_float)) * one) // \
            floating_point_precision
    number_one = number * one
    while True:
        num_x_old = num_x
        num_x = (num_x + number_one // num_x) // 2
        if num_x == num_x_old:
            break
    return num_x


def pi_chudnovksy(one):
    """
    Calculate pi using a Chudnovksy's series.
    This calculates it in fixed point, using the precision passed in.
    """
    k = 1
    a_k = one
    a_tot = one
    b_tot = 0
    c = 640320
    c3_over_24 = c ** 3 // 24
    while True:
        a_k *= -(6 * k - 5) * (2 * k - 1) * (6 * k - 1)
        a_k //= k ** 3 * c3_over_24
        a_tot += a_k
        b_tot += k * a_k
        k += 1
        if a_k == 0:
            break
    total = 13591409 * a_tot + 545140134 * b_tot
    pi = (426880 * square_root(10005 * one, one) * one) // total
    return pi


def validate_nonNegative_integer():
    """
    Ask the user for input and only return when a nonnegative integer under
    10000 is given.
    """
    while True:
        s = input("How many digits of pi do you want to see? ")
        try:
            digits = int(s)
            if digits >= 10000:
                print("Enter a number smaller than 10000.")
            elif digits > 0:
                return digits
            else:
                print("Enter a nonnegative integer.")
        except ValueError:
            print("Enter a nonnegative integer.")


def main():
    digits = validate_nonNegative_integer()
    pi = str(pi_chudnovksy(10 ** (digits * 10)))[:digits]
    print(pi[0] + "." + pi[1:])


if __name__ == "__main__":
    main()
