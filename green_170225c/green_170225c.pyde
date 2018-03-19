class Bloom(object):
    def __init__(self,temp_x,temp_y):
        blossom_spread_x = 80 #maximum width of blossom
        self.x = temp_x
        self.y = temp_y
        self.child_x = []
        self.child_y = []
        self.child_ts = []
        self.child_fill = []
        for x in range(36):
            self.child_x.append(self.x - (blossom_spread_x/2) + random(blossom_spread_x))
            self.child_y.append(self.y - 40 + random(81))
            self.child_ts.append(random(10,60))
            self.child_fill.append(random(90))
            
    def blossom(self,steps,txt):
        for x in range(steps):            
            fill(self.child_fill[x])
            textSize(self.child_ts[x])
            text(txt,self.child_x[x],self.child_y[x])
            
x = Bloom(100,100)
y = Bloom(100,200)
z = Bloom(100,300)

def setup():
    size(400,712)    
    frameRate(24)
    
    
def draw():
    global x,y,z
    if frameCount % 36 == 0:
       px = random(width); py = random(height)
       x = Bloom(px,py)
    if ((frameCount - 24) % 36) == 0:
       px = random(width); py = random(height)
       y = Bloom(px,py)
    if ((frameCount - 12) % 36) == 0:
       px = random(width); py = random(height)
       z = Bloom(px,py)   
    background(255)
    if frameCount >= 24:
        x.blossom((frameCount % 36),"x")
        y.blossom(((frameCount - 24) % 36),"y")
        z.blossom(((frameCount - 12) % 36),"z")
    
    
    #print frameCount 
    #if frameCount < 720:
    #    saveFrame("output-####.png")