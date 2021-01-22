# Type out pet class method
from random import randrange

class Pet():
  boredom_decrement = 4 
  hunger_decrement = 6
  boredom_threshold = 5
  hunger_threshold = 10
  sounds = ['Mrrp']

  def __init__(self, name='Pet'):
    self.name = name
    self.hunger = randrange(self.hunger_threshold)
    self.boredom = randrange(self.boredom_threshold)
    self.sounds = self.sounds[:]  # copy the class attribute, so that when we make changes to it, we won't affect the other Pets in the class

  def clock_tick(self):
    self.boredom += 1
    self.hunger += 1

  def mood(self):
    if self.hunger <= hunger_threshold and self.boredom <= self.boredom_threshold:
      return 'Happy'
    elif self.hunger > self.hunger_threshold:
      return 'Hungry'
    else:
      return 'Bored'

  def __str__(self):
    state = " I'm " + self.name + "."
    state += "   I feel " + self.mood() + ". "
    return state 

  def hi(self):
    print(self.sounds[randrage  (len (self.sounds)) ])
    self.reduce_boredom()

  def teach(self, word):
    self.sounds.append(word)
    self.reduce_boredom()

  def feed(self):
    self.reduce_hunger()

  def reduce_hunger(self):
    self.hunger = max(0, self.hunger - self.hunger_decrement)

  def reduce_boredom(self):
    self.boredom = max(0, self.boredom - self.boredom_decrement)

# A new class that inherits from Pet, and overides the feed() method in Pet
class Dog(Pet):
  sounds = ['Woof', 'Ruff']

  def feed(self):
    # Pet.feed(self)
    print('Arf! Thanks')

d1 = Dog('Astro')

d1.feed()

# another way 
class Bird(Pet):
  sounds = ['Chirp']
  def __init__(self, name='Birdy', chirp_number=2):
    Pet.__init__(self, name) # call the parent class's constructor
     # basically, call the SUPER -- the parent version -- of the constructor, with all the parameters that it needs.
    self.chirp_number = chirp_number # now, also assign the new instance variable
  
  def hi(self):
    for i in range(self.chirp_number):
      print(self.sounds[randrange( len(self.sounds) )])
    self.reduce_boredom()

b1 = Bird('Tweety', 5)
b1.teach('Polly wanna cracker')
b1.hi()

# Q1
print(b1.sounds)

# Q2 
d1.feed()
