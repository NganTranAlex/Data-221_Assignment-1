# Controlled Multiplication Loop
threshold = 100
product = 1
current_number = 1

while product <= threshold:
    product *= current_number
    current_number += 1

print(f"The final product is: {product}")
print(f"The integer that caused the product to exceed the threshold is: {current_number - 1}")
