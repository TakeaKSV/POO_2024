from conexionBD import *

try: 
    micursor=conexion.cursor()

    sql="delete from clientes where id=4"
    micursor.execute(sql)

    conexion.commit()
    
except:
    print(f"Falleciooo :CCC")

else:
    print("Registro eliminado registramente")

