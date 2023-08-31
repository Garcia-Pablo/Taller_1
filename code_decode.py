# Función para validar la selección de proceso cifrar o decifrar
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

# Función para validar las 26 letras del alfabeto inglés en MAYÚSCULA y minúscula
def validar_alfabeto():
    while True:
        mensaje = input("Ingrese el mensaje (solo letras a-Z):\n>> ")
        # Se asegura que en el mensaje solo haya letras entre a - Z mediante rangos en la tabla ASCII
        for char in mensaje:
            if (ord('A') <= ord(char) <= ord('Z')) or (ord('a') <= ord(char) <= ord('z')):
                mensaje_valido = True
            else:
                print("El mensaje ingresado no es válido, recuerde que solo se aceptan letras (a-Z)\n")
                mensaje_valido = False
                break
        if mensaje_valido:                              # Retorna mensaje al ser validado
            return mensaje

# Función para asegurar que el número ingresado sea un número entero positivo
def num_entero_positivo():
    while True:
        num = input("Ingrese el valor del desplazamiento (número entero):\t")
        # Si el isdigit es Verdadero, significa que el num ingresado es un entero positivo
        if num.isdigit():
            return int(num)                     # Se pasa num de string a entero
        else:
            print("El desplazamiento debe ser un número entero postivo.\tVerifique que no haya ingresado espacios\n")

def cifrado(texto_entrada, desplazamiento):

    men_cifrado = ""                        # Variable en la que se guarda el mensaje cifrado
    for char in texto_entrada:              # Recorre todos los caracteres del texto de entrada
        valor_ascii = ord(char)             # Valor Ascii del caracter
        
        if char.isupper():                  # Conocer si el caracter es una letra mayuscula para ubicarse en la tabla Ascii
            punto_partida = ord('A')        # Ascii 65
        else:
            punto_partida = ord('a')        # Ascii 97
        # Se necesita conocer el punto de partida, para poder ubicarse en el alfabeto inglés de la tabla Ascii
        cifrado_ascii = ((valor_ascii - punto_partida + desplazamiento) % 26) + punto_partida
        men_cifrado += chr(cifrado_ascii)
        
    print(f"El mensaje {texto_entrada} cifrado con desplazamiento {desplazamiento} es:\t {men_cifrado}")

def decifrado(texto_entrada, desplazamiento):

    men_decifrado = ""                      # Variable en la que se guarda el mensaje cifrado
    for char in texto_entrada:              # Recorre todos los caracteres del texto de entrada
        valor_ascii = ord(char)             # Valor Ascii del caracter
        
        if char.isupper():                  # Conocer si el caracter es una letra mayuscula para ubicarse en la tabla Ascii
            punto_partida = ord('A')        # Ascii 65
        else:
            punto_partida = ord('a')        # Ascii 97
        # Se necesita conocer el punto de partida, para poder ubicarse en el alfabeto inglés de la tabla Ascii
        decifrado_ascii = ((valor_ascii - punto_partida - desplazamiento) % 26) + punto_partida
        men_decifrado += chr(decifrado_ascii)
        
    print(f"El mensaje {texto_entrada} decifrado con desplazamiento {desplazamiento} es:\t {men_decifrado}\n")