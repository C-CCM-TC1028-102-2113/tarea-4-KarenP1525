def main():
  #escribe tu código abajo de esta línea
    sum=0
    i=0
    num=float(input("Dame un numero: "))
    while (num>=0):
        sum=sum+num
        i=i+1
        num=float(input("Dame un numero: "))
    print("El promedio es: ",sum/i)

if __name__ == '__main__':
    main()
