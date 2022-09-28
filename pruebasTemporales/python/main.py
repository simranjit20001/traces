from ast import In
from pickletools import genops
import random
import string
from webbrowser import get
import numpy as np

class Individual:
    def __init__(self):
        self.genoma = [ random.randint(0, 100) for i in range(5)]
        self.operators = ["add", "sub", "mul", "div"]

    def cross(self, other):
        nuevoIndividual = Individual()
        
        nuevoIndividual.genoma = [ random.choice([self.genoma[i], other.genoma[i]]) for i in range(len(self.genoma)) ]
        return nuevoIndividual
    
    def mutate(self):
        nuevoIndividual = Individual()
        return self.cross(self, nuevoIndividual)

    def obtainResult(self, operator, v1, v2):
        def obtainOperator(op):
            v = 0            
            for i in self.genoma:
                v = i * op
            
            for i in range(len(self.operators)):
                if(self.genoma[i] < v):
                    return self.operators[i]
            
            return "mul"
        
        operator = obtainOperator(ord(operator))

        if(operator == "add"):
            return v1 + v2
        elif(operator == "sub"):
            return v1 - v2
        elif(operator == "mul"):
            return v1 * v2
        elif(operator == "div"):
            if(v2 == 0):
                return 99999999
            return v1 / v2
        return None

    def puntuation(self, v1, v2, operator):
        val_calculated = self.obtainResult(operator, v1, v2)
        real_val = 0
        if(operator == "+"):
            real_val = v1+v2
        elif(operator == "-"):
            real_val = v1-v2
        elif(operator == "*"):
            real_val = v1*v2
        else:  
            if(v2 == 0):
                real_val = 99999999
            else:
                real_val = v1/v2
        
        return abs(real_val-val_calculated)*-1000

population = [  Individual() for i in range(1000)]

def puntua(indv):
    operators = ["+", "-", "*", "/"]
    return indv.puntuation(random.randint(0, 1000), random.randint(0, 1000), random.choice(operators))

for i in range(1000):
    performance = [ 0 for ind in population ]
    for i in range(40):
        for j in range(len(population)):
            performance[j] += puntua(population[j])
    
    percentilMinimun = sorted(performance)[80]

    best = []
    for j in range(len(performance) -1):
        if(performance[j] > percentilMinimun):
            best.append(population[j])
    
    population = [ random.choice(best).cross(random.choice(population)) for i in range(1000)  ]
    

performance = [ 0 for ind in population ]
for i in range(40):
    for j in range(len(population)):
        performance[j] += puntua(population[j])
maximo = max(performance)
mejor = population[performance.index(maximo)]

while(1):
    i = int(input("op1: "))
    ope = input("operator: ")
    i2 = int(input("op2: "))
    print(mejor.obtainResult(ope, i, i2))
   
    


        
        





    
