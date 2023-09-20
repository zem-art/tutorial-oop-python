# Belajar Override Method

class Hero:
    def __init__(self, name, bold):
        self.nama = name
        self.healty = bold

    def showInfo(self):
        print("Show Info Class Hero")
        print("{} Hp Dari : {}".format(self.nama, self.healty))


class Hero_Assasin(Hero):
  # Mengambil Data Dari Class hero
    def __init__(self, nama_Assasin):
        super().__init__(nama_Assasin, 90)

    # Override / Menimpa showInfo Dari Class Hero
    def showInfo(self):  # Tapi Cuman di subClass hero_assasin
        print("Showinfo Dari Sub Class")
        print("{} Tipe : Assasins , healty {}".format(
            self.nama, self.healty))


class Hero_Tank(Hero):
    def __init__(self, nama_Tank):
        super().__init__(nama_Tank, 100)


hayabusa = Hero_Assasin("Hayabusa")
kufra = Hero_Tank("Kufra")

hayabusa.showInfo()  # subClass yg sudah di Override
kufra.showInfo()  # Subclass Yg Belum Di Override
