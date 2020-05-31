import numpy as np
import random
import operator
import pandas as pd
import matplotlib.pyplot as plt
from directions import return_connection
import json

cityList = []
coordinat = [
    (55.75371, 37.61988),
    (55.75252, 37.62308),
    (55.744525, 37.605281),
    (55.7262, 37.55639),
    (55.75116, 37.62872),
    (55.66766, 37.67069),
    (55.7942, 37.74907),
    (55.76013, 37.61864),
    (55.74138, 37.62086),
    (55.75533, 37.61784),
    (55.7473, 37.60511),
    (55.76323, 37.57659),
    (55.76144, 37.58365),
    (55.76015, 37.62469),
    (55.75489, 37.62158)
]

full_list_of_directions = return_connection(coordinat)
# print(full_list_of_directions)


class City:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, city):
        # common.append((self, city))

        # if (self, city) not in unique:
        #     unique.append((self, city))

        # xDis = abs(self.x - city.x)
        # yDis = abs(self.y - city.y)
        # distance = np.sqrt((xDis ** 2) + (yDis ** 2))

        for i in range(0, len(full_list_of_directions)):
            if full_list_of_directions[i]['start'][0] == self.x and full_list_of_directions[i]['start'][1] == self.y and full_list_of_directions[i]['end'][0] == city.x and full_list_of_directions[i]['end'][1] == city.y:
                distance = full_list_of_directions[i]['direction']['distance']['value']
                return distance

    def __repr__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def __json__(self):
        return dict(x=self.x, y=self.y)


class MyUniversalEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, "__json__"):
            return obj.__json__()
        return json.JSONEncoder.default(self, obj)


class Fitness:
    def __init__(self, route):
        self.route = route
        self.distance = 0
        self.fitness = 0.0

    def routeDistance(self):
        if self.distance == 0:
            pathDistance = 0
            for i in range(0, len(self.route)):
                fromCity = self.route[i]
                toCity = None
                if i + 1 < len(self.route):
                    toCity = self.route[i + 1]
                else:
                    toCity = self.route[0]
                pathDistance += fromCity.distance(toCity)
            self.distance = pathDistance
        return self.distance

    def routeFitness(self):
        if self.fitness == 0:
            self.fitness = 1 / float(self.routeDistance())
        return self.fitness


def createRoute(cityList):
    route = random.sample(cityList, len(cityList))
    return route


def initialPopulation(popSize, cityList):
    population = []

    for i in range(0, popSize):
        population.append(createRoute(cityList))
    return population


def rankRoutes(population):
    fitnessResults = {}
    for i in range(0, len(population)):
        fitnessResults[i] = Fitness(population[i]).routeFitness()
    return sorted(fitnessResults.items(), key=operator.itemgetter(1), reverse=True)


def selection(popRanked, eliteSize):
    selectionResults = []
    df = pd.DataFrame(np.array(popRanked), columns=["Index", "Fitness"])
    df['cum_sum'] = df.Fitness.cumsum()
    df['cum_perc'] = 100*df.cum_sum/df.Fitness.sum()

    for i in range(0, eliteSize):
        selectionResults.append(popRanked[i][0])
    for i in range(0, len(popRanked) - eliteSize):
        pick = 100*random.random()
        for i in range(0, len(popRanked)):
            if pick <= df.iat[i, 3]:
                selectionResults.append(popRanked[i][0])
                break
    return selectionResults


def matingPool(population, selectionResults):
    matingpool = []
    for i in range(0, len(selectionResults)):
        index = selectionResults[i]
        matingpool.append(population[index])
    return matingpool


def breed(parent1, parent2):
    child = []
    childP1 = []
    childP2 = []

    geneA = int(random.random() * len(parent1))
    geneB = int(random.random() * len(parent1))

    startGene = min(geneA, geneB)
    endGene = max(geneA, geneB)

    for i in range(startGene, endGene):
        childP1.append(parent1[i])

    childP2 = [item for item in parent2 if item not in childP1]

    child = childP1 + childP2
    return child


def breedPopulation(matingpool, eliteSize):
    children = []
    length = len(matingpool) - eliteSize
    pool = random.sample(matingpool, len(matingpool))

    for i in range(0, eliteSize):
        children.append(matingpool[i])

    for i in range(0, length):
        child = breed(pool[i], pool[len(matingpool)-i-1])
        children.append(child)
    return children


def mutate(individual, mutationRate):
    for swapped in range(len(individual)):
        if(random.random() < mutationRate):
            swapWith = int(random.random() * len(individual))

            city1 = individual[swapped]
            city2 = individual[swapWith]

            individual[swapped] = city2
            individual[swapWith] = city1
    return individual


def mutatePopulation(population, mutationRate):
    mutatedPop = []

    for ind in range(0, len(population)):
        mutatedInd = mutate(population[ind], mutationRate)
        mutatedPop.append(mutatedInd)
    return mutatedPop


def nextGeneration(currentGen, eliteSize, mutationRate):
    popRanked = rankRoutes(currentGen)
    selectionResults = selection(popRanked, eliteSize)
    matingpool = matingPool(currentGen, selectionResults)
    children = breedPopulation(matingpool, eliteSize)
    nextGeneration = mutatePopulation(children, mutationRate)
    return nextGeneration


def geneticAlgorithm(population, popSize, eliteSize, mutationRate, generations):
    pop = initialPopulation(popSize, population)
    # print("Initial distance: " + str(1 / rankRoutes(pop)[0][1]))

    for i in range(0, generations):
        pop = nextGeneration(pop, eliteSize, mutationRate)

    # print("Final distance: " + str(1 / rankRoutes(pop)[0][1]))
    bestRouteIndex = rankRoutes(pop)[0][0]
    bestRoute = pop[bestRouteIndex]
    return bestRoute


for i in range(0, 15):
    cityList.append(
        City(x=(coordinat[i][0]), y=(coordinat[i][1])))


def return_salesman_result(popSize, eliteSize, mutationRate, generations):
    result = geneticAlgorithm(population=cityList, popSize=popSize,
                              eliteSize=eliteSize, mutationRate=mutationRate, generations=generations)
    print(result)
    return json.dumps(result, cls=MyUniversalEncoder)
