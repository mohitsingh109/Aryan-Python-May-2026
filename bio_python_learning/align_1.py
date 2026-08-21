from Bio import Align

aligner = Align.PairwiseAligner()

# # align() --> that tell the alignment between two seq¯
#
target = "GAACTTT"
query = "GATTT"
#
alignments = aligner.align(target, query)

for alignment in alignments:
    print(alignment)

# score() ==> How good is the alignment
score = aligner.score(target, query)
print(score)

# Global Vs Local alignment

# Global alignment ==> How well can I align the entire seq against the entire other sequence
print("==============Global Mode======================")
aligner.mode="global"

alignments = aligner.align(target, query)

for alignment in alignments:
    print(alignment)

print("==============Local Mode======================")
# Local alignment ==> Which part of these sequences matches best
aligner.mode="local"

alignments = aligner.align(target, query)

for alignment in alignments:
    print(alignment)

# ======================
"""
Scoring:
Match: +1
Mismatch: -1
Gap: -2

A T G C
| | | |
A T G C

4 x +1 = 4
"""
aligner.match_score = 2
aligner.mismatch_score = -1
aligner.gap_score = -2
aligner.extend_gap_score = -5
aligner.open_gap_score = -5

print(aligner.score("TTTATCGTTT", "ACGT")) # 8
print(aligner.score("ATCGT", "ACGT")) # 6 (8 - 2(gap) = 6)
print(aligner.score("ACGT", "ACAT")) # 5 (3 x +2 -1 = 5 )

# Why Gap open & Gap extend exist

"""
ACGTAAAA
ACGT----

Gap score: open gap score + (gap length - 1) x extend gap score
"""

