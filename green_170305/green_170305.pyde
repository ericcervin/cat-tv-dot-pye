text_array = ["j","a","s","p","e","r"]       #text that will be used to compose each blossom. 
                                             #please use a factor of 36 texts (1,2,3,4,6,9,12,18,36)   #captainObvious                                                                  

display_width = 400                          #width of the display window
display_height = 712                         #height of the display window
export_frames = 0                            #number of frames to export to sketch folder as pngs

bloom_list = []
bloom_spread = 36/len(text_array)

class Bloom(object):
    def __init__(self,temp_x,temp_y,age):
        max_blossom_spread_x = 80            #maximum width of blossom in pixels
        max_blossom_spread_y = 80            #maximum height of blossom in pixels
        
        max_text_size = 40                   #maximum size for char that is each "petal". 
                                             #No minimum.
                                             
        min_text_lightness = 55              #minimum lightness for char that is each "petal".
        max_text_lightness = 200             #maximum lightness for char that is each "petal". 
                                             #0 = pure black. 255 = pure white
                                             
        self.x = temp_x
        self.y = temp_y
        self.age = age
        self.child_x = []
        self.child_y = []
        self.child_ts = []
        self.child_fill = []
        for x in range(36):
            self.child_x.append(self.x - (max_blossom_spread_x/2) + random(max_blossom_spread_x))
            self.child_y.append(self.y - (max_blossom_spread_y/2) + random(max_blossom_spread_y))
            self.child_ts.append(random(max_text_size))
            self.child_fill.append(random(min_text_lightness,max_text_lightness))
            
    def blossom(self,txt):
        for x in range(self.age + 1):          
            if mousePressed == True:
                fill(255 - self.child_fill[x])
            else:
                fill(self.child_fill[x])  
            textSize(self.child_ts[x])
            text(txt,self.child_x[x],self.child_y[x])
            


def setup():
    size(display_width,display_height)    
    frameRate(24)
    for x in range(36):
        if x % bloom_spread == 0:
            bloom_list.append(Bloom(100,100,x))
        else:
            bloom_list.append("_")
    #print bloom_list
    
    
def draw():
    
    if mousePressed == True:
        background(0)
    else:
        background(255)
            
    for x in range(36):
        if x % bloom_spread == 0:
            bloom_list[x].blossom(text_array[x/bloom_spread])
            bloom_list[x].age += 1
            if bloom_list[x].age > 35:
                bloom_list[x] = Bloom(random(width),random(height),0)
    
    if frameCount < export_frames:
        print frameCount 
        saveFrame("output-####.png")