def main():
    # input
    N=int(input())
    ss = [input() for _ in range(N)]#複数の行に複数の入力

    # compute
    cuts=[0,0,0,0]
    for i in range(N):
        if ss[i]=="AC":
            cuts[0]+=1
        elif ss[i]=="WA":
            cuts[1]+=1
        elif ss[i]=="TLE":
            cuts[2]+=1
        else:
            cuts[3]+=1

    # output
    print("AC x",cuts[0])
    print("WA x",cuts[1])
    print("TLE x",cuts[2])
    print("RE x",cuts[3])
if __name__ == '__main__':
    main()
