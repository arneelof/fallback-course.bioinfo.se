# Session 2: Working like a computational biologist in Python

## Inside a class's method, what does `self` refer to?

- [x] The particular object the method was called on
- [ ] The class itself, shared by every object
- [ ] The module the class is defined in
- [ ] Nothing — `self` is optional and can be left out

## What is `__init__` for, in a Python class?

- [x] It's called automatically when a new object is created, to set up that object's initial data
- [ ] It's called every time any method on the object is called
- [ ] It converts the object to a string for printing
- [ ] It deletes the object when it's no longer needed

## `class Enzyme(Protein)` defines its own `__init__` but forgets `super().__init__(name, sequence)`. Creating `Enzyme("LYZ", seq, "3.2.1.17")` gives no error. What happens when you then call the inherited method `lyz.weight()`?

- [x] An AttributeError: the object has no `sequence`, because `Protein.__init__` never ran
- [ ] It works, because `Enzyme` inherits `weight()` from `Protein`
- [ ] Python raises the error already when the object is created
- [ ] `weight()` silently returns 0

## A PyTorch model is a class with `__init__` and `forward`. What runs when you write `model(x)`?

- [x] The special method `__call__`, which `nn.Module` defines to do some bookkeeping and then call `forward(x)`
- [ ] `__init__` again, which rebuilds the model for the new input
- [ ] Nothing: you must always write `model.forward(x)`
- [ ] The training loop, one step

## A single number, a list of 10 numbers and a 3×3 grid of numbers: which of them are tensors, in the general sense used in this course?

- [x] All three: tensors of dimension 0, 1 and 2
- [ ] Only the 3×3 grid, because a tensor needs at least two dimensions
- [ ] Only the list and the grid; a single number is a scalar, not a tensor
- [ ] None of them; tensors only exist inside PyTorch

## What does calling `.backward()` on a PyTorch tensor actually do?

- [x] It computes gradients by replaying the tensor's recorded operations backward and applying the chain rule
- [ ] It undoes the last operation performed on the tensor
- [ ] It reverses the order of the elements stored in the tensor
- [ ] It converts the tensor back into a plain Python list

## What does setting `requires_grad=True` on a tensor do?

- [x] It tells PyTorch to track operations on this tensor, so gradients can later be computed with respect to it
- [ ] It makes the tensor's values immutable
- [ ] It forces the tensor to be stored on the GPU
- [ ] It marks the tensor as a model's final output

## What does a pandas DataFrame add on top of a plain NumPy array?

- [x] Labeled rows and columns, so a table's columns can be referred to by name instead of position
- [ ] GPU acceleration that NumPy arrays lack
- [ ] Automatic differentiation of every stored value
- [ ] The ability to store more than two dimensions of data (NumPy arrays already support that)

## Compared to writing your own sequence class, what's the main practical advantage of using Biopython's `Seq` object?

- [x] It's a mature, widely used library with many more built-in sequence operations, so you don't have to reimplement standard ones yourself
- [ ] Biopython sequences use less computer memory than any custom class
- [ ] Only Biopython objects can be stored as a string
- [ ] A hand-written class always computes GC content incorrectly

## You have transcript lengths in a Python list, `lengths = [628, 577, 576]`. What does `lengths * 2` give?

- [x] The list repeated twice: [628, 577, 576, 628, 577, 576]
- [ ] Each length doubled: [1256, 1154, 1152]
- [ ] An error
- [ ] The sum of the lengths, doubled

## `df.describe()` on an RNA-seq results table shows that the largest p-value in the file is 0.12. What should you conclude?

- [x] The file is pre-filtered: it holds only genes with p below about 0.12, not all genes
- [ ] Every gene in the genome changed significantly
- [ ] The p-values were computed wrongly
- [ ] Nothing: the maximum p-value is not informative

## A histogram of log2 fold changes from that same file has an empty band around zero: no genes with very small changes. What is the most likely reason?

- [x] Genes with very small changes rarely reach p < 0.12, so the pre-filtering removed them
- [ ] Gene expression never stays the same between conditions
- [ ] The histogram has too few bins
- [ ] log2 of a fold change cannot be close to zero

## Pearson's r between raw mean expression and |log2 fold change| is -0.01 (p = 0.43), but a scatter plot with expression on a log axis shows a clear trend. What is the best next step?

- [x] Test what the plot shows: log-transform expression, or use Spearman's rank correlation
- [ ] Report that there is no relationship, since the test said so
- [ ] Remove the genes that don't fit the trend
- [ ] Use a larger significance threshold

## Why open files with `with open(path) as handle:` rather than `handle = open(path)`?

- [x] The file is closed automatically when the block ends, even if an error happens inside it
- [ ] It reads the file faster
- [ ] It is the only way to read FASTA files
- [ ] It decompresses the file automatically

## `df["log2FC"].mean()` raises `KeyError: 'log2FC'`. What is the quickest way to find the fix?

