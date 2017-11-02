#!/usr/bin/env python

from ete3 import *

tree = Tree("rhino_tree_reduced.newick")

cladesDico = {}

n=0
for node in tree.traverse():
	if not node.is_leaf():
		n+=1
		node.name = "C" + str(n)
		cladesDico[node.name]=(tree&node.name).get_leaf_names()
		(cladesDico[node.name]).sort()


nodesTaxa = {}
nodeClade = {}
with open("nodesTaxa.list",'r') as nodesInfo:
	for info in nodesInfo:
		info=info.rstrip()
		ID = info.split("\t")[0]
		TAXA = (info.split("\t")[1]).split(",")
		TAXA.sort()
		nodesTaxa[ID]=TAXA
		N=0
		for clade, taxa in cladesDico.iteritems():
			if taxa == nodesTaxa[ID]:
				nodeClade[ID]=clade
				N=1
			if N == 1:
				break
			
		
	

def PoT(n1,n2):
	for n in tree.get_leaf_names():
		A="."
		B="."
		if n in nodesTaxa[n1]:
			A="|"
		if n in nodesTaxa[n2]:
			B="|"
		print(A+"\t"+B+"\t"+n)
	

with open("typ2.edges",'r') as edges:
	for nodes in edges:
		nodes=nodes.rstrip()
		n1,n2 = nodes.split("\t")
		#print "r\t"+str(len(nodesTaxa[n1]))+"\t"+str(len(nodesTaxa[n2]))
		if (set([n1,n2])).issubset(set(nodeClade.keys())):
			print ">CladeInClade_"+str(n1)+"_"+str(n2)+"\n"
			PoT(n1,n2)
			print "\n-----------------\n"
		else:
			if (n1 in nodeClade.keys()) and (n2 not in nodeClade.keys()):
				print ">CladeNoClade_"+str(n1)+"_"+str(n2)+"\n"
				PoT(n1,n2)
				print "\n-----------------\n"
			elif (n1 not in nodeClade.keys()) and (n2 in nodeClade.keys()):
				print ">CladeNoClade_"+str(n1)+"_"+str(n2)+"\n"
				PoT(n1,n2)
				print "\n-----------------\n"
			elif (n1 not in nodeClade.keys()) and (n2 not in nodeClade.keys()):
				print ">NoCladeNoClade_"+str(n1)+"_"+str(n2)+"\n"
				PoT(n1,n2)
				print "\n-----------------\n"
			
		
	


#END
