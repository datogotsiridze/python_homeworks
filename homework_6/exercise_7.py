def total_price(cart):
    total = 0
    for price in cart.values():
        total += price
    return total

cart_1 = {"bread": 1.5, "milk": 4, "ketchup": 3}
cart_2 = { "pizza": 15, "cola": 2, "coctail": 12 }

print(total_price(cart_1))

print(total_price(cart_2))
