import mysql.connector 

#Conectar con la BD en Mysql
try:
    conexion=mysql.connector.connect(
    host='127.0.0.1n',
    user='root',
    password='',
    database='bd_python'
    )
except Exception as e:
    print(f"Error: {type(e)}")
    print(f"Tipo de excepcion: {type(e).__name__}")
    print(f"Ocurrio un error D: verifica")
    
else:
#Verificar si la conexion fue exitosa

    if conexion.is_connected():
        print('Se creo la conexion a la base de datos correctamente :D')
    
    else:
        print('No fue posible conectarse a la base de datos :C')
    
