class Enviroment(object):
    
    def __init__(self, best_samples, lucky_few, mutation_ratio, max_generation, max_diff):
        self.best_samples   = best_samples
        self.lucky_few      = lucky_few
        self.mutation_ratio = mutation_ratio
        self.max_generation = max_generation
        self.max_diff       = max_diff
        self.sample_size    = 
        self.run_time       = 0
        self.generations    = []
    
    def naturalSelection(population, best_sample, lucky_few):
        print("...Running Natural Selection...")
        survivers = []
        for b in range(best_sample):
            survivers.append(population[i])
        for l in range(lucky_few):
            survivers.append(random.choice(population))
        return survivers
    
    def createPopulation
    
    def run(self):
        start = time.time()
        actual_population = createPopulation()
        for g in range(self.max_generation):
            if !self.run_generation() break
        end = time.time()
        self.run_time = (end-start)  
        
    def run_generation(self, population):
        start = time.time()
        population = sortIndividuals(population)
        self.generations.append(population)
        #
        max_diff = population[0].getScore() - population[-1].getScore()
        if (max_diff < self.max_diff) return False
        #
        population = naturalSelection(population, self.best_sample, self.luck_few)
        #
        population = createChildren(population, 6)
        #
        population = mutatePopulation(population, self.mutation_ratio)
        end = time.time()
        generation_time.append(end - start)
        return True
    
    # Generate Mutation
def mutateIndividual(individual):
    for i in range(len(individual.getHyperVec())):
        mutation = individual.getHyper(i) + (0.5*random.random() - 1)
        individual.setHyper(0, max(0, mutation))
    return individual

#Mutation for all the population
def mutatePopulation(population, mutation_ratio):
    print("...Running Mutation... ") 
    for individual in population:
        if random.random() < mutation_ratio:
            mutateIndividual(individual)
    return population