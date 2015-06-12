__author__ = 'nick'

import numpy as np
import scipy.stats as st
import random

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


class MultiAllele:
    '''Simulates allele frequencies for a locus with an arbitrary number of alleles'''

    def __init__(self,
                 counts,
                 increment):
        '''A new MultiAllele object

        counts is a list of observed counts for each llele in a sample incerment in the step size between possible
        allele frequencies'''
        tot = sum(counts)
        self.alleles = [singleAllele(x, tot, increment) for x in counts]

    def getFreqs(self):
        '''Get a set of allele frequencies'''
        idx = range(len(self.alleles))
        random.shuffle(idx)
        freqs = [0.0 for i in idx]
        for i in idx[:-1]:
            freqs[i] = self.alleles[i].getFreq()
        freqs[idx[-1]] = 1.0 - sum(freqs)
        return freqs


