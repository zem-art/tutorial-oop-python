# Belajar Class Dan Instance Variabel

class Hero:  # Template
    # Class Variabel # Tidak akan Tercampur Dengan Instence Variabel
    jumlah = 0

    def __init__(self, inputName, power, deffend, bold):  # Bagian Instence Variabel
        self.name = inputName
        self.attack = power
        self.arrmor = deffend
        self.healty = bold
        Hero.jumlah += 1
        print("Membuat Hero Dengan Nama : " + inputName)


hero1 = Hero("Ruby", 100, 10, 7)
print(Hero.jumlah)
hero2 = Hero("Gushion", 100, 6, 10)
print(Hero.jumlah)
hero3 = Hero("Ucil", 1000, 7, 20)
print(Hero.jumlah)
hero4 = Hero('Fanny', 3000, 2000, 1000)
print(Hero.jumlah)
