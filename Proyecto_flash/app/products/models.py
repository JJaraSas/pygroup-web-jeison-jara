from datetime import datetime

from flask import jsonify

from app.db import db, ma


class Product(db.Model):
    """
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer, default=1)
    description = db.Column(db.String(500), nullable=True)
    refundable = db.Column(db.Boolean, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now())


class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product
        fields = ["id", "name", "price"]


class Category(db.Model):
    """
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now())


class CategorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Category


class Stock(db.Model):
    """
    """
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    quantity = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now())


def get_all_categories():
    categories = Category.query.all()
    category_schema = CategorySchema()
    categories = [category_schema.dump(category) for category in categories]
    return categories


def create_new_category(name):
    category = Category(name=name)
    db.session.add(category)

    if db.session.commit():
        return category

    return None

def get_all_products():
    products_qs = Product.query.all()
    product_schema = ProductSchema()
    products_serialization = [product_schema.dump(product) for product in
                              products_qs]

    return products_serialization


def get_product_by_id(id):
    product_qs = Product.query.filter_by(id=id).first()
    product_schema = ProductSchema()
    p = product_schema.dump(product_qs)
    return p

'''----modelos agregados----'''

def create_new_product(name, price, weight, description, refundable, category_id):
    
    product = Product(name=name, price=price, weight=weight, description=description, refundable=refundable, category_id=category_id)
    db.session.add(product)
    if db.session.commit():
        return product

    return None
    """category = db.session.query.filter(id == category_id)
    if category != []:
        return {"info" :ok} 
    return {"No hay info"}
    --------//--------
    category = Product.query.filter(id == category_id)
    if category == []:
        print ("No hay categoria")
    else:
        print (category)
    """

def create_new_stock(product_id, quantity):
    
    stock = Stock(product_id=product_id, quantity=quantity)
    db.session.add(stock)
    if db.session.commit():
        return stock

    return None