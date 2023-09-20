class Hero:

    def __init__(self, nama):
        self.health_pool = [0, 100, 200, 300, 400, 500]
        self.attPower_pool = [0, 10, 20, 30, 40, 50]
        self.armor_pool = [0, 1, 2, 3, 4, 5]
        # Nilai yg di atas akan di ubah di subClass nya
        self.__name = nama
        self.__level = 0
        self.__exp = 0

    def show_Info(self):
        print("{} \n\t level : {} \n\t healty : {} \n\t attack Power : {} \n\t Armor : {}".format(
            self.__name,
            self.__level,

            # Ini Untuk sub Class nya
            self.__healty,
            self.__attPower,
            self.__armor
        )
        )

    # Bagian Getter Untuk Mengubah Yg tadi nya private Menjadi Method / Property
    @property
    def health_pool(self):
        pass

    @property
    def attPower_pool(self):
        pass

    @property
    def armor_pool(self):
        pass

    @property
    def levelUp(self):
        pass

    @property
    def gainExp(self):
        pass

    # Dan Kita Setter / Panggil Si Getter Nya yg Sudah di jadikan Method / property
    @health_pool.setter
    def health_pool(self, input):
        self.__healty_pool = input

    @attPower_pool.setter
    def attPower_pool(self, input):
        self.__attPower_pool = input

    @armor_pool.setter
    def armor_pool(self, input):
        self.__armor_pool = input

    @gainExp.setter  # Exp Di Setter , Apabila Melebihi 100 Maka Di akan levelUp dan sisa nya di bulatkan
    def gainExp(self, input):
        self.__exp += input
        if (self.__exp >= 100):
            self.levelUp = self.__exp // 100  # Di Bagi Tapi Di bulat kan Ke Bawah
            self.__exp %= 100  # Sisa nya Berapa Dari level up nya

    @levelUp.setter  # Level Up Nya Di Set biar Bisa Berubah Ubah
    def levelUp(self, input):
        self.__level += input
        self.__healty = self.__healty_pool[self.__level]
        self.__attPower = self.__attPower_pool[self.__level]
        self.__armor = self.__armor_pool[self.__level]


class Hero_Assasin(Hero):

    def __init__(self, name_Assasin):
        super().__init__(name_Assasin)
        self.health_pool = [0, 50, 100, 150, 200, 250]
        self.attPower_pool = [0, 20, 40, 60, 80, 100]
        self.armor_pool = [0, 0.5, 2.0, 3, 4.5, 5]
        self.levelUp = 1


class Hero_Support(Hero):

    def __init__(self, name_Supprot):
        super().__init__(name_Supprot)
        self.health_pool = [0, 10, 20, 30, 40, 50]
        self.attPower_pool = [0, 5, 10, 15, 20, 30]
        self.armor_pool = [0, 0.5, 2.0, 3, 4.5, 5]
        self.levelUp = 1
