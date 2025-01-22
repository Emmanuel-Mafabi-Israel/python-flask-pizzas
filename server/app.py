# GLORY BE TO GOD,
# FLASK - PIZZAS APP,
# BY ISRAEL MAFABI EMMANUEL

from models import db, Restaurant, RestaurantPizza, Pizza
from flask_migrate import Migrate
from flask import Flask, request, make_response, jsonify
from flask_restful import Api, Resource
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
api = Api(app) # initializing Flask-RESTful api

# -------- resources --------
class Home(Resource):
    def get(self):
        # back-end main page...
        return make_response('<kbd>mafabi: site by Emmanuel Mafabi Israel.</kbd> <br> <kbd>site&nbsp;&nbsp;: the pizza society - backend.</kbd>', 200)

class Restaurants(Resource):
    def get(self):
        restaurants = Restaurant.query.all()
        restaurant_list = [restaurant.to_dict(only=('id', 'name', 'address')) for restaurant in restaurants]
        return make_response(jsonify(restaurant_list), 200)
    
class RestaurantByID(Resource):
    def get(self, id:int):
        restaurant = Restaurant.query.filter_by(id=id).first()
        if not restaurant:
            return make_response(jsonify({"error": "Restaurant not found."}), 404)
        
        return make_response(jsonify(restaurant.to_dict(only=('id', 'name', 'address', 'restaurant_pizzas'))), 200)
    
    def delete(self, id:int):
        restaurant = Restaurant.query.filter_by(id=id).first()
        if not restaurant:
            return make_response(jsonify({"error": "Restaurant not found."}), 404)
        
        db.session.delete(restaurant)
        db.session.commit()
        return make_response('', 204)
    
class Pizzas(Resource):
    def get(self):
        pizzas = Pizza.query.all()
        pizza_list = [pizza.to_dict(only=('id', 'name', 'ingredients')) for pizza in pizzas]
        return make_response(jsonify(pizza_list), 200)
    
class RestaurantPizzas(Resource):
    def post(self):
        data = request.get_json()
        if not data:
            return make_response(jsonify({"errors": ["Request body must be JSON data."]}), 400)
        
        try:
            price = data['price']
            pizza_id = data['pizza_id']
            restaurant_id = data['restaurant_id']
            
            if not isinstance(price, (int, float)):
                return make_response(jsonify({"errors": ["Price must be a number."]}), 400)
            if not isinstance(pizza_id, int):
                return make_response(jsonify({"errors": ["Pizza id must be an integer."]}), 400)
            if not isinstance(restaurant_id, int):
               return make_response(jsonify({"errors": ["Restaurant id must be an integer."]}), 400)
           
            new_restaurant_pizza = RestaurantPizza(
                price=price,
                pizza_id=pizza_id,
                restaurant_id=restaurant_id
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
        except KeyError:
            return make_response(jsonify({"errors": ["Invalid data values."]}), 400)
        except ValueError as e:
           return make_response(jsonify({"errors": [str(e)]}), 400)
        
# -------- resource mappings --------
api.add_resource(Home, '/')
api.add_resource(Restaurants, '/restaurants')
api.add_resource(RestaurantByID, '/restaurants/<int:id>')
api.add_resource(Pizzas, '/pizzas')
api.add_resource(RestaurantPizzas, '/restaurant_pizzas')

if __name__ == '__main__':
    app.run(port=5555, debug=True)