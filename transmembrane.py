#!/usr/bin/env python3

# Write a program that predicts if a protein is trans-membrane
# Trans-membrane proteins have the following properties
#	Signal peptide: https://en.wikipedia.org/wiki/Signal_peptide
#	Hydrophobic regions(s): https://en.wikipedia.org/wiki/Transmembrane_protein
#	No prolines (alpha helix)
# Hydrophobicity is measued via Kyte-Dolittle
#	https://en.wikipedia.org/wiki/Hydrophilicity_plot
# For our purposes:
#	Signal peptide is 8 aa long, KD > 2.5, first 30 aa
#	Hydrophobic region is 11 aa long, KD > 2.0, after 30 aa

import gzip
import sys

def read_fasta(filename):
	name = None
	seqs = []
	
	fp = None
	if filename == '-':
		fp = sys.stdin
	elif filename.endswith('.gz'):
		fp = gzip.open(filename, 'rt')
	else:
		fp = open(filename)

	for line in fp.readlines():
		line = line.rstrip()
		if line.startswith('>'):
			if len(seqs) > 0:
				seq = ''.join(seqs)
				yield(name, seq)
				name = line[1:]
				seqs = []
			else:
				name = line[1:]
		else:
			seqs.append(line)
	yield(name, ''.join(seqs))
	fp.close()

def kd(seq):
	score = 0
	for aa in seq:
		if aa == "I": score += 4.5
		elif aa == "L": score += 3.8
		elif aa == "V": score += 4.2
		elif aa == "F": score += 2.8
		elif aa == "C": score += 2.5
		elif aa == "M": score += 1.9
		elif aa == "A": score += 1.8
		elif aa == "G": score -= 0.4
		elif aa == "T": score -= 0.7
		elif aa == "S": score -= 0.8
		elif aa == "W": score -= 0.9
		elif aa == "Y": score -= 1.3
		elif aa == "P": score -= 1.6
		elif aa == "H": score -= 3.2
		elif aa == "E": score -= 3.5
		elif aa == "Q": score -= 3.5
		elif aa == "D": score -= 3.5
		elif aa == "N": score -= 3.5
		elif aa == "K": score -= 3.9
		elif aa == "R": score -= 4.5
	return score/len(seq)

def trans(seq, kd, length):
	for i in range(len(seq) -length +1):
		peptide = seq[i:i+length]
		if get(peptide) >= kd and 'P' not in peptide:
			return True
	return False

for name, seq in read_fasta('proteins.fasta.gz'):
	nterm = seq[0:30]
	cterm = seq[30:len(seq)]
	if trans(nterm, 8, 2.5) and trans(cterm, 11, 2.0): print(name)
	break
	
	
"""
18w
Dtg
Krn
Lac
Mcr
PRY
Pxt
Pzl
QC
Ror
S1P
S2P
Spt
apn
bai
bdl
bou
bug
cue
drd
ft
grk
knk
ksh
m
nac
ort
rk
smo
thw
tsg
waw
zye
"""
