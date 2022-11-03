class Kubus:
    def __init__(self, lebar, tinggi, panjang):
        self.__lebar = lebar
        self.__tinggi = tinggi
        self.__panjang = panjang

    def setLebar(self, value):
        self.__lebar = value

    def setTinggi(self, value):
        self.__tinggi = value

    def setPanjang(self, value):
        self.__panjang = value

    def setMassa(self, value):
        self.__massa = value

    def getMassaJenis(self):
        return (massa)/(lebar*tinggi*panjang)

lebar = float(input())
tinggi = float(input())
panjang = float(input())
massa = float(input())

kubus = Kubus(lebar,tinggi,panjang)

kubus.setMassa(massa)
print('Massa Jenis = ', kubus.getMassaJenis())
kubus.setMassa(massa*2)
print('Massa Jenis = ', kubus.getMassaJenis())