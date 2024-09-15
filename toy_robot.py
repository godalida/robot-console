from src.robot import ToyRobot
from src.commands import CommandProcessor

def main():
    robot = ToyRobot()
    processor = CommandProcessor(robot)
    
    print("Toy Robot Simulator: Type commands (PLACE X,Y,F | MOVE | LEFT | RIGHT | REPORT) or 'EXIT' to quit.")
    
    while True:
        command = input("Command: ").strip()
        if command == 'EXIT':
            break
        processor.process_command(command)

if __name__ == "__main__":
    main()
