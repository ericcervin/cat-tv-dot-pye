
export_frames = 0             #number of frames to export to sketch folder as pngs 
sz = 600                      #height/width/depth of the space
              
def setup():
    size(sz,sz,P3D)
    set_xyz()
    
def draw():
    global placeX, placeY, placeZ
    background(25)
    value = frameCount % 300
    translate((sin(value) * 10) + placeX, placeY, (cos(value) * 10) - placeZ)
    fill(255)
    sphere(50)
    if frameCount % 15 == 0:
        set_xyz()
    if frameCount < export_frames:
        print frameCount 
        saveFrame("output-####.png")
        
def set_xyz():
    global placeX, placeY,placeZ
    placeX = random(0,sz)
    placeY = random(0,sz)
    placeZ = random(0,sz)
    