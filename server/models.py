from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

import time

db = SQLAlchemy()

# Product model
class Product(db.Model,SerializerMixin):
    __tablename__ = 'products' 

    id = db.Column(db.Integer,primary_key=True)  
    name = db.Column(db.String)
    image = db.Column(db.String) 
    price = db.Column(db.Float)
    product_description = db.Column(db.String)

    # Relationships
    order_items = db.relationship('OrderItem', backref = 'product')

    # Serialization rules
    serialize_rules = ('-order_items.product', )

# User model
class User(db.Model,SerializerMixin):
    __tablename__ = 'users' 

    id = db.Column(db.Integer,primary_key=True)  
    name = db.Column(db.String)
    mail_address= db.Column(db.String)
    email_address = db.Column(db.String) 

    

    # Relationships
    orders = db.relationship('Order', backref = 'user')

    # Serialization rules
    serialize_rules = ('-orders.user', )

# Order model
class Order(db.Model,SerializerMixin):
    __tablename__ = 'orders' 

    id = db.Column(db.Integer,primary_key=True)  
    created_at = db.Column(db.DateTime,server_default =db.func.now())
    updated_at =db.Column(db.DateTime, onupdate = db.func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    # Relationships
    order_items = db.relationship('OrderItem', cascade = "all, delete", backref = 'order')

    # Serialization rules
    serialize_rules = ('-order_items.order', )

# OrderItem model
class OrderItem(db.Model,SerializerMixin):
    __tablename__ = 'order_items' 

    id = db.Column(db.Integer,primary_key=True)  
    quantity = db.Column(db.Integer)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))

    @validates('quantity')
    def validates_quantity(self,key,quantity):
        if not isinstance(quantity,int) and quantity < 0:
            raise ValueError('quantity must be a number')
        return quantity
      

    # Serialization rules
    serialize_rules = ('-product.order_items', '-order.order_items')
