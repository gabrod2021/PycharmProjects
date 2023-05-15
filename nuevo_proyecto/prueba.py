#1-NOMBRE DE RUTA DE SCRIPT DE PYTHON
import os
from pathlib import Path,PurePath

#2-LISTAR ARCHIVOS
#print(type(os.getcwd()))
#print(os.listdir('.idea'))
#print(type(Path.cwd()))
#print(list(Path('.idea').iterdir()))

#3-CONCATENAR RUTAS
#print(os.path.join(os.getcwd(),'.idea'))
#print(PurePath.joinpath(Path.cwd(),'.idea'))

#4-Crear carpetas usando Python:
#os.mkdir('Dataset')
#Path('Dataset').mkdir(exist_ok=True)
#os.makedirs(os.path.join('Dataset','Script'))
#PurePath.joinpath(Path.cwd(),'Dataset2','Script2').mkdir(parents=True)

#5-Renombrar
#os.rename('Dataset','Data')
#path_actual = Path('Dataset2')
#path_objetivo = Path('Data2')
#Path.rename(path_actual,path_objetivo)

#for file in os.listdir():
#    if file.endswith('.csv'):
#       os.rename(file,f'2023_{file}')

#6-Comprobar si existe una carpeta
#print(os.path.exists('Data'))
#archivo=Path('Data')
#print(archivo.exists())

#7-Metadata
#print(os.path.abspath('Data'))
script=Path('prueba.py')
#print(script.resolve())
#print(script.suffix)
print(script.stat().st_size)




