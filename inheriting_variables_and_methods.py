from random import randrange 

# Superclass
class Pet():
  boredom_decrement = 4
  hunger_decrement = 6
  boredom_threshold = 5
  hunger_threshold = 10
  sounds = ['Mrrp']
  def __init__(self, name='Kitty'):
    self.name = name
    self.hunger = randrange(self.hunger_threshold)
    self.boredom = randrange(self.boredom_threshold)
    self.sounds = self.sounds[:] # copy the class attribute, so that so that when we make changes to it, we won't affect the other Pets in the class

  def clock_tick(self):
    self.boredom += 1
    self.boredom += 1

  def mood(self):
    if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
      return 'Happy'
    elif self.hunger > self.hunger_threshold:
      return 'Hungry'
    else:
      return 'Bored'

  def __str__(self):
    state = "     I'm " + self.name + "."
    state += " I feel " + self.mood() + "."
    # state += "Hunger %d Boredom %d Words %s" % (self.hunger, self.boredom, self.sounds)
    return state

  def hi(self):
    print(self.sounds[randrange(len(self.sounds))])
    self.reduce_boredom()

  def teach(self, word):
    self.sounds_append(word)
    self.reduce_boredom()

  def feed(self):
    self.reduce_hunger()

  def reduce_hunger(self):
    self.hunger = max(0, self.hunger - self.hunger_decrement)

  def reduce_boredom(self):
    self.boredom = max(0, self.boredom - self.boredom_decrement)


# Create a Cat class, which will be a class of the Pet Superclass
class Cat(Pet):  #the class name that the new class inherits from goes in ()
  sounds = ['Meow']

  # Cat has 2 in 3 chance of cathcing rat - i.e. between 1 and 3
  def chasing_rats(self):
    i = randrange(1, 4)
    if i % 2 == 0:
      return 'Lost rat'
    else:
      return 'Caght rat'

# Create instances of the Pet class and Cat class
# left off
p1 = Pet()
p1.hi()    

cat1 = Cat('Fluffy')
print(cat1) # uses same __str__ method as Pets does

cat1.feed() # Totally fine, because the cat class inherits from the Pet class!
cat1.hi() 
print(cat1)

print(cat1.chasing_rats())

# Note
#print(p1.chasing_rats()) # This line will give us an error. The Pet class doesn't have this method!

# And you can continue the inheritance tree. We inherited Cat from Pet. Now say we want a subclass of Cat called Cheshire. A Cheshire cat should inherit everything from Cat, which means it inherits everything that Cat inherits from Pet, too. But the Cheshire class has its own special method, smile.

class Cheshire(Cat): # this inherits from Cat, which inherits from Pet
  
  def smile(self):  # this method is specific to instances of Cheshire
    print(" :D :D :D ")

# Instances 
cat1 = Cat('Fluffy')
cat1.feed() # Totally fine, because the cat class inherits from the Pet class!
cat1.hi() # Uses the special Cat hello
print(cat1)

new_cat = Cheshire('Pumpkin')  # create a Cheshire cat instance with name "Pumpkin"
new_cat.hi() # same as Cat
new_cat.chasing_rats() # Inherits from Cat
new_cat.smile() # Only for Cheshire instances (and any classes that you make inherit from Cheshire)

# cat1.smile() # This line would give you an error, because the Cat class does not have this method!

# None of the subclass methods can be used on the parent class, though.
p1 = Pet("Teddy")
p1.hi() # just the regular Pet hello
#p1.chasing_rats() # This will give you an error -- this method doesn't exist on instances of the Pet class.
#p1.smile() # This will give you an error, too. This method does not exist on instances of the Pet class.

#Q  What would print after running the following code:
new_cat = Cheshire("Pumpkin”)
class Siamese(Cat):
  def song(self):
    print("We are Siamese")
another_cat = Siamese("Lady")
new_cat.song()

