
# Basic Billing System


product = []
price = []

size = int(input('Enter List Size '))

for i in range(size):
    i = input('Enter Product Name - ')
    product.append(i)

for i in range(size):
    i = int(input('Enter Product Price  '))
    price.append(i)

print('-------------------------------------------------')

print('Product List  - ', product)
print('Price List - ', price)

total = sum(price)
print('Total Price - ', total)

print('-------------------------------------------------')

yes = input('Do you want to add GST - ')
if yes in ['yes', 'Yes', 'YES', 'y', 'Y']:
    gst_amount = int(input('Enter GST % '))
    gst = total * gst_amount / 100
    print('Total Price with GST - ', total + gst)
else:   
    print('Total Price without GST - ', total)
    
print('-------------------------------------------------')