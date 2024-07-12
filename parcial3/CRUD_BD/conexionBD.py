import mysql.connector

try:
    #Conectar con la bd en Mysql
    conexion=mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database='bd_python'
    )
except:
    print("Se hizo mal papu")
    
else:
    print("Ocurrio uno bueno tonoto")
    
#verificar si la conexxion fue exitosa
#if conexion.is_connected():
    #print(f"Se creo la coneccion con la base de datos correctamente")
##print(f"No fue posible conectarse con la base de datos............... verifique")