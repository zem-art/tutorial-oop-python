# Belajar Menggunkan Private Variabel
print("\n", "="*5, "Private Variabel", '='*5, "\n")

# class / tamplate


class Hero:
    # class Variabel
    jumlah = 0
    # contoh private var class
    __privateJumlah = 0

    def __init__(self, name, healty):
        self.nama = name
        self.hp = healty

        # variabel instance private(private variabel)
        self.__private = "Private"  # menambahkan 2 underscrore

        # variabel instance protected(protected variabel)
        self._protected = "testing"  # menambahkan 1 underscore


kagura = Hero("Kagura", 100)

print(kagura.__dict__)
# kagura.private = " Texting"  # Coba Buat Variabel baru # Adalah assigment diluar dari class bisa menambahkan diluar dari class / template

print(kagura._protected)
kagura._protected = "Uji Coba"

# variabel protected bisa di rubah nilai nya
print(kagura.__dict__)
print(kagura._protected)
# variabel protected hanya berlaku di class saja dan bisa di acsess tapi jgan di rubah nilai nya
print("=" * 7, "Private Di Class", "=" * 7)
print(Hero.__dict__)
# print(Hero._privateJumlah)
