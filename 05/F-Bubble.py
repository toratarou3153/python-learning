def bubble_sort(As :list)->list:
    for i in range(len(As)-1):
        for j in range(len(As)-i+1):
            if As[j]>As[j+1]:
                As[j],As[j+1] = As[j+1],As[j]
    return As
def main():
    # input
    As = list(map(int,input().split()))

    # compute

    # output
    print(bubble_sort(As))
if __name__ == '__main__':
    main()
