# A class to create the student population of the simulation
class population_S:
    def __init__(self):
        self.health = 480
        self.sick = 0
        self.infected = 2

    def __str__(self):
        return f"{self.health} {self.sick} {self.infected} "

# A class to create the teacher population of the simulation
class population_A:
    def __init__(self):
        self.health = 250
        self.sick = 0
        self.infected = 2

    def __str__(self):
        return f"{self.health} {self.sick} {self.infected} "