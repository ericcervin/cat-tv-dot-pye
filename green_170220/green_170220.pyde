def setup():
    global back_img, front_img, x, y
    size(200,356)    
    frameRate(24)
    front_img = loadImage("lil_red.png")
    back_img = loadImage("green_l_blank.jpg")
    image(back_img,0,0,200,356) 
    x = random(100); y = random(180)
    
def draw():
    global x,y
    if frameCount % 24 == 0:
       x = random(100); y = random(180)
       image(back_img,0,0,200,356)
    image(front_img, x + random(54), y + random(54),20,20)
    
    #print frameCount 
    #if frameCount < 144:
    #    saveFrame("output-####.png")