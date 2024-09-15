import unittest
from toy_robot.robot import ToyRobot

class TestToyRobot(unittest.TestCase):
    
    def setUp(self):
        self.robot = ToyRobot()
    
    def test_place_robot(self):
        self.robot.place(0, 0, 'NORTH')
        self.assertEqual((self.robot.x, self.robot.y, self.robot.f), (0, 0, 'NORTH'))

    def test_move_north(self):
        self.robot.place(0, 0, 'NORTH')
        self.robot.move()
        self.assertEqual((self.robot.x, self.robot.y), (0, 1))

    def test_turn_left(self):
        self.robot.place(0, 0, 'NORTH')
        self.robot.left()
        self.assertEqual(self.robot.f, 'WEST')

    def test_turn_right(self):
        self.robot.place(0, 0, 'NORTH')
        self.robot.right()
        self.assertEqual(self.robot.f, 'EAST')

    def test_prevent_falling(self):
        self.robot.place(0, 0, 'SOUTH')
        self.robot.move()  # No movement as it would fall
        self.assertEqual((self.robot.x, self.robot.y), (0, 0))

if __name__ == '__main__':
    unittest.main()