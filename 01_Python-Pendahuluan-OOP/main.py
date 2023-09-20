# Belaja OOP Di Python

# Programing Paradigma(Cara Berfikir)

# 1. Struktural => Prosudural
# 2. OOP(Object Orietic Programming)

# Prosudural => Ciri Ciri nya Di eksekusi Berdasarkan Urutan

# Class / Template Memilkik 2 nilai
# 1 . Attribut ("Nama", "Power","Defence")
# 2 . Method ("Menyerang" ,"Bergerak")

class Hero:  # Template
    pass


hero1 = Hero()  # Object / Instance(Prosesnya)
hero2 = Hero()
hero3 = Hero()

hero1.nama = "Alex"
hero1.healty = 100

hero2.nama = "Sven"
hero2.healty = 200

hero3.nama = "Kasep"
hero3.healty = 1000

print(hero1.__dict__)  # Jangan lupa dict => Melihat Tipe Data nya

print(hero1.nama)
