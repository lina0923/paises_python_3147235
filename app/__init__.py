##importar, utilizar
# una dependecia en python

from flask import Flask, render_template

#crear la aplicacion
#de flask

app = Flask(__name__)

#utilizar app
# para crear una ruta
@app.route ('/prueba')
def prueba ():
    #defino listo de paises
    paises =[
                {
                    'nombre': 'Argentina',
                    'capital': 'Buenos Aires',
                    'moneda': 'Peso argentino',
                    'poblacion': 45700000,
                    'superficie': 2780400,
                    'ciudades_principales': ['Córdoba', 'Rosario', 'Mendoza']
                },
                {
                    'nombre': 'Brasil',
                    'capital': 'Brasilia',
                    'moneda': 'Real brasileño',
                    'poblacion': 203000000,
                    'superficie': 8515767,
                    'ciudades_principales': ['São Paulo', 'Río de Janeiro', 'Salvador']
                },
                {
                    'nombre': 'México',
                    'capital': 'Ciudad de México',
                    'moneda': 'Peso mexicano',
                    'poblacion': 126000000,
                    'superficie': 1964375,
                    'ciudades_principales': ['Guadalajara', 'Monterrey', 'Puebla']
                },
                {
                    'nombre': 'España',
                    'capital': 'Madrid',
                    'moneda': 'Euro',
                    'poblacion': 47600000,
                    'superficie': 505990,
                    'ciudades_principales': ['Barcelona', 'Valencia', 'Sevilla']
                },
                {
                    'nombre': 'Colombia',
                    'capital': 'Bogotá',
                    'moneda': 'Peso colombiano',
                    'poblacion': 52000000,
                    'superficie': 1141748,
                    'ciudades_principales': ['Medellín', 'Cali', 'Barranquilla']
                },
                {
                    'nombre': 'Chile',
                    'capital': 'Santiago',
                    'moneda': 'Peso chileno',
                    'poblacion': 19600000,
                    'superficie': 756102,
                    'ciudades_principales': ['Valparaíso', 'Concepción', 'La Serena']
                }
            ]
    
    ##envio listas de paises
    # a la vista
    return render_template('paises.html',paises=paises,usuario="Lina")