- [x] Inspect `df.columns` to see what the column is actually called
- [ ] Reinstall pandas
- [ ] Convert the DataFrame to a list
- [ ] Restart the computer

## An AI assistant suggests `from Bio.SeqUtils import GC`, and the import fails. What is the most likely explanation?

- [x] The suggestion is outdated: GC no longer exists in current Biopython, and the documentation names its replacement, gc_fraction
- [ ] Biopython is not installed
- [ ] The sequence is too short
- [ ] Imports only work in the first cell of a notebook

## An AI assistant's code runs without errors. What should you still do before using its result?

- [x] Verify it: run it on a small example with a known answer, and check shapes and ranges
- [ ] Nothing: code that runs is correct
- [ ] Run it twice to see if the result changes
- [ ] Ask the assistant whether it is correct

## You edit cell 3 but don't re-run it, then re-run cell 7, which uses a variable from cell 3. What does cell 7 use?

- [x] Cell 3's old value, still in memory from its last run
- [ ] Cell 3's new value, since notebooks stay in sync with the page
- [ ] Nothing: editing a cell deletes its variables
- [ ] An error is always raised

## Six human globin mRNAs range from 576 to 1,962 nt, but their proteins are all 142-190 amino acids. Where is most of the difference?

- [x] In the untranslated regions (UTRs) of the mRNAs
- [ ] In the introns of the mRNAs
- [ ] The longer mRNAs code for several proteins
- [ ] In the start codons

## `hbb = Seq("ATGGTGCATCTGACTCCTGAGGAGAAGTCT")` translates to MVHLTPEEKS. What does `hbb[1:].translate()` give?

- [x] A different, meaningless peptide with a stop codon (WCI*LLRRS), plus a warning about a partial codon
- [ ] The same protein, MVHLTPEEKS
- [ ] An error, because the sequence does not start with ATG
- [ ] An empty sequence

## Translating the whole HBB mRNA from its first base gives a peptide without a starting M and with 7 stop codons. Why?

- [x] The mRNA starts with a 50-nt untranslated region, so base 1 is in the wrong frame; the protein starts at the CDS
- [ ] The mRNA is corrupted
- [ ] Biopython cannot translate human sequences
- [ ] Hemoglobin consists of seven separate proteins

## `df[(df["padj"] < 0.05) and (df["log2_FoldChange"] > 1)]` raises "The truth value of a Series is ambiguous". What is the fix?

- [x] Use & instead of and, keeping the parentheses
- [ ] Remove the parentheses
- [ ] Convert the DataFrame to a list first
- [ ] Use a smaller threshold

## Which plot shows the distribution of a single variable?

- [x] A histogram
- [ ] A scatter plot
- [ ] A volcano plot
- [ ] A heatmap

## You meant to plot GC content against mRNA length but swapped the arguments to `plt.scatter`. The plot appears without errors. Which kind of mistake is this?

- [x] Correct code, wrong analysis
- [ ] A Python error
- [ ] A biologically nonsensical result
- [ ] Not a mistake, since the order of the arguments does not matter

## Computing protein length as mRNA length divided by 3 gives 654 amino acids for cytoglobin. Which kind of mistake is this?

- [x] A biologically nonsensical result: globins are about 150 amino acids, and the mRNA includes untranslated regions
- [ ] A Python error
- [ ] Correct: every three nucleotides code for one amino acid
- [ ] Correct code, wrong analysis: a column is misnamed

## Consider this function:

<!-- coding-exercise -->

```python
def gc_content(sequence):
    sequence = sequence.upper()
    gc = sum(1 for base in sequence if base in "GC")
    return gc / len(sequence)
```

Without running it: what does `gc_content("ttttaaaa")` return?

- [x] 0.0
- [ ] 0.5
- [ ] 1.0
- [ ] It raises an error, because the input isn't uppercase

## A notebook open in VS Code runs on a Colab machine and saves `results.csv`. Where is the file?

- [x] On the Colab machine, which is deleted when the session ends, unless you download it or write it to Google Drive
- [ ] In the same folder as the notebook on your laptop
- [ ] In your GitHub repository
- [ ] Nowhere: Colab notebooks cannot write files

## What does `git commit -m "Add volcano plot"` do?

- [x] Records a snapshot of the changes you have staged with `git add`, with a message, in your local repository's history
- [ ] Uploads your files to GitHub
- [ ] Downloads other people's changes
- [ ] Deletes the files you have changed

## In a Spearman correlation heatmap of an RNA-seq table, `log2_FoldChange` and `FC`, or `pvalue` and `minus_log10_pvalue`, have a correlation of exactly 1 or -1. Why?

- [x] Each column of such a pair is a monotonic transformation of the other, so their ranks are identical (or exactly reversed)
- [ ] The genes in the file are sorted by those columns
- [ ] The heatmap rounds all strong correlations to 1
- [ ] Spearman's correlation is 1 for any two columns from the same experiment
