from tkinter import *
from tkinterhtml import HtmlFrame
import folium
import pandas as pd
import os
from dataRetriever import getGraphPoints


def dijkstra(graph,inf_value, src, dest):
    '''
    This function returns minimum distance between src and dest along with 'path' dictionary
    return value = int,dictionary
    graph : it is the dictionary 
    inf_value : it is the infinity value for particular graph
    src : source vertex of the graph
    dest : destination vertex of the graph
    '''
    
    #initialization of data structures
    graph,points = getGraphPoints()
    nodes = len(graph)
    visited  = {}
    distance = {}
    path = {}
    path[src] = '-1'  #taking this value for to stop looking for path at source
    
    #calculating cities dynamically
    cities = []
    city_list = pd.read_csv('Lat_Long.csv')
    
    for i in city_list['City']:
        cities.append(i)

    print(cities)
    
    for i in cities:
        if i == src:
            distance[src] = 0
        else:
            distance[i] = 99999999999
        visited[i] = False
#     print(distance)
#     print(visited)
    
    #traversing the nodes n-1 times
    i = 0
    while i < (nodes-1):   
        
        #code for finding mini distance non visited node
        min_key = mini_not_visited(distance, visited)
#         print(min_key)
                
        #marking the visited node
        visited[min_key] = True
        
        for neigh_city,val in graph[min_key].items():
            val = int(val)
            if val != inf_value and visited[neigh_city] == False:
                #relaxation
                newDist = distance[min_key] + val
                if newDist < distance[neigh_city]:
                    distance[neigh_city] = newDist
                    #setting path also
                    path[neigh_city] = min_key
        #increment
        i+=1
        
    return distance[dest],path

def mini_not_visited(distance, visited):
    mini = 999999999999
    min_key = ''
    for key,val in distance.items():
        if val < mini and visited[key] == False:
            min_key = key
            mini = val
    return min_key