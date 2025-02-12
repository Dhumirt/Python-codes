# Advance Billing System

products = []
prices = []

i=1 

while True:
    product =input(f'Enter th product :- ')
    products.append(product)
    
    more_prod = input('Do you want more products[Y/N] \n').strip().lower()
    
    if more_prod != 'y':
        break

    i += 1
    
size = len(products)  
    
for i in range(size):
    i = float(input(f'Enter {products[i]} price   :- '))
    prices.append(i)
    
total = sum(prices)    
    
gst_apply = input('Do you want to add GST[Y/N] \n').strip().lower()

        
        
if gst_apply == 'y':
    gst_percentage = float(input("Enter GST % = \n"))
    gst_ammount= total * (gst_percentage/100)
    final_value= total + gst_ammount


else:
    final_value= total
    
for i in range(len(products)): 
    print(f'{i+1} {products[i]} = {prices[i]}')
        
    print('-------------------------------------------------')
    
    print('Total Price - ', total)
if gst_apply == 'y':
    print(f"GST = {gst_percentage}%")
    print('-------------------------------------------------')
    
    print("Totaly the ammount is :- ",final_value)