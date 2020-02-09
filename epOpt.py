import sys

CDS = sys.argv[1]

with open(CDS) as seqfile:
    f= seqfile.readlines()

    seq = f[1]
    print(seq)
    seqLen = (len(seq)-1)/3

    protein = {}
