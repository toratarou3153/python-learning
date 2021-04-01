def main():
    # input
    N=str(input())
    # compute
    a=0
    for i in range(len(N)):
        a+=int(N[i])

    if a%9 == 0:
        print("Yes")
    else:
        print("No")
    # output

if __name__ == '__main__':
    main()
