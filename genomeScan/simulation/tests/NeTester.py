

import sys, os

#add parent dir to path so we can import module to test
sys.path.append(os.getcwd() + "/..")

import NeGenerator as g

gr = g.NeGenerator("sample.logliks")

out = open("generatedNe.txt", "w")

sampleSize = 1000

for x in range(sampleSize):
    out.write(str(gr.getNe()) + '\n')

out.close()