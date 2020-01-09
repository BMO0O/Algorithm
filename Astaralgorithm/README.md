# Astar_algorithm

This is Python3 program for A* algorithm.

A* algorithm combines the strengths of Dijkstra algorithm and Greedy best-first algorithm.

A precedence value in priority queue is the sum of cumulative charging of dijkstra and remaining distance to destination.

Cost calculations are same as dijkstra algorithm, 
just a precedence value is changed to the sum of cumulative charging and hueristic. 