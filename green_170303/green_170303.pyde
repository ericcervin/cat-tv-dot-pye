text_array = ["x","o","*"]                   #text that will be used to compose the 3 blooms

class Bloom(object):
    def __init__(self,temp_x,temp_y):
        max_blossom_spread_x = 80            #maximum width of blossom in pixels
        max_blossom_spread_y = 80            #maximum height of blossom in pixels
        
        max_text_size = 40                   #maximum size for char that is each "petal". 
                                             #No minimum.
                                             
        min_text_lightness = 55              #minimum lightness for char that is each "petal".
        max_text_lightness = 200             #maximum lightness for char that is each "petal". 
                                             #0 = pure black. 255 = pure white
                                             
        self.x = temp_x
        self.y = temp_y
        self.child_x = []
        self.child_y = []
        self.child_ts = []
        self.child_fill = []
        for x in range(36):
            self.child_x.append(self.x - (max_blossom_spread_x/2) + random(max_blossom_spread_x))
            self.child_y.append(self.y - (max_blossom_spread_y/2) + random(max_blossom_spread_y))
            self.child_ts.append(random(max_text_size))
            self.child_fill.append(random(min_text_lightness,max_text_lightness))
            
    def blossom(self,steps,txt):
        for x in range(steps):          
            if mousePressed == True:
                fill(255 - self.child_fill[x])
            else:
                fill(self.child_fill[x])  
            textSize(self.child_ts[x])
            text(txt,self.child_x[x],self.child_y[x])
            
x = Bloom(100,100)
y = Bloom(125,125)
z = Bloom(150,150)

def setup():
    size(400,712)    
    frameRate(24)
    
    
def draw():
    global x,y,z
    if frameCount % 36 == 0: x = Bloom(random(width),random(height))
    if ((frameCount - 24) % 36) == 0: y = Bloom(random(width),random(height))
    if ((frameCount - 12) % 36) == 0: z = Bloom(random(width),random(height))
    
    if mousePressed == True:
        background(0)
    else:
        background(255)
        
    if frameCount >= 24:
        x.blossom((frameCount % 36),text_array[0])          
        y.blossom(((frameCount - 24) % 36),text_array[1])
        z.blossom(((frameCount - 12) % 36),text_array[2])
    
    
    #print frameCount 
    #if frameCount < 744:
    #    saveFrame("output-####.png")