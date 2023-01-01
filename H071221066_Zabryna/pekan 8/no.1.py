class Person :
    def __init__ (self, nama, usia, gender, alamat, cita2, prodi) :
        self.name = nama
        self.age = usia
        self.IsMale = gender 
        self.alamat = alamat 
        self.cita2 = cita2
        self.prodi = prodi

    def setAge(self, usia) :
        self.age = usia 
    def cetakAge(self) :
        print(f"Umur : {self.age}")

    def setName(self, nama) :
        self.name = nama 
    def cetakName(self) :
        print(f"Nama : {self.name}")

    def setGender(self, gender) :
        self.IsMale = gender 
    def cetakGender(self) :
        if self.IsMale == True :
            print("Gender : Laki-laki")
        else : 
            self.IsMale == False
            print("Gender : Perempuan")

    def setAlamat(self, alamat) :
        self.alamat = alamat
    def cetakAlamat(self) :
        print(f"Alamat : {self.alamat}")

    def setCita2(self, cita2) :
        self.cita2 = cita2
    def cetakCita2(self) :
        print(f"Cita-cita : {self.cita2}")

    def setProdi(self, prodi) :
        self.prodi = prodi 
    def cetakProdi(self) :
        print(f"Prodi : {self.prodi}")
    

andiny = Person("Zabryna Andiny", 18, False, "Jl. Gontang Raya", "Programmer", "Sistem Informasi")
andiny.cetakName()
andiny.cetakAge()
andiny.cetakGender()
andiny.cetakAlamat()
andiny.cetakCita2()
andiny.cetakProdi()