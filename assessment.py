# The class, Pokemon, is provided below and describes a Pokemon and its leveling and evolving characteristics. An instance of the class is one pokemon that you create.

# Grass_Pokemon is a subclass that inherits from Pokemon but changes some aspects, for instance, the boost values are different.

# For the subclass Grass_Pokemon, add another method called action that returns the string "[name of pokemon] knows a lot of different moves!". Create an instance of this class with the name as "Belle". Assign this instance to the variable p1.

class Pokemon(object):
  attack = 12
  defense = 10
  health = 15
  p_type = 'Normal'

  def __init__(self, name, level = 5):
    self.name = name   
    self.level = level 
  
  def train(self):
    self.update() 
    self.attack_up() 
    self.defense_up() 
    self.health_up()
    self.level = self.level + 1
    if self.level % self.evolve == 0:
      return self.level, 'Evolved!'
    else:
      return self.level  
  
  def attack_up(self):
    self.attack = self.attack + self.attack_boost 
    return self.attack 

  def defense_up(self):
    self.defense = self.defense + self.defense_boost
    return self.health 
  
  def health_up(self):
    self.health = self.health + self.health_boost
    return self.health 

  def update(self):
    self.health_boost = 5
    self.attack_boost = 3 
    self.defense_boost = 2 
    self.evolve = 10

  def __str__(self):
    return 'Pokemon name: {}, Type: {}, Level: {}'.format(self.name, self.p_type, self.level )

# subclass Q1 
class Grass_Pokemon(Pokemon):
  attack = 15
  defense = 14
  health = 12 
  p_type = 'Grass'

  def update(self):
    self.health_boost = 6
    self.attack_boost = 2
    self.defense_boost = 3
    self.evolve = 12

  def moves(self):
    self.p_moves = ['razor leaf', 'synthesis', 'petal']
  
  def action(self):
    return self.name + " knows a lot of different moves!"

p1 = Grass_Pokemon('Belle')

# subclass Q2 
class Grass_Pokemon(Pokemon):
  attack = 15
  defense = 14
  health = 12 
  p_type = 'Grass'

  def update(self):
    self.health_boost = 6
    self.attack_boost = 2
    self.defense_boost = 3
    self.evolve = 12

  def moves(self):
    self.p_moves = ['razor leaf', 'synthesis', 'petal']
  
  def action(self):
    return self.name + " knows a lot of different moves!"
  
  # override the train() method while also using parent.method(self) to import all the original actions
  def train(self):
          Pokemon.train(self)
          if self.level >= 10:
              self.attack_up()
        
    
            
            
p2 = Grass_Pokemon('Bulby')
p3 = Grass_Pokemon('Pika')

p3.train()

# Along with the Pokemon parent class, we have also provided several subclasses. Write another method in the parent class that will be inherited by the subclasses. Call it opponent. It should return which type of pokemon the current type is weak and strong against, as a tuple.

# Grass is weak against Fire and strong against Water

# Ghost is weak against Dark and strong against Psychic

# Fire is weak against Water and strong against Grass

# Flying is weak against Electric and strong against Fighting

# For example, if the p_type of the subclass is 'Grass', .opponent() should return the tuple ('Fire', 'Water')
class Pokemon():
    attack = 12
    defense = 10
    health = 15
    p_type = "Normal"

    def __init__(self, name,level = 5):
        self.name = name
        self.level = level
        self.weak = "Normal"
        self.strong = "Normal"

    def train(self):
        self.update()
        self.attack_up()
        self.defense_up()
        self.health_up()
        self.level = self.level + 1
        if self.level%self.evolve == 0:
            return self.level, "Evolved!"
        else:
            return self.level

    def attack_up(self):
        self.attack = self.attack + self.attack_boost
        return self.attack

    def defense_up(self):
        self.defense = self.defense + self.defense_boost
        return self.defense

    def health_up(self):
        self.health = self.health + self.health_boost
        return self.health

    def update(self):
        self.health_boost = 5
        self.attack_boost = 3
        self.defense_boost = 2
        self.evolve = 10

    def opponent(self):
        return self.weak, self.strong


    def __str__(self):
        self.update()
        return "Pokemon name: {}, Type: {}, Level: {}".format(self.name, self.p_type, self.level)

class Grass_Pokemon(Pokemon):
    attack = 15
    defense = 14
    health = 12
    p_type = "Grass"

    def __init__(self, name, level = 5):
      self.name = name
      self.level = level
      self.strong = 'Water'
      self.weak = 'Fire'
    
    def update(self):
        self.health_boost = 6
        self.attack_boost = 2
        self.defense_boost = 3
        self.evolve = 12
        

class Ghost_Pokemon(Pokemon):
  p_type = 'Ghost'

  def __init__(self, name, level = 5):
    self.name = name
    self.level = level 
    self.strong = 'Psychic'
    self.weak = 'Dark'

  def update(self):
    self.health_boost = 3
    self.attack_boost = 4
    self.defense_boost = 3

class Fire_Pokemon(Pokemon):
  p_type = 'Fire'

  def __init__(self, name, level = 5):
    self.name = name
    self.level =  level
    self.strong = 'Grass'
    self.weak = 'Water'

class Flying_Pokemon(Pokemon):
  p_type = 'Flying'

  def __init__(self, name, level = 5):
    self.name = name  
    self.level = level 
    self.strong = 'Fighting'
    self.weak = 'Electric'

grass = Grass_Pokemon('grassy')
print(grass.opponent())
ghost = Ghost_Pokemon('ghosty')
print(ghost.opponent() )
fire = Fire_Pokemon('firey')
print(fire.opponent())
flying = Flying_Pokemon('birdy')
print(flying.opponent())
