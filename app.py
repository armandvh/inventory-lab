print("=== Inventory Management System ===")
print("Enter product name:")
product_name = input()
print("Enter unit price:")
unit_price = input()
print("Enter quantity:")
quantity = input()
if((unit_price.isdigit()) == False):
    print("Price must be a valid integer.")
    exit()

if((quantity.isdigit()) == False):
    print("quantity must be a valid integer.")
    exit()
if(quantity<0):
    print("quantity is negative")
    exit()
if(0 >unit_price):
    print("unit price is negative")
    exit()
if(product_name==""):
    print("product name cant be empty")
    exit()
print("-----Result------")
print("product name:",product_name)
print("unit price:",unit_price)
print("quantity:",quantity)
print("total inventory value: ",int(unit_price)*int(quantity))