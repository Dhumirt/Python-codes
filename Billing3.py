


products = []

while True:
    name = input("Enter Product Name: ")
    price = float(input("Enter " + name + " Price: ").replace('/-', ''))
    quantity = int(input("Enter " + name + " Quantity: "))
    products.append([name, price, quantity])
    
    more = input("Do you want to add more [Y/N]: ")
    if more != 'Y':
        break

total = sum(price * quantity for _, price, quantity in products)
gst_rate = 0

gst_input = input("Do You Want to add GST [Y/N]: ")
if gst_input == 'Y':
    gst_rate = float(input("Enter GST %: "))
total_with_gst = total + (total * gst_rate / 100)

offer_choice = int(input("Select Offer (1. 2% OFF, 2. 4% OFF, 3. 8% OFF): "))
offer_rates = {1: 2, 2: 4, 3: 8}
offer_rate = offer_rates.get(offer_choice, 0)
final_total = total_with_gst - (total_with_gst * offer_rate / 100)


print("\n------- BILL -------")
for name, price, quantity in products:
    print(name, "=", price * quantity, "/-")
print("-------------------")
print("Total", "=", total, "/-")
print("GST", "=", gst_rate, "%")
print("Offer", "=", offer_rate, "%")
print("-------------------")
print("Final Total:", "=", round(final_total, 2), "/-")

