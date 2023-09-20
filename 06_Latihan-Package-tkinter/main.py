# Latihan OOP tkinter

import tkinter

main_window = tkinter.Tk()  # class nya menggunkan huruf besar
# dan ini class nya dari package tkinter.

label1 = tkinter.Label(main_window, text="label1")
label2 = tkinter.Label(main_window, text="label2")

tombol1 = tkinter.Button(main_window, text="Klik Saya ")
tombol2 = tkinter.Button(main_window, text="Klik Saya 2")


# Menggunkan Positioning / method (fungsi)
label1.pack()  # label1 akan menaruh posisinya dirinya sendri
label2.pack()  # label1 akan menaruh posisinya dirinya sendiri
tombol1.pack()
tombol2.pack()

# Method Unutk Menampilkanya
main_window.mainloop()  # Agar Meluping Terus menerus
