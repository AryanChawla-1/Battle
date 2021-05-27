from classes.game import person, brcolors, jutsus

player = person(6000, 150, 60, 69)
jutsu = jutsus(15000)
enemy = person(12000, 65, 45, 25)
battle = True

print(brcolors.fail+ brcolors.bold + 'ENEMY APPROACHED!'+ brcolors.endc)

while battle:
  print('======================================')
  player.chooseAct()
  choice = input('choose your actions wisely')
  index = int(choice) - 1
  
  if index == 0:
    dmg  = player.genDmg()
    enemy.takeDmg(dmg)
    print('your attcked', dmg, 'enemy hp is', enemy.getHp())
  elif index == 1:
    jutsu.allType()
    magicChoice = int(input('choose type')) - 1
    jutsu.techniqueOnType(magicChoice)
    jutsua = int(input('choose jutsu')) - 1
    magicD = jutsu.genDmg(magicChoice, jutsua)
    spells = jutsu.jutsuN(magicChoice, jutsua)
    cost = jutsu.justuC(magicChoice, jutsua)

    currentMP = jutsu.getChakra()

    if int(cost) > int(currentMP) :
      print(brcolors.fail + 'you dont have enough mp' + brcolors.endc)
      continue
    jutsu.reduceC(int(cost))
    enemy.takeDmg(magicD)
    print('your attcked', magicD, 'enemy hp is', enemy.getHp())  

  enemyC = 1
  enemyD = enemy.genDmg()
  player.takeDmg(enemyD)
  print('you have been attacked for', enemyD, 'your hp is', player.getHp())

  if enemy.getHp() == 0:
    print(brcolors.green + 'You Won, nerd!' + brcolors.endc)
    battle  = False

  elif player.getHp() == 0:
    print(brcolors.fail + 'You Lost noob!' + brcolors.endc)
    battle = False
  
  else :
    
    print('=================================')
    print(brcolors.fail , 'enemy health points are', enemy.getHp(), brcolors.endc)
    print(brcolors.green, 'your Hp is', player.getHp(), 'out of', player.getMaxHp(), brcolors.endc)
    
    print(brcolors.green,  'your mp is', jutsu.getChakra(),
    'out of ',jutsu.getMaxChakra(), brcolors.endc)


