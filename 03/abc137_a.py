# ABC137A - +-x

def main():
    # input
    A, B = map(int, input().split())

    # compute
    list=[A+B,A-B,A*B]
    list.sort()
    # output
    print(list[2])

if __name__ == '__main__':
    main()
