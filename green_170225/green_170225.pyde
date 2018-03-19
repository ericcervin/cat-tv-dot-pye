


   
def setup():
    global back_img, front_img, x, y, x2, y2
    size(200,356)    
    frameRate(24)
    front_img = loadImage("lil_red.png")
    back_img = loadImage("green_l_blank.jpg")
    image(back_img,0,0,200,178)
    image(back_img,0,178,200,178) 
    x = random(100); y = random(90)
    x2 = random(100); y2 = random(90) + 178
    
def draw():
    global x,y,x2,y2
    if frameCount % 12 == 0:
       x = random(100); y = random(90)
       image(back_img,0,0,200,178)
    if (frameCount - 6) % 12 == 0:
       x2 = random(100); y2 = random(90) + 178
       image(back_img,0,178,200,178)
    hw = random(10,45)
    image(front_img, x + random(54), y + random(54),hw,hw)
    image(front_img, x2 + random(54), y2 + random(54),hw,hw)
    
    #print frameCount 
    #if frameCount < 144:
    #    saveFrame("output-####.png")