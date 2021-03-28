import random as RD
import os 

print ("¡Bienvenio, vamos a juegar !")
print ("ADIVINA LA PALABRA")
print ("Hay palabras en Español y en Ingles, ambas con el mismo tema COMPUTACIÓN")
seleccion = int(input("Para jugar en ESPAÑOL ingrese 1/Para jugar en INGLES ingrese 2  "))


Palabra = ["PROGRAMA", "SOFTWARE", "PYTHON","EJECUTAR", "PARADIGMA"
"OBJETO", "LENGUAJE", "COMPUTADORAS", "MOUSE", "INTERNET", "TECLADO", "SISTEMA",
"RESDES", "PROGRAMACIÓN ", "INFORMÁTICA", "BOCINA", "DISPOSITIVO", "ENTRADA", "SALIDA"
"INGENIERO", "ANALISTA", "DATOS", "REQUERIMIENTO", "NUBE", "ALMACENAMIENTO", "RAM", "MEMORIA",
"CHIP","CALCULADORA"]

WORDENGLISH = ["PROGRAM", "SOFTWARE", "PYTHON","EXECUTE", "PARADIGMA"
"OBJECT", "LANGUAGE", "COMPUTERS", "MOUSE", "INTERNET", "KEYBOARD", "SYSTEM",
"RESDES", "PROGRAMMING", "INFORMATICS", "SPEAKER", "DEVICE", "INPUT", "OUTPUT"
"ENGINEER", "ANALYST", "DATA", "REQUIREMENT", "NUBE", "STORAGE", "RAM", "MEMORY",
"CHIP","CALCULATOR"]


if seleccion ==1:
	indice = RD.randint (0, len(Palabra) - 1)
	pal = Palabra[indice].upper()
	l1 = pal [0]
	lu = pal[-1]
	n =len(pal)-2
	guiones = n * " _ " 
	pista = l1  +  guiones + lu
	print (pista)
	Palaingresada = input ("ADIVINA cual es la palabra ").upper()

if Palaingresada == pal:
	print ("felicidades acertaste!!")

	print ("""
              
              [O]
              /|/
               |
              _|_
  
	 """)
else:
	print ("mejor suerte para la proxima, la palabra era:", pal)
	print (""" 

                _______
               |       |
              [x]      |
              /|/      |
               |       | 
              _|_    __| _____


		""")
	print ("BYE")


if seleccion ==2:
	indice = RD.randint (0, len(WORDENGLISH ) - 1)
	pal = WORDENGLISH [indice].upper()
	l1 = pal [0]
	lu = pal[-1]
	n =len(pal)-2
	guiones = n * " _ " 
	Pis = l1 +  guiones + lu
	print (Pis)
	Palaingresada = input ("guess what the word is ").upper()

if Palaingresada == pal:
	print ("congratulations you got it right!!")

	print ("""
              
              [O]
              /|/
               |
              _|_
  
	 """)
else:
	print ("better luck for the next one the word was: ", pal)
	print (""" 

                _______
               |       |
              [x]      |
              /|/      |
               |       | 
              _|_    __| _____


		""")
	print ("BYE")











	







