# finds all prime numbers within the range 0, 100.

def main():
    number_range = []
    for nrange in range(100):
        number_range.append(nrange)

    ii = []

    for prime2 in range(1001):
        ii.append(prime2 * 2)

    iii = []

    for prime3 in range(1001):
        iii.append(prime3 * 3)

    v = []

    for prime5 in range(1001):
        v.append(prime5 * 5)

    vii = []

    for prime7 in range(1001):
        vii.append(prime7 * 7)

    for two in ii:
        if two in number_range:
            number_range.remove(two)

    for three in iii:
        if three in number_range:
            number_range.remove(three)

    for five in v:
        if five in number_range:
            number_range.remove(five)

    for seven in vii:
        if seven in number_range:
            number_range.remove(seven)

    number_range.remove(1)
    number_range.insert(0, 2)
    number_range.insert(1, 3)
    number_range.insert(2, 5)
    number_range.insert(3, 7)

    for prime_numbers in number_range:
        print(prime_numbers)

    print("\nThere are {} prime numbers in the range 0, 100!".format(len(number_range)))

if __name__ == "__main__":
    main()
