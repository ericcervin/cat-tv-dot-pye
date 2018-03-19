max_population  = 3                          #max number of letters that will appear on the screen at once                
                                             #please use a factor of 36 (1,2,3,4,6,9,12,18,36)   #captainObvious                    

display_width = 200                          #width of the display window
display_height = 356                         #height of the display window
export_frames = 0                            #number of frames to export to sketch folder as pngs

letter_list = []
chr_val = 97
letter_spread = 36/max_population

class LetSplash(object):
    def __init__(self,temp_x,temp_y,temp_age,temp_chr):
                                             
        min_circ_lightness = 55              #minimum lightness for each circle
        max_circ_lightness = 200             #maximum lightness for each circle
                                             #0 = pure black. 255 = pure white
                                             
        max_circ_diameter = 100              #maximum diameter of circles around each letter
                                             
        self.x = temp_x
        self.y = temp_y
        self.char = temp_chr
        self.age = temp_age
        self.child_diameter = []
        self.child_hue = []
        for x in range(36):
            self.child_diameter.append(random(25,max_circ_diameter))
            self.child_hue.append(random(min_circ_lightness,max_circ_lightness))
            
    def render(self):
        textSize(20)
        if mousePressed == True:
            fill(255)
        else:
            fill(0)
        textMode(CORNER)
        text(self.char,self.x-5,self.y+5)
        
        noFill()
        strokeWeight(2)
        ellipseMode(CENTER)
        for x in range(self.age + 1):          
            if mousePressed == True:
                stroke(255 - self.child_hue[x])
            else:
                stroke(self.child_hue[x])  
            ellipse(self.x,self.y,self.child_diameter[x],self.child_diameter[x]) 
            


def setup():
    global chr_val
    size(display_width,display_height)    
    frameRate(24)
    for x in range(36):
        if x % letter_spread == 0:
            letter_list.append(LetSplash(random(display_width),random(display_height),x,chr(chr_val)))
            chr_val += 1
        else:
            letter_list.append("_")
    #print bloom_list
    
    
def draw():
    global chr_val
    if mousePressed == True:
        background(0)
    else:
        background(255)
            
    for x in range(36):
        if x % letter_spread == 0:
            letter_list[x].render()
            letter_list[x].age += 1
            if letter_list[x].age > 35:
               letter_list[x] = LetSplash(random(width),random(height),0,chr(chr_val))
               chr_val += 1
               if chr_val > 122: chr_val = 97
    
    if frameCount < export_frames:
        print frameCount 
        saveFrame("output-####.png")