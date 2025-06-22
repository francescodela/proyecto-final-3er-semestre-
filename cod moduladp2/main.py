import tkinter as tk
from Models.datosbase import ConexionBD
from Controllers.controllers import SistemaRestaurante
from Views.Loggin import Login

def main():
    # Inicializar base de datos
    db = ConexionBD()

    

    # Inicializar sistema
    sistema = SistemaRestaurante(db)

    # Insertar un mesero de prueba si no hay
    if not sistema.obtenerMeseros():
        db.hacerConsultas("""
            INSERT INTO mesero (cedula, nombre, telefono, direccion, email, password)
            VALUES (?, ?, ?, ?, ?, ?)
        """, ("111", "Pedro", "123456", "Calle A", "pedro@rest.com", "mesero123"))
        print(" Mesero de prueba insertado")

    # Insertar un cliente de prueba si no hay
    if not sistema.obtenerClientes():
        db.hacerConsultas("""
            INSERT INTO cliente (cedula, nombre, telefono, direccion, email, password)
            VALUES (?, ?, ?, ?, ?, ?)
        """, ("222", "Laura", "789012", "Calle B", "laura@cliente.com", "cliente123"))
        print(" Cliente de prueba insertado")

    # Insertar una mesa si no hay
    if not sistema.obtenerMesas():
        for i in range(1, 6):
            db.hacerConsultas("INSERT INTO mesa (numero, estado) VALUES (?, ?)", (i, 'libre'))
        print(" Mesas iniciales registradas")

    # Insertar algunos platos si no hay
    if not sistema.obtenerPlatos():
        platos = [("Arroz con pollo", 12000), ("Pasta carbonara", 15000), ("Jugo natural", 5000)]
        for nombre, precio in platos:
            db.hacerConsultas("INSERT INTO plato (nombre, precio) VALUES (?, ?)", (nombre, precio))
        print(" Platos registrados")

    # Mostrar login
    root = tk.Tk()
    Login(root, sistema)
    root.mainloop()

    # Cerrar conexión al salir
    db.cerrarConexion()

if __name__ == "__main__":
    main()
