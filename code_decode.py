def select_opciones():
    while True:
        opcion = input("Ingrese 'c' para codificar o 'd' para decodificar su mensaje:\t")
        if len(opcion)==1:                  # Se asegura que solo haya recibido 1 caracter
            char = opcion.lower()           # Convierte la opción seleccionada en minúscula
            caracteres = 'cd'               # String que contiene las opciones permitidos

            if char in caracteres:          # Verifica que la opción esté en los caracteres permitidos
                return char  
            else:
                print("El caracter ingresado es diferente de 'c' y 'd', inténtelo de nuevo\n")
        else:
            print("Verifique que su opción seleccionada sea 'c' o 'd' y no contenga espacios\n")


def validar_alfabeto():
    while True:
        mensaje = input("Ingrese el mensaje (solo letras a-Z):\n>> ")
        
        for char in mensaje:
            if (ord('A') <= ord(char) <= ord('Z')) or (ord('a') <= ord(char) <= ord('z')):      # Se asegura que en el mensaje solo haya letras entre a - Z
                mensaje_valido = True
            else:
                print("El mensaje ingresado no es válido, recuerde que solo se aceptan letras (a-Z)\n")
                mensaje_valido = False
                break
        if mensaje_valido:
            return mensaje
        
def num_entero_positivo():
    while True:
        num = input("Ingrese el valor del desplazamiento (número entero):\t")

        if num.isdigit():
            return int(num)
        else:
            print("El desplazamiento debe ser un número entero postivo.\tVerifique que no haya ingresado espacios\n")

def cifrado(texto_entrada, desplazamiento):

    men_cifrado = ""                        # Variable en la que se guarada el mensaje cifrado
    for char in texto_entrada:              # Recorre todos los caracteres del texto de entrada
        valor_ascii = ord(char)             # Valor Ascii del caracter
        
        if char.isupper():                  # Conocer si el caracter es una letra mayuscula para ubicarse en la tabla Ascii
            punto_partida = ord('A')        # Ascii 65
        else:
            punto_partida = ord('a')        # Ascii 97
        
        cifrado_ascii = ((valor_ascii - punto_partida + desplazamiento) % 26) + punto_partida
        men_cifrado += chr(cifrado_ascii)
        
    print(f"El mensaje {texto_entrada} cifrado con desplazamiento {desplazamiento} es:\t {men_cifrado}")

def decifrado(texto_entrada, desplazamiento):

    men_decifrado = ""                        # Variable en la que se guarada el mensaje cifrado
    for char in texto_entrada:              # Recorre todos los caracteres del texto de entrada
        valor_ascii = ord(char)             # Valor Ascii del caracter
        
        if char.isupper():                  # Conocer si el caracter es una letra mayuscula para ubicarse en la tabla Ascii
            punto_partida = ord('A')        # Ascii 65
        else:
            punto_partida = ord('a')        # Ascii 97
        
        decifrado_ascii = ((valor_ascii - punto_partida - desplazamiento) % 26) + punto_partida
        men_decifrado += chr(decifrado_ascii)
        
    print(f"El mensaje {texto_entrada} decifrado con desplazamiento {desplazamiento} es:\t {men_decifrado}")

cifrar_decifrar = select_opciones()
texto_entrada = validar_alfabeto()
desplazamiento = num_entero_positivo()

if cifrar_decifrar == 'c':
    cifrado(texto_entrada,desplazamiento)
else:
    decifrado(texto_entrada,desplazamiento)