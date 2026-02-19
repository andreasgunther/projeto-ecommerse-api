from flask import Blueprint, request, jsonify
from flask_login import login_user, login_required, logout_user, current_user, LoginManager
from .models import db, User, Product, CartItem

bp = Blueprint('main', __name__)

@bp.route('/')
def initial():
    return 'API up - made by andreas hehehe :D'

@bp.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data.get("username")).first()

    if user and data.get("password") == user.password:
        login_user(user)
        return jsonify({"message": "Logged in successfully"})

    return jsonify({"message": "Unauthorized. Invalid credencials"}), 401

@bp.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logout successfully"})

# Definindo rota de adicionar um produto
@bp.route('/api/products/add', methods=["POST"])
@login_required
def add_product():
    data = request.json
    if 'name' in data and 'price' in data:
        product = Product(name=data["name"], price=data["price"], description=data.get("description", ""))
        db.session.add(product)
        db.session.commit()
        return jsonify({"message": "Product added successfully"})
    return jsonify({"message": "Invalid product data"}), 400

# Definindo rota de deletar um produto pelo id
@bp.route('/api/products/delete/<int:product_id>', methods=["DELETE"])
@login_required
def delete_product(product_id):
    # Recuperar o produto da base de dados
    product = Product.query.get(product_id)
    # Verificar se o produto existe
    if product:
    # Se existe, apagar o produto
        db.session.delete(product)
        db.session.commit()
        return jsonify({"message": "Product deleted successfully"})
    # Se nao existe, retorar 404 not found
    return jsonify({"message": "Product not found"}), 404

# Definindo rota de visualizar um produto pelo id
@bp.route('/api/products/<int:product_id>', methods=["GET"])
def get_product_details(product_id):
    product = Product.query.get(product_id)
    if product:
        return jsonify({
            "id": product.id,
            "nome": product.name,
            "price": product.price,
            "description": product.description
        })
    return jsonify({"message": "Product not found"}), 404

# Rota de atualizacao de produto pelo id
@bp.route('/api/products/update/<int:product_id>', methods=["PUT"])
@login_required
def update_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({"message": "Product not found"}), 404

    data = request.json
    if 'name' in data:
        product.name = data['name']

    if 'price' in data:
        product.price = data['price']

    if 'description' in data:
        product.description = data['description']

    db.session.commit()
    return jsonify({"message": "Product updated successfully"})

# Rota de exibicao dos produtos
@bp.route('/api/products', methods=["GET"])
def get_products():
    products = Product.query.all()
    product_list = []
    for product in products:
        product_data = {
            "id": product.id,
            "nome": product.name,
            "price": product.price
        }
        product_list.append(product_data)
    
    return jsonify(product_list)

# Checkout
@bp.route('/api/cart/add/<int:product_id>', methods=['POST'])
@login_required
def add_to_cart(product_id):
    # Usuario
    user = User.query.get(int(current_user.id))
    # Produto
    product = Product.query.get(int(product_id))

    if user and product:
        cart_item = CartItem(user_id=user.id, product_id=product.id)
        db.session.add(cart_item)
        db.session.commit()
        return jsonify({"message": "Item added to the cart successfully"})
    
    return jsonify({"message": "Failed to add item to the cart"}), 400

@bp.route('/api/cart/remove/<int:product_id>', methods=['DELETE'])
@login_required
def remove_from_cart(product_id):
    # Produto + Usuario = Item no carrinho
    cart_item = CartItem.query.filter_by(user_id=current_user.id, product_id=product_id).first()
    if cart_item:
        db.session.delete(cart_item)
        db.session.commit()
        return jsonify({"message": "Item removed from the cart successfully"})
    return jsonify({"message": "Failed to remove item from the cart"}), 400

@bp.route('/api/cart')
@login_required
def view_cart():
    # Usuario
    user = User.query.get(int(current_user.id))
    cart_items = user.cart
    cart_content = []
    for cart_item in cart_items:
        product = Product.query.get(cart_item.product_id)
        cart_content.append({
            "id": cart_item.id,
            "user_id": cart_item.user_id,
            "product_item": cart_item.product_id,
            "product_name": product.name,
            "product_price": product.price
        })
    return jsonify(cart_content)

@bp.route('/api/cart/checkout', methods=['POST'])
@login_required
def checkout():
    user = User.query.get(int(current_user.id))
    cart_items = user.cart
    for cart_item in cart_items:
        db.session.delete(cart_item)
        db.session.commit()
    return jsonify({"message": "Checkout successfully. Cart has been cleared."})
