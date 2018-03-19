planet_count = 9                            # number of planets in system

display_width = 200                          #width of the display window
display_height = 356                         #height of the display window
export_frames = 0                            #number of frames to export to sketch folder as pngs




class planetoid():
    def __init__(self,temp_x,temp_y,temp_o_rate,temp_p_diameter):
        self.x = temp_x
        self.y = temp_y
        self.o_rate = temp_o_rate
        self.p_diameter = temp_p_diameter
        self.o_diameter = self.p_diameter + (self.p_diameter * random(1,4))
        
    def render(self):
        
        noFill()
        stroke(random(100,255))
        ellipse(self.x,self.y,self.o_diameter,self.o_diameter)
        
        fill(random(100,255),random(100,255))
        ellipse(self.x,self.y,self.p_diameter,self.p_diameter)
        
        ht = self.y + (sin(radians(frameCount * self.o_rate)) * (self.o_diameter/2)) 
        wt = self.x + (cos(radians(frameCount * self.o_rate)) * (self.o_diameter/2))
        fill(random(100,255),random(100,255))
        ellipse(wt,ht,10,10)

def populate_system():
    global planet_system
    planet_system = []
    for x in range(planet_count):
        planet_system.append(planetoid(random(width),random(height),random(4,24),random(15,30)))
    

def setup():
    frameRate(24)
    size(display_width,display_height)
    populate_system()
    
def draw():
    background(0)
    
    for x in range(planet_count):
        planet_system[x].render()
    
    if frameCount % 24 == 0:
        populate_system()
        
    if frameCount < export_frames:
        print frameCount 
        saveFrame("output-####.png")
    
    