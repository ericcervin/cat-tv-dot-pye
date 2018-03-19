#based on Simulate Particles
#from Form+Code in Design, Art, and Architecture by Reas, etc.

display_width = 180             #width of display in pixels
display_height = 320            #height of display in pixels
particle_count = 250            #number of lines in the drawing
export_frames = 0               #number of frames to export to sketch folder as pngs
life_span = 75                  #number of frames before rebirth (~60 frames/second)

particles = []

def setup():
    size(display_width,display_height)
    smooth()
    birth()
        
def draw():
    background(255)
    for i in range(len(particles)):
           particles[i].update()
           particles[i].draaw()
           
    if frameCount < export_frames:
        print frameCount 
        saveFrame("output-####.png")
        
    if frameCount % life_span == 0: birth()
        
def birth():
    global particles
    particles = []
    start_x = random(width * 0.25,width * 0.75)
    start_y = random(height-75,height-25)
    for i in range(particle_count):
        particles.append(Particle(PVector(start_x,start_y)))
         
class Particle(object):
    loc = PVector()
    vel = PVector()
    acc = PVector()
    
    hist = []
        
    def __init__(self,l):
        global vel,acc,loc
        self.randmin = -HALF_PI
        self.randmax = 0
        
        self.counter = 0
        
        self.r = random(0,TWO_PI)
        self.x = cos(self.r)
        self.y = sin(self.r)
        self.acc = PVector(self.x/15,self.y/15)#PVector(self.x/250,self.y/250)
        
        self.q = random(0,1)
        self.r= random(self.randmin,self.randmax)
        self.x = cos(self.r) * self.q
        self.y = sin(self.r) * self.q
        self.vel = PVector(self.x,self.y)
        self.loc = l.get()
        self.hist = []
    
    #update location
    def update(self):
        self.vel.add(self.acc)
        self.loc.add(self.vel)
        #save locations every 10 frames
        if ((frameCount % 10 == 0) and (self.counter < particle_count)):
            self.hist.append(self.loc.get())
            self.counter += 1
    
    #draw particle
    def draaw(self):
        fill(100,50)
        noFill()
        #draw history path
        stroke(0,100)
        beginShape()
        for i in range(self.counter):
            vertex(self.hist[i].x,self.hist[i].y)
        if (self.counter > 0): vertex(self.loc.x,self.loc.y)
        endShape()
        