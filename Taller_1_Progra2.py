def metodo_euler (x,y,paso,num_pasos,edo):
    
    
    print("Solucion de Ecuacion diferencial ordinaria por el metodo de Euler")
    print("Iteraciones\t x\t    y\n-------------------------------\n")

    for i in range(int(x),num_pasos+1):
           #x = cond_ini_x + paso
            # y = cond_ini_y + paso
            #y1 = y*eval(edo)
        print(f"\t{i}\t {x:.1f}\t {y:.4f}")     #Muestra la tabla
        i += 1
        ec = eval(edo)
        x = x + paso
            #y = y + paso 
            #ec = eval(edo)

        y = y + (paso * ec)

# Función para validar variables en la ecuación diferencial
def validar_xy(ecuacion):
    variables_permitidas = 'xy'                             # Se enlistan las variables contenidas en la ecuación
    
    for char in ecuacion:                                           # Se recorre la ecuacion para validación
        if char.isalpha() and (char not in variables_permitidas):
            return False
    return True

x = float(input("Ingrese la condicion inicial de x(0):\t"))
y = float(input("Ingrese la condicion inicial de y(0):\t"))
h = float(input("Ingrese el tamaño del paso(h):\t"))
num_pasos = int(input("Ingrese el numero de pasos (n):\t"))
while (True):
    # Pedir la ecuación al usuario
    edo=input("Ingrese la ecuación diferencial ordinaria en terminos de 'x' y 'y':\t")
    # Validar la ecuación
    if validar_xy(edo):
        print("Ecuación válida")
        break
    else:
        print("Ecuación inválida. Solo se permiten las letras x o y. \n")
metodo_euler(x,y,h,num_pasos,edo)

