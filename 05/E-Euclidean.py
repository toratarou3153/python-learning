def gcd(As :list)->int:
    M,N=As[0],As[1]
    while N!=0:
        M,N = N,M%N
    return M

def main():
    # input

    # compute
    As = list(map(int,input().split()))

    # output
    print(gcd(As))
if __name__ == '__main__':
    main()
