import unittest
import logging
from src.robot import ToyRobot

# Configure logging
logging.basicConfig(level=logging.INFO)

class TestToyRobot(unittest.TestCase):
    
    def setUp(self):
        self.robot = ToyRobot()
    
    def test_place_robot(self):
        self.robot.place(0, 0, 'NORTH')
        logging.info(f'Placed robot at: {(self.robot.x, self.robot.y, self.robot.f)}')
        self.assertEqual((self.robot.x, self.robot.y, self.robot.f), (0, 0, 'NORTH'))

    def test_move_north(self):
        self.robot.place(0, 0, 'NORTH')
        self.robot.move()
        logging.info(f'Moved robot to: {(self.robot.x, self.robot.y)}')
        self.assertEqual((self.robot.x, self.robot.y), (0, 1))

    def test_turn_left(self):
        self.robot.place(0, 0, 'NORTH')
        self.robot.left()
        logging.info(f'Robot turned left, now facing: {self.robot.f}')
        self.assertEqual(self.robot.f, 'WEST')

    def test_turn_right(self):
        self.robot.place(0, 0, 'NORTH')
        self.robot.right()
        logging.info(f'Robot turned right, now facing: {self.robot.f}')
        self.assertEqual(self.robot.f, 'EAST')

    def test_prevent_falling(self):
        self.robot.place(0, 0, 'SOUTH')
        self.robot.move()  # No movement as it would fall
        logging.info(f'Robot position after move attempt: {(self.robot.x, self.robot.y)}')
        self.assertEqual((self.robot.x, self.robot.y), (0, 0))

if __name__ == '__main__':
    unittest.main()