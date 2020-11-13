from http import HTTPStatus
from flask import Blueprint, Response, request

from app.products.models import get_all_categories, create_new_category, \
    get_all_products, get_product_by_id, create_new_product, create_new_stock

products = Blueprint("products", __name__, url_prefix='/products')

EMPTY_SHELVE_TEXT = "Empty shelve!"
PRODUCTS_TITLE = "<h1> Products </h1>"
DUMMY_TEXT = "Dummy method to show how Response works"
RESPONSE_BODY = {
    "message": "",
    "data": [],
    "errors": [],
    "metadata": []
}


@products.route('/dummy-product', methods=['GET', 'POST'])
def dummy_product():
    """ This method test the request types. If is GET Type it will
    render the text Products in h1 label with code 500.
    If is POST Type it will return Empty shelve! with status code 403
    """
    if request.method == 'POST':
        return EMPTY_SHELVE_TEXT, HTTPStatus.FORBIDDEN

    return PRODUCTS_TITLE, HTTPStatus.INTERNAL_SERVER_ERROR


@products.route('/dummy-product-2')
def dummy_product_two():
    """ This method shows how Response object could be used to make API
    methods.
    """
    return Response(DUMMY_TEXT, status=HTTPStatus.OK)


@products.route('/categories')
def get_categories():
    """
        Verificar que si get_all_categories es [] 400, message = "No hay nada"
    :return:
    """
    categories = get_all_categories()
    status_code = HTTPStatus.OK

    if categories:
        RESPONSE_BODY["message"] = "OK. Categories List"
        RESPONSE_BODY["data"] = categories
    else:
        RESPONSE_BODY["message"] = "OK. No categories found"
        RESPONSE_BODY["data"] = categories
        status_code = HTTPStatus.NOT_FOUND

    return RESPONSE_BODY, status_code


@products.route('/add-category', methods=['POST'])
def create_category():
    """
    Agrega categoria a la base de datos
    :return:
    """
    RESPONSE_BODY["message"] = "Method not allowed"
    status_code = HTTPStatus.METHOD_NOT_ALLOWED
    if request.method == "POST":
        data = request.json
        category = create_new_category(data["name"])
        RESPONSE_BODY["message"] = "OK. Category created!"
        RESPONSE_BODY["data"] = category
        status_code = HTTPStatus.CREATED

    return RESPONSE_BODY, status_code


@products.route('/')
def get_products():
    products_obj = get_all_products()

    RESPONSE_BODY["data"] = products_obj
    RESPONSE_BODY["message"] = "Products list"

    return RESPONSE_BODY, 200


@products.route('/product/<int:id>')
def get_product(id):
    product = get_product_by_id(id)

    RESPONSE_BODY["data"] = product
    return RESPONSE_BODY, 200


@products.route('/product-stock/<int:id>')
def get_product_stock(product_id):
    pass


@products.route('/need-restock')
def get_products_that_need_restock():
    pass


@products.route('/register-product-stock/<int:id>', methods=['PUT', 'POST'])
def register_product_refund_in_stock():
    pass

'''------Vistas agregadas------'''

@products.route('/add-product', methods=['POST'])
def create_product():
    """
    Agregar producto a la base de datos
    :return:
    """
    RESPONSE_BODY["message"] = "Method not allowed"
    status_code = HTTPStatus.METHOD_NOT_ALLOWED
    if request.method == "POST":
        data = request.json
        product = create_new_product(data["name"], data["price"], data["weight"], data["description"], data["refundable"], data["category_id"])
        RESPONSE_BODY["message"] = "OK. Product created!"
        RESPONSE_BODY["data"] = product
        status_code = HTTPStatus.CREATED

    return RESPONSE_BODY, status_code


@products.route('/add-stock', methods=['POST'])
def create_stock():
    """
    Agregar stock a la base de datos
    """
    RESPONSE_BODY["message"] = "Method not allowed"
    status_code = HTTPStatus.METHOD_NOT_ALLOWED
    if request.method == "POST":
        data = request.json
        stock = create_new_stock(data["product_id"], data["quantity"])
        RESPONSE_BODY["message"] = "OK. Stock created!"
        RESPONSE_BODY["data"] = stock
        status_code = HTTPStatus.CREATED

    return RESPONSE_BODY, status_code