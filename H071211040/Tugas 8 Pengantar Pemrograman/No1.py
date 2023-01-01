class Person:

    def __init__(self, name, age, IsMale,kendaraan,merek_hp,merek_laptop):
        self.__name = name
        self.__age = age
        self.__IsMale = IsMale
        self.__kendaraan = kendaraan
        self.__merek_hp = merek_hp
        self.__merek_laptop = merek_laptop

    def getName(self):
        return self.__name
    def setName(self, value):
        self.__name = value

    def getAge(self):
        return self.__age
    def setAge(self, value):
        self.__age = value

    def getIsMale(self):
        return self.__IsMale
    def setIsmale(self, value):
        self.__IsMale = value

    def getKendaraan(self):
        return self.__kendaraan
    def setKendaraan(self, value):
        self.__kendaraan = value

    def getMerek_hp(self):
        return self.__merek_hp
    def setMerek_hp(self, value):
        self.__merek_hp = value
        
    def getMerek_laptop(self):
        return self.__merek_laptop
    def setMerek_laptop(self, value):
        self.__merek_laptop = value

nama = str(input())
umur = int(input())
kelamin = bool(input())
kendaraan = str(input())
merek_hp = str(input())
merek_laptop = str(input())

orang1 = Person(nama,umur,kelamin,kendaraan,merek_hp,merek_laptop)

orang1.setName(nama)
orang1.setAge(umur)
orang1.setIsmale(kelamin)
orang1.setKendaraan(kendaraan)
orang1.setMerek_hp(merek_hp)
orang1.setMerek_laptop(merek_laptop)

print(orang1.getName())
print(orang1.getAge())
print(orang1.getIsMale())
print(orang1.getKendaraan())
print(orang1.getMerek_hp())
print(orang1.getMerek_laptop())