# 4. Para la aceptación de un artículo en un congreso se definen las siguientes especificaciones que
# deben cumplir y recomendaciones de escritura:
# • título: 10 palabras como máximo
# • cada oración del resumen:
# – hasta 12 palabras: fácil de leer
# – entre 13-17 palabras: aceptable para leer
# – entre 18-25 palabras: difícil de leer
# – mas de 25 palabras: muy difícil
# Dado un artículo en formato string, defina si cumple las especificaciones del título y cuántas ora-
# ciones tiene de cada categoría. El formato estándar en que recibe el string tiene la siguiente forma:

evaluar = """título: Experiences in Developing a Distributed Agent-based Modeling Toolkit with Python
resumen: Distributed agent-based modeling (ABM) on high-performance computing resources 
provides the promise of capturing unprecedented details of large-scale complex systems.
However, the specialized knowledge required for developing such ABMs creates barriers to
wider adoption and utilization. Here we present our experiences in developing an initial
implementation of Repast4Py, a Python-based distributed ABM toolkit. We build on our
experiences in developing ABM toolkits, including Repast for High Performance Computing
(Repast HPC), to identify the key elements of a useful distributed ABM toolkit. We leverage
the Numba, NumPy, and PyTorch packages and the Python C-API to create a scalable modeling
system that can exploit the largest HPC resources and emerging computing architectures.
"""
# En este ejemplo debería informar:
# • titulo está ok
# • Cantidad de oraciones fáciles de leer: 1, aceptables para leer: 2, dificil de leer: 1, muy dificil
# de leer: 2

# Notas: * investigue Pattern Matching para una solución simplificada. * ¿cuántas variables utilizó
# para guardar la cantidad de cada categoría, se podría usar alguna estructura?

categorias = [0,0,0,0]
titulo = evaluar.split('\n')[0].split('titulo: ')[0].split(' ')
if(len(titulo)-1 <= 10):
    print('El titulo esta OK')
else:
    print('El titlo esta MAL')

resumen = evaluar.replace('\n',' ')[:-1]
resumen = resumen.split('resumen: ')[1].split('.')

for sentence in resumen:
    largo = len(sentence.split())
    if(largo <= 12):
        categorias[0] +=1
    elif(largo <=17):
        categorias[1] +=1 
    elif(largo <=25): 
        categorias[2] +=1
    else:
        categorias[3] +=1
print(f'Cantidad de oraciones faciles de leer: {categorias[0]}')
print(f'Aceptables para leer: {categorias[1]}')
print(f'Dificil de leer: {categorias[2]}')
print(f'Muy dificil  de leer:{categorias[3]}')







