# Belajar Method Resulution Order // Multiple Inheritence

print("\n", '=' * 5, "Belajar Method Resulution Order", "=" * 5, "\n")

# Kasus nya Method nya sama


class A:
    def show_Info(self):
        print("Ini Adalah Show Info A")


class B:
    def show_Info(self):
        print("Ini Adalah Show Info B")


class C(A, B):  # Method yg Di inheritance Dari Sebuah Class Tergantung Cara Penulisan Inheritance nya . Contoh : (A,B) Apabila A di depan Maka Akan Di tampilkan Method Dari A lebih Dahulu & Dan Apabila (B,A) Maka Akan Ditampilkan B terlebih Dahulu
    pass
    # def show_Info(self):
    #     print("Ini Adalah Show Info C")


objek = C()
objek.show_Info()
# help(objek) # Help Untuk mengetahui Urutan Eksekusi nya Dari Mana Terlebih Dahulu
