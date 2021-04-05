def my_max(num :list)->int:
    return num.sort(reverse=True)


def main():
    # input
    num = list(map(int,input().split()))
    # compute

    # output
    print(my_max(num[0]))
if __name__ == '__main__':
    main()

#未完
