def main():
    height = int(input("Enter triangle height: "))
    #escribe tu código abajo de esta línea
    i=1
    
    while(i<=height):
        k=1
        espacios=height-i
        j=1
        asteriscos=height-espacios
        cadena=""
        while(j<=espacios):
            cadena=cadena+" "
            j=j+1
        while(k<=asteriscos):
            cadena=cadena+"*"
            k=k+1
        print(cadena,"\n")
        i=i+1
        


    pass

if __name__ == '__main__':
    main()
