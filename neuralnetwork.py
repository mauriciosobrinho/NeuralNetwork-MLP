import math
import random
import string 
import numpy as np

class NeuralNetwork:

    def __init__(self, nodei, nodeh, nodeo):

        self.ni = nodei + 1
        self.nh = nodeh
        self.no = nodeo

        # create array
        self.wi = np.zeros(self.ni, self.nh)
    sefl.wh = np.zeros(self.nh, self.no)

        # init array with zeros
    for i in range(self.ni):
        for j in range(self.nh):
            self.wi[i][j] = rand(-0.1, 0.1)
    
    for i in range(self.nh):
            for j in range(self.no):
                self.wh[i][j] = rand(-0.1, 0.1)

    # make a vector of the inputh
    self.ai = [1.0] * self.ni 
    self.ah = [1.0] * self.nh

    # tanh is a little nicer than the standard 1/(1+e^-x)
    def sigmoid(x):
        return math.tanh(x)

    def update(input):

           if len(input) != self.n-1:
               raise ValueError(' input error ..')

           for i in range(self.ni):
               self.ai[i] = input[i]

           for i in range(self.ni):
               sum = 0.0
               for j in range (self.nh): # por el numero de intradas
                   sum = sum + self.wi[i][j] * self.ai[j]
               self.ah[j] = sigmoid(sum)
               
           for i in range(self.nh):
            sum = 0.0
    for j in range (self.no): # por el numero de intradas
        sum = sum + self.wo[i][j] * self.ai[j]
        self.ao[j] = sigmoid(sum)
              
        
    def backprogAlgorimth ():
