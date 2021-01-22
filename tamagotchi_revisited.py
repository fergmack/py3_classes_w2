from random import randrange

# Q - what does object mean below?
class Pet(object):
  boredom_decrement = 4
  hunger_decrement = 6
  boredom_threshold = 5
  hunger_threshold = 10
  sounds = ['Mmrp']

  def __init__(self, name = 'Pet'):
    self.name = name
    self.hunger = randrange(self.hunger_threshold)
    self.boredom = randrange(self.boredom_threshold)
    self.sounds = self.sounds[:] # # copy the class attribute, so that when we make changes to it, we won't affect the other Pets in the class

  # the operational gamplay methods 
  def clock_tick(self):
    self.boredom += 1
    self.hunger += 1
  
  def mood(self):
    if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
      return 'Happy!'
    elif self.hunger > self.hunger_threshold:
      return 'Hungry!'
    else: 
      return 'Bored!'

  #  print out mood
  def __str__(self):
    state = " I'm " + self.name + ". "
    state += " I feel " + self.mood() + ". "
    return state

  # methods to interact with the pet
  def hi(self):
    print(self.sounds[ randrange(len(self.sounds)) ] ) 
    # reduce boredom
    self.update_boredom()

  def teach(self, word): 
    self.sounds.append(word)
    # reduce boredom
    self.update_boredom()

  def feed(self):
    self.update_hunger()
  
  # methods to update hunger and boredom (i.e. reduce them)
  # note: hunger is set in the __init__ method above using randrange
  def update_hunger(self):
    self.hunger = max(0,  self.hunger - self.hunger_decrement ) 

  # note: boredom is also set in the __init__ method above using randrange
  def update_boredom(self):
    self.boredom = max(0, self.boredom - self.boredom_decrement)

# Subclasses that inherit from the Superclass above
class Cat(Pet):
  sounds = ['Meow']

  def mood(self):
    if self.hunger > self.hunger_threshold:
      return 'Hungry...'
