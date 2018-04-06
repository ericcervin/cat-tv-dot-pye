#made while translating pg159 
#from Getting Started With Processing" 2nd ed.

buglist = [];

class JitterBug ():
  def __init__(self,temp_x, temp_y, temp_diameter):
    self.x = temp_x
    self.y = temp_y
    self.diameter = temp_diameter
    self.speed = 2.5

  def move(self):
    self.x += ((-1 * self.speed) + (2 * random(self.speed)))
    self.y += ((-1 * self.speed) + (2 * random(self.speed)))
  
  def display(self):
    ellipse(self.x, self.y, self.diameter, self.diameter);
  

def setup():
  size(1200,600)
  background(0)
  fill(255,32)
  for i in range(33):
    buglist.append(JitterBug(random(width),random(height), i))

def draw():
   for i in buglist:
     i.move()
     i.display()                                