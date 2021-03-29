# ABC147A - Blackjack

def main():
    # input
    As = list(map(int, input().split()))

    # compute
    if sum(As)>=22:
        print("bust")
    else:
        print("win")

    # output


if __name__ == '__main__':
    main()
