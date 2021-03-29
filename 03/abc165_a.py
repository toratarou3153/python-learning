# ABC165A - We Love Golf

def main():
    # input
    K = int(input())
    A, B = map(int, input().split())

    # compute
    km=False
    for i in range(A,B+1):
        if i%K ==0:
            km=True

    # output
    if km:
        print("OK")
    else:
        print("NG")
if __name__ == '__main__':
    main()
