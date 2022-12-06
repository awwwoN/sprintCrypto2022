from PIL import Image

image = Image.open("../images/trashed.png")

new_img = Image.new(image.mode, image.size)

largeur, hauteur = image.size

for x in range(hauteur):
    for y in range(largeur):
        pixel = image.getpixel((y, x))
        bits_pixel = ""
        r = pixel[0]
        div = 128
        count1 = 0
        while div >= 1:
            # print("R = ",r, "  div = ", div)
            if (r - div >= 0):
                bits_pixel += "1"
                r -= div
                count1 += 1
            else:
                bits_pixel += "0"
            div = div // 2

        v = pixel[1]
        div = 128
        while div >= 1:
            # print("V = ",v, "  div = ", div)
            if (v - div >= 0):
                bits_pixel += "1"
                v -= div
                count1 += 1
            else:
                bits_pixel += "0"
            div = div // 2

        b = pixel[2]
        div = 128
        while div >= 1:
            # print("B = ",b, "  div = ", div)
            if (b - div >= 0):
                bits_pixel += "1"
                b -= div
                count1 += 1
            else:
                bits_pixel += "0"
            div = div // 2

        if count1 % 2 == 0:
            new_img.putpixel((y, x), (255, 255, 255))
        else:
            new_img.putpixel((y, x), (0, 0, 0))

new_img.save('new_calosoma.png')
new_img.show()

image.close()
new_img.close()
