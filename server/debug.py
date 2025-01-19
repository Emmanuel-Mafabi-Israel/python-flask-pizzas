#!/usr/bin/env python3

# GLORY BE TO GOD,
# FLASK - PIZZAS APP,
# BY ISRAEL MAFABI EMMANUEL

from app import app
from models import db, Restaurant, Pizza, RestaurantPizza

if __name__ == '__main__':
    with app.app_context():
        import ipdb
        ipdb.set_trace()