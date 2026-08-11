from Bio.Blast import NCBIWWW
from Bio import SeqIO

# Running over internet
#help(NCBIWWW.qblast)

sequence_record = next(SeqIO.parse(open("blast_example.fasta"), "fasta"))
print(sequence_record.seq)

result_handle = NCBIWWW.qblast("blastn", "nt", sequence_record.seq, format_type="html")
print(result_handle) # blast_result object

with open("blast_result.html", "w") as f:
    blast_result = result_handle.read()
    f.write(blast_result)

result_handle.close()