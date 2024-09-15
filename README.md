# robot-console
# Toy Robot Simulation

This project is a console application that simulates a toy robot moving on a 5x5 tabletop grid. The robot can be controlled using simple commands: `PLACE`, `MOVE`, `LEFT`, `RIGHT`, and `REPORT`.

## Table of Contents
- [Requirements](#requirements)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Project Structure](#example-usage)
- [How to run tests](#testing)

## Requirements
- Python 3.x

## Installation
1. Clone the repository or download the source code.
2. Navigate to the project directory.

```bash
git clone https://github.com/godalida/robot-console.git
cd robot-console
```

## Running the Application
```bash
python toy_robot.py
```

## Project Structure
```
toy_robot_project/
│
├── src/
│   ├── __init__.py                # Marks the directory as a Python package
│   ├── robot.py                   # Main logic for ToyRobot class
│   └── commands.py                # Command processor for parsing and handling input
│
├── tests/
│   ├── __init__.py                # Marks the directory as a Python package
│   └── test_toy_robot.py          # Unit tests for ToyRobot class
├── LICENSE                        # License file
├── README.md                      # Documentation file
├── toy_robot.py                   # Entry point for running the application
```



## How to run tests
```bash
python -m unittest test_toy_robot.py
```

