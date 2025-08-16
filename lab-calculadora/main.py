def addmultiplenumbers(numeros):
  if not numeros:
    return 0
  else:
    return sum(numeros)

def multiplymultiplenumbers (numeros):
    if not numeros:
      return 0
    else:
      #para multiplicar la lista primero vamos a comenzar con un valor 1
      resultado = 1
      for a in numeros:
        resultado *= a
      return resultado  
    
def isiteven (numeros):
    #para validar si es par o no
    if numeros % 1 != 0:
      return False
    numeros = int(numeros)
    return numeros % 2 == 0

def isitaninteger(numeros):
    #para validar si es entero
    return  numeros % 1 == 0
    
def main():
  opcion = str(input("Ingresa que operación quieres hacer: suma, multiplicacion, par , entero  "))

  if opcion == "suma":
    ingresa = input("Por favor ingresa los valores que quieras sumar, separados por un espacio: ")
    #en esta parte como pueden ser valores negativos o algun error de usuario
    try:
      lista_numeritos = [float(numero) for numero in ingresa.split()]
      resultado = addmultiplenumbers(lista_numeritos)
      print("La suma de los valores es: ", resultado )
    except ValueError:
      print("Error: Ingresa solo numeros validos separados por espacios")

  elif opcion == "multiplicacion":
    ingresa = input("Por favor ingresa los valores que quieras multiplicar, separados por un espacio: ")
    
      #en esta parte como pueden ser valores negativos o algun error de usuario
    try:
      lista_numeritos = [float(numero) for numero in ingresa.split()]
      resultado = multiplymultiplenumbers(lista_numeritos)
      print("La multiplicacion de los valores es: ", resultado )
    except ValueError:
      print("Error: Ingresa solo numeros validos separados por espacios") 

  elif opcion == "par":
    ingresa = input("Por favor ingresa el valor que deseas saber si es par o impar  ")

     #en esta parte como pueden ser valores negativos o algun error de usuario
    try:
      numerito = float(ingresa)
      resultado = isiteven(numerito)
    except ValueError:
      print("Error: Ingresa un numero valido")

  elif opcion == "entero":
    ingresa = input("Por favor ingresa el valor que deseas saber si es entero:  ")

     #en esta parte como pueden ser valores negativos o algun error de usuario
    try:
      numerito = float(ingresa)
      resultado = isitaninteger(numerito)
    except ValueError:
      print("Error: Ingresa un numero valido") 

  else:     
    print("Error: Ingresa solo opciones validas") 

if __name__=="__main__":
  main()



