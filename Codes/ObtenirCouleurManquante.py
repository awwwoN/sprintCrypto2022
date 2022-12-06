#!/usr/bin/env python3
from PIL import Image

img=Image.open('/home/o2181698@campus.univ-orleans.fr/Bureau/CryptoSprint2022/img/otr.png').convert('RGB')
outputFolder="/home/o2181698@campus.univ-orleans.fr/Bureau/CryptoSprint2022/img/rgb/"
outputFile='otr'

w,h=img.size
maskR=Image.new('L', (w, h), color = 255)
maskG=Image.new('L', (w, h), color = 255)
maskB=Image.new('L', (w, h), color = 255)

def unsteg(x):
    return 255*(x%2)

for y in range(h):
    for x in range(w):
        (r,g,b)=img.getpixel((x,y))
        maskR.putpixel((x,y), unsteg(r))
        maskG.putpixel((x,y), unsteg(g))
        maskB.putpixel((x,y), unsteg(b))
maskR.save(outputFolder+outputFile+'_rouge.png')
maskG.save(outputFolder+outputFile+'_vert.png')
maskB.save(outputFolder+outputFile+'_bleu.png')
