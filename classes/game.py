import random
import numpy as np


class brcolors:
  header = '\033[95m'
  blue = '\033[94m'
  green = '\033[92m'
  warn = '\033[93m'
  fail = '\033[91m'
  endc = '\033[0m'
  bold = '\033[01m'
  underline = '\033[4m'

class person:
  def __init__(self, hp, mp, atk, df):
    self.maxhp = hp
    self.hp = hp
    self.maxmp = mp
    self.mp = mp
    self.atkl = atk -10
    self.atkh = atk + 10
    self.df = df
    self.actions = ['attack', 'magic']
  
  def genDmg(self):
    return random.randrange(self.atkl, self.atkh)
  
  def genSpellDmg(self, i):
    mgl = self.magic[i]["dmg"] - 10
    mgh = self.magic[i]["dmg"] + 10
    return random.randrange(mgl, mgh)

  def takeDmg(self, dmg):
    self.hp = self.hp - dmg
    if self.hp < 0 :
      self.hp = 0
      return self.hp
  
  def getHp(self):
    return self.hp
  
  def getMaxHp(self):
    return self.maxhp
  
  def getMp(self):
    return self.mp
  
  def getMaxMp(self):
    return self.maxmp

  def chooseAct(self):
    i = 1
    for item in self.actions:
      print(str(i) + ':', item)
      i += 1
  
  def chooseSpell(self):
    i = 1
    for spell in self.magic:
      print(str(i) + ':' + spell['name'])
      i += 1

fire = np.array([['Fire Release: Flame Spread Technique','fire',20,250],['Fire Release: Dragon Fire Technique','fire',30,300]])

water = np.array([['Water Mirror Technique','water',20,250],['Water Prison Technique','water',25,300]])

earth = np.array([['Earth Release: Rock Throw Technique','earth',25,250],['Swift Earth','earth',25,252]])

ligthining = np.array([['chidori','lightning',40,450],['raikri','lightning',50,500],['rasenshuriken','wind',80,450]])

wind = np.array([['wind scythe','wind',35,350],['rasenshuriken','wind',80,450]])

class jutsus():
  def __init__(self, chakra):
    self.chakra = chakra
    self.maxChakra = chakra

  def techniqueOnType(self, i):
    if i == 0:
      print(str(fire))
    elif i == 1:
      print(str(wind))
    elif i == 2:
      print(str(water))
    elif i == 3:
      print(str(ligthining))
    elif i == 4:
      print(str(earth))


  def genDmg(self, nature, i):
    if nature == 0:
      atkl = int(fire[i,3]) - 10
      atkh = int(fire[i,3]) + 10
      return random.randrange(atkl, atkh)
    elif nature == 1:
      atkl = int(wind[i,3]) - 10
      atkh = int(wind[i,3]) + 10
      return random.randrange(atkl, atkh)
    elif nature == 3:
      atkl = int(ligthining[i,3]) - 10
      atkh = int(ligthining[i,3] )+ 10
      return random.randrange(atkl, atkh)
    elif nature == 4:
      atkl = int(earth[i,3]) - 10
      atkh = int(earth[i,3]) + 10
      return random.randrange(atkl, atkh)
    
    elif nature == 2:
      atkl = int(water[i,2]) - 10
      atkh = int(water[i,2]) + 10
      return random.randrange(atkl, atkh)
    
  def justuC(self, nature, i):
    if nature == 0:
      return fire[i,2]
    elif nature == 2:
      return water[i,2]
    elif nature == 1:
      return wind[i,2]
    elif nature == 3:
      return ligthining[i,2]
    elif nature == 4:
      return earth[i,2]
    
  def reduceC(self,cost):
    self.chakra = self.chakra - cost

  def jutsuN(self, nature, i):
    if nature == 0:
      return fire[i,0]
    elif nature == 1:
      return wind[i,0]
    elif nature == 2:
      return water[i,0]
    elif nature == 3:
      return ligthining[i,0]
    elif nature == 4:
      return water[i,0]
    
  def allType(self):
    print('1 : fire')
    print('2 : wind')
    print('3 : water')
    print('4 : ligthining')
    print('5 : earth')
  
  def getChakra(self):
    return self.chakra

  def getMaxChakra(self):
    return self.maxChakra