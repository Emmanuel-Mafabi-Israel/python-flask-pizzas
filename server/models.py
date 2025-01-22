# GLORY BE TO GOD,
# FLASK - PIZZAS APP,
# BY ISRAEL MAFABI EMMANUEL

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Restaurant(db.Model, SerializerMixin):
    __tablename__ = 'restaurants'

    id                = db.Column(db.Integer, primary_key=True)
    name              = db.Column(db.String)
    address           = db.Column(db.String)

    # relationships
    # restaurant and restaurant pizza, 1..many
    restaurant_pizzas = db.relationship('RestaurantPizza', back_populates="restaurant", cascade="all, delete-orphan")
    # our association proxy
    pizza             = association_proxy('restaurant_pizzas', 'pizza')

    # serialization rules
    serialize_rules   = ('-restaurant_pizzas.restaurant', '-pizzas.restaurants')

    def __repr__(self):
        return f'<Restaurant {self.name}>'

class Pizza(db.Model, SerializerMixin):
    __tablename__ = 'pizzas'

    id                = db.Column(db.Integer, primary_key=True)
    name              = db.Column(db.String)
    ingredients       = db.Column(db.String)

    # relationships
    restaurant_pizzas = db.relationship('RestaurantPizza', back_populates='pizza', cascade="all, delete-orphan")
    # our association proxy
    restaurants       = association_proxy('restaurant_pizzas', 'restaurant')

    # serialization rules
    serialize_rules   = ('-restaurant_pizzas.pizza', '-restaurants.pizzas')

    def __repr__(self):
        return f'<Pizza {self.name}, {self.ingredients}>'

class RestaurantPizza(db.Model, SerializerMixin):
    __tablename__ = 'restaurant_pizzas'

    id                = db.Column(db.Integer, primary_key=True)
    price             = db.Column(db.Integer, nullable=False)
    pizza_id          = db.Column(db.Integer, db.ForeignKey('pizzas.id'), nullable=False)
    restaurant_id     = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)

    # relationships
    pizza             = db.relationship('Pizza', back_populates='restaurant_pizzas')
    restaurant        = db.relationship('Restaurant', back_populates='restaurant_pizzas')

    # serialization rules
    serialize_rules   = ('-pizza.restaurant_pizzas', '-restaurant.restaurant_pizzas')

    # validation
    @validates('price')
    def validate_price(self, key, price):
        # ensuring the price is always an integer and is within the valid range...
        if not isinstance(price, int) or price < 1 or price > 30:
            raise ValueError("validation errors")
        return price

    def __repr__(self):
        return f'<RestaurantPizza ${self.price}>'