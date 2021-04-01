def main():
    s=list(str(input()))
    t=list(str(input()))

    a=0
    for i in range(len(s)):
        if s[i] !=t[i]:
            a=1

    if a==0:
        print("Yes")
    else :
        print("No")

if __name__ == '__main__':
    main()
