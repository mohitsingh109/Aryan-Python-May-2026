from Bio import SeqIO, Blast

# record = SeqIO.read("blast_example_1.fasta", "fasta")
#
# result_stream = Blast.qblast("blastn", "nt", record.seq, format_type="JSON2")
#
# data = result_stream.read()
#
# # it's in byte format so that data can be transfer fast
# print(data[:4])  # b'PK\x03\x04'
#
# # Write the zip file
# with open("myzipfile.zip", "wb") as f:
#     f.write(data)

# Read the zip file
import zipfile

myzipfile = zipfile.ZipFile("myzipfile.zip")
file_list = myzipfile.namelist() # List of file names ['87N79GNG016.json', '87N79GNG016_1.json']
print(file_list)
stream = myzipfile.open(file_list[0])
data = stream.read()
data = data.decode()
print(data)

stream = myzipfile.open(file_list[1])
data = stream.read()
data = data.decode()
print(type(data), data)

# convert str to json
import json
d = json.loads(data)
print(type(d))
program = d["BlastOutput2"]["report"]["program"]
version = d["BlastOutput2"]["report"]["version"]
print(program)
print(version)

