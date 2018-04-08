imgs = []
rates = [1,6,12,24,60]

frame_counter = 0
rate_counter = 0


def setup():
  global imgs;
  imgs.append(loadImage("dog.jpg"))
  imgs.append(loadImage("bird.jpg"))
  size(350,350)
  frameRate(rates[rate_counter]) 


def draw():  
  global frame_counter;
  background(0)
  image(imgs[frame_counter],0,0,330,330) 
  frame_counter += 1
  if (frame_counter > len(imgs) - 1):
    frame_counter = 0
    
  fill(255)
  text(str(rates[rate_counter]) + " frames/second. (click to change)",5,350);


def mouseClicked():
  global rate_counter;
  rate_counter += 1
  if (rate_counter > (len(rates) - 1)):
    rate_counter = 0
  frameRate(rates[rate_counter]) 