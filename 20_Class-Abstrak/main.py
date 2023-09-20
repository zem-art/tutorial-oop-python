# Belajar Class Abstrak
# abc => abstack base class
# Modul Dari python nya
from abc import ABC, abstractmethod

print("\n", "=" * 5, "Belajar Class Abstak", "=" * 5, "\n")

# === READ ME === +++ PLEASE +++

# Class Biasa intence nya => Objeck
# implementsikan Dgn inheritance menggunkan Super Class

# Class Abstak instence Nya =>  Class

# 1 .  Memaksa class untuk mengimplementasikan method nya Menjadi class
# 2 . CLass Abstak Tidak Bisa di Implementasikan method nya menjadi Objeck
# 3 Abstak Class mengimplementasikan dari class menjadi class

# Contoh Class Abstak
print("=== Contoh Class Abstak===")


class Button(ABC):  # inherit dia dari ABC / Abstack base class

    @abstractmethod  # kita taruh decorator dari ABC trsbt
    def clik(self):
        pass


class PushBotton(Button):
    # memaksa untuk Mengimplementasikan method dari class Button
    def clik(self):
        print("Push Button Clik")


class RadioButton(Button):
    def clik(self):
        print("Select To")


# Instanya
tombol = PushBotton()
tombol1 = RadioButton()

tombol.clik()
tombol1.clik()
# help(tombol)
