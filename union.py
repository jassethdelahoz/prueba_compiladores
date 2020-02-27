import re

alfabeto = input("ingrese primer afabeto: ")
primeras_letras = alfabeto.replace('{','').replace('}','').replace(',','')
print ("estas son las primeras letras: " + primeras_letras)

alfabeto2 = input ("ingrese segundo alfabeto: ")
segundo_alfabeto = alfabeto2.replace('{','').replace('}','').replace(',','')
print ("estas son las segundas letras: " + segundo_alfabeto)

resultado = ""

for a in primeras_letras:
    letras_diferen = re.search(a,resultado)
    if (letras_diferen):
        pass
    else:
        resultado += a
    letras_diferen = False

for e in segundo_alfabeto:
    letras_diferen2 = re.search(e,resultado)
    if (letras_diferen2):
        pass
    else:
        resultado += e
    letras_diferen2 = False

print ("la union de los dos alfabetos es:" + resultado)