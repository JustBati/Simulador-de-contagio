from population import population_S, population_A
import random

class simulation:
    #----------------------------------------------------------------------------------------------------
    #                       METRICS AND CONSTANTS
    #----------------------------------------------------------------------------------------------------

    # Metrics to do the calculations for the simulation
    def __init__(self, higienic, concurrency, agressiveness, health, contact, state, medical_care):
        self.higienic = higienic # .2, .5, .8 how hygienic is the population
        self.concurrency = concurrency #.2, .5, .8 How many people go out
        self.agressiveness = agressiveness  #.5, 1, 1.3, 1.7 How agressive is the virus
        self.health = health  # .5, .8, 1   How healthy is the population
        self.medical_care = medical_care # .2, .5, .8 How good is the medical care

        self.population_S1 = population_S()
        self.population_S2 = population_S()
        self.population_S3 = population_S()
        self.population_S4 = population_S()
        self.population_A1 = population_A()
    # Metod to return the values of the simulation it cames valid just calling the object
    def __str__(self):
        return f"{self.population_A1} {self.population_S1} {self.population_S2} {self.population_S3} {self.population_S4} "

    #----------------------------------------------------------------------------------------------------
    #                       FORMULA FOR THE STATE OF THE POPULATION
    #----------------------------------------------------------------------------------------------------

    # Method to calculate the number of infected people
    def newe_infected(self):
        health_population = self.population_A1.health + self.population_S1.health + self.population_S2.health + self.population_S3.health + self.population_S4.health
        infected_population = self.population_A1.infected + self.population_S1.infected + self.population_S2.infected + self.population_S3.infected + self.population_S4.infected

        contact = infected_population / health_population 
        prob_contagion = self.concurrency * (1- self.health) * (contact * self.agressiveness)
        new_infected = 0
        for i in range(health_population):
            if random.randint(0, 100) <= prob_contagion:
                new_infected += 1
        return new_infected        

    # Method to calculate the number of people who recover from sickness
    def s_recovery(self):
        sick_population = self.population_A1.sick + self.population_S1.sick + self.population_S2.sick + self.population_S3.sick + self.population_S4.sick
        pro_recover = (self.health * self.medical_care * self.higienic) * 100
        new_recover = 0
        for i in range(sick_population):
            if random.randint(0, 100) <= pro_recover:
                new_recover += 1
        return new_recover
    
    # Metod to calculate the number of people who recover from infection
    def i_recovery(self):
        infected_population = self.population_A1.infected + self.population_S1.infected + self.population_S2.infected + self.population_S3.infected + self.population_S4.infected
        pro_recover = (self.health * self.medical_care * self.higienic) * 100
        new_recover = 0
        for i in range(infected_population):
            if random.randint(0, 100) <= pro_recover:
                new_recover += 1
        return new_recover
    # Metod to calculate the number of people who get sick
    def get_sick(self):
        infected_population = self.population_A1.infected + self.population_S1.infected + self.population_S2.infected + self.population_S3.infected + self.population_S4.infected
        pro_get_sick = ((1- self.health ) * (1- self.higienic )) * 100
        new_sick = 0
        for i in range(infected_population):
            if random.randint(0, 100) <= pro_get_sick:
                new_sick += 1
        return new_sick

    #----------------------------------------------------------------------------------------------------
    #                       ASIGN THE NEW VALUES TO THE POPULATION
    #----------------------------------------------------------------------------------------------------
    
    # Method to asign the new values to the population
    def Run(self):
        new_infected = self.newe_infected()
        new_sick = self.get_sick()
        new_recover = self.s_recovery()
        new_recover_i = self.i_recovery()

        while new_infected > 0:
            j = random.randint(0, 4)
            if ((j == 0) and (self.population_A1.health > 0)):
                self.population_A1.infected += 1
                self.population_A1.health -= 1
                new_infected -= 1

            elif (j == 1) and (self.population_S1.health > 0):
                self.population_S1.infected += 1
                self.population_S1.health -= 1
                new_infected -= 1

            elif (j == 2) and (self.population_S2.health > 0):
                self.population_S2.infected += 1
                self.population_S2.health -= 1
                new_infected -= 1

            elif (j == 3) and (self.population_S3.health > 0):
                self.population_S3.infected += 1
                self.population_S3.health -= 1
                new_infected -= 1

            elif (j == 4) and (self.population_S4.health > 0):
                self.population_S4.infected += 1
                self.population_S4.health -= 1
                new_infected -= 1


        while new_sick > 0:
            j = random.randint(0, 4)
            if ((j == 0) and (self.population_A1.infected > 0)):
                self.population_A1.sick += 1
                self.population_A1.infected -= 1
                new_sick -= 1

            elif (j == 1) and (self.population_S1.infected > 0):
                self.population_S1.sick += 1
                self.population_S1.infected -= 1
                new_sick -= 1

            elif (j == 2) and (self.population_S2.infected > 0):
                self.population_S2.sick += 1
                self.population_S2.infected -= 1
                new_sick -= 1

            elif (j == 3) and (self.population_S3.infected > 0):
                self.population_S3.sick += 1
                self.population_S3.infected -= 1
                new_sick -= 1

            elif (j == 4) and (self.population_S4.infected > 0):
                self.population_S4.sick += 1
                self.population_S4.infected -= 1
                new_sick -= 1

        while new_recover > 0:
            j = random.randint(0, 4)
            if ((j == 0) and (self.population_A1.sick > 0)):
                self.population_A1.health += 1
                self.population_A1.sick -= 1
                new_recover -= 1

            elif (j == 1) and (self.population_S1.sick > 0):
                self.population_S1.health += 1
                self.population_S1.sick -= 1
                new_recover -= 1

            elif (j == 2) and (self.population_S2.sick > 0):
                self.population_S2.health += 1
                self.population_S2.sick -= 1
                new_recover -= 1

            elif (j == 3) and (self.population_S3.sick > 0):
                self.population_S3.health += 1
                self.population_S3.sick -= 1
                new_recover -= 1

            elif (j == 4) and (self.population_S4.sick > 0):
                self.population_S4.health += 1
                self.population_S4.sick -= 1
                new_recover -= 1

        while new_recover_i > 0:
            j = random.randint(0, 4)
            if ((j == 0) and (self.population_A1.infected > 0)):
                self.population_A1.health += 1
                self.population_A1.infected -= 1
                new_recover_i -= 1

            elif (j == 1) and (self.population_S1.infected > 0):
                self.population_S1.health += 1
                self.population_S1.infected -= 1
                new_recover_i -= 1

            elif (j == 2) and (self.population_S2.infected > 0):
                self.population_S2.health += 1
                self.population_S2.infected -= 1
                new_recover_i -= 1

            elif (j == 3) and (self.population_S3.infected > 0):
                self.population_S3.health += 1
                self.population_S3.infected -= 1
                new_recover_i -= 1

            elif (j == 4) and (self.population_S4.infected > 0):
                self.population_S4.health += 1
                self.population_S4.infected -= 1
                new_recover_i -= 1

if __name__ == "__main__":
    sim = simulation(0.2, 0.5, 1, 0.8, 0.5, .4, 0.5)
    for i in range(20):
        sim.Run()
        print(sim)