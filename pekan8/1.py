class person :
    def __init__ (self, nama, umur, gender, Hobi, Warna, kampus):
        self.name = nama
        self.age = umur
        self.isMale = gender
        self.Hobbies = Hobi 
        self.color = Warna
        self.campus = kampus

    def setAge(self, umur):
        self.age= umur
    def cetakAge(self):
        print(f'umur : {self.age}')

    def setName(self, nama):
        self.name= nama
    def cetakName(self):
        print(f'nama : {self.name}')

    def setGender(self,gender):
        self.gender = gender
    def cetakGender(self):
        if self.isMale == True :
            print ("gendernya lakilaki")
        else :
            self.isMale == False
            print("Gendernya bukan lakilaki")

    def setHobi(self, Hobi):
        self.Hobbies = Hobi
    def cetakHobi(self):
        print(f"Hobi {self.name} adalah: {self.Hobbies} ")

    def setColor(self, Warna):
        self.color = Warna 
    def cetakColor(self):
        print(f"warna kesukaan {self.name} adalah: {self.color} ")

    
    def setCampus(self, kampus):
        self.campus = kampus 
    def cetakCampus(self):
        print(f"kampus {self.name} di: {self.campus} ")
    
    
nadjwa = person ("nadjwa", 18, False, "Belajar", "abuabu", "UNHAS")
nadjwa.cetakName()
nadjwa.cetakAge()
nadjwa.cetakGender()
nadjwa.cetakHobi()
nadjwa.cetakColor()
nadjwa.cetakCampus()
           
