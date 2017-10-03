def setup():
    size(640, 480, P2D)
    ellipseMode(CENTER)
    global foo1, foo2 
    foo1 = Foo()
    foo2 = Foo()
    foo2.p.y = (height/3)*2
    foo2.speed *= 2
    
def draw():
    background(0)
    foo1.run()
    foo2.run()
    
class Foo(object):
    def __init__(self):
        self.p = PVector(0,height/3)
        self.speed = 2
        
    def update(self):
        self.p.x += self.speed
        if (self.p.x < 0 or self.p.x > width):
            self.speed *= -1
        
    def draw(self):
        stroke(255, 127, 127, 127)
        strokeWeight(2)
        fill(127, 127, 255, 127)
        ellipse(self.p.x, self.p.y, 45, 25)
        stroke(255, 127)
        fill(0, 127, 255)
        ellipse(self.p.x, self.p.y, 20, 20)
        noStroke()
        fill(0)
        ellipse(self.p.x, self.p.y, 10, 10)
        
    def run(self):
        self.update()
        self.draw()