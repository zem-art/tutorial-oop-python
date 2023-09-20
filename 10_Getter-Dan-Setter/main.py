# Belajar Getter Dan Shetter

print("\n", "="*5, "Belajar Getter Dan Shetter", "="*5, "\n")


class Hero:

    def __init__(self, name, armor, healty):
        self.nama = name
        self.__body = armor
        self.__hp = healty
        # User Jadi Bisa mengakses dan Merubah Datanya
        # self.__info = "Name {} :\n\thealty : {}" .format(
        #     self.__nama, self.__hp)

    # def getHealty(self):
    #     return self.__hp
    @property  # dianggap varibel / merubah method menjadi variabel
    def info(self):
        return "Name {} :\n\thealty : {}" .format(
            self.nama, self.__hp)

    # Cara Encapsulasi Menggunakan Cara nya Python
    @property  # Merubah Armor
    def armor(self):
        pass

    @property  # Merubah Darah
    def healty(self):
        pass

    # Menggunakan Decorator

    # Getter
    @armor.getter
    def armor(self):
        return self.__body  # Nilai nya masih private

    # Setter
    @armor.setter
    def armor(self, input):
        self.__body = input

    # Deleter / Delete
    @armor.deleter
    def armor(self):
        print("Armor Di Delete")
        self.__body = None  # Tidak Ada nilai nya


Nana = Hero("Nana", 50, 100)

print("Merubah Info")
# print(Nana.info)
# Nana.info = "info"  # Cara Untuk Mengubah Public Function
# Value Name Di Ubah
print(Nana.info)
Nana.nama = "Dadang"
print(Nana.info)

print("Getter Dan Setter untuk __armor")
print(Nana.armor)  # Yg Tadi nya Nilai Nya none
print(Nana.__dict__)

# Nilai Armor di ubah
Nana.armor = 10
print(Nana.armor)
print(Nana.__dict__)

# Nilai Armor nya Di delete
del Nana.armor
print(Nana.__dict__)
