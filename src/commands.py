"""
This file contains the logic to handle input commands 
and route them to the appropriate robot methods.
"""
import logger

class CommandProcessor:
    def __init__(self, robot):
        self.robot = robot

    def process_command(self, command):
        parts = command.strip().split()
        if not parts:
            return
        
        if parts[0] == 'PLACE' and len(parts) == 2:
            try:
                x, y, f = parts[1].split(',')
                self.robot.place(int(x), int(y), f)
            except ValueError as e:
                logger.error(f"Invalid PLACE command: {e}")
        elif parts[0] == 'MOVE':
            self.robot.move()
        elif parts[0] == 'LEFT':
            self.robot.left()
        elif parts[0] == 'RIGHT':
            self.robot.right()
        elif parts[0] == 'REPORT':
            print(self.robot.report())