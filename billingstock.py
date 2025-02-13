


products = []

while True:
    sku = input("Enter SKU ( Unique Number ) : ")
    product_name = input("Enter Product Name : ")
    product_qt = int(input("Enter Product QT : "))
    single_price = float(input("Enter Single Book Price : ").replace('/-', ''))

    product = {
        "SKU": sku,
        "Product Name": product_name,
        "Product QT": product_qt,
        "Single Book Price": single_price
    }
    products.append(product)

    more = input("Do you Want Add more [Y/N] ").strip().upper()
    if more == 'N':
        break

print(products)

print("SKU\tProduct Name\tProduct QT\tSingle Book Price")
for product in products:
    print(f"{product['SKU']}\t{product['Product Name']}\t{product['Product QT']}\t{product['Single Book Price']}")
    print(f"Total Price : {product['Product QT'] * product['Single Book Price']}")
    print("------------------------------------------------------")
    
print("-----------------searching for a product-----------------")
search = input("Enter the product item from SKU: ")
for product in products:
    if product['SKU'] == search:
        print(f"SKU : {product['SKU']}")
        print(f"Product Name : {product['Product Name']}")
        print(f"Product QT : {product['Product QT']}")
        print(f"Single Book Price : {product['Single Book Price']}")
        print(f"Total Price : {product['Product QT'] * product['Single Book Price']}")
        break


for product in products:
    print(f"{product['SKU']}\t{product['Product Name']}\t{product['Product QT']}\t{product['Single Book Price']}")
    print(f"Total Price : {product['Product QT'] * product['Single Book Price']}")
    print("------------------------------------------------------")

