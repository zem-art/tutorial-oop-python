# Belajar magic Method
print("\n", "=" * 5, "Belajar Magic Method", "=" * 5, "\n")


class Mangga:
    # Magic Method
    def __init__(self, name, jumlah):
        self.nama = name
        self.price = jumlah

    def __repr__(self):  # Repr Apabila Programnya Belum Jadi makan Dia Untuk DEBUGGING
        return "Dari Reppert : Buah : {} dengan Jumlah : {}".format(self.nama, self.price)

    def __str__(self):  # Str Apabila Programnya sudah Jadi , Maka Dia Akan Di Jalan Kan
        return "Buah : {} dengan Jumlah : {}".format(self.nama, self.price)

    def __add__(self, objek):  # Add untuk Menambah kan suatu angka di dalam class
        return self.price + objek.price

    @property
    def __dict__(self):  # Menggunakan dict Harus Menambahkan @properti dia atas nya
        return "Objeck Ini Mempunyai Nama Dan Jumlah"


belanja = Mangga("Pisang", 8)
belanja1 = Mangga("Mangga", 10)

# Cara Memanggil Repr
print(repr(belanja))
print(repr(belanja1))
print("="*50)
# Cara Memanggil Str
print(belanja)
print(belanja1)
print("="*50)
# Cara Memanggil Magic Method Add
print('Jumlah Buah', belanja.nama, "Ditambah Jumlah Buah",
      belanja1.nama, 'Hasil Nya', belanja + belanja1)
print('='*50)
# Cara menggunakan dict
print(belanja.__dict__)
