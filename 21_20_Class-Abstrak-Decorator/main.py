# Belajar Class Abstack (Selesai)

from abc import ABC, abstractmethod
print("\n", "=" * 5, "Belajar Class Abstak Terakhir", "=" * 5, "\n")


class Hero(ABC):

    def __init__(self, set_link):
        self.link = set_link  # Ini Getter

    @abstractmethod
    def clik(self):
        pass

    @property  # Kita buat Getter dan di gabungkan dengan abstack class
    @abstractmethod
    def link(self):
        pass


class Hero_Fighter(Hero):

    def clik(self):
        print("Go to : {}".format(self.link))  # ini Setter Dari __init__

    # self.link yg di atas adalah yg di bawah ini
    # yg di paksa di implementasikan(di terapkan) di bawah
    @Hero.link.getter
    def link(self):
        return self.__link

    @link.setter  # kenapa harus di tambahkan Hero supaya bisa di akses abstak class nya
    def link(self, input):
        self.__link = input


yuzhong = Hero_Fighter("www.Portofolio.id")

yuzhong.clik()
