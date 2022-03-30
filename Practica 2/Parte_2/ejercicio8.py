# 8. Escriba un programa que solicite por teclado una palabra y calcule el valor de la misma dada
# la siguiente tabla de valores del juego Scrabble:
import re 
tabla_de_valores = ('[AEIOULNRST]','[DG]','[BCMP]','[FHVWY]','[K]','[JX]','[QZ]')
puntaje = (1,2,3,4,5,8,10)

frase = input('Ingrese una frase ').upper()
total = 0 
for i,valores in enumerate(tabla_de_valores):
    valor = re.findall(valores,frase)
    total += len(valor)*puntaje[i]
    print(valor)
print (f'Total de puntos {total}')