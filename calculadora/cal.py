import math

#ya me quedo la suma normal, ahora hay que intentar meter todo en un if

calculo = str(input("Escribe la operacion que vamos a realizar: suma, resta, division, multiplicacion o modulo: "))
cantidad = int(input("De cuantos numeros sera tu operacion 2 o 3: "))

if cantidad == 2: 

    if calculo == "suma":
        # primero intentare hacer una suma normal
        def suma(val1, val2):
            resultado  = val1 + val2
            print ("El resultado de la suma es: ", resultado)
        val1 = float (input("Ingresa el primero numero a sumar: "))
        val2 = float (input("Ingresa el segundo numero a sumar: "))
        suma(val1,val2)

        #copie la misma funcion solo lo adecue
    elif calculo == "resta":
        def resta(val1, val2):
            resultado  = val1 - val2
            print ("El resultado de la resta es: ", resultado)
        val1 = float (input("Ingresa el primero numero a restar: "))
        val2 = float (input("Ingresa el segundo numero a restar: "))
        resta(val1,val2)

    elif calculo == "multiplicacion":
        def multi(val1, val2):
            resultado  = val1 * val2
            print ("El resultado de la resta es: ", resultado)
        val1 = float (input("Ingresa el primero numero a multiplicar: "))
        val2 = float (input("Ingresa el segundo numero a multiplicar: "))
        multi(val1,val2)

    elif calculo == "division":
        def div(val1, val2):
            resultado  = val1 / val2
            print ("El resultado de la resta es: ", resultado)
        val1 = float (input("Ingresa el primero numero a dividir: "))
        val2 = float (input("Ingresa el segundo numero a dividir: "))
        div(val1,val2)

    elif calculo == "modulo":
        def mod(val1, val2):
            resultado  = val1 % val2
            print ("El resultado es: ", resultado)
        val1 = int (input("Ingresa el primero numero: "))
        val2 = int (input("Ingresa el segundo numero: "))
        mod(val1,val2)    
    else:
        print("opcion no valida")    

elif cantidad == 3:
        def suma(val1, val2, val3):
            resultado  = val1 + val2 + val3
            print ("El resultado de la suma es: ", resultado)
        val1 = float (input("Ingresa el primero numero a sumar: "))
        val2 = float (input("Ingresa el segundo numero a sumar: "))
        val3 = float (input("Ingresa el tercer numero a sumar: "))
        suma(val1,val2,val3)    
else:
    print("opcion no valida")   