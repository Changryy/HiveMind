import csv
from random import random, choices, randrange


input_path = "Tests/input2.txt"
output_path = "Data/output.csv"
evaluation_path = "Data/evaluation.csv"


with open(input_path, "r") as f:
    meadow = [x for x in csv.reader(f)]

try:
    with open(evaluation_path, "r") as f:
        evaluation = [x for x in csv.reader(f)]
except: evaluation = None




class Bee:
    def __init__(self) -> None:
        self.is_alive = True
        self.path = ""
        self.step = self.position = 0

    def fly(self, direction) -> None:
        self.step += 1
        self.position += direction
        self.path += str(direction)
        self.land_on_flower()

    def land_on_flower(self) -> None:
        try:
            safety_level = (float(meadow[self.step][self.position]) + 1.0) / 21.0
            if random() > safety_level: self.die()
        except:
            print(self.step, self.position)
    
    def die(self) -> None:
        self.is_alive = False

    def navigate(self) -> None:
        fly_randomly = lambda: self.fly(randrange(2))

        if evaluation:
            weight = evaluation[self.step+1][self.position:self.position+2]
            if "0" in weight: fly_randomly()
            else:
                direction = choices([0,1],weight)[0]
                self.fly(direction)
        else: fly_randomly()
    
    def explore(self):
        flight_range = len(meadow) - 1
        while self.is_alive and self.step < flight_range:
            self.navigate()
        return f"{self.step}:{int(self.path, 2)},"


