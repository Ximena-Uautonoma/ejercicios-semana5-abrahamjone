'''Cajero automático: validación de retiro
Un cajero permite retirar solo montos mayores a 0 y múltiplos de 10.
Solicita el monto hasta que sea válido y luego muestra "Retiro exitoso".'''

monto_a_sacar=int(input("ingrese la cantidad a retirar"))
otro_retiro=0
while(otro_retiro==0):
    while(monto_a_sacar == 0):
        print("porfavor ingrse un monto valido mayor a 0")
        otro_retiro=int(input("si desea salir aprete cualquier numero:"))
    retiro=monto_a_sacar%10
    if (retiro==0):
        print("retiro exitoso")
        otro_retiro=int(input("si desea salir aprete cualquier numero:"))
    elif(retiro!=0):
        print("porfavor ingrese una opcion valida")
        otro_retiro=int(input("si desea salir aprete cualquier numero:"))