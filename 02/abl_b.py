# ABLB - Integer Preference

def main():
    # input
    A, B, C, D = map(int, input().split())

    # compute
    if A<=C<=B or A<=D<=B:
        print("Yes")
    elif C<=A<=D or C<=B<=D:
        print("Yes")
    else:
        print("No")


    # output


if __name__ == '__main__':
    main()
