"""
Par o impar

Lo primero que vamos a realizar es dar la bienvenida preguntando un número entre 1 y 1000

Cuando el usuario proporciona el número, comprobaremos si es par o impar y después imprimimos el mensaje con el resultado.

Ejemplo:

Mensaje que se muestra: ¿En qué número estás pensando?
Entrada: 25
Salida: ¡Es un número impar! ¿Puedes añadir otro?
     
"""

# Variable que utilizo como bandera en el while
bandera_ingreso = True

# Mensaje de bienvenida y mensaje de pedido de numero
print("Bienvenidos")
print("Elige un numero entre 1 y 1000 inclusive")

# Bucle principal de ingreso de valores
while (bandera_ingreso):

    # Manejador de error (Por si se ingresa un valor no entero)
    try:
        numero_ingresado = int(input("¿En que numero estas pensando? ")) # Input para ingreso del valor por teclado / Se castea el string a int

    # Si se ingresa un valor no valido dentro de los 'int'
    except: 
        print("Se ingreso un valor no valido, vuelva a ingresar el numero") # Mensaje de error
    
    # Si no sucede ningun error se sigue con la verificacion de paridad
    else:  
        
        # Condicional para verificar la paridad
        if (numero_ingresado % 2 == 0 and 1000 >= numero_ingresado > 0): # Si es par
            print("¡Es un numero par! ¿Quieres ingresar otro numero? (y/n)")
        elif (numero_ingresado % 2 != 0 and 1000 >= numero_ingresado > 0): # Si es impar
            print("¡Es un numero impar! ¿Quieres ingresar otro numero? (y/n)")
        else: # Si no se encuentra entre 1 y 1000
            print("El numero no se encuentra entre 1 y 1000")
            continue
        
        # While para verificar si continua en el programa    
        while (True):
            
            # Opcion ingresada para verificar si continua o no en el programa
            opcion_seguir = input()
            
            if (opcion_seguir == 'n' or opcion_seguir == 'N'): # Si no quiere continar
                bandera_ingreso = False 
                break 
            elif (opcion_seguir == 'y' or opcion_seguir == 'Y'): # Si se quiere continuar
                break
            else: # Si se ingreso otro caracter
                print("Ingrese 'y' o 'n' por favor") 
