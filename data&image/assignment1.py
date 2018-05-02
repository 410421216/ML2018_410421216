import PIL
from PIL import Image
import numpy
import scipy.misc
import random

#key1 = Image.open("key1.png")  #加密圖1
#key2 = Image.open("key2.png")  #加密圖2
#I = Image.open("I.png")  #加密前
#E = Image.open("E.png")  #加密後
#Eprime = Image.open("Eprime.png")  #解鎖圖

#print (key1.format, key1.size, key1.mode)
#print (key2.format, key2.size, key2.mode)
#print (I.format, I.size, I.mode)
#print (E.format, E.size, E.mode)
#print (Eprime.format, Eprime.size, Eprime.mode)

key1 = numpy.array(Image.open("key1.png"))

#print (key1)  #test

key2 = numpy.array(Image.open("key2.png"))
I = numpy.array(Image.open("I.png"))
E = numpy.array(Image.open("E.png"))
Eprime = numpy.array(Image.open("Eprime.png"))

#print (key1[0][1])  #test

epoch = 1
MaxlterLimit = 100

w1 = numpy.array([random.uniform(-1,1),random.uniform(-1,1),random.uniform(-1,1)])
w2 = numpy.zeros(3,dtype = 'float')

while epoch == 1 or (epoch < MaxlterLimit and (abs(w2[0] - w1[0]) > 0.00000001 and abs(w2[1] - w1[1]) > 0.00000001 and abs(w2[2] - w1[2]) > 0.00000001)):
    
    w2[0] = w1[0]
    w2[1] = w1[1]
    w2[2] = w1[2]
    
    for i in range(0,300):
        for j in range(0,400):
            a = w1[0] * key1[i][j] + w1[1] * key2[i][j] + w1[2] * I[i][j]
            e = E[i][j] - a
            w1[0] = w1[0] + 0.00001 * e * key1[i][j]
            w1[1] = w1[1] + 0.00001 * e * key2[i][j]
            w1[2] = w1[2] + 0.00001 * e * I[i][j]
            
    epoch += 1
    print (epoch)

print (epoch,w2[0],w2[1],w2[2])

ansimg = numpy.zeros((300,400),dtype = 'float')

for i in range(0,300):
    for j in range(0,400):
        ansimg[i][j] = (Eprime[i][j] - w2[0] * key1[i][j] - w2[1] * key2[i][j])/w2[2]

scipy.misc.imsave('answer.png',ansimg)