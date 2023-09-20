# Belajar Encaplusiasi
print("\n", "="*5, "Belajar Encapsulisi", "="*5, "\n")

# Aturan Nya
# 1 . Buat Semua Variabel Private
# 2 . mengambil data uh kita butuh kan menggunakan gether dan setter
# Getter => Mengambil Variabel
# Setter => Menseting Variabel


class Hero:
    def __init__(self, name, healty, attackPower):
        self.__nama = name
        self.__Hp = healty
        self.__power = attackPower

    # CONTOH ENCAPSULISASI Menggunakan :
    # == Getter ==
    def GetName(self):
        return self.__nama

    def GetHealty(self):
        return self.__Hp

    # === Setter ===

    # Mengubah Di Dalam Class nya
    def diserang(self, serang):
        self.__Hp -= serang

    # Membuat si Fungsi Ini Menjadi Pulic
    def setAttPower(self, serangBaru):
        self.__attPower = serangBaru


# Awal Dari Game
ruby = Hero("Ruby", 100, 30)

# Game Berjalan

print(ruby.GetName())  # Cara Mengambil Variabel Yg Di Private
print(ruby.GetHealty())
ruby.diserang(10)
print(ruby.GetHealty())
