
capacidad= 10
eleemntos= [0]*capacidad
tope= -1

print(" Teclea elementos de la pila (termina con -1)")

x=0
CLAVE= -1

while x!= CLAVE:
    entrada= input()
    if entrada.isdigit():
        x =int(entrada)
        if tope<capacidad -1:
            tope += 1
            eleemntos[tope] = x
        else:
            print("Excepcion: Pila llena")
            break
    else:
       print("Excepcion: Entrada no Valida")

if tope>=0:
    print("Elementos de pila:", end=" ")
    while tope>0:
        x= eleemntos[tope]
        tope= -1
        print(x,end=" ")
else:
    print("Pila vacia")