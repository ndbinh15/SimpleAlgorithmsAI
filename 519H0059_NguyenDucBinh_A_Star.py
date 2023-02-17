# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 19:45:37 2021

@author: truon
"""

from queue import PriorityQueue
from collections import defaultdict

data = defaultdict(list)
data['A'] = ['S', 140, 'T', 118, 'Z', 75, 366]
data['B'] = ['F', 211, 'G', 90, 'P', 101, 'U', 85, 0]
data['C'] = ['D', 120, 'P', 138, 'R', 146, 160]
data['D'] = ['C', 120, 'M', 75, 242]
data['E'] = ['H', 86, 161]
data['F'] = ['B', 211, 'S', 99, 176]
data['G'] = ['B', 90, 77]
data['H'] = ['E', 86, 'U', 98, 151]
data['I'] = ['N', 87, 'V', 92, 226]
data['L'] = ['M', 70, 'T', 111, 244]
data['M'] = ['D', 75, 'L', 70, 241]
data['N'] = ['I', 87, 234]
data['O'] = ['S', 151, 'Z', 71, 380]
data['P'] = ['B', 101, 'C', 138, 'R', 97, 100]
data['R'] = ['C', 146, 'P', 97, 'S', 80, 193]
data['S'] = ['A', 140, 'F', 99, 'O', 151, 'R', 80, 253]
data['T'] = ['A', 118, 'L', 111, 329]
data['U'] = ['B', 85, 'H', 98, 'V', 142, 80]
data['V'] = ['I', 92, 'U', 142, 199]
data['Z'] = ['A', 75, 'O', 71, 374]

dictionary = {"Arad":"A", "Bucharest":"B", "Craiova":"C", "Dobreta":"D", 
              "Eforie":"E","Fagaras":"F", "Giurgiu":"G", "Hirsova":"H", 
              "Iasi":"I", "Lugoj":"L", "Mehadia":"M","Neamt":"N", 
              "Oradea":"O", "Pitesti":"P", "Rimnicu Vikea":"R", "Sibiu":"S",
              "Timisoara":"T", "Urziceni":"U", "Vaslui":"V", "Zerind":"Z"}

dictionary2 = {"A":"Arad", "B":"Bucharest", "C":"Craiova", "D":"Dobreta", 
              "E":"Eforie","F":"Fagaras", "G":"Giurgiu", "H":"Hirsova", 
              "I":"Iasi", "L":"Lugoj", "M":"Mehadia","N":"Neamt", 
              "O":"Oradea", "P":"Pitesti", "R":"Rimnicu Vikea", "S":"Sibiu",
              "T":"Timisoara", "U":"Urziceni", "V":"Vaslui", "Z":"Zerind"}

class Node:
    def __init__(self, name, g = 0, h = 0, par = None):
        self.name = name
        self.g = g
        self.h = h
        self.par = par
        
    def __lt__(self, other):
        if other == None:
            return False
        return self.g + self.h < other.g + other.h
    
    def __eq__(self, other):
        if other == None:
            return False
        return self.name == other.name
    
def equal(O, G):
    if O.name == G.name:
        return True
    return False

def getPath(O):
    print(dictionary2[O.name])
    if O.par != None:
        getPath(O.par)
    else:
        return

def A(S, G):
    O = PriorityQueue()
    C = PriorityQueue()
    
    S.h = data[S.name][-1]
    O.put(S)
    
    while True:
        if(O.empty() == True):
            print('Error')
            return
        rs = O.get()
        C.put(rs)
        print('Finding: ', rs.name, rs.g, rs.h)
        
        if(equal(rs, G) == True):
            print('Success: ')
            getPath(rs)
            print("Total:", rs.g + rs.h)
            return
        
        i = 0
        while i < len(data[rs.name]) - 1:
            name = data[rs.name][i]
            g = rs.g + data[rs.name][i+1]
            h = data[name][-1]
            tmp = Node(name, g, h)
            tmp.par = rs

            O.put(tmp)
            i += 2
        
            
if __name__ == "__main__":
    """
    input from keyboard the place you want to go
    ex: 
        Arad (enter)
        Bucharest (enter)
    """
    start = input("Enter name start: ")
    S = dictionary[start]
    
    end = input("Enter name end: ")
    E = dictionary[end]
    A(Node(S), Node(E))  
    
    