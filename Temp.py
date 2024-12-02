from PIL import Image,ImageOps,ImageDraw

im = Image.open(r"E:\Pictures\photo_2023-09-16_20-56-30.jpg")
im=ImageOps.grayscale(im)
im=ImageOps.equalize(im)


dicew=110
dicesize=int(im.width/dicew)
diceh= int(im.height / dicesize)

print (dicesize,diceh)

nim = Image.new("L",(im.width,im.height),"white")
nimd=ImageDraw.Draw(nim)
DiceCount = 0
print("you will need ",DiceCount,"Dices")

for y in range (0,im.height-dicesize,dicesize):
    for x in range( 0,im.width-dicesize,dicesize):
        thisSectorColor=0
        for dicex in range (0,dicesize):
            for dicey in range (0,dicesize):
                thisColor = im.getpixel((x+dicex,y+dicey))
                thisSectorColor+=thisColor
        thisSectorColor= int(thisSectorColor/dicesize**2)
        nimd.rectangle([(x,y),(x+dicesize,y+dicesize)],thisSectorColor)
        dicenumber = int ((255-thisSectorColor)*5/255+1)
        DiceCount+=1
        if dicenumber == 1:
            dicenumber = " . "
        if dicenumber == 2:
            dicenumber=" : "
        if dicenumber == 3:
            dicenumber = ":. "
        if dicenumber == 4:
            dicenumber=": :"
        if dicenumber == 5:
            dicenumber=":.:"
        if dicenumber == 6:
            dicenumber=":::"    

        print (dicenumber,end="")
    print("")
    
