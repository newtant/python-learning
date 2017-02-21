import sys
def calc_mean():
    mean = 0
    for number in sys.argv[1:]:
        mean += int(number)
    return mean / len(sys.argv)

if __name__ == '__main__':
    print(calc_mean())
