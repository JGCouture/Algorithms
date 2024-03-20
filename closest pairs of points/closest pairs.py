from math import sqrt
from math import comb
import random
import time

import MinHeap

def find_closest_pairs(P, m):
    distances = []

    # Calculate distances between all pairs of points
    for i in range(len(P)):
        for j in range(i + 1, len(P)):
            distance = calculate_distance(P[i], P[j])
            distances.append([distance, P[i], P[j]])

    # Use a min-heap to maintain the m smallest distances
    min_heap = MinHeap.MinHeap()
    min_heap.heapify_arr(distances)

    # Extract the m smallest distances
    closest_pairs = [min_heap.heap_pop(distances) for _ in range(min(m, len(distances)))]

    return closest_pairs


def calculate_distance(p1, p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

if __name__ == "__main__":

    
    a = input("Please input how many pairs you want to generate: ")

    #Error checks
    while not a.isdigit():

        print("Your input must be a positive integer value, please try again!")
        a = input("Please input how many pairs you want to generate: ")


    a = int(a)

    #Error checks

    while a < 2:
        print("Your input must be greater than 1, please try again!")
        a = input("Please input how many pairs you want to generate: ")
        a = int(a)
        

    m = input("Please input how many closest pairs you want to get: ")


    #Error checks
    while not m.isdigit():

        print("Your input must be an integer value, please try again!")
        m = input("Please input how many closest pairs you want to get: ")

    m = int(m)

    #Error checks
    while m < 1:
        print("Your input must be greater than 0, please try again!")
        m = input("Please input how many closest pairs you want to get: ")
        
        m = int(m)
        
    combination = comb(a, 2)

    #Error checks
    while m > combination:

        print("m must be not greater than " + str(combination) +", please try again!")

        m = input("Please input how many closest pairs you want to get: ")

        m = int(m)

    points = []

    for _ in range(a):
        ran1 = random.randint(-100, 100)
        ran2 = random.randint(-100, 100)
        points.append([ran1, ran2])
    print("-------------------------------------------------------------------------")
    print("Your generated pairs are: ", points)
    print("-------------------------------------------------------------------------")
    print("m is : ", m)

    


    '''
    #Example usage from the meeting:
    points = [[-56, -100], [-6, -37], [-5, 91], [-89, 9], [24, 99]]

    m= 2
    print("-------------------------------------------------------------------------")
    print("Your generated pairs are: ", points)
    print("-------------------------------------------------------------------------")
    print("m is : ", m)
    '''

    #Generate the result
    print("-------------------------------------------------------------------------")
   
    closest_pairs = find_closest_pairs(points, m)
    for distance, p1, p2 in closest_pairs:
        print(f"Distance: {distance}, Points: {p1}, {p2}")
        
    
    





      
