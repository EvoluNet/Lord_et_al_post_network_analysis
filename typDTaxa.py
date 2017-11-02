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




treeLeaves = []
for leaf in tree.get_leaves():
        treeLeaves.append(leaf.name)
nodesTaxa = {}
nodeClade = {}
nodesTaxaPos = {}

with open("nodesTaxa.list",'r') as nodesInfo:
	for info in nodesInfo:
		info=info.rstrip()
		ID = info.split("\t")[0]
		TAXA = (info.split("\t")[1]).split(",")
		#print ID
		#print TAXA
		TAXA.sort()
		nodesTaxa[ID]=TAXA
		pos = []
		for i in TAXA:
			pos.append(treeLeaves.index(i))
		pos.sort()
		nodesTaxaPos[ID]=[pos[0],pos[-1],len(pos)]
		N=0
		for clade, taxa in cladesDico.iteritems():
			if taxa == nodesTaxa[ID]:
				nodeClade[ID]=clade
				N=1
			if N == 1:
				break
			
		
	

def PoT(n1,n2,n3):
	for n in tree.get_leaf_names():
		A="."
		B="."
		C="."
		if n in nodesTaxa[n1]:
			A="|"
		if n in nodesTaxa[n2]:
			B="|"
		if n in nodesTaxa[n3]:
			C="|"
		print(A+"\t"+B+"\t"+C+"\t"+n)
	

with open("typD.edges",'r') as edges:
	for nodes in edges:
		nodes=nodes.rstrip()
		n1,n2,n3 = nodes.split("\t")[0:3]
		pn1 = nodesTaxaPos[n1]
		pn2 = nodesTaxaPos[n2]
		pn3 = nodesTaxaPos[n3]
		if ((pn1[0] < pn3[0] and pn1[1] < pn3[0]) or (pn3[0] < pn1[0] and pn3[1] < pn1[0])) and (( pn1[0] < pn2[0] <= pn1[1] and pn3[0] <= pn2[1] < pn3[1]) or (pn3[0] < pn2[0] <= pn3[1] and pn1[0] <= pn2[1] < pn1[1])):
			if (n1 in nodeClade.keys()) and (n2 in nodeClade.keys()) and (n3 in nodeClade.keys()):
                                print ">ncaCladeCladeClade_"+str(n1)+"_"+str(n2)+"_"+str(n3)+"\n"
                                PoT(n1,n2,n3)
                                print "\n-----------------\n"
			elif (n1 not in nodeClade.keys()) and (n2 not in nodeClade.keys()) and (n3 not in nodeClade.keys()):
				print ">ncaNoCladeNoCladeNoClade_"+str(n1)+"_"+str(n2)+"_"+str(n3)+"\n"
				PoT(n1,n2,n3)
				print "\n-----------------\n"
			elif (n1 in nodeClade.keys()) and (n2 not in nodeClade.keys()) and (n3 not in nodeClade.keys()):
				print ">ncaCladeNoCladeNoClade_"+str(n1)+"_"+str(n2)+"_"+str(n3)+"\n"
				PoT(n1,n2,n3)
				print "\n-----------------\n"
			elif (n1 in nodeClade.keys()) and (n2 in nodeClade.keys()) and (n3 not in nodeClade.keys()):
				print ">ncaCladeCladeNoClade_"+str(n1)+"_"+str(n2)+"_"+str(n3)+"\n"
				PoT(n1,n2,n3)
				print "\n-----------------\n"
			elif (n1 not in nodeClade.keys()) and (n2 in nodeClade.keys()) and (n3 not in nodeClade.keys()):
				print ">ncaNoCladeCladeNoClade_"+str(n1)+"_"+str(n2)+"_"+str(n3)+"\n"
				PoT(n1,n2,n3)
				print "\n-----------------\n"
			elif (n1 not in nodeClade.keys()) and (n2 not in nodeClade.keys()) and (n3 in nodeClade.keys()):
				print ">ncaNoCladeNoCladeClade_"+str(n1)+"_"+str(n2)+"_"+str(n3)+"\n"
				PoT(n1,n2,n3)
				print "\n-----------------\n"
			elif (n1 not in nodeClade.keys()) and (n2 in nodeClade.keys()) and (n3 in nodeClade.keys()):
				print ">ncaNoCladeCladeClade_"+str(n1)+"_"+str(n2)+"_"+str(n3)+"\n"
				PoT(n1,n2,n3)
				print "\n-----------------\n"
		else :
			if (n1 in nodeClade.keys()) and (n2 in nodeClade.keys()) and (n3 in nodeClade.keys()):
                                print ">CladeCladeClade_"+str(n1)+"_"+str(n2)+"_"+str(n3)+"\n"
                                PoT(n1,n2,n3)
                                print "\n-----------------\n"
			elif (n1 not in nodeClade.keys()) and (n2 not in nodeClade.keys()) and (n3 not in nodeClade.keys()):
                                print ">NoCladeNoCladeNoClade_"+str(n1)+"_"+str(n2)+"_"+str(n3)+"\n"
                                PoT(n1,n2,n3)
                                print "\n-----------------\n"
                        elif (n1 in nodeClade.keys()) and (n2 not in nodeClade.keys()) and (n3 not in nodeClade.keys()):
                                print ">CladeNoCladeNoClade_"+str(n1)+"_"+str(n2)+"_"+str(n3)+"\n"
                                PoT(n1,n2,n3)
                                print "\n-----------------\n"
                        elif (n1 in nodeClade.keys()) and (n2 in nodeClade.keys()) and (n3 not in nodeClade.keys()):
                                print ">CladeCladeNoClade_"+str(n1)+"_"+str(n2)+"_"+str(n3)+"\n"
                                PoT(n1,n2,n3)
                                print "\n-----------------\n"
                        elif (n1 not in nodeClade.keys()) and (n2 in nodeClade.keys()) and (n3 not in nodeClade.keys()):
                                print ">NoCladeCladeNoClade_"+str(n1)+"_"+str(n2)+"_"+str(n3)+"\n"
                                PoT(n1,n2,n3)
                                print "\n-----------------\n"
                        elif (n1 not in nodeClade.keys()) and (n2 not in nodeClade.keys()) and (n3 in nodeClade.keys()):
                                print ">NoCladeNoCladeClade_"+str(n1)+"_"+str(n2)+"_"+str(n3)+"\n"
                                PoT(n1,n2,n3)
                                print "\n-----------------\n"
                        elif (n1 not in nodeClade.keys()) and (n2 in nodeClade.keys()) and (n3 in nodeClade.keys()):
                                print ">NoCladeCladeClade_"+str(n1)+"_"+str(n2)+"_"+str(n3)+"\n"
                                PoT(n1,n2,n3)

