# %% [markdown]
# # Session 2 live coding: six globins, and three kinds of mistakes
#
# Instructor script for the Session 2 lecture (about 20 minutes). Run it cell by
# cell in VS Code ("# %%" cells) or paste the cells into a notebook. Type the
# code live rather than pasting it; the point is to show how you find and fix
# problems. The three planted mistakes are marked MISTAKE 1-3. Type the wrong
# version first, let the class see what happens, then fix it.
#
# 1. A Python error (KeyError): the easy kind; Python tells you.
# 2. Correct code, wrong analysis (swapped axes): nothing fails.
# 3. A biologically nonsensical result (protein length from mRNA length):
#    nothing fails, and the numbers look plausible unless you know the biology.
#
# Mistakes 2 and 3 are the important ones. AI assistants are very good at
# removing errors of the first kind, and do much less to stop you answering
# the wrong question.

# %% Step 1: fetch six globin mRNAs from NCBI (one request)
from Bio import Entrez, SeqIO
from Bio.SeqUtils import gc_fraction
import pandas as pd
import matplotlib.pyplot as plt

Entrez.email = "your.name@su.se"          # use your own address
accessions = ["NM_000518.5", "NM_000558.5", "NM_000517.6",
              "NM_001382809.1", "NM_021257.4", "NM_134268.5"]
names = ["HBB", "HBA1", "HBA2", "MB", "NGB", "CYGB"]

try:
    with Entrez.efetch(db="nuccore", id=",".join(accessions), rettype="gb", retmode="text") as handle:
        records = list(SeqIO.parse(handle, "genbank"))
except Exception as err:                   # no network in the lecture hall: use the stored values
    print("NCBI not reachable:", err)
    records = None

# %% Step 2: a DataFrame, one row per gene
if records:
    genes = pd.DataFrame({"gene": names,
                          "length": [len(r.seq) for r in records],
                          "gc_content": [gc_fraction(r.seq) for r in records]})
else:
    genes = pd.DataFrame({"gene": names,
                          "length": [628, 577, 576, 1286, 1778, 1962],
                          "gc_content": [0.513, 0.645, 0.644, 0.553, 0.623, 0.623]})
genes

# %% MISTAKE 1: a Python error
# Type this first:
#     genes["gc"].mean()
# -> KeyError: 'gc'. Read the LAST line first: no column called "gc".
# Inspect instead of guessing:
print(genes.columns)
print(genes["gc_content"].mean())          # the fix

# %% MISTAKE 2: correct code, wrong analysis
# Question: "Is GC content related to mRNA length?", so length should be
# on the x-axis and GC content on the y-axis. Type the swapped version:
#     plt.scatter(genes["gc_content"], genes["length"])
#     plt.xlabel("mRNA length (nt)"); plt.ylabel("GC content")
# It runs, and the labels even look right. Ask the class: which gene is on
# the far right? (CYGB, the longest mRNA, should be.) Now read the tick
# values: the x-axis runs 0.5-0.65. That is GC content, not length. The
# labels are wrong, not the data. Fix the call:
plt.scatter(genes["length"], genes["gc_content"])
plt.xlabel("mRNA length (nt)"); plt.ylabel("GC content")
for _, row in genes.iterrows():
    plt.annotate(row["gene"], (row["length"], row["gc_content"]))
plt.show()
# Lesson: check that each axis shows what its label says, e.g. by locating
# one point you know.

# %% MISTAKE 3: a biologically nonsensical result
# "Every three nucleotides code for one amino acid, so protein length is
# length / 3." Type:
genes["protein_length"] = genes["length"] // 3
genes
# CYGB: 654 amino acids, HBB: 209. Nothing failed. But globins are about 150
# amino acids long (one globin fold). Ask: what is wrong with the biology?
# The mRNA includes untranslated regions (5' and 3' UTRs); only the coding
# sequence (CDS) is translated. Use the CDS annotated in the record:

# %% The fix: use the CDS feature
if records:
    protein_lengths = []
    for r in records:
        cds = [f for f in r.features if f.type == "CDS"][0]
        protein_lengths.append(len(cds.qualifiers["translation"][0]))
    genes["protein_length"] = protein_lengths
else:
    genes["protein_length"] = [147, 142, 142, 154, 151, 190]
genes["untranslated"] = genes["length"] - 3 * genes["protein_length"] - 3   # minus the stop codon
genes
# Proteins 142-190 aa; the mRNAs differ threefold because of the UTRs.
# Lesson: sanity-check results against what you know about the biology.
