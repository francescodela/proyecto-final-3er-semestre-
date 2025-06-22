#codigo modificado y mejorado del anterior (18/06 hora 9:08 am ) 
#FUNCIONAL SIN ERRORES 


import tkinter as tk
from tkinter import messagebox
from Controllers.AdminFuncion import FuncionesAdmin  # Importar funciones

class AdminVista:
    def __init__(self, root, sistema):
        self.root = root
        self.sistema = sistema
        self.funciones = FuncionesAdmin(self, sistema)  # Instancia funciones

        self.root.title("Sistema de Comandas - Administrador")
        self.root.geometry("800x600")

        self.menu_bar = tk.Menu(self.root)

        meseros_menu = tk.Menu(self.menu_bar, tearoff=0)
        meseros_menu.add_command(label="Registrar Mesero", command=self.funciones.registrar_mesero)
        meseros_menu.add_command(label="Eliminar Mesero", command=self.funciones.eliminar_mesero)
        self.menu_bar.add_cascade(label="Gestionar Meseros", menu=meseros_menu)

        informes_menu = tk.Menu(self.menu_bar, tearoff=0)
        informes_menu.add_command(label="Informe Diario", command=self.funciones.generar_informe)
        self.menu_bar.add_cascade(label="Informes", menu=informes_menu)

        self.menu_bar.add_command(label="Salir", command=self.root.quit)
        self.root.config(menu=self.menu_bar)

        # Frame principal
        self.main_frame = tk.Frame(self.root, bd=2, relief=tk.GROOVE)
        self.main_frame.place(x=20, y=20, width=760, height=560)

        # Título
        self.title_label = tk.Label(self.main_frame, text="Panel de Administración", font=("Helvetica", 16))
        self.title_label.place(x=250, y=10)

        # Botones tipo pestañas sin command
        self.btn_meseros = tk.Button(self.main_frame, text="Meseros")
        self.btn_meseros.place(x=10, y=50, width=100, height=30)
        self.btn_meseros.bind("<Button-1>", lambda event: self.funciones.mostrar_meseros())

        self.btn_comandas = tk.Button(self.main_frame, text="Comandas")
        self.btn_comandas.place(x=120, y=50, width=100, height=30)
        self.btn_comandas.bind("<Button-1>", lambda event: self.funciones.mostrar_comandas())

        # Frames que actúan como pestañas
        self.meseros_frame = tk.Frame(self.main_frame, bd=1, relief=tk.SUNKEN)
        self.meseros_frame.place(x=10, y=90, width=740, height=460)

        self.comandas_frame = tk.Frame(self.main_frame, bd=1, relief=tk.SUNKEN)
        self.comandas_frame.place(x=10, y=90, width=740, height=460)

        # Inicialmente muestro meseros
        self.funciones.mostrar_meseros()

        # Cargar tablas con datos (los métodos de funciones manejan la UI dentro de estos frames)
        self.funciones.cargar_meseros()
        self.funciones.cargar_comandas()

        btn_ayuda = tk.Button(self.main_frame, text=" Ayuda")
        btn_ayuda.place(x=700, y=10, width=70, height=30)  # Ajusta posición y tamaño según sea necesario
        btn_ayuda.bind("<Button-1>", self.funciones.mostrar_ayuda)



'''
    def mostrar_meseros(self):
        self.meseros_frame.lift()  # Traer al frente el frame meseros

    def mostrar_comandas(self):
        self.comandas_frame.lift()  # Traer al frente el frame comandas
'''

