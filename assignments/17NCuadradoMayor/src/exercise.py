def main():
    import math
    num = int(input("Escribe un numero : "))
    elevado=0
    i=0
    while (elevado<=num):
        i=i+1
        elevado=math.pow(i,2)
    print(int(math.sqrt(elevado)))

    pass

if __name__ == '__main__':
    main()
