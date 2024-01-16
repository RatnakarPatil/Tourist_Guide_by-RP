# # import TGWebsite as webb
# #
# # print("\nEnter The Type Of Trip U Want:")
# # print("\n1.Family trip \n2.Friend trip \n3.Bussiness Trip \n4.Couples Trip \n5.Religious Trip \n6.Solo Trip\n")
# # n = int(input())
# from tkinter import *
# from PIL import Image, ImageTk
# root = Tk()
# root.geometry("516x623")
# root.title("MAIN FRAME")                                                                                                                                                    # extra
# main_frame = Frame(root)
# main_frame.pack(expand=1, fill=BOTH)
# Label(main_frame, text=" l- Tourist Guide -l", font="Calibri 50 bold",
#       fg="white", bg="black").pack(padx=10, pady=10)
# image = Image.open("zTGlogo.png")
# image = image.resize((120, 100), Image.LANCZOS)
# photo = ImageTk.PhotoImage(image)
# Label(main_frame, image=photo).pack()
#
# root.mainloop()

# physics PBL
from cmath import log
import math
from matplotlib import pyplot as plt
import array as arr
import numpy as np

k = 1.380649*10**-23
ks = 11.8
h = 6.626176*10**-34
me = 9.1*10**-31
mh = 17.945*10**-32
t = 300
q = 1.6*10**-19
eg = 1.12
enout = 8.8541878128*10**-12


na = float(input("na-"))
nd = float(input("nd-"))
print("~~~~~~~~~~")
# a = 2*3.14*me*k*t
# a1 = a**1.5
# a2 = a1/h**3
# nc = a2*2
nc = 2.8*10**19
print("nc-",nc)

# c = 2*3.14*mh*k*t
# c1 = c**1.5
# c2 = c1/h**3
# nv = c2*2
nv = 1.04*10**19
print("nv-",nv)

d = nc*nv
d4 = d**0.5
d1 = -k*t
d5 = d1/q
d2 = eg/d5
d3 = 2.718**d2
d6 = d3**0.5
ni = d6*d4
# ni = 2030000
print("ni-",ni)

b = na*nd
b1 = ni**2
b2 = (b/b1)
b3 = log(b2)
b4 = b3*k*t
vbi = b4/q
print("vbi-",vbi)


e = 2*ks*enout*nd*vbi
e1 = q*na
e2 = (na+nd)
e3 = e1*e2
e4 = e/e3
xp = e4**0.5
print("xp-",xp)

f = 2*ks*enout*na*vbi
f1 = q*nd
f2 = (na+nd)
f3 = f1*f2
f4 = f/f3
xn = f4**0.5
print("xn-",xn)


x = xp + xn

g = q*na
g1 = x
g2 = g1**2
g3 = g*g2
g4 = 2*ks*enout
vxn = g3/g4
print("potential at xp-",vxn)


h = -q*na*x
h1 = h/enout
print("electric field",h1)


i = enout*vbi*2*ks
i1 = 1/na
i2 = 1/nd
i3 = i2+i1
i4 = i3*i
i5 = i4/q
i6 = i5**0.5
print("deplitation width(W)",i6)
