from string import maketrans

bases = ["A","C","T","G"]
codons = [a+b+c for a in bases for b in bases for c in bases]
aasymbols = 'KNNKTTTTIIIMRSSRQHHQPPPPLLLLRRRR*YY*SSSSLFFL*CCWEDDEAAAAVVVVGGGG'
codon_table = dict(zip(codons,aasymbols))


lines = [line.strip() for line in open("rosalind_orf.txt")]
seq = lines[1]
print seq

def convert(string):
    aa= []
    prtn = ''
    for i in ([string[i:i+3] for i in range (0, len(string),3)]):
        if len(i) == 3:
            prtn += (codon_table[i])
    flag = False
    for i in prtn:
        if i == 'M':
            flag = True
        if flag == True:
            aa.append(i)
        if i == '*':
            flag = False
            break
    return ''.join(aa)

read_frame1 = seq
print "1:" , convert(read_frame1)

read_frame2 = seq[1:]
print "2:" ,convert(read_frame2)

read_frame3 = seq[2:]
print "3:" ,convert(read_frame3)

read_frame4 = seq[::-1].translate(maketrans("ACGT","TGCA"))
print "4:" ,convert(read_frame4)

read_frame5 = read_frame4[1:]
print "5:" ,convert(read_frame5)

read_frame6 = read_frame4[2:]
print "6:" ,convert(read_frame6)
