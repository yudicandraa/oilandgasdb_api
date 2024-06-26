# app/main.py

from flask import Blueprint, jsonify
import sqlite3

app = Blueprint('main', __name__)

# Function to execute a query and fetch all results
def execute_query(query):
    conn = sqlite3.connect('oilandgas_company.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

# Function to get all products from the database
def get_all_products():
    query = 'SELECT * FROM Products'
    return execute_query(query)

# Function to get all users from the database
def get_all_users():
    query = 'SELECT * FROM Users'
    return execute_query(query)

# Function to get all clients from the database
def get_all_clients():
    query = 'SELECT * FROM Clients'
    return execute_query(query)

# Define routes to get all products, users, and clients
@app.route('/products', methods=['GET'])
def list_products():
    products = get_all_products()
    products_list = [
        {"product_id": row[0], "product_name": row[1], "description": row[2], "price": row[3]}
        for row in products
    ]
    return jsonify(products_list)

@app.route('/users', methods=['GET'])
def list_users():
    users = get_all_users()
    users_list = [
        {"user_id": row[0], "name": row[1], "email": row[2], "password": row[3]}
        for row in users
    ]
    return jsonify(users_list)

@app.route('/clients', methods=['GET'])
def list_clients():
    clients = get_all_clients()
    clients_list = [
        {"service_id": row[0], "user_id": row[1], "start_date": row[2], "contract_value": row[3]}
        for row in clients
    ]
    return jsonify(clients_list)

