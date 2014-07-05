import sys
from numpy import *
import re
string1 = ''
string2 = ''
sequence1 = open(sys.argv[1],'r')
for line in sequence1:

	if line.startswith(">"):
		pass
	else:
		string1 = string1 + line.strip()
for line in string1:
	if re.search("[B,J,O,U,X,Z]", line):
		print 'Error! Unrecognized Amino Acid encountered. Please enter a valid sequence'
		sys.exit()
sequence2 = open(sys.argv[2],'r')
for line in sequence2:
	if line.startswith(">"):
		pass
	else:
		string2 = string2 + line.strip()
for line in string2:
	if re.search("[B,O,U,X,J,Z]", line):
		print 'Error!  Unrecognized Amino Acid encountered. Please enter a valid sequence'
		sys.exit()
m = len(string1)-1 
n = len(string2)-1

gap_penalty = -2
match = 2
mismatch = -1

score = zeros((m+1 , n+1))
traceback = zeros ((m+1 , n+1))
max_score = 0

for i in range(1,m+1):
	for j in range(1,n+1):
		up=score[i-1][j]+gap_penalty
		down=score[i][j-1]+gap_penalty
		if string1[i-1] == string2[j-1]:
    			diagonal = score[i-1][j-1] + match
		else:
			diagonal = score[i-1][j-1] + mismatch	
    		score[i][j]=max(0,up,down,diagonal)
    		if score[i][j]==0:
      			traceback[i][j]=0 
    		if score[i][j]==up:
      			traceback[i][j]=1
    		if score[i][j]==down:
      			traceback[i][j]=2 
    		if score[i][j]==diagonal:
      			traceback[i][j]=3 
    		if score[i][j]>=max_score:
      			max_i=i
      			max_j=j
      			max_score=score[i][j];


aligned_seq1 = ''
aligned_seq2 = ''


while traceback [i][j]!=0:
	if traceback[i][j] == 3:
		aligned_seq1= aligned_seq1 + string1[i-1]
		aligned_seq2= aligned_seq2 + string2[j-1]
		i=i-1
		j=j-1
	elif traceback[i][j] == 2:
		aligned_seq1=aligned_seq1 + '-'
    		aligned_seq2= aligned_seq2 + string2 [j-1]
    		j=j-1
  	elif traceback[i][j]==1:
    		aligned_seq1 = aligned_seq1 + string1 [i-1]
    		aligned_seq2 = aligned_seq2+ '-'
    		i=i-1

aligned_seq1 = aligned_seq1 [: :-1]
aligned_seq2 = aligned_seq2 [: :-1]

file_out = open(sys.argv[3],'w')
file_out.write(aligned_seq1)
file_out.write('\n')
file_out.write(aligned_seq2)
