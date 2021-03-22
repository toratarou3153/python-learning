# ABC183B - Billiards

def main():
    # input
    SX, SY, GX, GY = map(int, input().split())

    # compute
    x=SX+((GX-SX)/(GY+SY))*SY



    # output
    print(x)


if __name__ == '__main__':
    main()
