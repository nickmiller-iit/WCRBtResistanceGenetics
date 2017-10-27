"""
Created on Fri Oct 27 13:59:39 2017

@author: Nick Miller

An extremely simple coalescent simulation model. For the purposes of these
simulations, we do not need to keep track of branch lengths. We simply 
coalesce back to the ancestors in the "hybrod generation. The we onlyt need
to be able to set the state of each ancestral allele and propagate that to the
alleles in the sample.
"""

import numpy as np

class Node:
    """
    Simple node. Each node has a reference to a list of all the alleles in the 
    sample. This allows the nod to propagte an allele state to all of its
    descendents in the sample. Coalescnce is represented by transferring all 
    of one node's descenents to another.
    """
    
    def __init__(self,
                 sampleList,
                 descendentIDs):
        self.sampleList = sampleList #reference to sample alleles
        self.descendentIDs = np.array(descendentIDs) #makes a new copy
        
    def addDescendents(self,
                       newDescendents):
        """
        Adds additional descendents.
        
        Only adds to an existing descendents list, does not re-set a
        list of descendents IDs
        """
        self.descendentIDs = np.concatenate((self.descendentIDs, newDescendents))
        
    def setDescendents(self,
                       state):
        """
        Sets descendents in the sampleList's value to state
        
        Intended for setting allele states
        """
        for idx in self.descendentIDs:
            self.sampleList[idx] = state
    
    def yieldDescendents(self):
        """
        Returns the list of descendent indexes.
        
        Needed to coalesce to another node"""
        return(self.descendentIDs)
        
