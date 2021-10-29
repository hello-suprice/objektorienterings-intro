class Car():
    brand = str()
    color = str()
    mileage = int()

    # Metoden __init__, körs alltid då ett objekt skapas

    def __init__(self, brand, color, mileage):
        # Nedanstående variabler kallas för attribut.
        # Alla objekt av klassen Car har egna värden på dessa.
        self.brand = brand
        self.color = color
        self.mileage = mileage

    def get_brand(self):
        print(f"Color: {self.color}")
        
        print(f"Brand: {self.brand}")

        print(f"Mileage: {self.mileage}")
       

    def set_brand(self, new_brand):
        '''
        Parameter: new_brand | sträng
        Uppdaterar bilmärket om det existerar. Om det inte existerar
        så tilldelas aktuellt objekt märket enligt parametern.
        '''
        self.brand = new_brand


# ----------Huvudprogram----------
# Nu när klassen finns kan vi skapa objekt (variabler) med denna typ.
# Dessa objekt har också tillgång till klassens metoder (funktioner).
a_car = Car('Volvo', 'Blå', 1587)
a_car.set_brand('Renault')
b_car  = Car('BMW', 'Svart', 2020)
c_car = Car('Mercedes', 'Vit', 2019)

my_cars = [a_car, b_car, c_car]

for cars in my_cars:
    cars.get_brand()
    print("....")
