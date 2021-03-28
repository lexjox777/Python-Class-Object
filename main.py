from animal import Animal

# instance object
dog = Animal(name = 'Lizzy', age = 5)
cat = Animal(name= 'Jade', age = 10)

print(dog.speak())
print(cat.speak())

print(dog.intro())
print(cat.intro())