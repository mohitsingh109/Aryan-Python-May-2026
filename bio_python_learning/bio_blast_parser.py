from Bio.Blast import NCBIXML

blast_records = NCBIXML.parse(open("blast_result.xml"))

E_VALUE_THRESHOLD = 1e-52

for record in blast_records:
   for alignment in record.alignments:
       for hsp in alignment.hsps:
           if hsp.expect >= E_VALUE_THRESHOLD:
               print("**Alignment:**")
               print("Sequence title:", alignment.title)
               print("Sequence length:", alignment.length)
               print("e-value:", hsp.expect)
               print(hsp.query)
               print(hsp.match)
               print(hsp.sbjct)
