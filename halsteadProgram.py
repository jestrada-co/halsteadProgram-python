import math
import re

delimitadores = ('(', ')', '[', ']', '{', '}', ',', '.', ';', '@', "'", "'")

operadores = {
	'=' : 0,
	'+' : 0,
	'-' : 0,
	'*' : 0,
	'/' : 0,
	'%' : 0,
	'@' : 0,
	'&' : 0,
	'|' : 0,
	'^' : 0,
	'~' : 0,
	'<' : 0,
	'>' : 0,
	':' : 0,
	'**' : 0,
	'//' : 0,
	'<<' : 0,
	'>>' : 0,
	'<=' : 0,
	'>=' : 0,
	'==' : 0,
	'!=' : 0,
	'->' : 0,
	'+=' : 0,
	'-=' : 0,
	'*=' : 0,
	'/=' : 0,
	'%=' : 0,
	'@=' : 0,
	'&=' : 0,
	'|=' : 0,
	'^=' : 0,
	'//=' : 0,
	'>>=' : 0,
	'<<=' : 0,
	'**=' : 0,
	'False' : 0,
	'None' : 0,
	'True' : 0,
	'and' : 0,
	'as' : 0,
	'assert' : 0,
	'break' : 0,
	'class' : 0,
	'continue' : 0,
	'def' : 0,
	'del' : 0,
	'elif' : 0,
	'else' : 0,
	'except' : 0,
	'finally' : 0,
	'for' : 0,
	'from' : 0,
	'global' : 0,
	'if' : 0,
	'import' : 0,
	'global' : 0,
	'if' : 0,
	'import' : 0,
	'in' : 0,
	'is' : 0,
	'lambda' : 0,
	'nonlocal' : 0,
	'not' : 0,
	'or' : 0,
	'pass' : 0,
	'raise' : 0,
	'return' : 0,
	'try' : 0,
	'while' : 0,
	'with' : 0,
	'yield' : 0
}

operandos = dict()
n1 = 0
n2 = 0
N1 = 0
N2 = 0
LoC = 0
CLoC = 0

with open('romanConverter.py') as archivo:

	for linea in archivo:

		linea = linea.lstrip()
		linea = linea.rstrip()
		if "'''" in linea:
			CLoC += 1
			linea = linea.replace(linea[linea.find("'''"):len(linea)], '')
		if '#' in linea:
			CLoC += 1
			linea = linea.replace(linea[linea.find('#'):len(linea)], '')

		if linea:
			LoC += 1
			for delimitador in delimitadores:
				linea = linea.replace(delimitador, ' ')
				palabras = linea.split()

			for palabra in palabras:
				if palabra in operadores:
					if operadores[palabra] == 0:
						n1 += 1
					operadores[palabra] += 1
					N1 += 1
				else:
					N2 += 1
					if palabra in operandos:
						operandos[palabra] += 1
					else:
						operandos[palabra] = 1
						n2 += 1

H = n1 * math.log(n1, 2) + n2 * math.log(n2, 2)
N = N1 + N2
n = n1 + n2
V = N * math.log(n, 2)
D = (n1 / 2) * (N2 / n2)
L = 1 / D
E = V * D
T = E / 18

print ('M e t r i c a s')
print (f'1. Longitud Halstead o Densidad del Codigo: {H}')
print (f'2. Largo del programa: {N}')
print (f'3. Tamaño del Vocabulario del programa: {n}')
print (f'4. Volumen del programa: {V}')
print (f'5. Nivel de Dificultad: {D}')
print (f'6. Nivel de Programa: {L}')
print (f'7. Esfuerzo de Implementacion: {E}')
print (f'8. Tiempo de Entendimiento: {T}')
print (f'9. Total Líneas de Codigo: {LoC}')
print (f'10. Total Líneas de Codigo Comentadas: {CLoC}')
