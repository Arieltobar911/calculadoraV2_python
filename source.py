import os #importa el modulo OS, que permite hacer y modificar carpetas y archivos

from decimal import Decimal, getcontext, InvalidOperation #hace llamado al modulo decimal, y importa
#la decimal para usarla en definir los nums
#getcontext obtiene el contexto actual de las decimales, y poder alterar el comportamiento de estas
#InvalidOperation sera un tipo de error que usaremos en Except, en caso que las operaciones con decimales sean invalidas

getcontext().prec = 50 #aumenta el limite de digitos en los calculos decimales, gracias a getcontext

#crea la clase de mensajes personalizados para invalid operation, para su uso en exception
class InvalidDecimalError(Exception):
    def __init__(self, message): #define sus atributos 
        super().__init__(message) #hace llamado al atributo mensaje 

pre_resultados = None #define pre resultados (variable) como nada
#sera importante, para recordar la respuesta anterior y tener la opcion de usarla
#en tus calculos

historial = [] #crea la lista historial, para almacenar todos los calculos
#durante el uso del programa

#define la funcion para guardar archivos, y llama a la operacion
def guardar_en_archivo(operacion):
    carpeta = "resultados" #crea la variable carpeta, pque permitira que tenga de nombre resultados
    if not os.path.exists(carpeta): #en caso de no existir
        os.makedirs(carpeta) #crea esa carpeta
    archivo = os.path.join(carpeta, "historial_calculos.txt") #crea la ruta de la creacion o acceso del archivo, en este caso dentro de resultados
    with open(archivo, "a", encoding="utf-8") as file: #si el archivo lo crea y lo abre, si existe solamente lo abre en modo append con utf-8
        file.write(operacion + "\n") #
#el modo append sirve para modificar el .txt

#crea la funcion para cargar el contador
def cargar_contador():
    archivo = "resultados/contador.txt" #crea la variable, equivalente a la ubicacion y nombre del archivo
    if os.path.exists(archivo): #si el archivo existe
        with open(archivo, "r", encoding="utf-8") as file: #lo abre en modo lectura con utf-8
            return int(file.read().strip()) #lee el archivo, eliminando espacios y transformando todos los strings en int
    return 0 #si no existe el archivo, devuelve en 0 como inicial

#crea la funcion de guardar contador, llamando al valor del archivo
def guardar_contador(valor):
    archivo = "resultados/contador.txt" #especifica la ruta del archivo con una variable
    with open(archivo, "w", encoding="utf-8") as file: #abre el archivo en modo escritura con utf-8
        file.write(str(valor)) #cambia y transforma a string el valor

#cargar el contador de cálculos al inicio
total_calculos = cargar_contador()

