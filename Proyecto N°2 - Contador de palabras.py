"""

Contador de palabras
Preguntamos al usuario en que está pensando. Cuando se introduce la respuesta, realizará el conteo de palabras en la sentencia e imprimimos en la salida el resultado.

Ejemplo:

Pregunta: ¿En qué estás pensando?
Entrada: Bien, hoy es el día en el que me voy a crear un desarrollador experto
Salida: ¡Muy bien, tu me has mostrado tu pensamiento en 15 palabras!
Para llevar esto a cabo, vamos a crear un fichero de texto y añadimos una unas frases, y contamos cuántas palabras tiene y lo imprimimos.

"""

import string # Importo este modulo que contiene facilidades para los string

print("Bienvenid@")

while(True):
     
    pensamiento = input("Cuenteme, ¿En que estas pensando?\n")
    print(pensamiento.split(' '))
    
    break
    

