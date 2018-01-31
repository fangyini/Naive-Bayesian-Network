#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Coursework in Python 
from DAPICourseworkLibrary import *
from numpy import *
#
# Coursework 1 begins here
#
# Function to compute the prior distribution of the variable root from the data set
def Prior(theData, root, noStates):
    prior = zeros((noStates[root]), float )
# Coursework 1 task 1 should be inserted here
    for values in theData[:,root]:  #iterate through the root(first) colomn in 'theData'
        prior[values] += 1
    for i in range(len(prior)):
        prior[i] /= len(theData[:,0])
# end of Coursework 1 task 1
    return prior

# Helper function for task 2 which calculates the conditional probability P(C|P) given two variables
# varC and varP represent the index in the variable noStates
# stateC and stateP represent the state of each variable
def CP_Cal(theData, varC, varP, stateC, stateP):
    noP = 0
    noCandP = 0
    for i in range(len(theData[:,varP])):
        if theData[i][varP] == stateP:
            noP+=1
            if theData[i][varC] == stateC:
                noCandP += 1
    if noP == 0: #if there is no P with this state, then the probability is 0
        return 0
    else:
        return float(noCandP) / float(noP)

# Function to compute a CPT with parent node varP and xchild node varC from the data array
# it is assumed that the states are designated by consecutive integers starting with 0
def CPT(theData, varC, varP, noStates):
    cPT = zeros((noStates[varC], noStates[varP]), float )
# Coursework 1 task 2 should be inserte4d here
    for i in range(0,noStates[varC]):
        for j in range(0,noStates[varP]):
            cPT[i][j] = CP_Cal(theData,varC,varP,i,j)
# end of coursework 1 task 2
    return cPT

#Helper function for task 3 which returns the number of pair data in the data set
def noPairs(theData, varC, varP, stateC, stateP):
    number = 0
    for i in range(len(theData[:,varP])):
        if (theData[i][varP] == stateP and theData[i][varC] == stateC):
            number += 1
    return number

# Function to calculate the joint probability table of two variables in the data set
def JPT(theData, varRow, varCol, noStates):
    jPT = zeros((noStates[varRow], noStates[varCol]), float )
#Coursework 1 task 3 should be inserted here
    noPoints = len(theData)
    for i in range(0,noStates[varRow]):
        for j in range(0,noStates[varCol]):
            jPT[i][j] = float(noPairs(theData, varRow, varCol, i, j)) / float(noPoints)
# end of coursework 1 task 3
    return jPT
#
# Function to convert a joint probability table to a conditional probability table
def JPT2CPT(aJPT):
#Coursework 1 task 4 should be inserted here
    for j in range(len(aJPT[0])):
        sum = 0
        for values in (aJPT[:,j]):
            sum += values
        for i in range(len(aJPT)):
            aJPT[i][j] = aJPT[i][j] / sum
# coursework 1 taks 4 ends here
    return aJPT

#
# Function to query a naive Bayesian network
def Query(theQuery, naiveBayes): 
    rootPdf = zeros((naiveBayes[0].shape[0]), float)
# Coursework 1 task 5 should be inserted here
    for i in range(len(rootPdf)):
        rootPdf[i] = naiveBayes[0][i]   #naiveBayes[0] is the prior distribution
        for j in range(len(theQuery)):
            rootPdf[i] = rootPdf[i]*naiveBayes[j+1][theQuery[j]][i]  #naiveBayes[j+1] is the conditional probability table of (j+1)th root
            if rootPdf[i] == 0:
                break
    total=numpy.sum(rootPdf)
    if total == 0:   # if the four probabilities in the table are all 0, then each probability is 25%
        rootPdf += 0.25
    else:
        rootPdf /= total
# end of coursework 1 task 5
    return rootPdf
#
# End of Coursework 1
#
# Coursework 2 begins here
#
# Calculate the mutual information from the joint probability table of two variables
def MutualInformation(jP):
    mi=0.0
# Coursework 2 task 1 should be inserted here
   

# end of coursework 2 task 1
    return mi
#
# construct a dependency matrix for all the variables
def DependencyMatrix(theData, noVariables, noStates):
    MIMatrix = zeros((noVariables,noVariables))
# Coursework 2 task 2 should be inserted here
    

# end of coursework 2 task 2
    return MIMatrix
# Function to compute an ordered list of dependencies 
def DependencyList(depMatrix):
    depList=[]
# Coursework 2 task 3 should be inserted here
    

# end of coursework 2 task 3
    #return array(depList2)
#
# Functions implementing the spanning tree algorithm
# Coursework 2 task 4

def SpanningTreeAlgorithm(depList, noVariables):
    spanningTree = []
  
    return array(spanningTree)
#
# End of coursework 2
#

#
# main program part for Coursework 1
#
noVariables, noRoots, noStates, noDataPoints, datain = ReadFile("Neurones.txt")
theData = array(datain)
filename = 'DAPIResults01.txt'
AppendString(filename, "Coursework One Results by Yini Fang")
AppendString(filename, "") #blank line
AppendString(filename, "The prior probability of node 0")
AppendString(filename, "") #blank line
prior = Prior(theData, 0, noStates)
AppendList(filename, prior)
#
# continue as described
#
#
AppendString(filename,"The conditional probability matrix P(2|0)")
AppendString(filename,"") #blank line
cPT=CPT(theData, 2, 0, noStates)
AppendArray(filename, cPT)
AppendString(filename, "")
AppendString(filename, "The joint probability matrix P(2&0) ")
AppendString(filename, "") #blank line
jPT=JPT(theData, 2, 0, noStates)
AppendArray(filename, jPT)
AppendString(filename, "The conditional probability matrix P(2|0) calculated from the joint probability matrix P (2&0)")
AppendString(filename, "") #blank line
aJPT=JPT2CPT(jPT)
AppendArray(filename, aJPT)
#Question 5
cPT1=CPT(theData, 1, 0, noStates)
cPT3=CPT(theData, 3, 0, noStates)
cPT4=CPT(theData, 4, 0, noStates)
cPT5=CPT(theData, 5, 0, noStates)
naiveBayes=[prior,cPT1,cPT,cPT3,cPT4,cPT5]
rootPdf1=Query([4,0,0,0,5],naiveBayes)
AppendString(filename, "The result of query [4, 0, 0, 0, 5] on the naive network is: ")
AppendList(filename, rootPdf1)
AppendString(filename,"") #blank line
rootPdf2=Query([6,5,2,5,5],naiveBayes)
AppendString(filename, "The result of query [6, 5, 2, 5, 5] on the naive network is: ")
AppendList(filename, rootPdf2)

