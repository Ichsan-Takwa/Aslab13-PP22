class Person:

    def __init__(self, name, age, IsMale):
        self.__name = name
        self.__age = age
        self.__IsMale = IsMale

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

nama = str(input())
umur = int(input())
kelamin = bool(input())

orang1 = Person(nama,umur,kelamin)

orang1.setName(nama)
orang1.setAge(umur)
orang1.setIsmale(kelamin)

print(orang1.getName())
print(orang1.getAge())
print(orang1.getIsMale())
