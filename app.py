from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Apna Bazaar | Home Delivery</title>
<style>
* { box-sizing: border-box; }
body {
    margin: 0;
    font-family: Arial, sans-serif;
    background: #f5f7fa;
    color: #202938;
}
header {
    background: #116b50;
    color: white;
    padding: 20px 16px;
}
header h1 { margin: 0 0 6px; font-size: 26px; }
header p { margin: 0; font-size: 14px; }
.search {
    width: 100%;
    padding: 12px;
    border: 1px solid #ddd;
    border-radius: 8px;
    margin-top: 15px;
    font-size: 15px;
}
main { padding: 18px 14px; max-width: 1000px; margin: auto; }
h2 { font-size: 20px; }
.categories {
    display: flex;
    gap: 10px;
    overflow-x: auto;
}
.category {
    background: white;
    border-radius: 10px;
    padding: 14px;
    min-width: 115px;
    text-align: center;
    border: 1px solid #e5e7eb;
}
.products {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 12px;
}
.product {
    background: white;
    border-radius: 12px;
    padding: 14px;
    border: 1px solid #e5e7eb;
}
.product .emoji { font-size: 38px; }
.product h3 { font-size: 16px; margin: 10px 0 6px; }
.price { color: #116b50; font-weight: bold; }
button {
    background: #116b50;
    color: white;
    border: 0;
    padding: 11px;
    border-radius: 7px;
    width: 100%;
    cursor: pointer;
    font-size: 14px;
}
.cart {
    background: white;
    padding: 16px;
    margin-top: 22px;
    border-radius: 12px;
}
footer {
    text-align: center;
    padding: 25px 12px;
    color: #667085;
    font-size: 13px;
}
@media (min-width: 650px) {
    .products { grid-template-columns: repeat(4, 1fr); }
}
</style>
</head>
<body>
<header>
    <h1>Apna Bazaar</h1>
    <p>Aapke ghar tak, aapke apne bazaar se!</p>
    <input class="search" id="search" placeholder="Search products..."
           oninput="filterProducts()">
</header>
<main>
    <h2>Shop by Category</h2>
    <div class="categories">
        <div class="category">🧹<br>Home Care</div>
        <div class="category">📚<br>Stationery</div>
        <div class="category">📱<br>Accessories</div>
        <div class="category">🎋<br>Local Products</div>
    </div>

    <h2>Popular Products</h2>
    <div class="products" id="products">
        <div class="product" data-name="cleaning cloth">
            <div class="emoji">🧽</div>
            <h3>Cleaning Cloth</h3>
            <p class="price">₹49</p>
            <button onclick="addToCart('Cleaning Cloth',49)">
                Add to Cart
            </button>
        </div>
        <div class="product" data-name="notebook">
            <div class="emoji">📒</div>
            <h3>Notebook</h3>
            <p class="price">₹40</p>
            <button onclick="addToCart('Notebook',40)">
                Add to Cart
            </button>
        </div>
        <div class="product" data-name="phone stand">
            <div class="emoji">📱</div>
            <h3>Phone Stand</h3>
            <p class="price">₹99</p>
            <button onclick="addToCart('Phone Stand',99)">
                Add to Cart
            </button>
        </div>
        <div class="product" data-name="shopping bag">
            <div class="emoji">🛍️</div>
            <h3>Shopping Bag</h3>
            <p class="price">₹30</p>
            <button onclick="addToCart('Shopping Bag',30)">
                Add to Cart
            </button>
        </div>
    </div>

    <div class="cart">
        <h2>🛒 Your Cart (<span id="count">0</span>)</h2>
        <div id="cartItems">Your cart is empty.</div>
        <h3>Total: ₹<span id="total">0</span></h3>
        <p>Delivery charges will be confirmed before ordering.</p>
        <button onclick="checkout()">Continue to Order</button>
        <p id="message"></p>
    </div>
</main>
<footer>
    Apna Bazaar · Local shopping, delivered to your home
</footer>

<script>
let cart = [];

function addToCart(name, price) {
    cart.push({name, price});
    renderCart();
}

function renderCart() {
    document.getElementById('count').textContent = cart.length;
    document.getElementById('total').textContent =
        cart.reduce((sum, item) => sum + item.price, 0);

    const area = document.getElementById('cartItems');
    if (cart.length === 0) {
        area.textContent = 'Your cart is empty.';
        return;
    }

    area.innerHTML = '';
    cart.forEach((item, index) => {
        const line = document.createElement('p');
        line.textContent = item.name + ' — ₹' + item.price + ' ';
        const remove = document.createElement('button');
        remove.textContent = 'Remove';
        remove.style.width = 'auto';
        remove.style.marginLeft = '8px';
        remove.onclick = () => {
            cart.splice(index, 1);
            renderCart();
        };
        line.appendChild(remove);
        area.appendChild(line);
    });
}

function filterProducts() {
    const query = document.getElementById('search').value.toLowerCase();
    document.querySelectorAll('.product').forEach(product => {
        product.style.display =
            product.dataset.name.includes(query) ? '' : 'none';
    });
}

function checkout() {
    if (cart.length === 0) {
        document.getElementById('message').textContent =
            'Please add a product to your cart first.';
        return;
    }
    document.getElementById('message').textContent =
        'Demo only: checkout and order placement will be added next.';
}
</script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(debug=True)
