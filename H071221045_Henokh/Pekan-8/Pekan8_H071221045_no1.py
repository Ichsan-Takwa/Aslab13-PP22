class Computer:
    def __init__(self, cpu, gpu, ram):
        self.cpu = cpu
        self.gpu = gpu
        self.ram = ram
    def core(self):
        print("CPU-nya adalah", self.cpu)
    def graphic(self):
        print("GPU-nya adalah", self.gpu)
    def memory(self):
        print("RAM-nya sebanyak", self.ram)

computer1 = Computer("i5-7200U", "Nvidia 940mx", "4 GB")
computer2 = Computer("i7-10870H", "GTX-1650", "8 GB")
computer3 = Computer("Ryzen 7 5900X", "RTX 3070", "16 GB")

print("""============================================
Pilihlah jenis PC yang ingin dilihat:
1. Low Budget
2. Mid Budget
3. High Budget""")

while True:
    pc = int(input(">Enter: "))
    if pc == 1:
        computer1.core()
        computer1.graphic()
        computer1.memory()
        break
    elif pc == 2:
        computer2.core()
        computer2.graphic()
        computer2.memory()
        break
    elif pc == 3:
        computer3.core()
        computer3.graphic()
        computer3.memory()
        break
    else:
        print("Silahkan coba lagi")