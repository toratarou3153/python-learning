# ABC176A - Takoyaki

def main():
    # input
    N, X, T = map(int, input().split())

    # compute
    syou=N//X
    if N%X ==0:
        print(syou*T)
    else :
        print((syou+1)*T)
    # output

if __name__ == '__main__':
    main()
