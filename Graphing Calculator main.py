import matplotlib.pyplot as plt
import math, sys
import numpy as np


'''fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [1, 4, 2, 5])
plt.ylabel('some numbers')
plt.show()
'''


def main():
    def getEquation():
        print("Example Equation: ax^2 + bx + c; 2x^2 -5x + 1")
        a = input("What is a? ")
        b = input("What is b? ")
        c = input("What is c? ")
        try:
            a = float(a)
            b = float(b)
            c = float(c)
        except(ValueError):
            print("The numbers that have been entered are invalid. Please use the documentation or use the example equation to input valid values")
            sys.exit(1)
        return(a,b,c)
    

    def findRoots(a,b,c):
        radicand = b**2-(4*a*c) 
        if radicand >= 0:
            determinant = math.sqrt(radicand)
            posRoot = ((-1 *b) + determinant)/(2*a)
            negRoot = ((-1 *b) - determinant)/(2*a)
            posRoot = [round(posRoot, 3), 0]
            negRoot = [round(negRoot, 3), 0]
        else:
            radicand = radicand*(-1)
            determinant = math.sqrt(radicand)
            posRoot = [round((-1 *b)/(2*a), 3), round(determinant/(2*a), 3)]
            negRoot = [round((-1 *b)/(2*a), 3), round(-1*(determinant)/(2*a), 3)]
        return (posRoot,negRoot)

    def findAOS(a,b):
         return ((-1*float(b))/(2*float(a)))

    def findVertex(a, b, c):
        vertex=(findAOS(a, b),(((float(a)*findAOS(a, b))**2)+(float(b)*findAOS(a, b))+float(c)))
        return vertex

    def graphParabola(a,b,c):
        # create 1000 equally spaced points between -10 and 10
        x = np.linspace(-100+findAOS(a,b), 100+findAOS(a,b), 1000)
        # calculate the y value for each element of the x vector
        y = int(a)*(x**2)+int(b)*(x)+int(c)

        fig, ax = plt.subplots()
        ax.plot(x, y)
        plt.ylabel('y axis')
        plt.xlabel('x axis')
        fig.suptitle('Parabola', fontsize=16)
        plt.axvline(findAOS(a,b),color='red')
        plt.grid()
        plt.plot(*findVertex(a,b,c), marker="o", markersize=5,                 markeredgecolor="red", markerfacecolor="red")
        #plt.plot((0,0), marker=".")
        plt.show()

    def printRoots(posRoot,negRoot):
        if posRoot[1] == 0:
            print("The roots of this equation are", str(posRoot).replace("[","(").replace("]",")"), "and",str(negRoot).replace("[","(").replace("]",")"))
        else:
            print("A root of this equation is", "("+str(posRoot[0]),"+",str(posRoot[1])+"i"+")")
            print("The other root of this equation is", "("+str(negRoot[0]),"-", str(-1*negRoot[1])+"i"+")")

    (a,b,c) = getEquation()
    printRoots(*findRoots(a,b,c))
    graphParabola(a,b,c)

main()
