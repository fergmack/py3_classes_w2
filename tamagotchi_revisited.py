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
      # bit weird but boredom must be between 3 and 5 to return annoyed or happy - this is how it's coded in the book
    if self.boredom < 2:
      return 'Grumpy, leave me alone.'
    elif self.boredom > self.boredom_threshold:
      return 'Bored...'
    elif randrange(2) == 0:
      return 'Randomly annoyed'
    else:
      return 'Happy!'

    
class Dog(Pet): 
  sounds = ['Woof', 'Ruff']

  def mood(self):
    if (self.hunger > self.hunger_threshold and self.bored > self.boredom_threshold):
      return 'Bored and hungry...'
    else:
      return 'Happy!'

  # override feed mathod from Pet class. It use Pet.feed but with some extra functionality 
  def feed(self): 
    Pet.feed(self)
    print('Arf! Thanks!')


class Bird(Pet):
  sounds = ['Chirp']
  def __init__(self, name='Pet', chirp_number=2):
    Pet.__init__(self, name) # call the parent class's constructor
    # basically call the super, ie the parent version, with all the parameters that it needs 
    self.chirp_number = chirp_number # assign the new instance variable

  def hi(self):
    for i in range(self.chirp_number):
      print(self.sounds[randrange(len(self.sounds)) ])
    self.update_boredom() 

  
class Lab(Dog): 
  def fetch(self): 
    return 'I found the tennis ball!'
  
  def hi(self):
    print(self.fetch() )
    print(self.sounds[randrange (len(self.sounds)) ])

class Poodle(Dog):
  def haircut(self): 
    return 'I want a proper haircut'

  def hi(self):
    print(self.haircut())
    # the below actually inherits from the Pet class - .hi() is not defined in Dog, but inherited from the Pet class
    Dog.hi(self)
    
def whichone(petlist, name):
  for pet in petlist:
    if pet.name == name: 
      return pet 
  return None # no pet matched, ie the pet is not in petlist 

# A list of pet's you can adopt, so it's 'name': Class
pet_types = {'dog': Dog, 'lab': Lab, 'poodle': Poodle, 'cat': Cat, 'bird': Bird}

# select pet - enter 'name' and Class
def whichtype(adopt_type='general pet'):
  return pet_types.get(adopt_type.lower(), Pet)

def play():
  animals = []

  option = ""
  base_prompt = """"
  Type 'Quit' to Exit.
  Type 'Adopt <petname_with_no_spaces> <dog, cat, lab, poodle, bird>' to adopt pet
  Type 'Greet <pet_name>' to say hello!
  Type 'Tech <pet_name>' to teach your pet a new word.
  Type 'Feed <pet_name>' to feed your pet.

  Choice: 
  """

  feedback = "Pet status: "
  while True:
    action = input(feedback + "\n" + base_prompt)
    feedback = ""
    words = action.split()
    if len(words) > 0:
      command = words[0]
    else:
      command = None
    if command == "Quit":
      print("Exiting...")
      return

   
    # Commands Left off fix this
    elif command == "Adopt" and len(words) > 1:
      # look into how whichone() operates here 
      # whichone() makes sure you haven't chosen the same pet again - it returns none if you haven't already got a pet with that name
      if whichone(animals, words[1]):
        feedback += "You already have a pet with that name"
      else: # figure out which class it should be
        if len(words) > 2:
          # Get class
          # note words[2] is always the petname for 'Adopt' commnd. Finds the class in pet_types - e.g. 'dog' uses Dog class 
          Cl = whichtype( words[2] )
        else:
          Cl = Pet
      # Make an instance of that class and append it to the animals list defined at the start
      # Note: words[1] is the pet name ...e.g. Adopt <petname> dog
      # ************* This will add ?????? what does Cl ([words[1]] )
      animals.append( Cl ( [words[1]] ) ) 

    elif command == "Greet" and len(words) > 1:
      # Note how it differs to how whichoneis() used above. Used to check that you don't already have the pet above, but used to get the pet name below
      # e.g. words woud be Greet, dog
      pet = whichone(animals, words[1])
      if not pet: 
        feedback += " I didn't recognise that pet name. Please try again."  
        print()
      else:
        print.hi() 

    elif command == "Teach" and len(words) > 2:
      pet = whichone(animals, words[1])
      if not pet:
        feedback += " I didn't recognise that pet name. Please try again."
      else:
        # the words the user passed when typeing 'Teach dog hello'
        pet.teach(words[2])
    
    elif command == "Feed" and len(words) > 1:
      pet = whichone(animals, words[1])
      if not pet:
        feedback += " I didn't recognise that pet name. Please try again."
      else:
        pet.feed()

    else:
      feedback += "I didn't understand that. Please try again."

    # add clock to progress boredom 
    for pet in animals:
      pet.clock_tick()
      feedback += "\n" + pet.__str__()

play()



    
