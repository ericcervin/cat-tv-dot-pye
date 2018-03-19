


img_list = []

def setup():
    size(540,960)
    img_list.append(loadImage("green_l00.jpg"))
    img_list.append(loadImage("green_l01.jpg"))
    img_list.append(loadImage("green_l02.jpg"))
    img_list.append(loadImage("green_l03.jpg"))
    img_list.append(loadImage("green_l04.jpg"))
    img_list.append(loadImage("green_l05.jpg"))
    img_list.append(loadImage("green_l06.jpg"))
    img_list.append(loadImage("green_l07.jpg"))
    img_list.append(loadImage("green_l08.jpg"))
    img_list.append(loadImage("green_l09.jpg"))
    img_list.append(loadImage("green_l10.jpg"))
    img_list.append(loadImage("green_l11.jpg"))
    textSize(90)
    frameRate(12)

def draw():
    image(img_list[frameCount % 12],0,0,540,960)
    print frameCount 
    if frameCount > 12:
        text('kie',190,270)
    if frameCount > 24:
        text('hap',60,80)
    if frameCount > 36:
        text('day',220,180)
    if frameCount > 48:
        text('fran',30,270)
    if frameCount > 60:
        text('py',220,80)
    if frameCount > 72:
        text('birth',15,180)
    #if frameCount < 144:
    #    saveFrame("output-####.png")