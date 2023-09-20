# Belajar Static Method Dan ClassMethod
print("\n", "="*5, "StaticMethod Dan ClassMethod", "="*5, "\n")


class Hero:
    # Private Variabel
    __jumlah = 0

    def __init__(self, name):
        self.__nama = name
        Hero.__jumlah += 1

    # Method Ini Hanya Berlaku Untuk objek
    def getJumlah(self):
        return Hero.__jumlah

    # Method Ini Hanya Berlaku Untuk objek , tapi Berlaku Untuk Class
    def JumlahHero():
        return Hero.__jumlah

    # Method Static Menggunakana(decorator)
    @staticmethod  # ini akan Menempel Pada Class dan Objek nya
    def JumlahHeroAll():  # Menggunakan Encapsulasi
        return Hero.__jumlah  # static Method tidak menggunakan argument

    # Class Static Menggunakana(decorator)
    @classmethod  # ini akan Menempel benar benar Ke Class nya
    # Diberi Argument biar Tidak mengubah Class nya lagi
    def JumlahHeroAll2(cls):  # Berguna Untuk Inheritence
        return cls.__jumlah  # classMethod Menggunkan Argument


Jon = Hero("Jonson")

# print(Hero.getJumlah())  # Menggunakan Cara Yg Ke 1
# print(Hero.JumlahHero())  # Menggunakan Cara Yang Ke 2
print(Hero.JumlahHeroAll())  # Menggunakan Cara Yang Ke 3
Tigreal = Hero("Tigreal")
# Menggunakan Cara Yang Ke 3 Menggunkan StaticMethod
print(Tigreal.JumlahHeroAll())
Gatot = Hero("Gatot Kaca")
# Menggunkan Cara yg ke 4 menggunakan ClassMethod
print(Jon.JumlahHeroAll2())
