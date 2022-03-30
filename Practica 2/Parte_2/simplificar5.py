# 5_ Retomamos el código visto en la teoría, que informaba si los caracteres “@” o “!” formaban
# parte de una palabra ingresada

# cadena = input("Ingresa la clave (debe tener menos de 10 caracteres y no contener los símbolos:@ y !):")
# if len(cadena) > 10:
#     print("Ingresaste más de 10 caracteres")
# cant = 0
# for car in cadena:
#     if car == "@" or car == "!":
#         cant = cant + 1
# if cant >= 1:
#     print("Ingresaste alguno de estos símbolos: @ o !" )
# else:
#     print("Clave válida")

# ¿Cómo podemos simplificarlo?

cadena = input(
    "Ingresa la clave (debe tener menos de 10 caracteres y no contener los símbolos:@ y !):")
if len(cadena) > 10:
    print("Ingresaste más de 10 caracteres")
if ('@' in cadena) | ('!' in cadena):
    print('Pusiste: @ y ! en la cadena campeón')
else:
    print('Clave valida ')
