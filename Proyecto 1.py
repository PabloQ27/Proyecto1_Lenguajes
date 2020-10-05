from Clase2 import clase
import os.path
import re



"""
clase1 = clase()
clase2 = clase()
print(clase.num2)
print("-------------------------------------------------------")
print("Nombre: Pablo Rufino Quevedo Berdúo  \nCarne: 201701081" )
print("-------------------------------------------------------")
print("BIENVENIDO \nIngrese el numero de una opción o exit para salir")
print("1.  Cargar Archivo    \n2.  Graficar Operacion \n3. Graficar Ruta   \n4.  Salir")
palabras reservada ruta,nombre,peso,inicio,fin,estacion,estado,color
"""

p_reserv = ["ruta", "nombre", "peso", "inicio", "fin", "estacion", "estado", "color"]
cont_col = 0
cont_fil = 0
estado = 0
lexema =""
estado2 = 0
lexema2 = ""
caractemp = ""
estacionnombre = ""
rutanombre = ""
valor = 0
#hacer metodo validar el lexema y meterlos a los arreglos y usar en estancionnombre y rutanombre
def afd2(): #meter en un for
    global lexema2,estado2,caractemp,rutanombre,estacionnombre #el lexema puede variar
    simbst1 = "@#_"
    num = r"[0-9]"
    for x in range(2):
        if estado2 == 0:
            print("est0")
            print("el lex 2", lexema2)
            if lexema2.lower() == "inicio" or lexema2.lower() == "fin" or valor == 2:#estacionnombre usar arreglo
                if lexema2.lower() == "color":
                    estado2 = 4
                else: 
                    estado2 = 1
            elif lexema2.lower() == "peso":
                estado2 = 2
            elif valor == 1: #rutanombre hay que usar un arreglo
                estado2 = 3
            elif lexema2.lower() == "color":
                estado2 = 4
        elif estado2 == 1:
            print("st1")  
            if re.search(num,caractemp):

                print(" fin ini o estnom xd ", caractemp)
            else:
                print("et nel ", caractemp)
            estado2 = 0
        elif estado2 == 2:
            print("st2")
            if re.search(num,caractemp) or caractemp == ".":
                print("enteros y decimales", caractemp)
            else:
                print("no pes ", caractemp)
            estado2 = 0
        elif estado2 == 3:
            print("st3")
            if (simbst1.find(caractemp) != -1) or re.search(num,caractemp) :    
                print("rutnomb ", caractemp)
            else:
                print("et nel ", caractemp)
            estado2 = 0
        elif estado2 == 4:
            print("st4")
            if re.search(num,caractemp) or caractemp == "#":
                print("exa ", caractemp)
            else: 
                print("et nel ex ", caractemp)
            estado2 = 0
        else:
            print("no se afd2")

def palabra_reservada():
    global lexema,lexema2,rutanombre,estacionnombre,valor
    for x in range(0,len(p_reserv)): 
        if lexema.lower() == p_reserv[x]:
            #hay que ver si meter otro if para validar que nombre viene, si es de la estacion, de la rutoa o del mapa
            if lexema.lower() == lexema2:
                print("ya estaba ", lexema2)
                lexema2 = ""
                lexema = ""
                #que afd2 se salgo o cambie el estado con un numero
            else:
                print("lexema ",lexema, " encontrado")
                #que afd2 se meta
                if lexema.lower()=="ruta":
                    valor = 1
                elif lexema.lower() == "estacion":
                    valor = 2
                lexema2 = lexema
                lexema=""
        else:
            pass
            #print("lex inc o no", end = "")


def afd(caract):
    global estado,lexema, cont_col,cont_fil,caractemp
    abc = r"[A-Za-z]"
    simb ="@#_"
    if estado == 0:
        #print("estado 0")
        if caract == "<":
            estado = 2
        else:
            print("no ",caract," fila ",cont_fil, " columna ",cont_col)
            estado = 1
    elif estado == 1:
       # print("estado 1")
        if caract == "<":
            estado = 2
        elif caract == ">":
            estado = 5
        else:
            print("no ",caract," fila ",cont_fil, " columna ",cont_col)
            estado = 1
    elif estado == 2:
        #print("estado 02")
        if re.search(abc,caract) or (simb.find(caract) != -1):
            lexema += caract
            #print ("pal lex st2 ", caract, " lex", lexema)
            palabra_reservada()
            estado = 2
        elif caract == "/":
            estado = 4
        elif caract == ">":
            estado = 5
        elif caract == "<":
            estado = 2
        else:
            print("no ",caract," fila ",cont_fil, " columna ",cont_col)
            estado = 3
    elif estado == 3:
       # print("estado 3")
        if re.search(abc,caract):
            lexema += caract
            print ("pal lex ", caract, " lex", lexema)
            palabra_reservada()
            estado = 2
        elif caract == ">":
            estado = 5
        elif caract == "/":
            estado = 4
        else:
            print("no ",caract," fila ",cont_fil, " columna ",cont_col)
            estado = 3
    elif estado == 4:
       # print("estado 4")
        if re.search(abc,caract):
            lexema += caract
            #print("pal lex st4 ", caract, " lex", lexema)
            palabra_reservada()
            estado =2
        else:
            print("no ",caract," fila ",cont_fil, " columna ",cont_col)
            estado = 3
    elif estado == 5:  
        #print("estado 5")     
        if caract == "<":
            estado =2      
        elif re.search(abc,caract):#agregar otro elif para cuando sea puntos y numeros y tambiar ver si vienen algo fuera de las etiquetas
            print ("almacena ", caract)     
            #print(lexema)  
        else:
            caractemp = caract
            afd2()           
    else:
        print("no se que px")
       

def readCaractAfd(cadena):   
    global cont_col
    for x in range(0,len(cadena)):
        cont_col += 1
        if cadena[x].isspace():
            cont_col -= 1
            #print(".")#lee los espaciones en blanco
        else:
            afd(cadena[x])
            
def validar_arch():  # validacion de la extension correcta   
    global cont_col,cont_fil
    ruta = input()#aqui esta la ruta del archivo
    nombre_archivo, extension = os.path.splitext(ruta)
    if extension == ".txt":
        print("Ruta correcta")
        archivo = open(ruta, "r", encoding="utf-8")    
        for linea in archivo.readlines(): #separa con cada salto de linea 
            cont_fil += 1    
            comp = linea.split()# comp se vuelve en un arreglo con cada linea
            if len(comp) == 0:  # valida si vienen una linea vacia                            
                print("aqui hay lineas en blanco xd")
            else:               
                readCaractAfd(linea) 
            cont_col = 0             
        archivo.close()
    else:
        print("la ruta ingresada es incorrecta")

def menu():
    opc = input()
    fin = True
    while fin:
        if opc == "1":           
            print("1.  Cargar Archivo    \n2.  Graficar Operacion \n3.  Graficar Ruta   \n4.  Salir")
            menu()
            break
        elif opc == "2":           
            print("1.  Cargar Archivo    \n2.  Graficar Operacion \n3.  Graficar Ruta   \n4.  Salir")           
            break
        elif opc == "3":
            #agregar metodo para mostrar la ruta
            print("1.  Cargar Archivo    \n2.  Graficar Operacion \n3.  Graficar Ruta   \n4.  Salir")
        elif opc == "exit":
            print("pa juera")
            fin = False
        else:
            print("Número inválido, vuelva a intentar.")
            opc = input()

validar_arch()

"""
i=0
while i != 10:   
    i+=1
    print(i)
"""