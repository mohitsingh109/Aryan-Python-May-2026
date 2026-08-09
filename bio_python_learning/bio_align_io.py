from Bio import AlignIO
from Bio import pairwise2
from Bio.pairwise2 import format_alignment
from Bio.Seq import Seq

# AlignIO --> Also created a SeqRecord
file = open("PF18225.alignment.seed")
alignment = AlignIO.read(file, "stockholm")
# print(alignment)

# for align in alignment:
#     print(f"Type: {type(align)}")
#     print(align.seq)

# Pairwise Sequence Alignment


seq1 = Seq("LQNIPRAQLPALIKEARDEHNVRVWLLDRQGSDLAGADVPPAVHDLARELQGRKRRAFSRSPDG")
seq2 = Seq("LQNQPNDALAATIAEVYQEHRVKVFLLNEASEDVLGRRVPAQVSEVAQRLGDGSRRAFLRGDRR")
# globalxx --> it find the best possible alignment between two sequences
alignments_between_two_seq = pairwise2.align.globalxx(seq1, seq2)

# for alignment in alignments_between_two_seq:
#     print(alignment)

for alignment in alignments_between_two_seq:
    print(format_alignment(*alignment))