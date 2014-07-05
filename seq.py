import sys, string
from numpy import *
from matplotlib import *

#read the first sequence
f1=open(sys.argv[1], 'r')
seq1=f1.readline()
seq1=string.strip(seq1)

#read the second sequence
f2=open(sys.argv[2], 'r')
seq2=f2.readline()
seq2=string.strip(seq2)

#read in BLOSUM62 matrix
#f3=open(sys.argv[3],'r')
#BLOSUM62=[]
#for line in f3.readlines():
 # BLOSUM62.append(map(int, line.split()))

#define similar amino acids
#similarAA=['ST','TS','SP','PS','SA','AS','SG','GS','TP','PT','TA','AT','TG','GT','PA','AP','PG','GP','AG','GA','ND','DN','NE','EN','NQ','QN','DE','ED','DQ',
#'QD','EQ','QE','HR','RH','HK','KH','RK','KR','MI','IM','ML','LM','MV','VM','IL','LI','IV','VI','LV','VL','FY','YF','FW','WF','YW','WY'];

m,n =  len(seq1),len(seq2) #length of two sequences

penalty= -2;   #define the gap penalty
mismatch = -1;
match = 2; 

#generate DP table and traceback path pointer matrix
score=zeros((m+1,n+1))   #the DP table
pointer=zeros((m+1,n+1))  #to store the traceback path

P=0;

#def match_score(alpha,beta,BLOSUM62): #the function to find match/dismatch score from BLOSUM62 by letters of AAs
 # alphabet={}
  #alphabet["A"] = 0
  #alphabet["R"] = 1
  #alphabet["N"] = 2
  #alphabet["D"] = 3
  #alphabet["C"] = 4
  #alphabet["Q"] = 5
  #alphabet["E"] = 6
  #alphabet["G"] = 7
  #alphabet["H"] = 8
  #alphabet["I"] = 9
  #alphabet["L"] = 10
  #alphabet["K"] = 11
  #alphabet["M"] = 12
  #alphabet["F"] = 13
  #alphabet["P"] = 14
  #alphabet["S"] = 15
  #alphabet["T"] = 16
  #alphabet["W"] = 17
  #alphabet["Y"] = 18
  #alphabet["V"] = 19
  #alphabet["B"] = 20
  #alphabet["Z"] = 21
  #alphabet["X"] = 22
  #lut_x=alphabet[alpha]
  #lut_y=alphabet[beta]
  #return BLOSUM62[lut_x][lut_y]

max_score=P;  #initial maximum score in DP table

#calculate DP table and mark pointers
for i in range(1,m+1):
  for j in range(1,n+1):
    score_up=score[i-1][j]+penalty;
    score_down=score[i][j-1]+penalty;
    if seq1[i]== seq2[j]:
    	score_diagonal=score[i-1][j-1]+match;
    else:
	score_diagonal = score[i-1][j-1]+mismatch;
    score[i][j]=max(0,score_up,score_down,score_diagonal);
    if score[i][j]==0:
      pointer[i][j]=0; #0 means end of the path
    if score[i][j]==score_up:
      pointer[i][j]=1; #1 means trace up
    if score[i][j]==score_down:
      pointer[i][j]=2; #2 means trace left
    if score[i][j]==score_diagonal:
      pointer[i][j]=3; #3 means trace diagonal
    if score[i][j]>=max_score:
      max_i=i;
      max_j=j;
      max_score=score[i][j];
#END of DP table


align1,align2='',''; #initial sequences

i,j=max_i,max_j; #indices of path starting point

#traceback, follow pointers
while pointer[i][j]!=0:
  if pointer[i][j]==3:
    align1=align1+seq1[i-1];
    align2=align2+seq2[j-1];
    i=i-1;
    j=j-1;
  elif pointer[i][j]==2:
    align1=align1+'-';
    align2=align2+seq2[j-1];
    j=j-1;
  elif pointer[i][j]==1:
    align1=align1+seq1[i-1];
    align2=align2+'-';
    i=i-1;
#END of traceback

align1=align1[::-1]; #reverse sequence 1
align2=align2[::-1]; #reverse sequence 2

i,j=0,0;

#calcuate identity, similarity, score and aligned sequeces
def result(align1,align2):
  symbol='';
  found=0;
  score=0;
  penalty=-2;
  identity,similarity=0,0;
  for i in range(0,len(align1)):
    if align1[i]==align2[i]:     #if two AAs are the same, then output the letter
      symbol=symbol+align1[i];
      identity=identity+1;
      similarity=similarity+1;
      score=score+match(align1[i],align2[i]);
    elif align1[i]!=align2[i] and align1[i]!='-' and align2[i]!='-': #if they are not identical and none of them is gap
      score=score+match(align1[i],align2[i]);
      for j in range(0,len(similarAA)-1):
        if align1[i]+align2[i]==similarAA[j]: #search whether these two AAs form a pair in similar AA table
          found=1;
      if found==1:
        symbol=symbol+':';   #if they are similar AA, output ':'
        similarity=similarity+1;
      if found==0:
        symbol=symbol+' ';  #o/w, output a space
      found=0;
    elif align1[i]=='-' or align2[i]=='-':   #if one of them is a gap, output a space
      symbol=symbol+' ';
      score=score+penalty;

  identity=float(identity)/len(align1)*100;
  similarity=float(similarity)/len(align2)*100;

  print 'Identity =', "%3.3f" % identity, 'percent';
  print 'Similarity =', "%3.3f" % similarity, 'percent';
  print 'Score =', score;
  print align1
  print symbol
  print align2
  #END of function result

  result(align1,align2,BLOSUM62)
