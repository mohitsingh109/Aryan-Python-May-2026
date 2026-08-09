from Bio.Seq import Seq

# Seq ---> It use internally byte array (because of byte array you can perform any array operation)
# byte array ---> string

dna = Seq('ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG')

print(f"DNA: {dna}")
print(f"Length: {len(dna)}")
print(f"First nucleotide: {dna[0]}")
print(f"First three nucleotides: {dna[0:3]}")
print(f"Count of 'A': {dna.count('A')}")

new_seq = Seq('AGCT') + dna
print(f"New sequence: {new_seq}")

rna = Seq('agct')
rna = rna.upper()
print(f"RNA: {rna}")

print(f"Find G: {dna.find('G')}")
print(f"Reverse Find G: {dna.rfind('G')}")
print(f"Check if T is present: {'T' in dna}")
print(f"Split Sequence By A: {dna.split('A')}")

strip_seq = Seq('  AGCT  ')
strip_seq = strip_seq.strip()
print(f"Stripped sequence: {strip_seq}")

# Complement
complement_seq = dna.complement()
print(f"Complement sequence: {complement_seq}")

# Reverse Complement
reverse_complement_seq = dna.reverse_complement()
print(f"Reverse complement sequence: {reverse_complement_seq}")

# DNA -> RNA
rna = dna.transcribe() # T --> U
print(f"RNA: {rna}")
print(f"Reverse the DNA from RNA: {rna.back_transcribe()}")

# Translation
protein = dna.translate()
print(f"Protein: {protein}")
print(f"Protein without break: {dna.translate(to_stop=True)}")

from Bio.Data import CodonTable, IUPACData
table = CodonTable.unambiguous_dna_by_name['Standard']
print(table)
print(f"Protein letters: {IUPACData.protein_letters}")

