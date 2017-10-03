# Manually import code from other tabs
from Eye import Eye

def setup():
    size(640, 480, P2D)
    #~
    # Declare globals here
    global eye1, eye2 
    #~
    ellipseMode(CENTER)
    rectMode(CORNER)
    background(0)
    eye1 = Eye(PVector(0, (height/3)*1), 2)
    eye2 = Eye(PVector(0, (height/3)*2), 4)
    
def draw():
    noStroke()
    fill(0, 5)
    rect(0,0,width,height)
    eye1.run()
    eye2.run()