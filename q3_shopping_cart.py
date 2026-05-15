def add_item(item, cart=[]):
    cart.append(item)
    return cart

print(add_item("apple"))
print(add_item("banana"))
print(add_item("milk", cart=["bread"]))
print(add_item("eggs"))

# Explanation:
# The default list cart=[] is created only once.
# So the same list is reused in multiple function calls.
# That is why apple, banana, and eggs remain in the same list.

print("=" * 50)

def add_item_fixed(item, cart=None):

    if cart is None:
        cart = []

    cart.append(item)
    return cart

print(add_item_fixed("apple"))
print(add_item_fixed("banana"))
print(add_item_fixed("milk", ["bread"]))
print(add_item_fixed("eggs"))

print("=" * 50)

def create_cart(owner, discount=0):

    cart = {
        "owner": owner,
        "items": [],
        "discount": discount
    }

    return cart


def add_to_cart(cart, name, price, qty=1):

    item = {
        "name": name,
        "price": price,
        "qty": qty
    }

    cart["items"].append(item)

    print(f"{name} added to {cart['owner']}'s cart")


def update_price(price_tuple, new_price):

    # tuple values cannot be changed
    # because tuples are immutable

    price_tuple[0] = new_price


def calculate_total(cart):

    total = 0

    for item in cart["items"]:

        total += item["price"] * item["qty"]

    discount_amount = (total * cart["discount"]) / 100

    final_total = total - discount_amount

    return final_total


def main():

    cart1 = create_cart("Navya", 10)
    cart2 = create_cart("Harshi", 5)

    print("Carts created")
    print(cart1)
    print(cart2)

    print("-" * 40)

    add_to_cart(cart1, "Laptop", 50000, 1)
    add_to_cart(cart1, "Mouse", 1000, 2)

    add_to_cart(cart2, "Phone", 20000, 1)
    add_to_cart(cart2, "Charger", 1500, 1)

    print("-" * 40)

    print("Cart 1")
    print(cart1)

    print()

    print("Cart 2")
    print(cart2)

    print("-" * 40)

    print("Total for cart1:", calculate_total(cart1))
    print("Total for cart2:", calculate_total(cart2))

    print("-" * 40)

    price_data = (1000, "Keyboard")

    try:
        update_price(price_data, 2000)

    except TypeError as e:
        print("Error:", e)


main()

# -----------------------------
# Discussion Points
# -----------------------------

# 1. Why is discount=0 safe but cart=[] dangerous?
#
# discount=0 is safe because integers are immutable.
# cart=[] is dangerous because lists are mutable and shared
# between function calls.


# 2. Difference between rebinding and mutating
#
# Rebinding means Variable points to a completely new object.
# Mutating means Existing object itself gets modified.


# 3. Mutable and Immutable Types
#
# Mutable:
# list, dict, set
#
# Immutable:
# tuple, str, int


# 4. When a list is passed into a function and modified,
# do changes reflect outside?
#
# Yes.
# Because lists are mutable and Python passes a reference
# to the same object.