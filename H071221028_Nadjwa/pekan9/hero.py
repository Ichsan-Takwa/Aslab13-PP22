class Human:
    def __init__ (self, name, pos_x):
        self.nama = name
        self.__posisi = pos_x
        self._speed = 1
    def movement(self, arah):
        if arah == "L":
            self.__posisi = self.__posisi - self._speed
        elif arah == "R":
            self.__posisi = self.__posisi + self._speed
        
    def getPosisi (self):
        return self.__posisi
    
    def getSpeed (self):
        return self._speed
    def setSpeed (self,newSpeed):
        self._speed = newSpeed

class Hero(Human):
    def __init__ (self, name, pos_x):
        super().__init__(name, pos_x)
        self._power = 15
        self._health = 400
        self._armor = 15
        self._speed = 3

    def attack (self, target):
        newHealth = target.getHealth() - self._power
        target.setHealth (newHealth)
        # target._health = target._health - self._power

    def getPower (self):
        return self._power 
    def setPower (self, newPower):
        self._power = newPower

    def getHealth(self):
        return self._health
    def setHealth (self, newHealth):
        self._health = newHealth

    def getArmor(self):
        return self._armor
    def setArmor (self, newArmor):
        self._armor = newArmor

    def getspeed(self):
        return self._speed 
    def setSpeed (self, newSpeed):
        self._speed = newSpeed

class Warior(Hero): 
    def __init__ (self, name, pos_x):
        super().__init__(name, pos_x)
        self._power = 26
        self._armor = 30
    
    
    def special (self,target):
        self._armor = 45
        self._power = 32
        self.attack(target)

        

class Assasin(Hero): 
    def __init__ (self, name, pos_x):
        super().__init__(name, pos_x)
        self._power = 35
        self._speed = 4
    def special (self, target):
        self._speed = 7
        self._power = 42
        self.attack(target)


class Support(Hero):
    def __init__ (self, name, pos_x):
        super().__init__(name, pos_x)
        self._health = 500
        self._armor= 8
        self._speed = 4
    def special(self, target):
        self._speed = 6
        # target._health = target._health + 150
        newHealth = target.getHealth() + 150
        target.setHealth (newHealth)
        

nadjwa = Warior("nadjwa", 5)
amalia = Assasin ("amalia", 7)
andiny = Support("andiny", 11)


nyawa =  nadjwa.getHealth()
print("sebelum", nyawa)
amalia.special(nadjwa)
nyawa =  nadjwa.getHealth()
print("Sesudah", nyawa)







# nadjwa.movement("L")
# posisi = nadjwa.getPosisi()

# nyawa = nadjwa.getHealth()
# print(posisi, nyawa)
