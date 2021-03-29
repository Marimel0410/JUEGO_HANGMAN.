import random as RD
import os 

print ("¡Bienvenio, vamos a juegar !")
print ("ADIVINA LA PALABRA")
print ("Hay palabras en Español y el tema COMPUTACIÓN")

Palabra = ["PROGRAMA", "SOFTWARE", "PYTHON","EJECUTAR", "PARADIGMA"
"OBJETO", "LENGUAJE", "COMPUTADORAS", "MOUSE", "INTERNET", "TECLADO", "SISTEMA",
"RESDES", "PROGRAMACIÓN ", "INFORMÁTICA", "BOCINA", "DISPOSITIVO", "ENTRADA", "SALIDA"
"INGENIERO", "ANALISTA", "DATOS", "REQUERIMIENTO", "NUBE", "ALMACENAMIENTO", "RAM", "MEMORIA",
"CHIP","CALCULADORA"]


indice = RD.randint (0, len(Palabra) - 1)
pal = Palabra[indice].upper()
l1 = pal [0]
lu = pal[-1]
n =len(pal)-2
guiones = n * " _ " 
pista = l1  +  guiones + lu
print (pista)
Palla =(input("ADIVINA cual es la palabra "))
        
if Palla == pal:
	print ("felicidades acertaste!!")

	print ("""
              
              [O]
              /|/
               |
              _|_
  
	 """)
if Palla != pal:
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












	







