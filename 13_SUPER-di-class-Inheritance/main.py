# Belajar Super Inheritance

class Hero:

    def __init__(self, name, healty):
        self.nama = name
        self.bold = healty

    def showInfo(self):
        print("{} dengan Healty : {}".format(self.nama, self.bold))


class Hero_Fighter(Hero):
    def __init__(self, nama_Figter):
        # Hero.__init__(self, nama_Figter, 100)  # Cara 1
        super().__init__(nama_Figter, 150)
        # Menggunkan Method Super Dari dan mengambil Method __init__ Dari Super
        super().showInfo()
        # bisa Menggunkan ini
        Hero.showInfo(self)
        # Tapi Apabila Kita Ubah Class Super nya maka Harus Mengubah 1/1 syntax nya apabila sudah banyak


class Hero_Mage(Hero):
    def __init__(self, nama_Mage):
        # Hero.__init__(self, nama_Figter, 100)  # Cara 1
        super().__init__(nama_Mage, 50)
        # Menggunkan Method Super Dari dan mengambil Method __init__ Dari Super
        super().showInfo()
        # bisa Menggunkan ini
        Hero.showInfo(self)
        # Tapi Apabila Kita Ubah Class Super nya maka Harus Mengubah 1/1 syntax nya apabila sudah banyak


terizila = Hero_Fighter("Terizela")
cecilion = Hero_Mage("Cecilion")
