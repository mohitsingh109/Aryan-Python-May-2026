def total_sum(product_values):
    # product_values = [3, 6, 1]
    total = 0
    for product in product_values:
        total += product

    return total

cart_product_values = [3, 6, 1]
total = total_sum(cart_product_values)
print(f"Total sum: {total}")