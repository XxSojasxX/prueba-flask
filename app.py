from conexion import abrirconexion

def registro():
        conexion = abrirconexion()
        cursor   = conexion.cursor()
        cursor.execute('SELECT * FROM Usuario')
        print(cursor.fetchall())
        conexion.commit()
        
registro()