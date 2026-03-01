products = {
    "rice": 60,
    "sugar": 50,
    "milk": 30,
    "oil": 120,
    "bread": 40,
    "egg": 7,
    "apple": 120,
    "banana": 50,
    "potato": 25,
    "onion": 30
}

cart = {}

def add_item(item, qty):
    item = item.lower().rstrip('s')
    if item in cart:
        cart[item] += qty
    else:
        cart[item] = qty

def generate_bill():
    total = 0
    print("\n---- BILL ----")
    for item, qty in cart.items():
        price = products.get(item, 0)
        subtotal = price * qty
        print(item, qty, subtotal)
        total += subtotal
    print("Total:", total)
    return total
