
import pandas as pd
import mysql.connector

# Leer el archivo de Excel
datos = pd.read_excel("data.xlsx")

# Conectarse a MySQL
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Karol2208",
    database="proyecto_normalización"
)

cursor = conexion.cursor()

# Insertar los niveles educativos que aparecen en Excel
for nivel in datos["nivel_edu"].dropna().unique():
    cursor.execute(
        "INSERT IGNORE INTO nivel_educativo (nombre) VALUES (%s)",
        (str(nivel),)
    )

# Insertar los sexos que aparecen en Excel
for sexo in datos["sex"].dropna().unique():
    cursor.execute(
        "INSERT IGNORE INTO sexo (nombre) VALUES (%s)",
        (str(sexo),)
    )

conexion.commit()

# Consultar los identificadores de las categorías
cursor.execute("SELECT id_nivel_educativo, nombre FROM nivel_educativo")
niveles = {nombre: identificador for identificador, nombre in cursor.fetchall()}

cursor.execute("SELECT id_sexo, nombre FROM sexo")
sexos = {nombre: identificador for identificador, nombre in cursor.fetchall()}

# Insertar las personas
for _, fila in datos.iterrows():
    nivel = str(fila["nivel_edu"]) if pd.notna(fila["nivel_edu"]) else None
    sexo = str(fila["sex"]) if pd.notna(fila["sex"]) else None

    cursor.execute(
        """
        INSERT INTO persona
        (id_persona, edad, id_nivel_educativo, anios_esc,
         ingreso_mensual, id_sexo)
        VALUES (%s, %s, %s, %s, %s, %s)
        """,
        (
            int(fila["id"]),
            int(fila["edad"]) if pd.notna(fila["edad"]) else None,
            niveles.get(nivel),
            int(fila["anios_esc"]) if pd.notna(fila["anios_esc"]) else None,
            float(fila["ingreso_mensual"]) if pd.notna(fila["ingreso_mensual"]) else None,
            sexos.get(sexo)
        )
    )

conexion.commit()
print("Datos cargados correctamente.")

cursor.close()
conexion.close()


