# type out again 
from random import randrange

# Here's the original Pet class
class Pet():
    boredom_decrement = 4
    hunger_decrement = 6
    boredom_threshold = 5
    hunger_threshold = 10
    sounds = ['Mrrp']
    def __init__(self, name = "Kitty"):
        self.name = name
        self.hunger = randrange(self.hunger_threshold)
        self.boredom = randrange(self.boredom_threshold)
        self.sounds = self.sounds[:]  # copy the class attribute, so that when we make changes to it, we won't affect the other Pets in the class

    def clock_tick(self):
        self.boredom += 1
        self.hunger += 1

    def mood(self):
        if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
            return "happy"
        elif self.hunger > self.hunger_threshold:
            return "hungry"
        else:
            return "bored"

    def __str__(self):
        state = "     I'm " + self.name + ". "
        state += " I feel " + self.mood() + ". "
        # state += "Hunger %d Boredom %d Words %s" % (self.hunger, self.boredom, self.sounds)
        return state

    def hi(self):
        print(self.sounds[randrange(len(self.sounds))])
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



# ***********
# Now let’s make two subclasses, Dog and Cat. Dogs are always happy unless they are bored and hungry. Cats, on the other hand, are happy only if they are fed and if their boredom level is in a narrow range and, even then, only with probability 1/2.

class Cat(Pet):
  sounds = ['Meow']

  def mood(self):
    if self.hunger > self.hunger_threshold:
      return 'Hungry'
    if self.boredom < 2:
      return 'Grumpy, leave me alone'
    elif self.boredom > self.boredom_threshold:
      return 'Bored'
    elif randrange(2) == 0:
      return 'Randomly annoyed'
    else: 
      return 'happy'

class Dog(Pet):
  sounds = ['Woof', 'Ruff']

  def mood(self):
    if (self.hunger > self.hunger_threshold) and (self.boredom > self.boredom_threshold):
      return 'Bored and hungry'
    else:
      return 'Happy'
    

c1 = Cat('Fluffy')
d1 = Dog('Astro')

c1.boredom = 1
print(c1.mood())
c1.boredom = 3

for i in range(10):
  print(c1.mood() )

print(d1.mood() )
