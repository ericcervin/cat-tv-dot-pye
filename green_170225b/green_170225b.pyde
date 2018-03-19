class Bloom(object):
    def __init__(self,temp_x,temp_y):
        self.x = temp_x
        self.y = temp_y
        self.child_x = []
        self.child_y = []
        self.child_ts = []
        self.child_fill = []
        for x in range(24):
            self.child_x.append(self.x - 27 + random(54))
            self.child_y.append(self.y - 27 + random(54))
            self.child_ts.append(random(10,40))
            self.child_fill.append(random(90))
            
    def blossom(self,steps):
        for x in range(steps):            
            fill(self.child_fill[x])
            textSize(self.child_ts[x])
            text("*",self.child_x[x],self.child_y[x])
            
x = Bloom(100,100)
y = Bloom(100,200)
z = Bloom(100,300)

def setup():
    size(200,356)    
    frameRate(24)
    
    
def draw():
    global x,y,z
    if frameCount % 24 == 0:
       px = random(200); py = random(356)
       x = Bloom(px,py)
    if ((frameCount - 16) % 24) == 0:
       px = random(200); py = random(356)
       y = Bloom(px,py)
    if ((frameCount - 8) % 24) == 0:
       px = random(200); py = random(356)
       z = Bloom(px,py)   
    background(255)
    if frameCount >= 12:
        x.blossom(frameCount % 24)
        y.blossom((frameCount - 12) % 24)
        z.blossom((frameCount - 8) % 24)
    
    
    #print frameCount 
    #if frameCount < 144:
    #    saveFrame("output-####.png")