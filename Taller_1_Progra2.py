""" 
___________     TALLER 1    ___________________
    INTEGRANTES:
        Esneyder Duarte Hernandez
        Grachi Gonzalez Pulgarin
        Pablo Garcia Suarez
 """
# Importamos todas las funciones necesarias para cifrar y decifrar
from code_decode import *
# Funcion para resolver ecuaciones ordinarias por el metodo de euler
def metodo_euler (x,y,paso,num_pasos,edo):                      # Parametros que debe ingresar el usuario
    print("Solucion de Ecuacion diferencial ordinaria por el metodo de Euler\n")
    print("Iteraciones\t x\t    y\n-------------------------------\n")

    for i in range(int(num_pasos + 1)):        
        print(f"\t{i}\t {x:.1f}\t {y:.4f}")                     # Muestra la tabla
        i += 1                                                  # Indice
        y = y + paso * eval(edo)                                # Utilizamos la funcion eval para evaluar la expresion en edo
        x = x + paso                                            # Formula de x

# Función para validar variables en la ecuación diferencial
def validar_xy(ecuacion):
    ecuacion = ecuacion.lower()                               # Se pasa la edo a letras minúsculas
    variables_permitidas = "xy"                               # Se enlistan las posibles variables contenidas en la ecuación
    
    for char in ecuacion:                                     # Se recorre la ecuacion para validación
        # Se verifica que las letras contenidas en la edo pertenezcan a las variables permitidas
        if char.isalpha() and (char not in variables_permitidas):
            return False
    return True

# Funcion para validar que ingresa un numero y retorna un float
def validar_num(variable):                  
    val1 = variable.replace('.','')             # Volvemos variable1 entero para utilizar la funcion isnumeric y evaluar si es numero
    if (val1.isnumeric()):
        variable = float(variable)              # Volvemos variable que es str en float
        return (variable)
    else:
        while(True):
            variable = input("La condicion debe ser un numero, ingrese un numero:\t")
            val1 = variable.replace('.','')                         # En caso de que sea un float lo volvemos entero para evaluar si es numero
            if (val1.isnumeric()):                                  # Si es numero lo volvemos float si no es numero vuelve al  principio del while
                variable = float(variable)
                return (variable)
                break

# Función para validar las opciones disponibles en el menú
def validar_menu(menu):
    opciones_menu = "123"                               # Se enlistan las posibles opciones del menú
    if len(menu) == 1 and (menu in opciones_menu):        # Se verifica que la opción ingresada sea válida
        return int(menu)                                # Si lo es, retorna el valor entero de la selección
    else:
        print("La opción de menú seleccionada, NO es válida\n")

# Inicio del programa
print("Bienvenido al Taller 1 de Programación Avanzada\n Por favor ingrese la opción que desea ejecutar: ")
while (True):
    # Despliegue de menú
    menu = input("Seleccione:\n1. Resolver EDO mediante método de EULER\n2. Codificar o Decodificar un mensaje, usando el cifrado de César\n3. Salir\n>> ")
    menu = validar_menu(menu)                                                   # Validación de opciones de menú
    if menu == 1:                                                               # Resolver EDO por método de Euler
        # Se validan las variables de entrada
        x = input("Ingrese la condicion inicial de x(0):\t")
        x = validar_num(x)
        y = input("Ingrese la condicion inicial de y(0):\t")
        y = validar_num(y)
        h = input("Ingrese el tamaño del paso(h):\t")
        h = validar_num(h)
        num_pasos = input("Ingrese el numero de pasos (n):\t")
        num_pasos = validar_num(num_pasos)
        while (True):
            # Pedir la ecuación al usuario
            edo=input("Ingrese la ecuación diferencial ordinaria en terminos de 'x' y 'y':\t")
            # Validar la ecuación
            if validar_xy(edo):
                print("Ecuación válida")
                break
            else:
                print("Ecuación inválida. Solo se permiten las letras 'x' y 'y'. \n")
        metodo_euler(x,y,h,num_pasos,edo)                                       # Se resuelve la EDO

    elif menu == 2:                                                             # Cifrado y Decifrado de César
        cifrar_decifrar = select_opciones()                                     # Valida las opciones 'c' y 'd'
        texto_entrada = validar_alfabeto()                                      # Valida las letras del alfabeto inglés
        desplazamiento = num_entero_positivo()                                  # Valida número entero positivo
        # Dependiendo de la opción seleccionada realiza 'c' Cifado o 'd' Decifrado
        if cifrar_decifrar == 'c':
            cifrado(texto_entrada,desplazamiento)
        else:
            decifrado(texto_entrada,desplazamiento)
    
    elif menu == 3:                                                             # Opción de Salida (EXIT)
        print("Gracias por utilizar nuestros servicios, Vuelva pronto\n")
        break
    else:                                                                       # PASS para opción inválida
        pass

