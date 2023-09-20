# Belajar Latihan Encapsulasi

class Hero:
    # Private Class Variabel
    __jumlah = 0

    def __init__(self, name, healty, power, armor):
        self.__nama = name
        self.__hpBase = healty
        self.__attackBase = power
        self.__bodyBase = armor
        self.__level = 1  # nilai awalnya
        self.__exp = 0  # nilai awalnya

        # aktivitas penyerangan
        self.__hpMax = self.__hpBase * self.__level
        self.__attPower = self.__attackBase * self.__level
        self.__armor = self.__bodyBase * self.__level

        self.__hpBase = self.__hpMax

        Hero.__jumlah += 1

    @property
    def info(self):  # Info Hero Nya Berdasarkan Hero Nya
        return "{}  level = {} :\n\thealty = {}\{} \n\tattack = {} \n\tarmor = {}".format(self.__nama, self.__level, self.__hpBase, self.__hpMax, self.__attPower, self.__armor)

    @property
    def gainExp(self):
        pass

    # Menset Exp Apabila Dia Sudah Mencapai 100
    @gainExp.setter
    def gainExp(self, addExp):
        self.__exp += addExp
        if (self.__exp >= 100):  # jika level exp sudah melebihi 100 maka
            print(self.__nama, "level Up")
            self.__level += 1  # menaikan level nya
            self.__exp -= 100  # mereset ulang apabila di sudah mencapai level 100

        # Aktifitas Untuk Mengembalikan Nilai nya Dan Mengupgrade nya
        self.__hpMax = self.__hpBase * self.__level
        self.__attkPower = self.__attackBase * self.__level
        self.__armor = self.__bodyBase * self.__level

    def attack(self, musuh):
        self.gainExp = 50


kagura = Hero("Kagura", 100, 5, 10)
Franco = Hero("Franco", 100, 5, 10)

print(kagura.info)
kagura.attack(Franco)
kagura.attack(Franco)
kagura.attack(Franco)
print(kagura.info)
print(Franco.gainExp)
