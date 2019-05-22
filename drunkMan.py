import random

def movimiento(r,value,direccion,sentido):
    if r == value:
        direccion += sentido
        return direccion
    else:
        return direccion

def drunkMan(cuadras):
    x=0
    y=0
    for i in range(cuadras):
        r= random.randint(1,4)
        x=movimiento(r,1,x,1) #Movimiento al norte suma 1
        x=movimiento(r,2,x,-1) #Movimiento al sur suma -1
        y=movimiento(r,3,y,1) #Movimiento al este suma 1
        y=movimiento(r,4,y,-1) #Movimiento al oste suma -1
    posicion = abs(x) + abs(y)
    return posicion

def main():
    dosCuadras = 0 
    intentos = 1000
    for i in range(intentos):
        if 2 == drunkMan(10):
            dosCuadras += 1
        else:
            pass
    print("Veces a dos Cuadras: "+str(dosCuadras))
    print("Probabilidad: "+ str(dosCuadras/intentos))

if __name__ == "__main__":
    main()
    