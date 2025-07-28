# sum all integers

def sum_integers(x):
    sum = 0
    for i in str(x):
        sum += int(i)
    print(f"sum: {sum}")


if __name__ == "__main__":
    number = 1238975
    sum_integers(number)
