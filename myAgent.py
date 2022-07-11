import numpy as np
import random as rand

playerName = "myAgent"
nPercepts = 75
nActions = 5

trainingSchedule = [("random", 1000), ("self", 1)]

class MyCreature:

    def __init__(self):
        self.chromosome = np.random.rand(nPercepts * nActions)

    def AgentFunction(self, percepts):
        actions = np.zeros(5)
        count = 0
        all_percepts = percepts.flatten()
        responses = np.zeros(375)
        for j in range(5):
            for percept in all_percepts:
                responses[count] = self.chromosome[count] * percept
                count += 1

        count = 0
        for i in range(375):
            actions[count - 1] += responses[i]
            if i % 75 == 0:
                count += 1

        return actions


def newGeneration(old_population):

    N = len(old_population)
    fitness = np.zeros(N)

    for n, creature in enumerate(old_population):

        if creature.alive:
            fitness[n] += 1000

        fitness[n] += creature.turn
        fitness[n] += creature.squares_visited
        fitness[n] += creature.size * creature.strawb_eats * 5
        fitness[n] += creature.size * creature.enemy_eats * 10

    new_population = list()
    for n in range(N):
        tournament = list()
        tournament_fitness = []
        for i in range(int(N / 2)):
            randomval = rand.randint(0, N - 1)
            tournament.append(old_population[randomval])
            tournament_fitness.append(fitness[randomval])

        insertionSort(tournament, tournament_fitness)

        parent1 = tournament[len(tournament) - 1]
        parent2 = tournament[len(tournament) - 2]

        child = MyCreature()

        for x in range(0, nPercepts * nActions):
            coin = rand.randint(0, 1)
            if coin == 0:
                child.chromosome[x] += parent1.chromosome[x]
            else:
                child.chromosome[x] += parent2.chromosome[x]

        new_population.append(child)
    avg_fitness = np.mean(fitness)
    return new_population, avg_fitness


def insertionSort(array, fitness):
    for step in range(1, len(array)):
        key1 = fitness[step]
        key2 = array[step]
        j = step - 1
        while j >= 0 and key1 < fitness[j]:
            fitness[j + 1] = fitness[j]
            array[j + 1] = array[j]
            j = j - 1
        fitness[j + 1] = key1
        array[j + 1] = key2
    return array, fitness
