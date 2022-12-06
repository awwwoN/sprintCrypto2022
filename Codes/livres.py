#!/usr/bin/env python
from Crypto.Cipher import AES
from Crypto.Hash import SHA256, HMAC
from Crypto.Util.Padding import pad, unpad
from sys import argv
import binascii
import os

cle = argv[1].encode()
k=SHA256.new(cle).digest() # ou 'CAKE' est X
k1c=HMAC.new(k,b"fichier",SHA256).hexdigest()
k2=HMAC.new(k,b"donnees",SHA256).digest()
iv=bytes.fromhex('43414b4543414b4543414b4543414b45')

direc = os.listdir('C:/Users/hugoc/Desktop/M1 MIAGE/Semestre 1/Cryptographie et Sécurité/Crypto/Sprint/chapitre 1/livres/indices')

val = None
var = False
for x in direc:
	print(f'{x}: {x == k1c}')
	if(x == k1c):
		var = True
		val = x


if(var):
	with open('C:/Users/hugoc/Desktop/M1 MIAGE/Semestre 1/Cryptographie et Sécurité/Crypto/Sprint/chapitre 1/livres/indices/'+val, 'rb') as f:
		mcode = f.read()
	cipher=AES.new(k2,AES.MODE_CBC,iv)

	dec = unpad(cipher.decrypt(mcode),AES.block_size)

	print(dec.decode())