import sys
import logging

class Rover:
    def __init__(self, x, y, direction, grid_size, commands, obstacles):
        self.x = x
        self.y = y
        self.direction = direction
        self.grid_size = grid_size
        self.commands = commands
        self.obstacles = obstacles

    def run(self):
        for command in self.commands:
            command.execute(self)

    def move(self):
        if self.direction == 'N':
            self.y += 1
        elif self.direction == 'W':
            self.x -= 1
        elif self.direction == 'S':
            self.y -= 1
        else:
            self.x += 1

        if not self.is_valid_move():
            logging.error("Obstacle or out of bounds! Rover stopped.")
            raise Exception("Obstacle or out of bounds!")

    def turn_right(self):
        directions = ['N', 'E', 'S', 'W']
        current_index = directions.index(self.direction)
        self.direction = directions[(current_index + 1) % 4]

    def turn_left(self):
        directions = ['N', 'E', 'S', 'W']
        current_index = directions.index(self.direction)
        self.direction = directions[(current_index - 1) % 4]

    def is_valid_move(self):
        return (0 <= self.x < self.grid_size[0]) and (0 <= self.y < self.grid_size[1]) and ((self.x, self.y) not in self.obstacles)

    def generate_status_report(self):
        direc = ""
        match self.direction:
            case 'N':
                direc = "North"
            case 'E':
                direc = "East"
            case 'S':
                direc = "South"
            case _:
                direc = "West"
        return f"Status Report: Rover is at ({self.x}, {self.y}) facing {direc}. No obstacles detected."

class Command:
    def execute(self, rover):
        pass

class MoveCommand(Command):
    def execute(self, rover):
        rover.move()

class TurnRightCommand(Command):
    def execute(self, rover):
        rover.turn_right()

class TurnLeftCommand(Command):
    def execute(self, rover):
        rover.turn_left()

# Input
grid_size = []
print("Enter grid size in row x column format: ")
grid_size = list(map(int, input().split()))

print("Enter the commands : ")
commands = [MoveCommand() if cmd == 'M' else TurnRightCommand() if cmd == 'R' else TurnLeftCommand() for cmd in input().upper()]

print("Enter no. of Obstacles : ")
obs = int(input())
obstacles = []
for i in range(obs):
    print(f"Enter obstacle {i+1} coordinates in the format x y")
    x, y = map(int, input().split())
    obstacles.append((x, y))

# Rover initialization
rover = Rover(0, 0, "N", grid_size, commands, obstacles)

# Run the simulation
try:
    rover.run()
    print(rover.generate_status_report())
except Exception as e:
    logging.error(f"Simulation failed: {str(e)}")

print(f"Final Position: ({rover.x}, {rover.y}, {rover.direction})")
