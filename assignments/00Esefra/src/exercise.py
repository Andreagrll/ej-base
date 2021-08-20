import math
def main():
    #escribe tu código abajo de esta línea
    radio= float(input("Dame el radio: "))

    area= 4 * math.pi*math.pow(radio,2)
    volumen= (4*math.pi*radio**3)/3

    print(f"El área de la esfera es: {area}")
    print(f"El volumen de la esfera es: {volumen}")
  
if __name__=='__main__':
    main()
