#import matplotlib.pyplot as plt
import numpy as np
import random

def meshGenerator(numSides):
    if numSides < 3:
        return("Ensure the number of sides is three or more")
    sideLength = np.zeros(numSides)
    for i in range(numSides):
        sideLength[i] = random.randint(1, 10)
    return(sideLength)
    
print(meshGenerator(4))