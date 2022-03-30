# 5. Dada una frase y un string ingresados por teclado (en ese orden), e informe la cantidad de
# veces que se encuentra el string en la frase. No distingir entre mayúsculas y minúsculas.


# frase = 'A la grande le puse cuca'

# string = input('Ingrese una cadena: ').lower()

# palabras = frase.split()
# repetidas = 0
# for palabra in palabras:
#     if(palabra == string):
#         repetidas += 1
# print(f'La palabra {string} se encuentra {repetidas} veces')

#CON COUNT

frase = input('Ingrese una frase ')

string = input('Ingrese una cadena: ').lower()

palabras = frase.lower().split()

print(f'La palabra {string} se encuentra {palabras.count(string)}')