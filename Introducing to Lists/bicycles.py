# Lists
# bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# print(bicycles)



# Accessing Elements in a List
# bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# print(bicycles[0])



# bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# print(bicycles[0].title())


# bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# print(bicycles[1])
# print(bicycles[3])

# bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# print(bicycles[-1])


# bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# message = f"My first bicycle was a {bicycles[0].title()}."

# print(message)



# Exersice 2.1
# names = ['asad', 'neyaj', 'zafar', 'anand']
# print(names[0])
# print(names[1])
# print(names[2])
# print(names[3])

# Exersice 2.2
# names = ['asad', 'neyaj', 'zafar', 'anand']
# print(f"Hello {names[0]}, I hope you are fine!")

# print(f"Hello {names[1]}, I hope you are fine!")
# print(f"Hello {names[2]}, I hope you are fine!")
# print(f"Hello {names[3]}, I hope you are fine!")

# Exersice 2.3
# Cars = ['bmw', 'mercedies', 'hundai', 'ferari']
# print(f"I would like to own a {Cars[0].title()} car")
# print(f"I would like to own a {Cars[1].title()} car")
# print(f"I would like to own a {Cars[2].title()} car")
# print(f"I would like to own a {Cars[3].title()} car")



# Changing, Adding, and Removing Elements

# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)

# motorcycles[0] = 'ducati'
# print(motorcycles)


# Adding Elements to a Lise

# Appending Elements to the End of a List
# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)

# motorcycles.append('ducati')
# print(motorcycles)


# motorcycles = []
# motorcycles.append('honda')
# motorcycles.append('yamaha')
# motorcycles.append('suzuki')

# print(motorcycles)


# Inseting Elements into a List

# motorcycles = ['honda', 'yamaha', 'suzuki']
# motorcycles.insert(0, 'ducati')

# print(motorcycles)




# Removing Elements from a Lise
# Removing an item Using the del Statement

# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)

# del motorcycles[0]
# print(motorcycles)


# motorcycles = ['honda', 'yamha', 'suzuki']
# print(motorcycles)

# del motorcycles[1]
# print(motorcycles)



# Removing an item Using the pop() Method
# motorcycles = ['honda', 'yamha', 'suzuki']
# print(motorcycles)

# popped_motorcycle = motorcycles.pop()
# print(motorcycles)
# print(popped_motorcycle)


# motorcycles = ['honda', 'yamha', 'suzuki']

# last_owned = motorcycles.pop()
# print(f"The last motorcycle I owned was a {last_owned.title()}.")



# Popping Items from any Posiion in a List

# motorcycles = ['honda', 'yamha', 'suzuki']

# first_owned = motorcycles.pop(0)
# print(f"The first motorcycle I owned was a {first_owned.title()}.")


# Removing an Item by Value

# motorcycles = ['honda', 'yamha', 'suzuki', 'ducati']
# print(motorcycles)

# motorcycles.remove('ducati')
# print(motorcycles)


# motorcycles = ['honda', 'yamha', 'suzuki', 'ducati']
# print(motorcycles)

# too_expensive = 'ducati'
# motorcycles.remove(too_expensive)
# print(motorcycles)
# print(f"\nA {too_expensive.title()} is too expensive for me.")



# Exersice 2.4
# guests = ['albert einstein', 'marie curie', 'tesla']

# print(f"Hello {guests[0].title()} I will invite you to today's dinner party")
# print(f"Hello {guests[1].title()} I will invite you to today's dinner party")
# print(f"Hello {guests[2].title()} I will invite you to today's dinner party")


# Exersice 2.5
guests = ['albert einstein', 'marie curie', 'tesla']
print(f"Hello {guests[0].title()} I will invite you to today's dinner party")
print(f"Hello {guests[1].title()} I will invite you to today's dinner party")
print(f"Hello {guests[2].title()} I will invite you to today's dinner party")

print(f"You know {guests[2].title()} cannot come to this party")
print("\n")
guests[2] = 'musk'
print(f"Hello {guests[0].title()} I will invite you to today's dinner party")
print(f"Hello {guests[1].title()} I will invite you to today's dinner party")
print(f"Hello {guests[2].title()} I will invite you to today's dinner party")

print("\n")
print("I have a good news you know i found a bid table in today's dinner party so \n I invite three more perons for today's dinner party")
print('\n')

# Exersice 2.6
guests.insert(0, 'asad')
guests.insert(3, 'donald')
guests.append('anand')

print(guests)
print(f"Hello {guests[0].title()} I will invite you to today's dinner party")
print(f"Hello {guests[1].title()} I will invite you to today's dinner party")
print(f"Hello {guests[2].title()} I will invite you to today's dinner party")
print(f"Hello {guests[3].title()} I will invite you to today's dinner party")
print(f"Hello {guests[4].title()} I will invite you to today's dinner party")
print(f"Hello {guests[5].title()} I will invite you to today's dinner party")

# Exersice 2.7
print("\n")
print("Sorry you know i figure out that our dinner table cannot come at time so i have only places for two guests")

print(f"{guests.pop().title()} sorry i feel bad for you to not invite in today's dinner")
print(f"{guests.pop().title()} sorry i feel bad for you to not invite in today's dinner")
print(f"{guests.pop().title()} sorry i feel bad for you to not invite in today's dinner")
print(f"{guests.pop().title()} sorry i feel bad for you to not invite in today's dinner")


del guests[0]
del guests[0]
print(guests)

