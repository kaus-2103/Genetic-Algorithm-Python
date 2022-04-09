import numpy as np
from array import *
import random
from numpy.random.mtrand import randint

graph_matrix = []                   # 2D matrix that will read the file
population = []                     # 1D list of integers gotten by manipulating the first 2D matrix


# ============================== reading text file and inputting in the matrix ===========================

with open("input.txt", 'r') as f:
    lines = f.readlines()
for line in lines:
    graph_matrix.append(line.split())
print("Input : ", graph_matrix)
z = graph_matrix[0]
col = int(z[0])                     # number of transactions
row = col                           # number of individuals per Generation

# ============================== converting matrix to 1D suitable model ==================================

for row in range(len(graph_matrix)):        # we don't need the column because l or d sits on the first index
    if graph_matrix[row][0] == 'l':         # if the amount was being lend
        population.append(-1 * int(graph_matrix[row][1]))  # we consider lend as negative
    elif graph_matrix[row][0] == 'd':       # if the amount was being deposited
        population.append(int(+1 * graph_matrix[row][1]))  # we consider deposit as positive
print("Values : ", population)


# ================================ Creating Random Population  ====================================


weight = 0                                                  # our desired summation of transaction is 0
sample = []
sample_2 = []
sample = population
sample_2 = population
rand_pop = np.random.randint(0, 2, (row, col))              # Generating random population with binary values
print("Randomly Generated Population of Binary numbers, \n Generation - 1 : \n", rand_pop)
rand_pop_temp = np.random.randint(0, 2, (row, col))         # We will use this later to build the next Generation
summation = np.zeros((row, col))
rand_pop = np.append(rand_pop, summation, axis=1)
peak = 0                                                    # store maximum value
captureIndividual = []                                      # store associated individual


# =========================== Starting iteration and summing up the transactions ========================

for q in range(row):
    for i in range(col):
        addition1 = sum(np.multiply(sample, rand_pop[i, 0:col]))  # Calculating Total sum
        if addition1 == weight:
            captureIndividual = rand_pop[i, 0:col]
            peak = addition1
        rand_pop[i, col] = addition1
        addition2 = sum(np.multiply(sample_2, rand_pop[i, 0:col]))
        if addition2 == weight:
            captureIndividual = rand_pop[i, 0:col]
            peak = addition2
        rand_pop[i, col + 1] = addition2

# ================================= Calculating the fitness ========================================


for i in range(row):
    rand_pop[i, col+2] = rand_pop[i, col+1] / np.average(rand_pop[:, col+1])
    rand_pop[i, col+3] = round(rand_pop[i, col+2])
print("Addition values : \n", rand_pop[:, col:col+4].tolist())
print("Sum : ", sum(rand_pop[:, col+1]))
print("Average for fitness : ", np.average(rand_pop[:, col+1]))


# ======================= Determining number of chromosomes for next generation ======================


count = 0
c = 0
for i in range(row):
    numberOfChromosomes = rand_pop[i, 10]
    count += numberOfChromosomes
    if count > row:
        numberOfChromosomes -= 1
        for j in range(int(numberOfChromosomes)):
            rand_pop_temp = rand_pop[i, 0:col]
            c += 1
rand_pop[:, 0:col] = rand_pop_temp
print("Generation - 2: \n", rand_pop[:, 0:col])


# ============================ Selecting two random indices  ==================================


rand = np.array([])
while 1:
    randomIndex = np.random.randint(low=0, high=row, size=2)
    x, y = np.unique(randomIndex, return_counts=True)
    rand = x[y > 1]
    if rand.size == 0:
        break
print("Selecting two discrete transactions ")


# =========================== Selecting data points of those indices  =============================

f = 0
for i in randomIndex:
    rand_pop_temp[f] = rand_pop[i, 0:col]
    f += 1

# ============================ Determining crossover points  ======================================

a = np.random.randint(low=1, high=col, size=1)
print("Crossover point : ", int(a))
print("Pre-Crossover : \n", rand_pop_temp[0:round(col/2)])
b = []
c = []
b = rand_pop_temp[0, int(a):col].tolist()
c = rand_pop_temp[1, int(a):col].tolist()
rand_pop_temp[1, int(a):col] = b
rand_pop_temp[0, int(a):col] = c
print("Post-Crossover : \n", rand_pop_temp[0:4])


# ====================================  Next Generation   ====================================

d = 0
for i in randomIndex:
    rand_pop[i, 0:col] = rand_pop_temp[d]
    d += 0
print("Generation - 3 Post-Crossover : \n", rand_pop[:, 0:col])


# ====================================   Mutation    =================================================

# Converting 1 to 0 and 0 to 1
random_r = int(np.random.randint(0, row, (1, 1)))
random_c = int(np.random.randint(0, col, (1, 1)))
print("Mutation at position : \n", random_r, " , ", random_c)
rand_pop[random_r, random_c] = 1 - int(rand_pop[random_r, random_c])
print("Post-Mutation :\n", rand_pop[:, 0:col])

# =====================================    Final     =====================================================

for i in range(row):
    rand_pop[i, col+2] = rand_pop[i, int(z[0])+1] / np.average(rand_pop[:col+1])
    rand_pop[i, col+3] = round(rand_pop[i, col+2])
    print(rand_pop[i, col+1:col+2].tolist())

if len(captureIndividual) == 0:
    print("No such pattern found")
elif len(captureIndividual) != 0:
    print(" Pattern  : ", captureIndividual, " the summation : ", peak)

# =========================================================================================================
# def fitness(population, sample):
#     count = 0
#     for r in range(row):
#         for c in range(col):
#         # random_population[r][c] *= population[c]
#         # x += random_population[r][c]
#         # print(x)
#             sum_Population = sum(np.multiply(population[c], sample[r, 0:c]))
#             if sum_Population == 0:
#                 capture_Individual = (sample[r, 0:c])
#             print(capture_Individual)
#             count += 1
#     return count
# # print(fitness(population,sample))
# # Random Selection Function
# def selection(sample):
#     sample.sort(key=lambda x: sample.fitness(x), reverse=True)  # sorting
#     new_population = sample.sort[0:50]
# sample = []
# sample = np.random.randint(0, 2, (row, col))
# print("The Random Population : \n", sample)
# row = col**5  # number of different individuals
# random_population = np.random.randint(0, 2, (row, col))
# print("Generated Random Population : \n", random_population)
# x = 0
# capture_Individual = []
# rand_pop = np.append(rand_pop,addZeros,axis=1)
# print (n)
# print(graph_matrix[1][0])
# test.append(int(graph_matrix[1][1]))
# test[0]=-1*test[0]
# print(graph_matrix[2][0])
# test.append(int(graph_matrix[2][1]))
# test[1]=-1*test[1]
# print(test[0])
# print(test[1])
# if (graph_matrix[row] =='l'):
#     x=row
#     print(row)
# elif(graph_matrix[row] =='d'):
#     test.append(int(graph_matrix[row][1]))
