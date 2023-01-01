class Human:
    def __init__(self,name,pos_x):
        self.name = name
        self.__position =  pos_x 

    def movement(self,move):
        if move == "L":
            self.__position-= self._speed
        elif move == "R":
            self.__position += self._speed

    def getPosition(self):
        return self.__position

class Hero(Human):
    def __init__(self,name,pos_x):
        super().__init__(name,pos_x)
        self._power = 15 
        self._health = 400
        self._armor = 15
        self._speed = 5

    def getPower(self):
        return self._power
    def getHealth(self):
        return self._health
    def getArmor(self):
        return self._armor
    def getSpeed(self):
        return self._speed

class Warrior(Hero):
    def __init__(self,name,pos_x):
        super().__init__(name,pos_x)
        self._power = 26
        self._armor = 30

    def attack(self,target):
        target._health -= self._power 

    def special(self,target): 
        self._power = 32   
        self._armor = 45
        target._health -= self._power
        
    def getPower(self):
        return self._power
    def getHealth(self):
        return self._health
    def getArmor(self):
        return self._armor
    def getSpeed(self):
        return self.speed      

class Assassin(Hero):
    def __init__(self,name,pos_x):
        super().__init__(name,pos_x)            
        self._power = 35
        self.speed = 4

    def attack(self,target):
        target._health -= self._power

    def special(self,target): 
        self._armor = 42
        self._speed = 7   
        target._health -= self._power

    def getPower(self):
        return self._power
    def getHealth(self):
        return self._health
    def getArmor(self):
        return self._armor
    def getSpeed(self):
        return self.speed    

class Support(Hero):
    def __init__(self,nama,pos_x):
        super().__init__(nama,pos_x)
        self._health = 500
        self._armor = 8
        self.speed = 4

    def attack(self,target):
        target._health -= self._power

    def special(self,target): 
        self.speed = 6   
        target._health += 150

    def getPower(self):
        return self._power
    def getHealth(self):
        return self._health
    def getArmor(self):
        return self._armor
    def getSpeed(self):
        return self.speed 


warrior = Warrior("bambang", pos_x = 10)
assassin = Assassin("joko", pos_x = 25)
support = Support("udin",pos_x = 30)

print("health (before)", warrior.getHealth())
assassin.attack(warrior)
print('Posisi Awal',warrior.getPosition())
warrior.movement('R')
warrior.movement('R')

print("health (after)", warrior.getHealth())
print("-" * 15)
print('Posisi Akhir',warrior.getPosition())

print("Warrior (health)", warrior.getHealth())
print("Support (speed) : ",support.getSpeed())
support.special(warrior)

print("Warrior (health)", warrior.getHealth())
print("Support (speed): ",support.getSpeed())