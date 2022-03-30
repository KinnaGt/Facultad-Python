# 7. Escriba un programa que solicite que se ingrese una palabra o frase y permita identificar si la
# misma es un Heterograma (tenga en cuenta que el contenido del enlace es una traducción del
# inglés por lo cual las palabras que nombra no son heterogramas en español). Un Heterograma
# es una palabra o frase que no tiene ninguna letra repetida entre sus caracteres.

# Tener en cuenta - Lo que no se puede repetir en la frase son sólo aquellos caracteres que sean
# letras. - No se distingue entre mayúsculas y minúsculas, es decir si en la frase o palabra tenemos
# la letra “T” y la letra “t” la misma NO será un Hererograma. - Para simplificar el ejercicio vamos
# a tomar como que las letras con tilde y sin tilde son distintas. Ya que Python las diferencia:

#Forma por Filter
cadena = input('Ingresa una cadena y te digo si es un heterograma o no : ')
cadena = list(filter(lambda x: x.isalpha(),cadena))

if(len(cadena) == len(set(cadena))):
    print('Es un heterograma')
else:
    print('No lo es')


#Forma por comprension
cadena = input('Ingresa una cadena y te digo si es un heterograma o no : ')
cadena = [letter for letter in cadena if letter.isalpha()]

if(len(cadena) == len(set(cadena))):
    print('Es un heterograma')
else:
    print('No lo es')