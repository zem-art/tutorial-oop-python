# Membuat Game Sederhana

class Hero:
    def __init__(self, nama, healty, power, armor):
        self.name = nama
        self.bold = healty
        self.attack = power
        self.deffend = armor

    def serang(self, lawan):  # Membuat argument dari class trsbt
        # pngil argument trsb berdasarkan ...
        print(self.name + " menyerang " + lawan.name)
        lawan.diserang(self, self.attack)  # berdasarkan func dari class trsbt

    def diserang(self, lawan_balik, serang_lawan):
        # menbuat argument berdasrkan .....
        print(self.name + " diserang " + lawan_balik.name)
        attack_diterima = serang_lawan/self.deffend
        print("Serangan Terasa :" + str(attack_diterima))
        self.bold -= attack_diterima
        print('Darah :', self.name + ' tersisa : ' + str(self.bold))


harley = Hero('Harley', 100, 20, 60)
gusion = Hero("Gusion", 100, 10, 10)

print('=' * 50, '\n')

harley.serang(gusion)
print('='*40)
gusion.serang(harley)
