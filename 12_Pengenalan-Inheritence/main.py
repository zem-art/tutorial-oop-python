# Belajar Inheritance (Pewarisan)

class Hero:
    def __init__(self, name, healty):
        self.nama = name
        self.bold = healty

# Tinggal Memasukan class Super ke subclass nya


# Ini Subclass nya
class Hero_intelligent(Hero):  # konsep Inheritence
    pass


class Hero_Strangth(Hero):
    pass


lily = Hero("lily", 100)
angela = Hero_intelligent("Angela", 50)
zilong = Hero_Strangth('zilong', 100)

print(lily.__dict__)
print(angela.__dict__)
print(zilong.__dict__)
