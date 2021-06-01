import urllib.request
import pandas as pd
import matplotlib.pyplot as plt
import random
import numpy as np
from scipy.spatial import distance
url = 'https://raw.githubusercontent.com/maskot1977/ipython_notebook/master/toydata/location.txt'
urllib.request.urlretrieve(url, 'location.txt')

japan = pd.read_csv('location.txt')

from simanneal import Annealer
class TravellingSalesmanProblem(Annealer):

    """Test annealer with a travelling salesman problem.
    """

    # pass extra data (the distance matrix) into the constructor
    def __init__(self, state, distance_matrix):
        self.distance_matrix = distance_matrix
        super(TravellingSalesmanProblem, self).__init__(state)  # important!

    def move(self):
        """Swaps two cities in the route."""
        # no efficiency gain, just proof of concept
        # demonstrates returning the delta energy (optional)
        initial_energy = self.energy()

        a = random.randint(0, len(self.state) - 1)
        b = random.randint(0, len(self.state) - 1)
        self.state[a], self.state[b] = self.state[b], self.state[a]

        return self.energy() - initial_energy

    def energy(self):
        """Calculates the length of the route."""
        e = 0
        for i in range(len(self.state)):
            e += self.distance_matrix[self.state[i-1]][self.state[i]]
        return e


mat = japan[['Latitude', 'Longitude']].values
dist_mat = distance.cdist(mat, mat, metric='euclidean')
distance_matrix = {}
for i, town in enumerate(japan['Town']):
    if town not in distance_matrix.keys():
        distance_matrix[town] = {}
    for j, town2 in enumerate(japan['Town']):
        distance_matrix[town][town2] = dist_mat[i][j]



init_state = list(japan['Town'])
random.shuffle(init_state)

tsp = TravellingSalesmanProblem(init_state, distance_matrix)


tsp.set_schedule(tsp.auto(minutes=0.2))
tsp.copy_strategy = "slice"
state, e = tsp.anneal()

print(state)
