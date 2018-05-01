from PIL import Image
import numpy
import scipy.misc

key1 = Image.open("key1.png")  #加密圖1
key2 = Image.open("key2.png")  #加密圖2
I = Image.open("I.png")  #加密前
E = Image.open("E.png")  #加密後
Eprime = Image.open("Eprime.png")  #解鎖圖

im.show()