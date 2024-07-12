from conexionBD import *

try:
    micursor=conexion.cursor()

    sql="select nombre, * from clientes"
    micursor.execute(sql)

    #Crear un objeto para enviar el resultado de la ejecucion del execute para posteriormente mostrar con un ciclo
    resultado=micursor.fetchall()

except:
    print(f"Ocurrio un problemooon :C")

else:
    for x in resultado:
        print(x) 