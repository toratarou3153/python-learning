def main():
    # input
    N=int(input())
    Ps = list(map(int,input().split()))
    # compute
    cut = 0
    for i in range(N-1):
        if Ps[i] == i+1:
            Ps[i],Ps[i+1] = Ps[i+1],Ps[i]
            cut+=1
    if Ps[-1]==N:
        cut+=1
    # output
    print(cut)
if __name__ == '__main__':
    main()
