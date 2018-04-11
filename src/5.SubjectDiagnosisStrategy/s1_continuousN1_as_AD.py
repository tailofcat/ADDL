#!/usr/bin/env python

from __future__ import print_function

import os
import csv
import sys

inputFile = sys.argv[1]

recordList = []

isFirstLine = True
with open(inputFile, 'r') as ifile:
  for line in ifile:
    if isFirstLine: isFirstLine = False; continue

    res = str.split(line[:-2], ',')
    assert len(res) == 69
    for ii in xrange(1, len(res)):
      res[ii] = int(res[ii])

    subjectRecord = []
    subjectRecord += res[:5]
    subjectRecord.append(res[7:])
    recordList.append(subjectRecord)

#print(recordList)
#print(len(recordList))


def hasContinuousN1(N, sliceResList):
  assert N >= 1 and N <= 62

  retval = 0

  nContinuous1 = 0
  for item in sliceResList:
    if item == 1:
      nContinuous1 += 1
      if nContinuous1 >= N:
        retval = 1
        break
    else: # item == 0
      nContinuous1 = 0

  return retval


for N in xrange(1,63):
  totalSubject = 0
  totalRight   = 0

  for sbjRec in recordList:
    totalSubject += 1

    expRes = sbjRec[1]
    actRes = hasContinuousN1(N, sbjRec[-1])
    if expRes == actRes: totalRight += 1

  #print('N:', N, 'totalSubject:', totalSubject, 'totalRight:', totalRight, 'Accuracy:', float(totalRight)/float(totalSubject))
  print(float(totalRight)/float(totalSubject))
