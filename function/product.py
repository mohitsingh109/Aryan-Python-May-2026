# User input product id
# User input product name
# User input product price
# User input product quantity

# product_input() -> multiple value return
# display_product_info(id,product_name,price,quantity) print (we only want to print the info if validation pass)
# validate_product_info(id,product_name,price,quantity) True, "Success"
# False, "Error message"
# "Error message" --> product name less than 3 char
# "Error message" --> quantity is 0 or negative
# "Error message" --> price can't be 0 or less
# "Error message" -> id should not be empty
# keep asking user until you make it pass all the cases
# product description , add validation where product description should not be less than 5 characters , if validation pass and display

def product_input():
    product_id = input("Enter product id:")
    product_name = input("Enter product name:")
    product_price = float(input("Enter product price:"))
    product_quantity = int(input("Enter product quantity:"))
    product_description=input("Enter product description:")
    return product_id, product_name , product_price , product_quantity, product_description

def display_product_info(product_id,product_name,product_price,product_quantity,product_description_1):
    print(f" product id : {product_id} , product name : {product_name} , product price : {product_price} , product quantity:{product_quantity} ,product description: {product_description_1} ")

def validate_product_input(product_id, product_name,product_price,product_quantity,product_description):
    if len(product_name) <= 3:
        return False , "product name is too short"
    if product_quantity <= 0:
        return False, " product quantity should be greater than 0"
    if product_price <= 0:
        return False, "product price should be greate than 0"
    if product_id == "":
        return False , "product id is empty"
    if len(product_description) <= 5:
        return False, "product description is too short"
    return True , "product is valid"

while True:
    product_id, product_name, product_price, product_quantity, product_description = product_input()
    state, message = validate_product_input(product_id, product_name, product_price, product_quantity, product_description)
    if state == True:
        display_product_info(product_id, product_name, product_price, product_quantity, product_description)
        break
    else:
        print(f" validation failed due to: {message}")

