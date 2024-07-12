from conexionBD import *

try: 
    micursor=conexion.cursor()

    sql="update clientes set direccion='Col. Vizcaya' where id=5"
    micursor.execute(sql)

    conexion.commit()
    
except:
    print(f"Falleciooo :CCC")

else:
    print("Registro actualizado exitosamente")