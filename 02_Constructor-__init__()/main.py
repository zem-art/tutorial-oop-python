# Belajar Consctructor __init__

# __init__ => Yang Akan Di Jalan kan pertama Kali Si Object Itu Di Buat

class Hero:  # Template
    # ===Cara Penulisan Yang Pertama ===
    # def __init__(self, x):  # self ini merujuk ke hero1
    #     print("Alex", x)

    # ===Cara Penulisan Yang Ke Dua===
    def __init__(self, inputName, power, deffensd, bold):  # self ini merujuk ke hero1
        self.name = inputName
        self.attack = power
        self.arrmor = deffensd
        self.healty = bold

# Pemanggilan Dengan Cara 1
# hero1 = Hero(10)
# hero2 = Hero(10)


# Pemanggilan Dengan Cara Ke 2
hero1 = Hero("Ruby", 100, 10, 7)
hero2 = Hero("Gushion", 100, 6, 10)
hero3 = Hero("Ucil", 1000, 7, 20)

print(hero1.name)
print(hero3.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)
