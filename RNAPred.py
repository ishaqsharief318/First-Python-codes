import sys,string
from numpy import *

rnafile=open(sys.argv[1], 'r')
seq_list=[]
for line in rnafile.readlines():
	seq_list.append(string.strip(line));
allowed= "A,C,G,U"
for i in seq_list[1]:
	if i not in allowed:
		print "Error in file"
		sys.exit()
out_file = open(sys.argv[2],'w')

def delta(l,m):
	delta=0;
	if l=='A' and m=='U':
		return 1;
	elif l=='U' and m=='A':
		return 1;
	elif l=='G' and m=='C':
		return 1;
	elif l=='C' and m=='G':
		return 1;
	elif l=='G' and m=='U':
		return 1;
	elif l=='U' and m=='G':
		return 1;
	else:
		return 0;

def matrix(seq_list):
	L=len(seq_list);
	s=zeros((L,L));
	for n in xrange(1,L):
		for j in xrange(n,L):
			i=j-n;
			score1=s[i+1,j-1]+delta(seq_list[i],seq_list[j]);
			score2=s[i+1,j];
			score3=s[i,j-1];
			if i+3<=j:
				rna=[];
				for k in xrange(i+1,j):
					rna.append(s[i,k]+s[k+1,j]);
				score4=max(rna);
				s[i,j]=max(score1,score2,score3,score4);
			else:
				s[i,j]=max(score1,score2,score3);
	return s;

def traceback(s,seq_list,i,j,pair):
	if i<j:
		if s[i,j]==s[i+1,j]:
			traceback(s,seq_list,i+1,j,pair);
		elif s[i,j]==s[i,j-1]:
			traceback(s,seq_list,i,j-1,pair);
		elif s[i,j]==s[i+1,j-1]+delta(seq_list[i],seq_list[j]):
			pair.append([i,j,str(seq_list[i]),str(seq_list[j])]);
			traceback(s,seq_list,i+1,j-1,pair);
		else:
			for k in xrange(i+1,j):
				if s[i,j]==s[i,k]+s[k+1,j]:
					traceback(s,seq_list,i,k,pair);
					traceback(s,seq_list,k+1,j,pair);
					break;
	return pair;

for q in xrange(0,len(seq_list)):
	pair=traceback(matrix(seq_list[q]),seq_list[q],0,len(seq_list[q])-1,[])
	out1= "\n\nNumber of folding pairs possible for given sequence: "+str(len(pair));
	for x in xrange(0,len(pair)):
		out2= '\n %s--%s' % (pair[x][2],pair[x][3]);
		out_file.write(out2)
#print (out1)
#print (out2)
out_file.write(out1)
#out_file.write(out2)
