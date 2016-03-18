# system library
import numpy as np

# user-library
from RegressionDecisionTree import RegressionDecisionTree



def mainDecisionTreeReg():
    reg = RegressionDecisionTree()

    for i in range(8):
        print "Route: {}".format(i)
        reg.evaluateOneRouteForMultipleTimes(reg.routes[i], 7)

    #reg.evaluateOneRouteForMultipleTimes(reg.routes[7], 7)
    #reg.visualizePrediction(reg.routes[7])


if __name__ == "__main__":
    mainDecisionTreeReg()