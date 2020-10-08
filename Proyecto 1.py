from Clase2 import clase
import os.path
import re
from graphviz import Digraph
import csv
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table
import os



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
contenido = ""
list_error = []
list_token = []
cont_col2 = 0
val = 0
listaRuta = []
listaEstacion = []

#hacer metodo validar el lexema y meterlos a los arreglos y usar en estancionnombre y rutanombre
def afd2(): #meter en un for
    global lexema2,estado2,caractemp,rutanombre,estacionnombre,contenido #el lexema puede variar
    simbst1 = "@#_"
    num = r"[0-9]"
    for x in range(2):
        if estado2 == 0:
            #print("est0")
            #print("el lex 2", lexema2)
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
            #print("st1")  
            if re.search(num,caractemp):
                contenido += caractemp
                #print(" fin ini o estnom xd ", caractemp)
            else:
                #print("et nel ", caractemp)
                list_error.append(caractemp)
                list_error.append(cont_fil)
                list_error.append(cont_col)
            estado2 = 0
        elif estado2 == 2:
            #print("st2")
            if re.search(num,caractemp) or caractemp == ".":
                contenido += caractemp
                #print("enteros y decimales", caractemp)
            else:
                #print("no pes ", caractemp)
                list_error.append(caractemp)
                list_error.append(cont_fil)
                list_error.append(cont_col)
            estado2 = 0
        elif estado2 == 3:
            #print("st3")
            if (simbst1.find(caractemp) != -1) or re.search(num,caractemp) :   
                contenido += caractemp 
                #print("rutnomb ", caractemp)
            else:
                #print("et nel ", caractemp)
                list_error.append(caractemp)
                list_error.append(cont_fil)
                list_error.append(cont_col)
            estado2 = 0
        elif estado2 == 4:
            #print("st4")
            if re.search(num,caractemp) or caractemp == "#":
                contenido += caractemp
                #print("exa ", caractemp)
            else: 
                #print("et nel ex ", caractemp)
                list_error.append(caractemp)
                list_error.append(cont_fil)
                list_error.append(cont_col)
            estado2 = 0
        else:
            print("no se afd2")

def palabra_reservada():
    global lexema,lexema2,rutanombre,estacionnombre,valor,list_token,cont_col,cont_fil
    for x in range(0,len(p_reserv)): 
        if lexema.lower() == p_reserv[x]:
            #hay que ver si meter otro if para validar que nombre viene, si es de la estacion, de la rutoa o del mapa
            if lexema.lower() == lexema2:
                #print("ya estaba ", lexema2)
                list_token.append(lexema)
                list_token.append(cont_fil)
                list_token.append(cont_col)
                lexema2 = ""
                lexema = ""
                #que afd2 se salgo o cambie el estado con un numero
            else:
                #print("lexema ",lexema, " encontrado")
                list_token.append(lexema)
                list_token.append(cont_fil)
                list_token.append(cont_col)
                if lexema.lower()=="ruta":
                    """
                    if valor == 1: #esto servira para el metodo que lea de la lista
                        valor = 0
                    else:
                    """    
                    valor = 1
                elif lexema.lower() == "estacion":
                    """
                    if valor == 2:
                        valor = 0
                    else:
                    """
                    valor = 2
                lexema2 = lexema
                lexema=""
        else:
            pass
            #print("lex inc o no", end = "")

def afd(caract):
    global estado,lexema, cont_col,cont_fil,caractemp,contenido,list_error,cont_col2
    cont_col2 +=1
    abc = r"[A-Za-z]"
    simb ="@#_"
    if estado == 0:
        #print("estado 0")
        if caract == "<":
            
            estado = 2
        else:
           # print("no ",caract," fila ",cont_fil, " columna ",cont_col)
            list_error.append(caract)
            list_error.append(cont_fil)
            list_error.append(cont_col)
            estado = 1
    elif estado == 1:
       # print("estado 1")
        if caract == "<":
            val = 1
            estado = 2
        elif caract == ">":
            val= 1
            estado = 5
        else:
            #print("no ",caract," fila ",cont_fil, " columna ",cont_col)
            list_error.append(caract)
            list_error.append(cont_fil)
            list_error.append(cont_col)
            estado = 1
    elif estado == 2:
        #print("estado 02")
        if re.search(abc,caract) or (simb.find(caract) != -1):
            lexema += caract
            #print ("pal lex st2 ", caract, " lex", lexema)
            palabra_reservada()
            estado = 2
        elif caract == "/":
            val = 1
            #print("contenio es ", contenido) #para agregar hay que validar que no este vacio
            if len(contenido) == 0:
                print("ta vacio contenido")
            else:
                list_token.append(contenido)
                list_token.append(cont_fil)
                list_token.append(cont_col)
            contenido = ""
            estado = 4
        elif caract == ">":
            val = 1
            estado = 5
        elif caract == "<":
            val = 1
            estado = 2
        else:
            #print("no ",caract," fila ",cont_fil, " columna ",cont_col)
            list_error.append(caract)
            list_error.append(cont_fil)
            list_error.append(cont_col)
            estado = 3
    elif estado == 3:
       # print("estado 3")
        if re.search(abc,caract):
            lexema += caract
            #print ("pal lex ", caract, " lex", lexema)
            palabra_reservada()
            estado = 2
        elif caract == ">":
            estado = 5
        elif caract == "/":
            estado = 4
        else:
            #print("no ",caract," fila ",cont_fil, " columna ",cont_col)
            list_error.append(caract)
            list_error.append(cont_fil)
            list_error.append(cont_col)
            estado = 3
    elif estado == 4:
       # print("estado 4")
        if re.search(abc,caract):
            lexema += caract
            #print("pal lex st4 ", caract, " lex", lexema)
            palabra_reservada()
            estado =2
        else:
            #print("no ",caract," fila ",cont_fil, " columna ",cont_col)
            list_error.append(caract)
            list_error.append(cont_fil)
            list_error.append(cont_col)
            estado = 3
    elif estado == 5:  
        #print("estado 5")     
        if caract == "<":
            estado =2      
        elif re.search(abc,caract):#agregar otro elif para cuando sea puntos y numeros y tambiar ver si vienen algo fuera de las etiquetas
            #print ("almacena ", caract)  
            contenido += caract   
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


