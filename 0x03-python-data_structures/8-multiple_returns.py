#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        ntuple = (len(sentence), None)
    else:
        ntuple = (len(sentence), sentence[0])
    return ntuple
