# my project 
# class and object function

class Car:
    def __init__(self, year, model, fuel_capacity, horsepower):
        self.year = year
        self.model = model
        self.fuel_capacity = fuel_capacity
        self.horsepower = horsepower

    def info(self):
        print("Car information (Model, year, etc) :-")
        print(f"Year: {self.year}")
        print(f"Model: {self.model}")
        print(f"Fuel Capacity: {self.fuel_capacity}")
        print(f"Horsepower: {self.horsepower}")

c1 = Car(2022, "BMW M4 GT3", "3 liter", "543 hp")
c2 = Car(2023, "Audi R8", "4 liter", "532 hp")
c3 = Car(2024, "Ferrari 812", "6.5 liter", "789 hp")
c4 = Car(2027, "Ford Mustang", "5 liter", "480 hp")
c5 = Car(2030, "McLaren 720S", "4 liter", "710 hp")
c6 = Car(2031, "Bugatti Chiron", "8 liter", "1479 hp")

cars = [c1, c2, c3, c4, c5, c6]
print("------------------------Car info------------------------")
print("We have info of car companies which are [BMW, Audi, Ferrari, Ford, McLaren, Bugatti]")
search = input("Enter the car company info to know: ")

for car in cars:
    if search.lower() in car.model.lower():
        car.info()
        break
else:
    print("Car not found.")
    
    
# class bike
class bike:
    def __init__(self, year, model, fuel_capacity, horsepower):
        self.year = year
        self.model = model
        self.fuel_capacity = fuel_capacity
        self.horsepower = horsepower

    def info(self):
        print("bike information (Model, year, etc) :-")
        print(f"Year: {self.year}")
        print(f"Model: {self.model}")
        print(f"Fuel Capacity: {self.fuel_capacity}")
        print(f"Horsepower: {self.horsepower}")

b1 = bike(2023, "2023 Yamaha YZF-R1", "17 Liters", "200 hp")
b2 = bike(2024, "2024 Kawasaki Ninja ZX-14R", "22 Liters", "197 hp")
b3 = bike(2025, "2025 Ducati Panigale V4", "16 Liters", "214 hp")
b4 = bike(2026, "2026 Honda CBR1000RR", "16 Liters", "189 hp")
b5 = bike(2027, "2027 Suzuki Hayabusa", "20 Liters", "187 hp")
b6 = bike(2028, "2028 BMW S1000RR", "17.5 Liters", "205 hp")

bikes = [b1, b2, b3, b4, b5, b6]

print("------------------------Bike info------------------------")

print("We have info of bike companies which are [Yamaha, Kawasaki, Ducati, Honda, Suzuki, BMW]")
search = input("Enter the bike company info to know: ")

for bike in bikes:
    if search.lower() in bike.model.lower():
        bike.info()
        break
else:
    print("bike not found.")


