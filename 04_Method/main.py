# Belajar Method

# Method => aksi dari objeck / berinteraksi kkpd objeck lain

# Method di bagi 2:
# method interaktive => yg berinteraksi dengan claent
# Method yg berinteraksi dengan object


# Method Di Sini Terbagi menjadi 3
# 1 . Method menggunakan argument
# 2 . Method Tanpa Argument
# 3 . Method Menggunakan return

class Hero:
    # Class Variabel
    jumlah_hero = 0

    def __init__(self, inputName, inputHealty, inputPower, inputArmor):
        # Instanse Variabel
        self.name = inputName
        self.healty = inputHealty
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah_hero += 1

    # yg Tidak mengembalikan nilai dan tidak menggunkan return

    # Void function, Method tanpa return , tanpa argument
    def siapa(self):
        print("Nama Ku Adalah " + self.name)

    # Method Dengan Argument , tannpa return
    def healtUp(self, up):
        self.healty += up

    # Method Dengan return , Bisa di pakai Argument
    def getHealth(self):
        return self.healty


hero1 = Hero("Natalia", 100, 20, 5)
hero2 = Hero("UcilChan", 90, 30, 10)

print("="*50, "\n")
# Method tanpa return
hero1.siapa()
# Method Dengan Argument
hero1.healtUp(15)
print("Hp Ku Sekarang : ", hero1.healty)
# Method Dengan return
print('Hp Me', hero1.getHealth())
