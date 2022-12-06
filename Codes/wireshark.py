from Cryptodome.Util.strxor import strxor


b1 = bytes.fromhex("4c6e34b68ede1e438d81cb0c7d4695c16d10ffef031e3d50e8b6b3ab7f242adef1487d2b05b8132e3ab4fa61713226fcf444827648ef225f8417c9b542a2e0027e4769c1692ac0d6f6fdad2490d6e998a545fb37cacc2c47149a410160df348b240745aca07b54d936dc53de276f3f4e61ccb4820d25b0e80b06e1fd162137e4")
b2 = bytes.fromhex("ba9c71a8d3b154df5855cc2e784180a6fd39c2f70d6ed548a7e0efb727ef448be52af85da4728952395dd33048f4b41777b1cec99e6b0b525d28fe6388ee57662ec669")
b3 = bytes.fromhex("ba9c71a8d3b154df5955cf29721498e39c21ceb40427d54fa1fee3bb3ab74497a338bc09b733df06daafdc7511b012cd60f29b7c5c785f511c68b3")
b4 = bytes.fromhex("ba9c71a8d3b154df554fcb64361431069c33c4e60b27d54fadade8bd3cfe16dde52fb04af122d81599b2d7735af4fc12")
b5 = bytes.fromhex("ba9c71a8d3b154dfd9bdc3647af75ae8d975683448379b4ee8fde3b52cbb1398e679b641b834d0003973d73e119eb44470e88779196e4e474133ee39")

a1 = bytes.fromhex("1783cf6945abe7856a1b5adc7cea44d425f7fc8c85612f19ac2d0060696de41d5427b889d1fe93ab00a09b8eed6a95e40b10936ea807fd004421725a20093f8b941b5e60125ed5545fb94461b4289f206aa019fa673ded878f87e3bbac970fad8c71d14c18a14d637fce8cd5d8386b0f3880f0e1ff530ac2a668afac158bafc4")
a2 = bytes.fromhex("ba9c71a8d3b154df9523ff29b40bdfac7841b8b48482312c2fa3cf80132617e421b8e6846fbee8d43856f133e6f05c3bc7c58e5ff6e77e32426cca93e3")
a3= bytes.fromhex('ba9c71a8d3b154df9537e17cac0cf4ae7b06fcb4a88d7d2735bec38849761bea64e9e6a16ffba964bf43a331f2f4fcfa82da')
a4=bytes.fromhex('ba9c71a8d3b154df8736e739ae4feeef3a0bbef1b89f702123ff8ea60f2654ad0dbae68c3abae862f117b236f2ec5473c08c995fedfb6f770d')
a5=bytes.fromhex('ba9c71a8d3b154df8a23fa2fb34eb0ae7508b9f8aecc652d2ba1ddc9036355f921f6b4946eafba76ef52a370')
a6=bytes.fromhex('ba9c71a8d3b154df8811c1129262de815726cad588a95c0b0192fca4344f31c164eaebd83ab1ef76f617a52ce8f749900bc52099fea7')

tb = min(len(b1),len(b2))
ta = min(len(a5),len(a6))


eb = strxor(b1[:tb],b2[:tb])
ea = strxor(a5[:ta],a6[:ta])


m1xorm2 = eb[8:]
m2xorm3 = ea[8:]

def helpme(prefixe):
    return strxor(m1xorm2[:len(prefixe)], prefixe), len(m1xorm2)-len(prefixe)

def helpme2(prefixe):
    return strxor(m2xorm3[:len(prefixe)], prefixe), len(m2xorm3)-len(prefixe)

#print(helpme(b"Bonjour Alice, comment vas-tu ? "))
#print(helpme(b"Comme je te le disais, j'ai fait"))

#print(helpme2(b"Salut Bob ! On dirait bien que"))

#print(helpme2(b"Sur l'image calosoma.png ? Tu as trf "))

print(helpme2(b"Attends, j'essaie. Oh ! Il y a un ca"))

print(helpme2(b"Laisse-moi le temps de te rattraper"))