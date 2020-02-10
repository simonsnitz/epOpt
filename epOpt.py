import sys
import random

CDS = sys.argv[1]

with open(CDS) as seqfile:
    f= seqfile.readlines()

    seq = f[1]
    seqLen = (len(seq)-1)/3
    
    worst = {
            'A':6,'C':6,'D':7,'E':6,'F':6,'G':4,'H':7,'I':6,'K':6,'L':4,'M':6,'N':7,'P':6,'Q':6,'R':4,'S':4,'T':5,'V':5,'W':5,'Y':6 }

    values = {
            'AAA':6,
            'AAC':7,
            'AAG':6,
            'AAT':7,
            'ACA':6,
            'ACC':5,
            'ACG':6,
            'ACT':5,
            'AGA':5,
            'AGC':6,
            'AGG':6,
            'AGT':6,
            'ATA':6,
            'ATC':7,
            'ATG':6,
            'ATT':7,
            
            'CAA':6,
            'CAC':7,
            'CAG':6,
            'CAT':7,
            'CCA':6,
            'CCC':6,
            'CCG':6,
            'CCT':6,
            'CGA':4,
            'CGC':6,
            'CGG':5,
            'CGT':6,
            'CTA':5,
            'CTC':6,
            'CTG':5,
            'CTT':6,
            
            'GAA':6,
            'GAC':7,
            'GAG':6,
            'GAT':7,
            'GCA':6,
            'GCC':6,
            'GCG':6,
            'GCT':6,
            'GGA':4,
            'GGC':6,
            'GGG':5,
            'GGT':6,
            'GTA':5,
            'GTC':6,
            'GTG':5,
            'GTT':6,
            
            'TAA':0,
            'TAC':6,
            'TAG':0,
            'TAT':6,
            'TCA':4,
            'TCC':6,
            'TCG':5,
            'TCT':6,
            'TGA':0,
            'TGC':6,
            'TGG':5,
            'TGT':6,
            'TTA':4,
            'TTC':6,
            'TTG':5,
            'TTT':6,
            }
    protein = {}

    def calcWorstScore(x):
        score = 0
        proLen = len(x)
        for i in range(0,proLen-1):
            score += worst[x[i]]
        print(score)
    
    def calcEvScore(x):
        score = 0
        codon = ''
        aalen = int((len(x)+1)/3)
        for i in range(0,aalen):
            m = 3*i
            codon = x[m]+x[m+1]+x[m+2]
            score += values[codon]
        print(score)
    
    def optEvScore(x):
        newCDS = ''
        aalen = int((len(x)+1)/3)
        for i in range(0,aalen):
            m = 3*i
            codon = x[m]+x[m+1]+x[m+2]
                #Glycine
            if codon == ('GGA'or'GGG'):
                newCDS += random.choice(['GGC','GGT'])
                #Leucine
            elif codon == ('TTA'or'TTG'or'CTA'or'CTG'):
                newCDS += random.choice(['CTC','CTT'])
                #Serine
            elif codon == ('TCA'or'TCG'):
                newCDS += random.choice(['TCC','TCT','AGC','AGT'])
                #Arginine
            elif codon == ('CGA'or'CGG'or'AGA'):
                newCDS += random.choice(['CGC','CGT','AGG'])
                #Threonine
            elif codon == ('ACC'or'ACT'):
                newCDS += random.choice(['ACA','ACG'])
                #Isoleucine
            elif codon == 'ATA':
                newCDS += random.choice(['ATC','ATT'])
                #Valine
            elif codon == ('GTA'or'GTG'):
                newCDS += random.choice(['GTC','GTT'])
            else:
                newCDS += codon
        print(newCDS)
        return newCDS
    
    #calcEvScore(seq)
    #newCDS = optEvScore(seq)
    #calcEvScore(newCDS)
    calcWorstScore(seq)

