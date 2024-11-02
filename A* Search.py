#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 17:21:45 2024

@author: pavan
"""

import numpy as np

# Set of nodes
all_nodes = ['S', 'A', 'B', 'C', 'D', 'E', 'G']

# Start state
start_state = 'S'

# Goal state
goal_state = 'G'

# Number of nodes
N = len(all_nodes)

# Adjacency matrix
adj = np.zeros((N, N))

def add_edge(node_1, node_2):
	adj[all_nodes.index(node_1), all_nodes.index(node_2)] = 1

# Construct the graph
add_edge('S', 'A')
add_edge('S', 'D')
add_edge('D', 'B')
add_edge('D', 'E')
add_edge('A', 'B')
add_edge('A', 'C')
add_edge('B', 'C')
add_edge('B', 'E')
add_edge('C', 'G')
add_edge('E', 'G')

print('Adjacency matrix:')
print(adj)

#cost matrix
cost = np.zeros((N, N))
def set_cost(node_1,node_2,x):
    cost[all_nodes.index(node_1), all_nodes.index(node_2)] = x
    
set_cost('S', 'A', 3)
set_cost('S', 'D', 2)
set_cost('D', 'B', 1)
set_cost('D', 'E', 4)
set_cost('A', 'B', 5)
set_cost('A', 'C', 10)
set_cost('B', 'C', 2)
set_cost('B', 'E', 1)
set_cost('C', 'G', 4)
set_cost('E', 'G', 3)

heuristic = {'S':7,'A':9,'B':4,'C':2,'D':5,'E':3,'G':0}

visited = np.zeros((N))

parent = np.zeros((N))
parent[:] = -1
cost_matrix = np.full(N,np.inf)
cost_matrix[all_nodes.index(start_state)] = 0

def A_star_search(u):
    start_idx = all_nodes.index(u)
    
    explore_nodes = [(start_idx,cost_matrix[start_idx]+heuristic[u])]
    while explore_nodes:
        min_idx = 0
        for i in range(len(explore_nodes)):
            if explore_nodes[i][1] < explore_nodes[min_idx][1]:
                min_idx = i
        
        cur_idx = explore_nodes[min_idx][0]
        cur_node = all_nodes[cur_idx]
        
        if cur_node == goal_state:
            print('Goal found', cur_node)
            path  = []
            j = cur_idx
            while j != -1:
                path.append(j)
                j = int(parent[j])
                
            path.reverse()
            path = [all_nodes[element] for element in path]
            print('Path:', path)
            print('Cost:', int(cost_matrix[cur_idx]))
            return
        
        new_explore_nodes = []
        for i in range(len(explore_nodes)):
            if i != min_idx:
                new_explore_nodes.append(explore_nodes[i])
        
        explore_nodes = new_explore_nodes
        visited[cur_idx] = 1
        
        neighbors = []
        for i in range(N):
            if adj[cur_idx,i] == 1:
                neighbors.append(i)
                
        for n in neighbors:
            if visited[n] == 0:
                c_cost = cost_matrix[cur_idx] + cost[cur_idx][n]
                
                if c_cost < cost_matrix[n]:
                    parent[n] = cur_idx
                    cost_matrix[n] = c_cost
                    final_cost = cost_matrix[n] + heuristic[all_nodes[n]]
                    if n not in [i for i, j in explore_nodes]:
                        explore_nodes.append((n,final_cost))
    
    print('No path found')

A_star_search(start_state)