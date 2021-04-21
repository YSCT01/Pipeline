
#Pipeline
#Yared Said Chávez Del Toro  4°P  19310185

#Funciones
#Obtener posicion de 0
def getZeros(vector, pos, cont):
    # Inicio for
    for p in range(len(vector), 0, -1):
        cont += 1
        # inicio if
        if vector[p - 1] == "0":
            pos.append(cont) # Guardar posición de los 0
        # endif
    # endfor
    #print(pos)
    cont = 0#Resetea el contador

#Vector de colisión resultante
def vectorCol(pos, vector, result, cont, relation, lispos):
    helper = list(vector)#Convertir vector a lista
    helper2 = []

    #inicio for
    for n in range(pos):#LLenar con 0 según el vector
        helper.pop(len(helper)-1)
        helper.insert(0, "0")
    #endfor

    #inicio for
    for i in range(len(vector), 0, -1):#Comparar los valores para generar el vector inicial
        #inicio if
        if vector[i-1] == "1" or helper[i-1] == "1":
            helper2.append("1")
        else:
            helper2.append("0")
        #endif
    # endfor
    helper2.reverse()#Gira el arreglo
    stringhelp2 = ""
    shelper2 = stringhelp2.join(helper2)
    relation = relation +","+str(pos);
    result[f"{relation}"]=helper2#Lo guarda en un diccionario
    #inicio if
    if helper2 != vector and shelper2 != "111111" and shelper2 != vector:
        last = len(lispos)#Obtener valor actual recorrido de 0
        getZeros(helper2, lispos, cont)#Rellenar con 0 los nuevos valores
        #print(lispos)

        for n in range(last, len(lispos), 1):#Recorre los nuevos 0 encontrados
            #print(lispos[n])
            vectorCol(lispos[n], helper2, result, cont, relation, lispos)#evalúa el vector
        #print(result)
    #endif
    relation=""#vaciar cadena
    #inicio for
    #for l in helper:
    #    print(l, end="")
    #endfor
    #print("\n------")



#Main
print("Welcome\n")
vector = input("Enter the vector: ")
pos=[]
result ={}
cont =0
relation = ""
#Inicio if
if vector == "111111":
    print("Vector completo")
elif vector == "000000":
    print("Vector nulo")
else:
    # Inicio for
    for p in range(len(vector), 0, -1):
        cont += 1
        # inicio if
        if vector[p - 1] == "0":
            pos.append(cont)  # Guardar posición de los 0
        # endif
    # endfor
    cont = 0  # Resetea el contador
    for n in range(len(pos)):
        vectorCol(pos[n], vector, result, cont, relation, pos)


print(result)