def listaerrores():
    cont = 0     
    fileName2 = "Reporte_1.pdf"
    pdf = SimpleDocTemplate(
    fileName2,
    pagesize=letter
    )
    elems = []
    data = []
    fila=["No.","Error","Fila","Columna"]
    data.append(fila) 
    for i in range(0,len(list_error), 3):
        cont += 1
        fila =[str(cont),str(list_error[i]),str(list_error[i+1]),str(list_error[i+2])]
        data.append(fila)
        table = Table(data)
        #print(cont,"  ",list_error[i], " fila: ",list_error[i+1], " columna: ", list_error[i+2])
    elems.append(table)   
    pdf.build(elems)
  
nombremapa = ""
def listatoken():
    cont = 0
    fileName = "Reporte_2.pdf" 
    pdf = SimpleDocTemplate(
    fileName,
    pagesize=letter
    )
    elems = []
    data = []
    fila=["No.","Token","Fila","Columna"]
    data.append(fila)   
    #table = Table(data) 
    for i in range(0,len(list_token), 3):
        cont += 1
        fila =[str(cont),str(list_token[i]),str(list_token[i+1]),str(list_token[i+2])]
        data.append(fila)
        table = Table(data)
        #print(cont,"  ",list_token[i], " fila: ",list_token[i+1], " columna: ", list_token[i+2])
    
    elems.append(table)   
    pdf.build(elems)

def separalista():
    # 0 nombre del mapa 1 es ruta y 2 es estacion
    global nombremapa
    num = 0
    for i in range(0,len(list_token),3):
        if str(list_token[i]).lower() == "ruta":
            if num != 1:
                num = 1
            else:
                num = 0
            listaRuta.append(list_token[i])
        elif num == 1:
            listaRuta.append(list_token[i])
        elif str(list_token[i]).lower() == "estacion":
            if num != 2:
                num = 2
            else:
                num = 0
            listaEstacion.append(list_token[i])
        elif num == 2:
            listaEstacion.append(list_token[i])
        else:
            if str(list_token[i]).lower() != "nombre":
                nombremapa = list_token[i]
                print("psible mapname", list_token[i])
    for i in range(0,len(listaRuta)):
        print(listaRuta[i])
    for i in range(0,len(listaEstacion)):
        print(listaEstacion[i])

def dibujarmapa():
    global nombremapa
    archivo = open('Mapa.dot','w')
    contenidoD = ""
    for i in range(0,len(listaEstacion)-2):
        if str(listaEstacion[i]).lower() == "nombre" and str(listaEstacion[i+2]).lower() == "nombre":
            contenidoD += str(listaEstacion[i+1])+"[label=" 
        elif str(listaEstacion[i]).lower() == "estado" and str(listaEstacion[i+2]).lower() == "estado":
            pass
        elif str(listaEstacion[i]).lower() == "color" and str(listaEstacion[i+2]).lower() == "color":
            contenidoD += "fillcolor ="+'"'+listaEstacion[i]+'"'
        else:
            contenidoD += "\n"
    print(contenidoD)
    archivo.write('digraph D {\n')
    archivo.write('label = '+'"'+nombremapa+'"')
    archivo.write('rankdir=LR')
    archivo.write('node [style= filled]')
    archivo.write(contenido + '\n')
    archivo.write('}')
    archivo.close()
    #os.system('dot -Tpdf Mapa.dot -o G1.pdf')
validar_arch()
listaerrores()
listatoken()
separalista()
dibujarmapa()



"""
i=0
while i != 10:   
    i+=1
    print(i)
"""