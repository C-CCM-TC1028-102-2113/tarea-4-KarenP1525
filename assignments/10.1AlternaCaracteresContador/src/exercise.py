def main():
  #escribe tu código abajo de esta línea

    num=int(input(" Ingresa un numero entero positivo: "))
    if(num>0):
        for i in range(1,num+1,1):
            if(i%2==0):
                print(i,"-%",end="\n" )
            else:
                print(i,"-#",end="\n" )
    else:
        print("Ingresa un número positivo")


if __name__ == '__main__':
    main()
