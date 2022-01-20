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

        flight_range = len(meadow) - 1
        while self.is_alive and self.step < flight_range:
            self.navigate()

    def fly(self, direction) -> None:
        self.step += 1
        self.position += direction
        self.path += str(direction)
        self.land_on_flower()

    def land_on_flower(self) -> None:
        try:
            danger = float(meadow[self.step][self.position]) / 20.0
            if random() > danger: self.die()
        except:
            print(self.step, self.position)
    
    def die(self) -> None:
        self.is_alive = False
        self.send_report()
    
    def send_report(self) -> None:
        with open(output_path, "a") as f:
            f.write(f"{self.step}:{int(self.path, 2)},")

    def navigate(self) -> None:
        fly_randomly = lambda: self.fly(randrange(2))

        if evaluation:
            weight = evaluation[self.step+1][self.position:self.position+2]
            if "0" in weight: fly_randomly()
            else:
                direction = choices([0,1],weight)[0]
                self.fly(direction)
        
        else: fly_randomly()