#CODIGO ANTERIOR FUNCIONABLE 
'''
from tkinter import ttk, messagebox
import tkinter as tk
from Controllers.AdminFuncion import FuncionesAdmin  # Importar funciones

class AdminView:
    def __init__(self, root, sistema):
        self.root = root
        self.sistema = sistema
        self.funciones = FuncionesAdmin(self, sistema)  # Instancia funciones

        self.root.title("Sistema de Comandas - Administrador")
        self.root.geometry("800x600")

        self.menu_bar = tk.Menu(self.root)

        meseros_menu = tk.Menu(self.menu_bar, tearoff=0)
        meseros_menu.add_command(label="Registrar Mesero", command=self.funciones.registrar_mesero)

    #   meseros_menu.add_command(label="Registrar Mesero", command=self.registrar_mesero)
        meseros_menu.add_command(label="Eliminar Mesero", command=self.funciones.eliminar_mesero)  # delega en funciones
        self.menu_bar.add_cascade(label="Gestionar Meseros", menu=meseros_menu)

        informes_menu = tk.Menu(self.menu_bar, tearoff=0)
        informes_menu.add_command(label="Informe Diario", command=self.funciones.generar_informe)  # delega en funciones
        self.menu_bar.add_cascade(label="Informes", menu=informes_menu)

        self.menu_bar.add_command(label="Salir", command=self.root.quit)
        self.root.config(menu=self.menu_bar)

        self.main_frame = ttk.Frame(self.root, padding="20")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(self.main_frame, text="Panel de Administración", font=("Helvetica", 16)).pack(pady=10)

        self.notebook = ttk.Notebook(self.main_frame)

        self.meseros_frame = ttk.Frame(self.notebook)
        self.funciones.cargar_meseros()
      # self.cargar_meseros()
        self.notebook.add(self.meseros_frame, text="Meseros")

        self.comandas_frame = ttk.Frame(self.notebook)
        self.funciones.cargar_comandas()
    #   self.funciones.cargar_comandas()
        self.notebook.add(self.comandas_frame, text="Comandas")


        
        self.notebook.pack(fill=tk.BOTH, expand=True)

     '''

#DEFS DESABILITADOS PORQUE YA ESTAN EN FUNCIONESADMIN 
'''
    def cargar_meseros(self):
        # Solo UI: limpiar y mostrar tabla con meseros
        for widget in self.meseros_frame.winfo_children():
            widget.destroy()
        meseros = self.sistema.obtener_meseros()
        columns = ("Cédula", "Nombre", "Teléfono", "Dirección", "Email")
        self.meseros_tree = ttk.Treeview(self.meseros_frame, columns=columns, show="headings")
        for col in columns:
            self.meseros_tree.heading(col, text=col)
            self.meseros_tree.column(col, width=120)
        for mesero in meseros:
            self.meseros_tree.insert("", tk.END, values=(
                mesero.cedula, mesero.nombre, mesero.telefono, mesero.direccion, mesero.email
            ))
        self.meseros_tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    def cargar_comandas(self):
        # Solo UI: limpiar y mostrar tabla con comandas
        for widget in self.comandas_frame.winfo_children():
            widget.destroy()
        comandas = self.sistema.obtener_comandas()
        columns = ("ID", "Cliente", "Mesa", "Total", "Estado")
        self.comandas_tree = ttk.Treeview(self.comandas_frame, columns=columns, show="headings")
        for col in columns:
            self.comandas_tree.heading(col, text=col)
            self.comandas_tree.column(col, width=120)
        for comanda in comandas:
            if comanda is None:
                continue
            self.comandas_tree.insert("", tk.END, values=(
                comanda.id, comanda.cedula_cliente, comanda.numero_mesa,
                f"${comanda.precio_total:,.2f}", comanda.estado
            ))
        self.comandas_tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    def registrar_mesero(self):
        # Crear ventana registro (UI)
        self.registro_window = tk.Toplevel(self.root)
        self.registro_window.title("Registrar Mesero")
        self.registro_window.geometry("400x300")
        frame = ttk.Frame(self.registro_window, padding="20")
        frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(frame, text="Registrar Mesero", font=("Helvetica", 14)).grid(row=0, column=0, columnspan=2, pady=10)
        fields = ["cedula", "nombre", "telefono", "direccion", "email", "password"]
        self.entries = {}
        for i, field in enumerate(fields, start=1):
            ttk.Label(frame, text=field.capitalize() + ":").grid(row=i, column=0, sticky=tk.W, pady=5)
            entry = ttk.Entry(frame, show="*" if field == "password" else None)
            entry.grid(row=i, column=1, sticky=tk.EW, pady=5)
            self.entries[field] = entry

        button_frame = ttk.Frame(frame)
        button_frame.grid(row=len(fields)+1, column=0, columnspan=2, pady=10)
        ttk.Button(button_frame, text="Guardar", command=self.funciones.guardar_mesero).pack(side=tk.LEFT, padx=5)  # lógica en funciones
        ttk.Button(button_frame, text="Cancelar", command=self.registro_window.destroy).pack(side=tk.LEFT, padx=5)
        frame.columnconfigure(1, weight=1)
'''