#crea un ciclo while que siempre sera verdadero, ESTE ES EL CICLO PADRE
while True:
    try: #este elemento es complementario, para la aclaracion de errores
        #crea la clase datis
        class Datis:
            #define sus atributos, llamando a num1 y 2
            def __init__(self, num1, num2):
                self.num1 = Decimal(num1) #transforma a estos 2 en 
                self.num2 = Decimal(num2) #decimales
            
            #crea funcion operaciones, creando su variable local operador
            def operaciones(self, operador):
                if operador == "+": #valida antes de iniciar la operacion, pero si es mas
                    return self.num1 + self.num2 #suma los numeros
                elif operador == "-": #si es menos
                    return self.num1 - self.num2 #resta los numeros
                elif operador == "*": #si es multiplicacion
                    return self.num1 * self.num2 #multiplica los numeros
                elif operador == "/": #si es division
                    if self.num2 == 0: #pero si num2 es 0
                        raise ZeroDivisionError("No puedes dividir con un cero.") #da error con ese mensaje, por que no puedes dividir por 0
                    return self.num1 / self.num2 #los divide
                elif operador == "**": #si es potencia
                    return self.num1 ** self.num2 #los multiplica al cuadrado
                else: #si el operador no es conocido
                    return "Operador inválido" #devuelve como invalido, y repite

        #crea la clase temistocles, que hereda los atributos y funciones de datis
        class Temistocles(Datis):
            def __init__(self, num1, num2): #crea y define el metodo de temistocles, con sus atributos
                super().__init__(num1, num2) #y llama al metodo de datis, iniciando las variables

            def select_ops(self, operador): #define select ops, creando metodo y atributos
                try: #tu ya sabes
                    global total_calculos, pre_resultados #globaliza las variables t_calculos y pre resultados
                                        
                    total_calculos += 1 #aumenta el contador en 1, por cada calculo
                    resultado = self.operaciones(operador) #crea la variable resultado, que llama a la funcion operaciones
                    operacion_str = f"Cálculo {total_calculos}: {self.num1} {operador} {self.num2} = {resultado}" #crea la variable operacion string, que es el texto que estas viendo
                    print(f"\n {operacion_str}") #registra la operacion en el historial de calculos
                    
                    historial.append(operacion_str)  #agrega el nuevo calculo al final
                    guardar_en_archivo(operacion_str)  #guarda los cambios en historial de calculos
                    guardar_contador(total_calculos)  #y actualiza el contador de calculos
                    
                    pre_resultados = resultado #pre resultados iguala a resultado
                except ZeroDivisionError as zen: #registra el error como zen
                    print(f" Error: {zen}")#imprime el mensaje del error

        def validator(val): #crea la funcion valitador, con su variable local val
            try: #tu ya sabes
                Decimal(val) #verifica si el valor es decimal
                return True #si lo es retorna a verdadero
            except InvalidOperation: #y te da este tipo de error 
                return False #si no lo es retorna a falso

        def sevs(CTR): #crea la funcion sevs, tomando una variable local como argumento
            return CTR in ["+", "-", "*", "/", "**"] #retorna verdadero si el operador esta en la lista
        
        #si pre resultados cuenta con un resultado anterior
        if pre_resultados is not None:
            print(f"\n Último resultado: {pre_resultados}") #muestra el resultado anterior
            reset = input("\n ¿Quieres hacer un cálculo desde cero? (si/no): ") #pregunta si lo quieres utilizar o descartar
            if reset.lower() == "si": #si eliges si
                pre_resultados = None #lo descarta, y reinicia
            else: #en cambio al poner lo que sea (despues arreglo esto)
                num1 = pre_resultados #retorma el resultado anterior, utilizandolo como num1
        
        #si pre resultados no cuenta con nada
        if pre_resultados is None:
            while True: #crea un siclo while siempre verdadero
                num1 = input("\n Ingresa el primer número: ") #pide que ingreses un numero
                if validator(num1): #llama a la funcion validator
                    num1 = Decimal(num1) #si num1 es decimal
                    break #rompe el ciclo
                print(" Error: Valor inválido.") #sino, imprime el error y continua el ciclo

        while True: #crea un siclo while siempre verdadero
            operador = input("\n Ingresa tu operador: ") #pide que ingreses un operador
            if sevs(operador): #llama a la funcion sevs y verifica si esta en la lista
                break #si esta en la lista, rompe el ciclo
            print(" Error: Operador no válido.")#sino, imprime el error y continua el ciclo

        while True: #crea un siclo while siempre verdadero
            num2 = input("\n Ingresa el segundo número: ") #pide que ingreses un numero
            if validator(num2): #llama a la funcion validator
                num2 = Decimal(num2) #si num2 es decimal
                break #rompe el ciclo
            print(" Error: Valor inválido.")#sino, imprime el error y continua el ciclo

        melancio = Temistocles(num1, num2) #crea la variable melancio, equivalente a temistocles con sus atributos
        melancio.select_ops(operador) #llama al metodo select ops de temistocles, despues utilizando el operador para ejecutar
        #finalmente la opreacion

    except Exception as a: #registra al error exception como a
        print(f" Error inesperado: {a}") #imprime el mensaje 
        continue #CONTINUA CON EL CICLO PADRE
    
    ask = input("\n ¿Quieres continuar? (si/no): ") #te pregunta si quieres seguir con el programa
    if ask.lower() == "si": #si es cribes si...
        continue #CONTINUA CON EL CICLO PADRE
    elif ask.lower() == "no": #si escribes no
        print("\n Programa finalizado") #te imprime este mensajes y...
        break #FINALIZA EL CICLO PADRE, finalizando el programa
    else: #si escoges otras que no sea "si" o "no"
        print("\n Tu opción no es válida, el programa continuará.") #te imprime este mensaje
        #y... CONTINUA CON EL CICLO PADRE
