# ==========================================
# Part A — Spot the Bug
# ==========================================
def add_item(item, cart=[]):
    cart.append(item)
    return cart
print("--- Part A ---")
print(add_item("apple"))            #  ['apple']
print(add_item("banana"))           #  ['apple', 'banana'] (List is getting mutated )
print(add_item("milk", cart=["bread"])) # ['bread', 'milk'] (New list passed, no mutation of default)
print(add_item("eggs"))             # ['apple', 'banana', 'eggs'] (Back to default list)
print("\n")


# ==========================================
# Part B — Fix It
# ==========================================
def add_item_fixed(item, cart=None):
    if cart is None:
        cart = [] # Create a new list every time
    cart.append(item)
    return cart

print("--- Part B ---")
print(add_item_fixed("apple"))      # ['apple']
print(add_item_fixed("banana"))     # ['banana'] (For every call you will have a Fresh list!)
print("\n")


# ==========================================
# Part C — Build the Cart
# ==========================================

def create_cart(owner, discount=0):
    # discount=0 is safe because integers are immutable.
    return {"owner": owner, "items": [], "discount": discount}

def add_to_cart(cart, name, price, qty=1):
    cart["items"].append({"name": name, "price": price, "qty": qty})

def update_price(price_tuple, new_price):
    # price_tuple = (name, price)
    try:
        # Tuples are immutable, they cannot be changed after creation.
        # This will raise a TypeError.
        price_tuple[1] = new_price
    except TypeError as e:
        print(f"Error caught: {e}")

def calculate_total(cart):
    total = 0
    for item in cart["items"]:
        total += item["price"] * item["qty"]
    
    final_total = total * (1 - (cart["discount"] / 100))
    return final_total

# Demonstrating independent carts
print("--- Part C ---")
cart1 = create_cart("Alice", discount=10)
cart2 = create_cart("Bob")

add_to_cart(cart1, "Laptop", 1000)
add_to_cart(cart2, "Mouse", 50)

print(f"{cart1['owner']}'s Cart: {cart1['items']}")
print(f"{cart2['owner']}'s Cart: {cart2['items']}")
print(f"Alice Total: {calculate_total(cart1)}")
print(f"Bob Total: {calculate_total(cart2)}")

# Tuple test
item_tuple = ("Keyboard", 100)
update_price(item_tuple, 120)

# ==========================================
# Discussion Points
# ==========================================
"""
1. Why is discount=0 safe but cart=[] dangerous?
   '0' is an integer, which is immutable. You cannot change the value 0; you can only
   assign the variable to a new number. '[]' is a list, which is mutable. The 
   default list object exists in memory, and .append() changes that specific object
   permanently.

2. What is the difference between rebinding and mutating?
   Mutating: Changing the state of an object (e.g., list.append(), dict[key] = val)
   Rebinding: Pointing a variable name to a new object (e.g., x = 5, then x = 6)

3. Which of these are mutable? — list, tuple, dict, set, str, int
   Mutable: list, dict, set
   Immutable: tuple, str, int

4. When you pass a list into a function and modify it, do changes reflect outside? Why?
   Yes. Python uses "pass-by-object-reference". When a list (mutable) is passed, 
   the function receives a reference to the same memory location as the original 
   list. Modifying it inside modifies the original.
"""