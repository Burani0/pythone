class Person:
    def __init__(self, name, age,height):
        self.name = name
        self.age = age
        self.height = height

class Male(Person):
    pass

class Boy(Male):
    def __init__(self, voice, color):
        self.voice = voice
        self.color = color


x = Boy("deep","light")   

print(x.voice)


m = Male("Joan",16,171 )

print(m.name)
print(m.age)
