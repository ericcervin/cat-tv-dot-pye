
text_array = ["n","o","i","s","e","l","i","f","e"]    #text that will appear in each splash. 
                                                      #please use a factor of 36 texts (1,2,3,4,6,9,12,18,36)   #captainObvious                  

display_width = 1200                        #width of the display window
display_height = 600                        #height of the display window

letter_list = []
letter_spread = 36/len(text_array)


min_circ_lightness = 55             #minimum lightness for each circle
max_circ_lightness = 200            #maximum lightness for each circle
                                            #0 = pure black. 255 = pure white
                                             
max_circ_diameter = 100            #maximum diameter of circles around each letter


class LetSplash():
        def __init__ (self,temp_x,temp_y,temp_age,temp_chr):                                     
            self.x = temp_x
            self.y = temp_y
            self.char = temp_chr
            self.age = temp_age
            self.child_diameter = []
            self.child_hue = []
            for i in range(36):
                self.child_diameter.append(random(25,max_circ_diameter))
                self.child_hue.append(random(min_circ_lightness,max_circ_lightness))
            

        def render(self):
            textSize(20)
            if (mousePressed):
               fill(255)
            else: 
               fill(0)
            rectMode(CORNER)
            text(self.char,self.x-5,self.y+5)
        
            noFill()
            strokeWeight(2)
            ellipseMode(CENTER)
            for i in range(self.age + 1):         
                if (mousePressed):
                    stroke(255 - self.child_hue[i])
                else:
                    stroke(self.child_hue[i])
            
                ellipse(self.x,self.y,self.child_diameter[i],self.child_diameter[i])

def setup():
    size(display_width,display_height)    
    frameRate(24)
    for i in range(36):
        if ((i % letter_spread) == 0):
            letter_list.append(LetSplash(random(display_width),random(display_height),i,text_array[(i / letter_spread)]))
        else:
            letter_list.append("_")
    
def draw():
    if (mousePressed):
        background(0)
    else:
        background(255)
            
    for i in range(36):
        if ((i % letter_spread) == 0):
            letter_list[i].render()
            letter_list[i].age += 1
            if (letter_list[i].age > 35):
               letter_list[i] = LetSplash(random(width),random(height),0,text_array[(i / letter_spread)])