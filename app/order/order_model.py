from flask.views import MethodView
from flask import Flask, jsonify, request, make_response, current_app as app
from app.menu.menu_model import Menu
from app.auth.auth_model import User
from app.auth.decorator import token_required
from app.order.order_helper import validate_order
from app.database.database import Database
from app.database.order_db_queries import OrderDbQueries
from app.database.menu_db_queries import MenuDbQueries


class Order:
    '''  Defines a Order class'''
    def __init__(self, orderId, item_name, quantity, username, status):
        ''' Initializes the order object'''
        self.orderId = orderId
        self.item_name = item_name
        self.quantity = quantity
        self.username = username
        self.status = status

    @classmethod
    def get_orders(cls, username):
        '''User orders'''
        order_db = OrderDbQueries()
        orders = order_db.fetch_all_orders_by_parameter('orders', 'username', username)
        for order in orders:
            if order:
                return jsonify({'orders': orders}), 200
        return jsonify({'message' : 'You have not made any orders'})
    
    @classmethod
    def get_all_orders(cls):
        order_db = OrderDbQueries()
        orders = order_db.fetch_all_orders()
        if orders == []:
            return jsonify(
                {"message": " There are no orders orders at the moment."}), 200
        return jsonify({"orders" : orders}), 200
