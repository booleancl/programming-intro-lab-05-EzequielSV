#funciones con parámetros

def print_param(daddy):
    print(daddy)
    print(daddy)

#no es necesario que el nombre del objeto que vamos a usar como argumento sea el mismo que el del parámetro
print_param(77)

singer = "marcianeke"
print_param(singer)

#calcular el radio de una esfera de radio 5
def volume(radio):
    result = 4/3 * 3.1416 * (radio)**3
    print(result)

big = 7
small = 2
volume(big)
volume(small)


def multiply_by_2(number):
    number = number * 2
    print(number)

multiply_by_2(big)
print(big)

#función de 2 parámetros

def concat_strings(str1,str2):
    longstr = str1 + " " + str2
    print(longstr)

text1 = "pasito a pasito"
text2 = "suave suavecito"

concat_strings(text1,text2)