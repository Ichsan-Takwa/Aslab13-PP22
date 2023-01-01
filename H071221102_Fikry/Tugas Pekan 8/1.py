class Person:
    def __init__(self, nama, umur, kelamin, suku, tinggi, hoby):
        self.nama = nama
        self.umur = umur
        self.kelamin = kelamin
        self.suku = suku
        self.tinggi = tinggi
        self.hoby = hoby

    def cetak_name(self):
        print(f'{self.nama}')

    def cetak_age(self):
        print(f'{self.umur}')

    def cetak_male(self):
        print(f'{self.kelamin}')

    def cetak_etnis(self):
        print(f'{self.suku}')
    
    def cetak_high(self):
        print(f'{self.tinggi}')

    def cetak_kegemaran(self):
        print(f'{self.hoby}')

nama = str(input())
umur = int(input())
kelamin = bool(input())
suku = str(input())
tinggi = int(input())
hoby = str(input())

Fikry = Person(nama, umur, kelamin, suku, tinggi, hoby)
Fikry.cetak_name()
Fikry.cetak_age()
Fikry.cetak_male()
Fikry.cetak_etnis()
Fikry.cetak_high()
Fikry.cetak_kegemaran()

