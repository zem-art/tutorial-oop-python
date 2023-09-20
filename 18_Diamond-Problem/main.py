# Belajar Menyelesaikan Diamond Problem

print("\n", "=" * 5, "Belajar Menyelesaikan Diamond Problem", "=" * 5, "\n")


# Diamon Problem yg Biasa Terjadi Dari Multiple Inheritance

class A:
    def show(self):
        print("Ini Adalah Show A")


class B(A):
    pass


class C(A):
    def show(self):
        print("Ini Adalah Show C")


class D(B, C):
    pass  # DI Cek Apabila Di Salah Satu sub CLass nya

  # =====READ ME==== Pleass

# Ini Lah Diamond Problem yg Mana sub Class D Akan Mengecek Apakah Ada Atribut / Method yg mau Di tampilkan , Di Dalam Class B & C Apabila Kedua nya Tidak Ada Method yg Di minta Maka Akan Mengecek Ke Class A Dan Class A Adalah induk Dari Semua Sub Class Yg Di Bawah nya


objek = D()
objek.show()
# help(objek)
