#based on Visualize Superformula
#from Form+Code in Design, Art, and Architecture by Reas, etc.

export_frames = 0             #number of frames to export to sketch folder as pngs 

scaler = 125
m = 2
n1 = 18.0
n2 = 1.0
n3 = 1.0
step_list = range(64) + range(64,0,-1)

def setup():
    size(300,300)
    smooth()
    noFill()
    stroke(255)
    
def draw():
    global mm,nn1,nn2,nn3,bloom
    background(0)
    pushMatrix()
    translate(width/2,height/2)
    
    newscaler = scaler
    steps = ((frameCount % 300) % 128)
        
    for s in range(step_list[steps],0,-1):
        beginShape()
        
        mm = float(m + s)
        nn1 = float(n1 + s)
        nn2 = float(n2 + s)
        nn3 = float(n3 + s)
        newscaler = newscaler * 0.98
        sscaler = float(newscaler)
        
        points = superformula(mm,nn1,nn2,nn3)
        curveVertex(points[len(points)-1].x * sscaler, points[len(points)-1].y * sscaler)
        for i in range(len(points)):
            curveVertex(points[i].x * sscaler, points[i].y * sscaler)
        curveVertex(points[0].x * sscaler, points[0].y * sscaler)
        endShape()
    popMatrix()
    if frameCount < export_frames:
        print frameCount 
        saveFrame("output-####.png")
     
def superformula(m,n1,n2,n3):  
    numPoints = 360
    phi = float(TWO_PI / numPoints)
    points = []
    for i in range(numPoints + 1):
        points.append(superformulaPoint(m,n1,n2,n3,phi * i))
    return points

def superformulaPoint(m,n1,n2,n3,phi):
    a = 1.0
    b = 1.0
    x = 0.0
    y = 0.0
    
    t1 = float(cos(m * phi / 4) / a)
    t2 = float(abs(t1))
    t1 = float(pow(t1,n2))
    
    t2 = float(sin(m * phi / 4) / b)
    t2 = float(abs(t2))
    t2 = float(pow(t2,n3))
    
    r = float(pow(t1+t2,1/n1))
    if(abs(r) == 0):
        x = 0
        y = 0
    else:
        r = float(1/r)
        x = float(r * cos(phi))
        y = float(r * sin(phi))
    
    return PVector(x,y)    