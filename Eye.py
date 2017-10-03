class Eye(object):
    def __init__(self, _p = PVector(0,0), _speed = 2):
        self.p = _p
        self.speed = _speed
        
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