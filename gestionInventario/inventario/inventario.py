# inventario.py
import sqlite3

class Inventario:
    def __init__(self, db_name="inventario.db"):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name, check_same_thread=False)  # Allow connection across threads
        self.c = self.conn.cursor()
        self.c.execute('''
        CREATE TABLE IF NOT EXISTS inventarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            precio REAL NOT NULL,
            unidad INTEGER NOT NULL
        )
        ''')
        self.conn.commit()

    def añadir(self, nombre, precio, unidad):
        self.c.execute("INSERT INTO inventarios (nombre, precio, unidad) VALUES (?, ?, ?)",
                       (nombre, precio, unidad))
        self.conn.commit()
        print("Añadido con éxito")

    def mostrar(self):
        self.c.execute("SELECT * FROM inventarios")
        datos = self.c.fetchall()
        return datos

    def buscar(self, id):
        self.c.execute("SELECT * FROM inventarios WHERE id = ?", (id,))
        return self.c.fetchone()

    def actualizar(self, id, nuevo_nombre, nuevo_precio, nueva_unidad):
        self.c.execute('''
        UPDATE inventarios
        SET nombre = ?, precio = ?, unidad = ?
        WHERE id = ?
        ''', (nuevo_nombre, nuevo_precio, nueva_unidad, id))
        self.conn.commit()

    def eliminar(self, id):
        self.c.execute("DELETE FROM inventarios WHERE id = ?", (id,))
        self.conn.commit()
