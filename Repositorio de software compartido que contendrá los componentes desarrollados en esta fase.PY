import pickle

class EjemploObjeto:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

# Función para serializar y almacenar el objeto en un archivo
def serializar_objeto(objeto, nombre_archivo):
    with open(nombre_archivo, 'wb') as archivo:
        pickle.dump(objeto, archivo)
    print(f'Objeto serializado y almacenado en {nombre_archivo}')

# Función para deserializar y recuperar el objeto desde el archivo
def deserializar_objeto(nombre_archivo):
    with open(nombre_archivo, 'rb') as archivo:
        objeto_recuperado = pickle.load(archivo)
    return objeto_recuperado

# Crear un objeto de ejemplo
objeto_original = EjemploObjeto(nombre="Juan", edad=25)

# Serializar y almacenar el objeto en un archivo
nombre_archivo_pickle = "ejemplo.pickle"
serializar_objeto(objeto_original, nombre_archivo_pickle)

# Deserializar y recuperar el objeto desde el archivo
objeto_recuperado = deserializar_objeto(nombre_archivo_pickle)

# Mostrar el contenido del objeto recuperado
print(f'\nContenido del objeto recuperado:')
print(f'Nombre: {objeto_recuperado.nombre}')
print(f'Edad: {objeto_recuperado.edad}')
