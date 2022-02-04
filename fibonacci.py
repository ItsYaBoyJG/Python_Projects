"""
asks the user how many fibonacci numbers to generate and then generates them
#### Fibonnaci sequence is a sequence of numbers where the next number in the
sequence is the sum of the previous tow numbers in the sequence
"""


# n = int(input('Enter how many numbers you would like to generate in the sequence '))


def fibonacci(num):
    assert num > 0

    series = [1]

    while len(series) < num:
        if len(series) == 1:
            series.append(1)
        else:
            series.append(series[-1] + series[-2])

    for i in range(len(series)):  # Convert the numbers to strings
        series[i] = str(series[i])

    return ', '.join(series)


def main():
    print(fibonacci(int(input("Enter the numbers needed for the sequence"))))


if __name__ == '__main__':
    main()
