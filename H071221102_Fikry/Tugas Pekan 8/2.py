class kubus:
    def __init__(self, lebar, tinggi, panjang):
        self.lebar = lebar
        self.tinggi = tinggi
        self.panjang = panjang
        

    def rumus(self, massa):
        self.massa = massa
        volume = self.lebar * self.tinggi * self.panjang
        rumus = self.massa / volume
        print(f'Massa jenis = {rumus}')
        

lebar = float(input("masukkan lebar: "))
tinggi = float(input("masukkan tinggi: "))
panjang = float(input("masukkan panjang: "))
massa = float(input("masukkan massa: "))

cube = kubus(lebar, tinggi, panjang)
cube.rumus(massa)
cube.rumus(massa*2)
