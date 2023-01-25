
def  ordenarFecha( a) :

    aux = [None] * (len(a))
    aux[0] = a[0]
    aux[1] = a[len(a) - 1]
    i = 2
    while (i < len(a)) :
        aux[i] = a[i - 1]
        i += 1
    return aux

def mostrarFecha( a) :

    datos=[]
    numero = int(len(a) / 2)
    con = 0
    i = 0
    while (i < len(a)) :
        if (con != numero) :
            ariel=str(a[i] + " vs " + a[(len(a) - con) - 1])
            con += 1
            datos.append(ariel)
        i += 1
    return datos

data=[]
#array de los nombres de los equipos

a = ["eq 1", "eq 2", "eq 3", "eq 4", "eq 5", "eq 6", "eq 7", "eq 8"]
print("las fechas de partidos son : " + str((len(a) - 1)))
if (len(a) % 2 == 0) :

    i = 0
    while (i < len(a) - 1) :

        print("=========== fecha " + str((i + 1)) + "==============")
        if (i == 0) :

            data.append(mostrarFecha(a))
        else :

            aux = ordenarFecha(a)
            data.append(mostrarFecha(aux))
            a = aux
        i += 1

print("-------------- datos ----------------------")
for a in data:
    print(a)
