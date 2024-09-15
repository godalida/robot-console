class ToyRobot:
    DIRECTIONS = ['NORTH', 'EAST', 'SOUTH', 'WEST']
    
    def __init__(self):
        self.x = None
        self.y = None
        self.f = None
        self.is_placed = False

    def place(self, x, y, f):
        if 0 <= x <= 4 and 0 <= y <= 4 and f in ToyRobot.DIRECTIONS:
            self.x = x
            self.y = y
            self.f = f
            self.is_placed = True

    def move(self):
        if not self.is_placed:
            return
        if self.f == 'NORTH' and self.y < 4:
            self.y += 1
        elif self.f == 'EAST' and self.x < 4:
            self.x += 1
        elif self.f == 'SOUTH' and self.y > 0:
            self.y -= 1
        elif self.f == 'WEST' and self.x > 0:
            self.x -= 1

    """
    The left and right methods in the ToyRobot class are 
    responsible for changing the robot's facing 
    direction based on its current orientation.
    """
    def left(self):
        if self.is_placed:
            self.f = ToyRobot.DIRECTIONS[(ToyRobot.DIRECTIONS.index(self.f) - 1) % 4]

    def right(self):
        if self.is_placed:
            self.f = ToyRobot.DIRECTIONS[(ToyRobot.DIRECTIONS.index(self.f) + 1) % 4]

    def report(self):
        if self.is_placed:
            return f"{self.x},{self.y},{self.f}"