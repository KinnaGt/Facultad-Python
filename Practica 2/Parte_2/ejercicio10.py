# Manipule estos archivos para realizar lo siguiente:
# • Generar una estructura con los nombres de los estudiantes y la suma de ambas notas.
# • Calcular el promedio de las notas totales e informar que alumnos obtuvieron menos que el
# promedio.

# nombres eval1 y eval2

def armarEstructura():
    nombres = open('nombres_1.txt', 'r', encoding='utf-8')
    ev1 = open('eval1.txt', 'r')
    ev2 = open('eval2.txt', 'r')
    arrAlumnos = []

    for x in nombres:
        suma_de_notas = int(ev1.readline().replace(',', '')) + \
            int(ev2.readline().replace(',', ''))
        arrAlumnos.append(
            (x.replace('\n', ''), suma_de_notas))

    ev1.close()
    ev2.close()
    nombres.close()

    return arrAlumnos


def sacarPromedio(arrAlumnos):
    prom = 0
    for i in arrAlumnos:
        prom += i[1]
    prom = prom / len(arrAlumnos)
    return prom


def printearMenoresAlPromedio(arrAlumnos,prom):
    for value in arrAlumnos:
        if(value[1] < prom):
            print(value[0].replace(',', '').replace('\'', ''))


arrAlumnos = armarEstructura()

prom = sacarPromedio(arrAlumnos)
print(f'Promedio de notas totales = {prom} ')

print('Alumnos con notas menor al promedio : ')
printearMenoresAlPromedio(arrAlumnos,prom)
