# 11. Con la información de los archivos de texto que se encuentran disponibles en el curso:
# • nombres_1
# • nombres_2
# • Indique los nombres que se encuentran en ambos. Nota: pruebe utilizando list comprehension.
# • Genere tres variables con la lista de notas y nombres que se incluyen en los archivos: nom-
# bres_1, eval1.txt y eval2.txt e imprima con formato los nombres de los estudiantes con las
# correspondientes nota y la suma de ambas como se ve en la imagen



def armarEstructuraDeNombres():
    f_nombres1 = open('nombres_1.txt','r',encoding='utf-8')
    f_nombres2 = open('nombres_2.txt','r',encoding='utf-8')
    nombres = f_nombres1.read()  + f_nombres2.read()
    f_nombres1.close()
    f_nombres2.close()
    return nombres

def imprimirConFormato():
    f_nombres1 =  open('nombres_1.txt','r',encoding='utf-8')
    f_eval1 = open('eval1.txt','r')
    f_eval2 = open('eval2.txt','r')
    print(f'Nombres          Eval1          Eval2           Total'),
    f_nombres1.close()
    f_eval2.close()
    f_eval1.close()

nombres = armarEstructuraDeNombres()
print (nombres)
imprimirConFormato()
# for key,value in arrAlumnos :
#     print(key,value[0],value[1],value[2])