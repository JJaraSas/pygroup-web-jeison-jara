from flask import Flask
from app.products.views import products

app = Flask(__name__)

@app.route('/')
def index():
    return "Hola esta es la pagina principal"

#from app.products import views
#from app.products.views import products
app.register_blueprint(products)

if __name__ == "__main":
    app.run(debug=True)