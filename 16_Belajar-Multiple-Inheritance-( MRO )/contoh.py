class Team:  # CLass Super

    def setTeam(self, team):
        self.tim = team

    def showTeam(self):
        print(self.tim)


class Tipe_Hero:  # Super Class

    def setTipe(self, tipe):
        self.kategori = tipe

    def showTipe(self):
        print(self.kategori)


class Hero(Team, Tipe_Hero):  # Sub Class Dari Class yg Di atas

    def __init__(self, name, healty):
        self.nama = name
        self.hp = healty


Bruno = Hero("Bruno", 100)  # Dia Berperan Sebagai Sub Class

Bruno.setTeam("Biru")  # Dia Berperan Sebagai Super Class TEAM
Bruno.setTipe("Marskman")  # Dia Berperan Sebagai Super Class Tipe

Bruno.showTeam()
Bruno.showTipe()
