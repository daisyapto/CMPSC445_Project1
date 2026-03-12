# Daisy Aptovska
# Project 1 - CMPSC 445
# Due: 3/17/26
from dataCol import *
from dataPre import *
from modelDev import *
from featureRank import *
from dataVis import *

def main():
    dc = dataCollection()
    dp = dataPreprocessing(dc)
    md = modelDevelopment(dp)
    fr = featureRank(md)
    #dv = dataVisualization(fr)

if __name__ == '__main__':
    main()

