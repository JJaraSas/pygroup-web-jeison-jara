from datetime import datetime

# from flask import jsonify

from app.db import db, ma
from app.products.exceptions import ProductNotFoundError


class Product(db.Model):
    """
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    image = db.Column(db.String(500), default="https://bit.ly/3loPYXP")
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
        fields = ["id", "name", "price", "description", "image", "refundable"]


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

    return category


def create_new_product(name, price, weight, description, refundable,
                       category_id, image):
    product = Product(name=name, price=price, weight=weight,
                      description=description, refundable=refundable,
                      category_id=category_id, image=image)
    db.session.add(product)
    if db.session.commit():
        return product

    return product


def get_all_products():
    products_qs = Product.query.all()
    product_schema = ProductSchema()
    products_serialization = [product_schema.dump(product) for product in
                              products_qs]

    return products_serialization


def get_product_by_id(id):
    product_qs = Product.query.filter_by(id=id).first()
    if product_qs:
        product_schema = ProductSchema()
        p = product_schema.dump(product_qs)
        return p
    else:
        raise ProductNotFoundError


def add_stock(product_id, quantity):
    stock = Stock.query.filter_by(product_id=product_id).first()
    if stock is None:
        stock = Stock(product_id=product_id, quantity=quantity)
        db.session.add(stock)
        if db.session.commit():
            return stock
    else:
        stock = Stock.query.filter_by(product_id=product_id).update(
            {"quantity": Stock.quantity + quantity})
        if db.session.commit():
            return stock

    return None
