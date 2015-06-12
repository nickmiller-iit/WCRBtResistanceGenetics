__author__ = 'nick'

import numpy as np
import scipy.stats as st

class singleAllele:

    def generateFreqSet(self,
                        increment):
        '''Generates a set of possible allele frequencies

        The generated set ranges from 0 to 1, in steps of increment'''

        r = np.arange(start = 0, stop = 1, step = increment, dtype = np.float64)
        return np.append(r, np.array(1.0, dtype = np.float64))

    def generateFreqProbs(self,
                          count,
                          total,
                          freqSet):
        '''Generates a set of probabilities of sampling each possible allele frequency

        Count is the number of times the allele was observed in a sample, total is the number of observed alleles in
        the total sample.'''

        prb = [st.binom.pmf(count, total, x) for x in freqSet]
        prb = [x / np.sum(prb) for x in prb]
        return prb

    def __init__(self,
                 count,
                 total,
                 increment):
        '''Instantiate a new singleAllele frequency sampler, based on an observed sample of alleles

        count is the number of times the allele was observed in a sample, total is the size if the sample of alleles
        increment is specifies the increment in posssible allele frequencies between 0 and 1.'''

        self.freqSet = self.generateFreqSet(increment)
        self.probs = self.generateFreqProbs(count, total, self.freqSet)

    def getFreq(self):
        '''Get an allele frequency

        Allele frequencies are sampled according to their relative probabilities.'''
        return np.random.choice(self.freqSet, p = self.probs)




