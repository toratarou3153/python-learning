#ABC164A - Sheep and Wolves

def main():
    # input
    S, W = map(int, input().split())

    # compute
    if W>=S:
        print("unsafe")
    else:
        print("safe")

    # output


if __name__ == '__main__':
    main()
