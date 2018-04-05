def setup():
  size(1200,600)  
  frameRate(6)

def owl (x, y, gray, scalar):
    pushMatrix()
    translate(x,y)
    scale(scalar)
    stroke((138 - gray), (138 - gray), (125 - gray)) #Set the color value
    strokeWeight(70)
    line(0, -35, 0, -65) #/Body
    noStroke()
    fill(255)
    ellipse(-17.5, -65, 35, 35) #Left eye dome
    ellipse(17.5, -65, 35, 35) #Right eye dome
    arc(0, -65, 70, 70, 0, PI) #Chin
    fill(51, 51, 30)
    ellipse(-14, -65, 8, 8) #Left eye
    ellipse(14, -65, 8, 8)  #Right eye
    quad(0, -58, 4, -51, 0, -44, -4, -51)#Beak
    popMatrix()






def draw ():
   background (176, 204, 226)
   for range(35, width, (60 + random(20))):
          gray = random(102)
          scalar = (0.25 + random(1.75))
          owl(i, 310, gray, scalar)
   