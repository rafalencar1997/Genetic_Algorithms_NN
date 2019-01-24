class Population(object):

    def __init__(self, pop_size, hyper_size):
        self.size       = size
        self.population = []
        for i in range(pop_size):
            hyper = []
            for h in range(hyper_size):
            hyper.append(random.random())
            self.population.append(Individual(hyper))
     