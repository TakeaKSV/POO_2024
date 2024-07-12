from conexionBD import *

try:
    micursor=conexion.cursor()
    
    nombre=input("Cual es tu nombre?")
    direccion=input("Cual es tu direccion?")
    tel=input("Cual es tu telefono?")
    
    #sql="insert into clientes(id,nombre,direccion,tel) values (null,'Daniel Contreras','Col. centro','6181234567')"
    sql="insert into clientes(id,nombre,direccion,tel) values (null,%s,%s,%s)"
    
    valores=(nombre, direccion, tel)
    
    micursor.execute(sql, valores)

    #Sirve para finalizar la ejecucion del SQL
    conexion.commit()

except:
    print(f"Ocurrio un problemin D:")
    
else:
    print(f"Registro Insertado Exitosamente")