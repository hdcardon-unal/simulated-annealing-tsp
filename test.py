from anneal import SimAnneal
import matplotlib.pyplot as plt
import random

coords = []
with open('coord.txt','r') as f:
    i = 0
    for line in f.readlines():
        line = [float(i.replace('\n','')) for i in line.split(' ')]
        coords.append([])
        for j in range(1,3):
            coords[i].append(line[j])
        i += 1

if __name__ == '__main__':
    #coords = [[round(random.uniform(-10000,10000),4),round(random.uniform(-10000,10000),4)] for i in range(50)]
    sa = SimAnneal(coords)
    sa.Anneal()
    sa.visualizeRotes()
    sa.plotLearning()