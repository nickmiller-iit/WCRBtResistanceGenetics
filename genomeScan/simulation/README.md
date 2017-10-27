# Simulation code for genome scans.

Simulations of drift in a pair of colonies derived from an initial field population x non-diapause colony mass mating. Needed to get the neutral distribution of divergence between colonies so that we can identify outliers that are candidates for responding to selection.

The basic approach is a very simple coalescent. Because we are working on very short time scales, we ignore the possibility of mutation. We are also working with small populations relative to sample size, so we step back generation by generation. we only need step back to the initial hybrid population (i.e. we don't go all the way to most recent common ancestor). This makes things very simple and we can run a "stripped down" coalescent where we don't care about branch lengths. 
