def main():
    index = int(input("Enter the index: "))
    n1=0
    i=1
    n2=1
    serie=0
    while (i<index):
        i=i+1
        serie=n1+n2
        n1=n2
        n2=serie
    print(serie)

    pass

if __name__ == '__main__':
    main()
