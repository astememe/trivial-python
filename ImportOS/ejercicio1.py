"""Vas a crear un programa en Python que gestione archivos y carpetas para una supuesta aplicación de respaldo.
El programa debe hacer lo siguiente:

1. Comprobar si existe un directorio llamado Origen.
2. Si no existe, crearlo y generar dentro varios archivos de texto.
3. Leer el contenido de los archivos usando open().
Comprobar:
4. Si el nombre del archivo termina en .txt usando endswith()
5. Si una palabra clave (por ejemplo "backup") está contenida en el texto usando la cláusula in
6. Copiar archivos válidos a un directorio Respaldo usando shutil.copy
7. Copiar todo el directorio Respaldo a RespaldoTotal usando shutil.copytree
8. Cambia el nombre del archivo que contiene backup a importante.txt
9. Elimina los archivos no válidos con os.unlink"""

import os, shutil
import random
import string

os.chdir("C:\\Users\\ememe\\Desktop\\Clase\\Programación Python\\ejercicios_mario\\escritura_lectura\\ImportOS")
if not os.path.exists("./Origen/"):
    os.mkdir("./Origen")

for i in range(10):
    if not os.path.exists("./Origen/archivo" + str(i+1)):
        open("Origen\\archivo"+str((i+1)), "x")
        with open("Origen\\archivo"+str(i+1), "w") as fichero:
            fichero.write(string.printable[random.randint(0, len(string.printable) - 1)])

numero_archivos = len(os.listdir("./Origen"))

for i in range(2, numero_archivos):
    with open("./Origen/archivo" + str(i - 1), "r") as fichero:
        linea = fichero.readline()
        while linea:
            print(linea)
            linea = fichero.readline()
    fichero.close()


for i in range(numero_archivos):
    if not os.listdir("./Origen")[i].endswith(".txt") and "backup" not in os.listdir("./Origen")[i]:
        shutil.copy("./Origen/" + str(os.listdir("./Origen")[i]), "./Respaldo")
    if "backup" in os.listdir("./Origen")[i]:
        print(os.listdir("./Origen")[i])
        shutil.move("./Origen/" + os.listdir("./Origen")[i], "./Origen/importante.txt")
    elif "importante" in os.listdir("./Origen")[i]:
        shutil.move("./Origen/" + os.listdir("./Origen")[i], "./Origen/backup_archivo.txt")


'''for archivo in os.listdir("./Origen"):
    if not archivo.endswith(".txt") and "backup" not in archivo:
        os.unlink("./Origen/" + archivo)'''


#shutil.copytree("./Respaldo", "./RespaldoTotal/Respaldo")
