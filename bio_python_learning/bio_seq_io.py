from Bio.SeqRecord import SeqRecord
from Bio.SeqIO import parse, write
from Bio.Seq import Seq

# file = open("ls_orchid.fasta", "r")
#
# for record in parse(file, "fasta"):
#     print(record)
#
# file.close()

# next() -> it is used to get the next element from the iterator. It returns the next item in the sequence and advances the iterator to the next position. If there are no more items, it raises a StopIteration exception.

# SeqRecord --> parse return the object of SeqRecord class

# first_seq_record = next(parse(open("ls_orchid.fasta"), "fasta"))
# print("Type: ", type(first_seq_record))
# print(f"Id: {first_seq_record.id}")
# print(f"Name: {first_seq_record.name}")
# print(f"Description: {first_seq_record.description}")
# print(f"Sequence: {first_seq_record.seq}")


# seq_itr = parse(open("ls_orchid.fasta"), "fasta")
# all_seq = [seq_record for seq_record in seq_itr]
# print(len(all_seq))
#
# max_seq_len = max(len(seq_record.seq) for seq_record in all_seq)
# print(max_seq_len)

#seq_record = SeqRecord
# Write fasta file
file = open("write_learning.fasta", "w")
# Changes in fasta file to add new seq record
# seq_record = SeqRecord(
#     id = "gi|2765658|emb|Z78533.1|CIZ78533",
#     seq = Seq("CGTAACAAGGTTT"),
#     name = "Aryan",
#     description = "This is bio python",
#     annotations={
#         'molecule_type': 'DNA'
#     }
# )
# write([seq_record], file, format="fasta")
#
# file = open("write_learning.gbk", "w")
# write([seq_record], file, format="genbank")
# file.close()

seq_record = next(parse(open("ls_orchid.gbk"), "genbank"))
print(f"Id: {seq_record.id}")
print(f"Name: {seq_record.name}")
print(f"Description: {seq_record.description}")
print(f"Sequence: {seq_record.seq}")
print(f"Annotations: {seq_record.annotations}")
