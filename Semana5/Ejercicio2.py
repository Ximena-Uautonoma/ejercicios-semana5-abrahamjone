'''Control de temperatura
Un sistema de climatización clasifica:
"Fría": menos de 10°C
"Templada": entre 10 y 25
"Calurosa": más de 25
Solicita la temperatura e indica la clasificación correspondiente.
'''
#entrar una temperatura y segmentarla en frio templado y caluroso
#como se hace
#for= un ciclo que se repite en un rango
temperatura=int(input("escriba la teperatura en grados celcius:"))
for temperatura in range (temperatura<10):
    print ("esta frio afuera")
for temperatura in range(10<=temperatura<=25):
    print("esta templado")
for temperatura in range (temperatura>=26):
    print("hace calor afuera")