# Session 4: Sequence Alignment

## Human hemoglobin and human myoglobin are separated by an ancient gene duplication. What relationship do they have?

- [ ] Orthologs
- [x] Paralogs
- [ ] Analogs
- [ ] They are not homologous

## Two aligned protein sequences have several positions where the residues differ but are both hydrophobic amino acids. Counting these positions toward how well-matched the sequences are corresponds to measuring their:

- [ ] Identity
- [x] Similarity
- [ ] Homology
- [ ] Orthology

## For two sequences of length around 100, why is it infeasible to try every possible alignment and keep the best one?

- [x] The number of possible alignments grows so fast (around 10^59 for n=100) that exhaustive search is computationally impossible
- [ ] Computers cannot store sequences longer than 100 characters
- [ ] Substitution matrices are only defined for sequences shorter than 50 residues
- [ ] Alignment scores are undefined once gaps are allowed

## Filling a Needleman-Wunsch cell: V(i-1,j-1) = 2, V(i-1,j) = 1, V(i,j-1) = 0, the substitution score s(x_i, y_j) = -1 (mismatch), and the gap penalty g = -2. What is V(i,j)?

The three candidates are the diagonal (2 + (-1) = 1), from above (1 + (-2) = -1), and from the left (0 + (-2) = -2).

- [x] 1
- [ ] -1
- [ ] -2
- [ ] 0

## Smith-Waterman turns Needleman-Wunsch's global algorithm into a local one with one specific change to the DP matrix. What is that change?

- [x] Negative values in the matrix are reset to zero, and traceback starts from the highest-scoring cell anywhere and stops at a zero
- [ ] The substitution matrix is replaced with a different one
- [ ] The gap penalty is changed from linear to affine
- [ ] The matrix's rows and columns are transposed

## A linear gap penalty charges the same total cost whether gaps are spread out or bunched together. What biological problem does this cause?

- [x] It can scatter single gaps throughout an alignment, breaking up a conserved motif that should stay together as one block
- [ ] It makes the dynamic-programming algorithm run in exponential time instead of polynomial time
- [ ] It prevents the algorithm from ever placing a gap
- [ ] It only produces valid alignments for RNA sequences, not proteins

## With an affine gap penalty g(n) = g_open + (n-1) × g_ext, using g_open = -10 and g_ext = -1, what is the total penalty for a single gap of length 4?

- [x] -13
- [ ] -40
- [ ] -11
- [ ] -4

## Which pairing correctly describes how PAM and BLOSUM numbering relate to evolutionary distance?

- [x] A higher PAM number means a more distant comparison; a higher BLOSUM number means a more similar (closer) comparison
- [ ] A higher PAM number means a more similar comparison; a higher BLOSUM number means a more distant comparison
- [ ] Both a higher PAM number and a higher BLOSUM number mean a more distant comparison
- [ ] Neither PAM nor BLOSUM numbering relates to evolutionary distance

## What is the key methodological difference in how PAM and BLOSUM matrices are derived?

- [x] PAM is built from an explicit phylogenetic-tree model of closely related sequences, extrapolated by matrix powers; BLOSUM is counted directly from local alignments of distantly related sequences, with no extrapolation
- [ ] PAM is derived from local, ungapped alignments while BLOSUM is derived from global alignments
- [ ] PAM matrices are built from DNA sequences and BLOSUM matrices from protein sequences
- [ ] There is no methodological difference — only the numbering direction differs

## The core cell-filling line of the notebook's Smith-Waterman implementation is:

<!-- coding-exercise -->

```python
S[i, j] = max(diag, up, left, 0.0)
```

If the `, 0.0` were removed from this `max(...)` call, which algorithm would this function then effectively compute?

- [x] Needleman-Wunsch's global alignment recurrence — negative scores would propagate instead of being reset to zero
- [ ] It would raise a runtime error immediately
- [ ] The exact same local alignments, just with different displayed scores
- [ ] Local alignment with a different substitution matrix

## Which of the following would a dot plot NOT directly give you?

- [ ] A quick visual sense of roughly where two sequences match
- [ ] A way to spot a repeated subsequence, as parallel diagonals
- [x] The exact optimal alignment and its score
- [ ] A way to spot an inverted repeat, as a diagonal running the opposite way

## Shuffling one of two sequences many times and realigning gives a distribution of scores for unrelated sequences. The real alignment scores far above all of them. What does that suggest?

- [x] That chance is an unlikely explanation for the similarity, which is evidence (not proof) of homology
- [ ] That the two sequences are identical
- [ ] That the alignment contains no gaps
- [ ] That the substitution matrix was wrong

## An alignment column of a protein family has the same residue in every sequence. What are its entropy and information content?

- [x] Entropy 0 bits, information content log2(20) ≈ 4.32 bits: a fully conserved position
- [ ] Entropy 4.32 bits, information content 0 bits
- [ ] Both 0 bits
- [ ] It depends only on the number of sequences

## In the Pfam globin family logo, Phe42 and His92 (human HBB numbering) are identical in all 73 sequences. What is the most likely reason?

- [x] They are essential for binding the heme group, so mutations there are removed by selection
- [ ] Histidine and phenylalanine cannot mutate
- [ ] The alignment program forces the first residues to match
- [ ] All 73 sequences come from the same species

## Why can a sequence logo made from only five sequences be misleading?

- [x] With so few sequences, columns can look conserved by chance, and the maximum possible entropy of a column is only log2(5) bits
- [ ] Logos require exactly 20 sequences
- [ ] Five sequences always give a flat logo
- [ ] Entropy is undefined for fewer than ten sequences

## Human alpha-globin and mouse beta-globin come from different species. What is their relationship?

- [x] Paralogs: the duplication that separated the alpha- and beta-globin genes happened before human and mouse diverged
- [ ] Orthologs, because they are in different species
- [ ] Orthologs, because both are haemoglobin subunits
- [ ] Not homologous

## In a gene tree, a node whose two branches both contain human, mouse and chicken genes is most likely what kind of event?

- [x] A gene duplication, before those species diverged
- [ ] A speciation event
- [ ] A sequencing error
- [ ] A horizontal gene transfer between the three species

## Why should a guide tree built for progressive alignment not automatically be read as a phylogeny?

- [x] It is an ordering device, usually built by UPGMA, which assumes equal evolutionary rates; a fast-evolving sequence can be placed in the wrong group
- [ ] Because guide trees contain no branch lengths
- [ ] Because a guide tree is built after the alignment is finished
- [ ] Because phylogenies can only be built from DNA

## What does a bootstrap value of 95 on a branch of a phylogenetic tree mean?

- [x] The branch reappeared in 95% of trees rebuilt from alignments made by resampling the columns, so the data support it consistently
- [ ] The branch is 95% likely to be the true evolutionary history
- [ ] 95% of the residues on that branch are identical
- [ ] The branch is 95 million years old

## A BLOSUM62 entry for K-Q is +1. What does a positive substitution score mean?

- [x] K and Q are aligned in conserved blocks of related proteins more often than expected from their background frequencies (a log-odds score above 0)
- [ ] K mutates into Q in exactly 1% of generations
- [ ] K and Q are chemically identical
- [ ] The pair is always a mismatch
