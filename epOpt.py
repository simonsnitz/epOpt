import sys

CDS = sys.argv[1]

with open(CDS) as seqfile:
    f= seqfile.readlines()

    seq = f[1]
    seqLen = (len(seq)-1)/3
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
            if codon == 'GGA':
                newCDS += 'GGC'
            elif codon == 'TTA':
                newCDS += 'CTC'
            elif codon == 'TCA':
                newCDS += 'TCC'
            elif codon == 'CGA':
                newCDS += 'CGC'
            else:
                newCDS += codon
        print(newCDS)
        return newCDS
    
    '''
    for i in range(0,int(seqLen)):
        m = 3*i
        protein[i] = seq[m]+seq[m+1]+seq[m+2]
        evScore += values[protein[i]]
    
        if protein[i] == 'GGA':
            newCDS += 'GGC'
        else:
            newCDS += protein[i]
        
        evScoreNewCDS += 
    '''
    calcEvScore(seq)
    newCDS = optEvScore(seq)
    
    calcEvScore(newCDS)
    #print(newCDS)
    #print(protein)
