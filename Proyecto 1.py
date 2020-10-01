from Clase2 import clase
import os.path



"""
clase1 = clase()
clase2 = clase()
print(clase.num2)
print("-------------------------------------------------------")
print("Nombre: Pablo Rufino Quevedo Berdúo  \nCarne: 201701081" )
print("-------------------------------------------------------")
print("BIENVENIDO \nIngrese el numero de una opción o exit para salir")
print("1.  Cargar Archivo    \n2.  Graficar Operacion \n3. Graficar Ruta   \n4.  Salir")
"""

def validar_arch():  # validacion de la extension correcta   
    ruta = input()
    nombre_archivo, extension = os.path.splitext(ruta)
    #aqui esta la ruta del archivo
    if extension == ".txt":
        print("ruta correcta")
        archivo = open(ruta, "r", encoding="utf-8")    
        for linea in archivo.readlines(): #separa con cada salto de linea
            #comp = linea.split()  # comp se vuelve en un arreglo con cada linea
            # range(1,len(comp))-- da la posicion sin incluir in, post o pre
            #print(linea)
            
            comp = linea.split()
            if len(comp) == 0:  # valida si vienen una linea vacia              
                print("aqui hay lineas en blanco xd")
            else:
                print(linea,end="")
                """
                for x in range(1, len(comp)):
                    print(comp[x])            
                #print("Operación", p,end=" ")
                """
        archivo.close()
    else:
        print("la ruta ingresada es incorrecta")
        # volver a llamar al metodo para volver a ingresar la ruta

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