class Bird:
    species = ""
    
    def fly(self):
        print("Flying high as a", self.species)


class FlightlessBird(Bird):
    def swim(self):
        print("Swimming gracefully as a", self.species)


class WildBird(Bird):
    def soar(self):
        print("Soaring majestically as a", self.species)


ostrich = FlightlessBird()
ostrich.species = "Ostrich"
print(ostrich.fly())
print(ostrich.swim())

penguin = FlightlessBird()
penguin.species = "Penguin"
print(penguin.fly())
print(penguin.swim())

eagle = WildBird()
eagle.species = "Eagle"
print(eagle.fly())
print(eagle.soar())

class Phone:
    brand = ""
    
    def make_call(self):
        print("Making a call from", self.brand)


class Samsung(Phone):
    def use_s_pen(self):
        print("Using the S Pen on", self.brand)


class NoteSerie(Phone):
    def take_notes(self):
        print("Taking notes on", self.brand)


samsung_s10 = Samsung()
samsung_s10.brand = "Galaxy S10"
Print(samsung_s10.make_call())
print(samsung_s10.use_s_pen())

samsung_s20 = Samsung()
samsung_s20.brand = "Galaxy S20"
print(samsung_s20.make_call())
print(samsung_s20.use_s_pen())

note20 = NoteSerie()
note20.brand = "Galaxy Note 20"
Print(note20.make_call())
print(note20.take_notes())



class Continent:
    name = ""
    
    def describe(self):
        print("This is", self.name)


class Country(Continent):
    def display_country_info(self):
        print("Displaying information about", self.name)


class Cities(Country):
    def display_city_info(self):
        print("There is no beautiful place than", self.name)


nyc = Cities()
nyc.name = "New York"
print(nyc.describe())
print(nyc.display_country_info())
print(nyc.display_city_info())

toronto = Cities()
toronto.name = "Toronto"
print(toronto.describe())
print(toronto.display_country_info())
print(toronto.display_city_info())

sydney = Cities()
sydney.name = "Sydney"
print(sydney.describe())
print(sydney.display_country_info())
print(sydney.display_city_info())
