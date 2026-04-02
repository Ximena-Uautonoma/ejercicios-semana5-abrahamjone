'''Registro de asistencia diaria
En una oficina se registra la asistencia hasta que el trabajador ingresa 0.
Solicita repetidamente:
1 si asistió
0 para terminar
Al final, muestra cuántos días asistió.'''
#1 asiste sumar x=cantidad de dias asistido x+1

asistencia=int(input("para marcar su asistencia escriba 1 y no escriba 0:"))

while(asistencia!=2) or(asistencia!=3) or (asistencia!=4)or (asistencia!=5)or (asistencia!=6)or (asistencia!=7)or (asistencia!=8)or (asistencia!=9):
    if(asistencia ==1):
       acumulacion=0
       print("otro dia asistido")
       acumulacion+1
       asistencia=int(input("para marcar su asistencia escriba 1 y no escriba 0:"))
    elif(asistencia==0):
        print("usted asistio",acumulacion,"dias")
        break
        


