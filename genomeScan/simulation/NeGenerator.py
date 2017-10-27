__author__ = "Nick Miller"

# There is uncertainty about the true effective population size
#
# The 'NB' R package by Tin-Yu Hui can calculate the likelihood of a given
# value of NE, for a dataset consisting of allele counts at 1 or more loci
# observed in 2 or more temporally separated samples of a populations.
#
# This module takes a set of log-likelihoods for a range of Ne values, as output
# by the NB package. It then sets up a sampler that returns Ne values based on
# their probablilities.
#
# The required format is a 2-column, tab-separated set of Ne values and
# associated log likelihoods i.e.:
#
#
# 148	-545.948847356686
# 149	-545.904270578429
# 150	-545.860620288316
# ...  ...
# 1147	-545.508536956412

import csv
import numpy as np

class NeGenerator:
    
    def readLikelihoods (self,
                         inFileName):
        '''Read in a set of Ne values and corresponding log likelihoods'''
        rdr = csv.reader(open(inFileName), delimiter = '\t')
        Ne = []
        lLikes = []
        #self.Ne = np.array([], dtype = np.int64)
        #self.lLikes = np.array([], dtype = np.float64)        
        for n, l in rdr:
            Ne.append(n)
            lLikes.append(l)
        self.Ne = np.array(Ne, dtype = np.int64)
        self.lLikes = np.array(lLikes, dtype = np.float64)
    
    def getSamplingProbs (self):
        '''Generate sampling probabilities fo Ne values provided in the input file
        
        Will throw an AssertionError if the smallest log likelihood would be converted
        to a probablility too small to be represented by s 64-bit float'''
        
        #maxLogLike = np.log(np.finfo(dtype = np.float64).max)
        
        #Taking the log of np.finfo().min directly causes an error
        minLogLike = - np.log(- np.finfo(dtype = np.float64).min)
        # check that we won't end up with a prob < machine min
        assert np.min(self.lLikes) > minLogLike
        self.samplingProbs = np.exp(self.lLikes) / np.sum(np.exp(self.lLikes))
    
    def __init__(self,
                 inFileName):
        self.readLikelihoods(inFileName)
        self.getSamplingProbs()
        
    def getNe(self):
        '''Provide a randomly sampled value of Ne'''
        return np.random.choice(self.Ne, p = self.samplingProbs)
        