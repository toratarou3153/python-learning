def main():
    # input
    N,A,B = map(int,input().split())
    # compute

    cut = 0
    for i in range(N+1):
         As = sum(list(map(int,str(i))))
         if A<= As <=B:
             cut+=i
    # output
    print(cut)
if __name__ == '__main__':
    main()
