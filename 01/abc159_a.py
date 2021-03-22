# ABC159A - The Number of Even Pairs

def main():
    # input
    N, M = map(int, input().split())

    # compute
    even=(N*(N-1))/2
    odd=(M*(M-1))/2



    # output
    print(int(even+  odd))


if __name__ == '__main__':
    main()
