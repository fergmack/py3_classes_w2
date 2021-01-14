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
    self.boredom = randrang(self.boredom_threshold)
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

