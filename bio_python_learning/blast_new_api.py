from unittest import result

from Bio import Blast, Seq

#help(Blast.qblast)

seq = Seq.Seq("ggtaagtcctctagtacaaacacccccaatattgtgatataattaaaattatattcatattctgttgccagaaaaaacacttttaggctatattagagccatcttctttgaagcgttgtc")

result_stream = Blast.qblast("blastn", "nt", seq, format_type="html")

with open("blast_new_result.html", "wb") as f:
    blast_result = result_stream.read()
    f.write(blast_result)

result_stream.close()