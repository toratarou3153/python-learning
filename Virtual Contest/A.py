def main():
    # input
    X,t = map(int,input().split())
    # compute
    if X > t:
        print(X-t)
    else:
        print(0)
    # output

if __name__ == '__main__':
    main()
