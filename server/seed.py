#!/usr/bin/env python3

# GLORY BE TO GOD,
# FLASK - PIZZAS APP,
# BY ISRAEL MAFABI EMMANUEL

from app import app
from models import db, Restaurant, Pizza, RestaurantPizza

with app.app_context():

    # This will delete any existing rows
    # so you can run the seed file multiple times without having duplicate entries in your database
    print("Deleting data...")
    Pizza.query.delete()
    Restaurant.query.delete()
    RestaurantPizza.query.delete()

    print("Creating restaurants...")
    shack = Restaurant(name="Karen's Pizza Shack", address='123 Main Street, Anytown, USA')
    bistro = Restaurant(name="Sanjay's Pizza", address='45 Oak Avenue, Suburbia, USA')
    palace = Restaurant(name="Kiki's Pizza", address='78 Pine Lane, Village, USA')
    slice_shop = Restaurant(name="The Slice Shop", address='222 Elm St, Metroville, USA')
    italian_oven = Restaurant(name="Italian Oven", address='555 Cedar Rd, Countryside, USA')
    pizza_planet = Restaurant(name="Pizza Planet", address='100 Space Way, Galaxy City, USA')
    tony_pizzaria = Restaurant(name="Tony's Pizzeria", address="77 Lake Drive, Townville, USA")
    restaurants = [shack, bistro, palace, slice_shop, italian_oven, pizza_planet, tony_pizzaria]


    print("Creating pizzas...")
    cheese = Pizza(name="Classic Cheese", ingredients="Dough, San Marzano Tomato Sauce, Fresh Mozzarella, Basil")
    pepperoni = Pizza(
        name="Pepperoni Passion", ingredients="Dough, Tomato Sauce, Mozzarella, Pepperoni, Oregano")
    veggie = Pizza(
        name="Veggie Delight", ingredients="Dough, Pesto, Mozzarella, Mushrooms, Bell Peppers, Onions, Olives")
    meat_lover = Pizza(
        name="Meat Lover's Feast", ingredients="Dough, Tomato Sauce, Mozzarella, Sausage, Pepperoni, Bacon, Ham")
    hawaiian = Pizza(
        name="Hawaiian Paradise", ingredients="Dough, Tomato Sauce, Mozzarella, Ham, Pineapple")
    bbq_chicken = Pizza(name="BBQ Chicken Bliss", ingredients="Dough, BBQ Sauce, Mozzarella, Grilled Chicken, Red Onion, Cilantro")
    margherita = Pizza(name="Margherita Supreme", ingredients="Dough, San Marzano Tomato Sauce, Fresh Mozzarella, Basil, Extra Virgin Olive Oil")
    pizzas = [cheese, pepperoni, veggie, meat_lover, hawaiian, bbq_chicken, margherita]


    print("Creating RestaurantPizza...")
    pr1 = RestaurantPizza(restaurant=shack, pizza=cheese, price=12)
    pr2 = RestaurantPizza(restaurant=bistro, pizza=pepperoni, price=15)
    pr3 = RestaurantPizza(restaurant=palace, pizza=veggie, price=17)
    pr4 = RestaurantPizza(restaurant=slice_shop, pizza=meat_lover, price = 18)
    pr5 = RestaurantPizza(restaurant=italian_oven, pizza=hawaiian, price=16)
    pr6 = RestaurantPizza(restaurant=pizza_planet, pizza=bbq_chicken, price=19)
    pr7 = RestaurantPizza(restaurant=tony_pizzaria, pizza=margherita, price = 14)
    restaurantPizzas = [pr1, pr2, pr3, pr4, pr5, pr6, pr7]

    db.session.add_all(restaurants)
    db.session.add_all(pizzas)
    db.session.add_all(restaurantPizzas)
    db.session.commit()

    print("Seeding done!")