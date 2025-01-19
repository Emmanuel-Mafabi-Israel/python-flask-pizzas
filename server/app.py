#!/usr/bin/env python3

# GLORY BE TO GOD,
# FLASK - PIZZAS APP,
# BY ISRAEL MAFABI EMMANUEL

from models import db, Restaurant, RestaurantPizza, Pizza
from flask_migrate import Migrate
from flask import Flask, request, make_response, jsonify
# from flask_restful import Api, Resource
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get(
    "DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)
 
@app.route('/')
def index():
    # back-end main page...
    return '<kbd>mafabi: site by Emmanuel Mafabi Israel.</kbd> <br> <kbd>site&nbsp;&nbsp;: the pizza society - backend.</kbd>'

@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    restaurant_list = [restaurant.to_dict(only=('id', 'name', 'address')) for restaurant in restaurants]
    return make_response(jsonify(restaurant_list), 200)

@app.route('/restaurants/<int:id>', methods=['GET', 'DELETE'])
def handle_restaurant(id):
    # retrive restaurants...
    restaurant = Restaurant.query.filter_by(id=id).first()
    if not restaurant:
       return make_response(jsonify({"error": "Restaurant not found."}), 404)

    if request.method == 'GET':
        return make_response(jsonify(restaurant.to_dict(only=('id', 'name', 'address', 'restaurant_pizzas'))), 200)

    if request.method == 'DELETE':
        db.session.delete(restaurant)
        db.session.commit()
        return make_response('', 204)
    
@app.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    pizza_list = [pizza.to_dict(only=('id', 'name', 'ingredients')) for pizza in pizzas]
    return make_response(jsonify(pizza_list), 200)

@app.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
    try:
        new_restaurant_pizza = RestaurantPizza(
            price=data['price'],
            pizza_id=data['pizza_id'],
            restaurant_id=data['restaurant_id']
        )
        db.session.add(new_restaurant_pizza)
        db.session.commit()
        return make_response(jsonify(new_restaurant_pizza.to_dict(
            only=(
                'id',
                'price',
                'pizza_id',
                'restaurant_id',
                'pizza',
                'restaurant'
                )
            )), 201)
    except ValueError as e:
        # wrong inputs...
        return make_response(jsonify({"errors": [str(e)]}), 400)
    except KeyError:
        return make_response(jsonify({"errors": ["Invalid data values."]}), 400)

if __name__ == '__main__':
    app.run(port=5555, debug=True)