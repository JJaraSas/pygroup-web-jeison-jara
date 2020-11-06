from flask import Blueprint, Response
#from app import app

products = Blueprint('products', __name__, url_prefix='/products')

@products.route('/<string:name>')
def get_products(name):
    """ 
    Description:
    param:  name
    return: respons 200: successful
            respons 400: error
    """
    if name == 'pygroup':
        return Response("<b>ERROR! No se puede usar el nombre pygroup", status=400)
    else:
        return Response("<b>Felicitaciones! Trabajo exitoso {}" .format(name), status=200)

"""
render_template 
Es una funcion de Flask y se utiliza generalmete para generar una salida a partir de un archivo
plantilla basado en Jinja2 que se encuentra en la carpeta de templates de la aplicacion. 
flask.templating render_template
"""