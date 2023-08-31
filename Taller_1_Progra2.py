#Funcion para resolver ecuaciones ordinarias por el metodo de euler
def metodo_euler (x,y,paso,num_pasos,edo):                      #Parametros que debe ingresar el usuario
    print("Solucion de Ecuacion diferencial ordinaria por el metodo de Euler\n")
    print("Iteraciones\t x\t    y\n-------------------------------\n")

    for i in range(int(num_pasos+1)):        
        print(f"\t{i}\t {x:.1f}\t {y:.4f}")     #Muestra la tabla
        i += 1                                   # Indice
        #ec = eval(edo)                           #Utilizamos la funcion eval para evaluar la exprecion en edo y le asigna el resultado de la expresion a ec
        #print(ec)
        y = y + paso * eval(edo)
        x = x + paso                             #Formula de x
                              # Formula de y

# Función para validar variables en la ecuación diferencial
def validar_xy(ecuacion):
    ecuacion = ecuacion.lower()
    variables_permitidas = "xy"                               # Se enlistan las variables contenidas en la ecuación
    
    for char in ecuacion:                                           # Se recorre la ecuacion para validación
        if char.isalpha() and (char not in variables_permitidas):
            return False
    return True

#Funcion para validar que ingresa un numero y retorna un float
def validar_num(variable):                  
    val1 = variable.replace('.','')         # Volvemos variable1 entero para utilizar la funcion isnumeric y evaluar si es numero
    if (val1.isnumeric()):
        variable = float(variable)              #Volvemos variable que es str en float
        return (variable)
    else:
        while(True):           #mientras que variable sea diferente de un numero float y un numero entero
            variable = input("La condicion debe ser un numero, ingrese un numero:\t")
            val1 = variable.replace('.','')                         #en caso de que sea un float lo volvemos entero para evaluar si es numero
            if (val1.isnumeric()):                                  #si es numero lo volvemos float si no es numero vuelve al  principio del while
                variable = float(variable)
                return (variable)
                break

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
metodo_euler(x,y,h,num_pasos,edo)

