#based on Parameterize Waves
#from Form+Code in Design, Art, and Architecture by Reas, etc.

display_width = 400            #width of display in pixels
display_height = 680           #height of display in pixels
export_frames = 0              #number of frames to export to sketch folder as pngs
frame_rate = 12                 #frames/second
perc_rev_bar = 8               #percentage of bars that are reversed
perc_rev_frame = 8             #percentage of frames that are reversed

brickWidth = 20                
brickHeight = 7                
cols = display_width / 30                         
rows = display_height / 16               
columnOffset = 30              
rowOffset = 15                
rotationIncrement = 0.15

def setup():
    size(display_width,display_height)
    stroke(0)
    frameRate(frame_rate)
    
def draw():
    rnd = random(0,1.0)
    if rnd >= ((1/100.0)*perc_rev_frame):
        fore_c = 0
        back_c = 255
    else:
        fore_c = 255
        back_c = 0
    background(back_c)
    translate(30,30);
    for i in range(cols):
        pushMatrix()
        translate(i * columnOffset, 0)
        r = random(-QUARTER_PI,QUARTER_PI)
        dir = 1
        for j in range(rows):
            pushMatrix()
            translate(0,rowOffset * j)
            rotate(r)
            rnd = random(0,1.0)
            if rnd >= ((1/100.0)*perc_rev_bar):
                fill(back_c)
            else:
                fill(fore_c)
            rect(-brickWidth/2,-brickHeight/2,brickWidth,brickHeight)
            popMatrix()
            r += dir * rotationIncrement
            if (r > QUARTER_PI) or (r < -QUARTER_PI):
                dir *= -1
        popMatrix()
        
    if frameCount < export_frames:
        print frameCount 
        saveFrame("output-####.png")
        