# There are two kinds of hot dogs sold:  
# Hot Dog ($3.50), Chili Dog ($4.50).  
# Additionally a person can order cheese ($0.50), peppers ($0.75), or grilled onions ($1.00).  
# Also tax is 7%. 
# Write a program the inputs the type of hot dog wanted and optional toppings.  
# The program then displays the hot dog cost, tax and total cost.
HOT_DOG_PRICE = 3.50
CHILI_DOG_PRICE = 4.50
CHEESE_PRICE = 0.50
PEPPERS_PRICE = 0.75
ONIONS_PRICE = 1.00
TAX_RATE = 0.07

print("Welcome to the Hot Dog Shop!")
print("Hot Dog = $3.50")
print("Chili Dog = $4.50")

hot_dog_type = input("Enter type of hot dog (hot or chili): ").strip().lower()

if hot_dog_type == "hot":
    base_price = HOT_DOG_PRICE
elif hot_dog_type == "chili":
    base_price = CHILI_DOG_PRICE
else:
    print("Invalid choice. Defaulting to Hot Dog.")
    base_price = HOT_DOG_PRICE

# Ask for toppings
toppings_total = 0.0

choice = input("Add cheese for $0.50? (yes/no): ").strip().lower()
if choice == "yes":
    toppings_total += CHEESE_PRICE

choice = input("Add peppers for $0.75? (yes/no): ").strip().lower()
if choice == "yes":
    toppings_total += PEPPERS_PRICE

choice = input("Add grilled onions for $1.00? (yes/no): ").strip().lower()
if choice == "yes":
    toppings_total += ONIONS_PRICE

subtotal = base_price + toppings_total
tax = subtotal * TAX_RATE
total = subtotal + tax

print("\n----- Order Summary -----")
print("Subtotal: ${:,.2f}".format(subtotal))
print(f"Tax (7%): ${tax:.2f}")
print(f"Total cost: ${total:.2f}")