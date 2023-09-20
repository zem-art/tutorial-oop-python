# Belajar Multiple Inheritence

class A:

    def method_A(self):
        print("Ini Adalah Method A")


class B:

    def method_B(self):
        print("Ini Adalah Method B")

# Multiple Inheritence Adalah mangambil 2 buah super class


class C(A, B):
    pass


objek = C()

objek.method_A()
objek.method_B()
