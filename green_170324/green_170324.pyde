#based on Repeat: Recursive Tree
#from Form+Code in Design, Art, and Architecture by Reas, etc.

dotSize = 8                              #size of starting dot to taper from
display_width = 400                      #width of the display window
display_height = 700                     #height of the display window
export_frames = 0                       #number of frames to export to sketch folder as pngs
frame_rate = 8                           #frames/second

def setup():
    global angleOffsetA, angleOffsetB
    size(display_width,display_height)
    noStroke()
    
    frameRate(frame_rate)
    
    angleOffsetA = radians(1)
    angleOffsetB = radians(30)
    
def draw():
    r = random(0,1.0)
    if r < 0.08:
        fill(0)
        background(255)
    else:
        fill(255)
        background(0)
    
    translate(width/1.1,height)
    seed1(dotSize,radians(270),0,0)
    
    if frameCount < export_frames:
        print frameCount 
        saveFrame("output-####.png")

def seed1(dotSize, angle, x, y):
    global angleOffsetA, angleOffsetB
    if dotSize > 1.0:
        r = random(0,1.0)
        if r > 0.02:
            ellipse(x,y,dotSize,dotSize)
            newx = x + cos(angle) * dotSize
            newy = y + sin(angle) * dotSize
            seed1(dotSize * 0.99, angle - angleOffsetA,newx,newy)
        else:
            ellipse(x,y,dotSize,dotSize)
            newx = x + cos(angle)
            newy = y + sin(angle)
            seed2(dotSize * 0.99, angle + angleOffsetA,newx,newy)
            seed1(dotSize * 0.60, angle + angleOffsetB,newx,newy)
            seed2(dotSize * 0.50, angle - angleOffsetB,newx, newy)
            
def seed2(dotSize, angle, x, y):
    global angleOffsetA, angleOffsetB
    if dotSize > 1.0:
        r = random(0,1.0)
        if r > 0.05:
            ellipse(x,y,dotSize,dotSize)
            newx = x + cos(angle) * dotSize
            newy = y + sin(angle) * dotSize
            seed2(dotSize * 0.99, angle + angleOffsetA,newx,newy)
        else:
            ellipse(x,y,dotSize,dotSize)
            newx = x + cos(angle)
            newy = y + sin(angle)
            seed1(dotSize * 0.99, angle + angleOffsetA,newx,newy)
            seed2(dotSize * 0.60, angle + angleOffsetB,newx,newy)
            seed1(dotSize * 0.50, angle - angleOffsetB,newx, newy)
            
            