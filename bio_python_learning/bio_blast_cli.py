import subprocess

BLASTP = "/usr/local/ncbi-blast-2.17.0+/bin/blastp"

CMD = [
    BLASTP,
    "-query",
    "/Users/mohitsingh/PycharmProjects/Aryan-Python-May-2026/swissprot.fasta",
    "-db",
    "/Users/mohitsingh/blastdb/swissprot",
    "-outfmt",
    "5",
    "-out",
    "/Users/mohitsingh/PycharmProjects/Aryan-Python-May-2026/result.xml"
]

result = subprocess.run(
    CMD,
    capture_output=True,
    text=True,
)

print("Return code:", result.returncode) # 0

if result.stdout:
    print(result.stdout)

if result.stderr:
    print(result.stderr)

if result.returncode == 0:
    print("BLAST completed successfully")
    print("Result saved to result.xml")