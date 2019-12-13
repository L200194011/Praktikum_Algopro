from tkinter import *

my_app=Tk(className="Data Diri")

L1=Label(my_app, text="Bangun Segitiga", font=('arial',30))
L1.grid(row=0, column=0)

L2=Label(my_app, text="Segitiga atau segi tiga (bahasa Inggris: triangle) adalah nama suatu bentuk yang dibuat dari tiga sisi yang berupa garis lurus dan tiga sudut. \nMatematikawan Euclid yang hidup sekitar tahun 300 SM menemukan bahwa jumlah ketiga sudut di suatu segi tiga pada bidang datar adalah 180 derajat.\nHal ini memungkinkan kita menghitung besarnya salah satu sudut bila dua sudut lainnya sudah diketahui.")
L2.grid(row=1, column=0)

L3=Label(my_app, text="Panjang Alas :")
L3.grid(row=2, column=0)

num1 = StringVar()
E3=Entry(my_app,textvariable=num1)
E3.grid(row=2, column=1)

L4=Label(my_app, text="Panjang Tinggi :")
L4.grid(row=3, column=0)

num2 = StringVar()
E3=Entry(my_app,textvariable=num2)
E3.grid(row=3, column=1)

res = StringVar()
def wewe():
    hitung=float(num1.get()) * float(num2.get()) / 2
    res.set(hitung)
    if (hitung == int(hitung)):
        hitung = int(hitung)
    return hitung

B=Button(my_app, text="Hitung", command=wewe)
B.grid(row=6, column=0)

L5 = Label(my_app, text="Luas =")
L5.grid(row=7, column=0)

result = Entry(my_app,textvariable=res)
result.grid(row=7, column=1)

my_app.mainloop()