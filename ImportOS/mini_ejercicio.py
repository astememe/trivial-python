import os, shutil

os.chdir("/ImportOS")
if not os.path.exists("./carpetanueva"):
    os.mkdir("carpetanueva")
if not os.path.exists("carpetanueva/fichero.txt"):
    open("carpetanueva/fichero.txt", "x")

# shutil.copytree("carpetanueva", "C:\\Users\\ememe\\Desktop\\Clase\\Programación Python\\ejercicios_mario\\escritura_lectura\\copias\\carpetanueva")
#shutil.move("mini_ejercicio.py", "./carpetanueva")

#os.unlink() #Borra los ficheros
#os.rmdir() #Borra los directorios vacíos
#shutil.rmtree #Borra la carpeta recursivamente

