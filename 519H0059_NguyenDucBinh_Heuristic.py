# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 14:12:05 2021

@author: truon
"""

from queue import PriorityQueue
from collections import defaultdict

data = defaultdict(list)
data['A'] = ['S', 'T', 'Z', 366]
data['B'] = ['F', 'G', 'P', 'U', 0]
data['C'] = ['D', 'P', 'R', 160]
data['D'] = ['C', 'M', 242]
data['E'] = ['H', 161]
data['F'] = ['B', 'S', 176]
data['G'] = ['B', 77]
data['H'] = ['E', 151]
data['I'] = ['N', 'V', 226]
data['L'] = ['M', 'T', 244]
data['M'] = ['D', 'L', 241]
data['N'] = ['I', 234]
data['O'] = ['S', 'Z', 380]
data['P'] = ['B', 'C', 'R', 100]
data['R'] = ['C', 'P', 'S', 193]
data['S'] = ['A', 'F', 'O', 'R', 253]
data['T'] = ['A', 'L', 329]
data['U'] = ['B', 'H', 'V', 80]
data['V'] = ['I', 'U', 199]
data['Z'] = ['A', 'O', 374]

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
    def __init__(self, name, h = 0, par = None):
        self.name = name
        self.h = h
        self.par = par
        
    def __lt__(self, other):
        if other == None:
            return False
        return self.h < other.h
    
    def __eq__(self, other):
        if other == None:
            return False
        return self.name == other.name
    
def equal(O, G):
    if O.name == G.name:
        return True
    return False

def getPath(O, fee):
    print(dictionary2[O.name])
    fee += O.h
    if O.par != None:
        getPath(O.par, fee)
    else:
        print("Total: ", fee)
        return
    
def Heuristic(S, G):
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
        print('Finding: ', rs.name, rs.h)
        
        if(equal(rs, G) == True):
            print('Success: ')
            fee = 0
            getPath(rs, fee)
            return
        
        i = 0
        while i < len(data[rs.name]) - 1:
            name = data[rs.name][i]
            h = data[name][-1]
            tmp = Node(name, h)
            tmp.par = rs

            O.put(tmp)
            i += 1
            
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
    Heuristic(Node(S), Node(E))