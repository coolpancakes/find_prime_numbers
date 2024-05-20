# Program that finds all the prime numbers in the range 0, 100

def main():
    solution = []

    for mainrange in range(51):
        multiple2 = mainrange * 2 - 1
        solution.append(multiple2)
        if mainrange == 500:
            break

    iii = []

    for multiple3 in range(334):
        iii.append(multiple3 * 3)

    v = []

    for multiple5 in range(200):
        iii.append(multiple5 * 5)

    vii = []

    for multiple7 in range(170):
        vii.append(multiple7 * 7)

    for numsiii in iii:
        if numsiii in solution:
            solution.remove(numsiii)

    solution.insert(2, 3)

    for numsv in v:
        if numsv in solution:
            solution.remove(numsv)

    for numvii in vii:
        if numvii in solution:
            solution.remove(numvii)

    solution.insert(3, 7)

    for numbers in solution:
        if numbers == -1:
            pass
        else:
            print(numbers)
    print(f"Length is:", len(solution))


if __name__ == "__main__":
    main()
