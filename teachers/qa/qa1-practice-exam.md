# KB8029 Bioinformatics: practice exam for Q&A 1 (Sessions 1-6)

Q&A 1, Wednesday 10 March 2027

**Instructions.** You have 37 minutes. Answer on paper, on your own, with the same aids as in the written exam: pen, paper and up to five single-sided pages of your own notes; no computer, phone or calculator. There are four questions of 5 points each, so plan for about 9 minutes per question and move on if you get stuck. The numbers are chosen so that you can do every calculation by hand; show your working, because the working earns most of the points. Nothing is collected or graded: after the break you swap papers with a neighbour and mark each other's answers against the marking guide.

---

## Question 1: A global alignment with BLOSUM62 (5 p)

Align the two short protein sequences

$$
x = \texttt{WKIE}, \qquad y = \texttt{WRE}
$$

globally with the Needleman-Wunsch algorithm. Use the BLOSUM62 scores below as the substitution score $s(x_i, y_j)$ and a linear gap penalty of $g = -4$ per gap position.

|       | W  | K  | R  | I  | E  |
|-------|----|----|----|----|----|
| **W** | 11 | -3 | -3 | -3 | -3 |
| **K** | -3 | 5  | 2  | -3 | 1  |
| **R** | -3 | 2  | 5  | -3 | 0  |
| **I** | -3 | -3 | -3 | 4  | -3 |
| **E** | -3 | 1  | 0  | -3 | 5  |

The recurrence is

$$
V(i,j) = \max \begin{cases} V(i-1,j-1) + s(x_i, y_j) \\ V(i-1,j) + g \\ V(i,j-1) + g \end{cases}
$$

a. **(2 p)** Fill in the dynamic-programming matrix $V$ (5 rows × 4 columns, including the first row and column for the sequence starts), with $x$ down the side and $y$ along the top.

b. **(2 p)** Trace back from the correct cell, write down the optimal global alignment, and check its score by adding up the substitution scores and gap penalties of the alignment.

c. **(1 p)** In your alignment, K is paired with R and the gap is placed opposite I. Explain, using what a BLOSUM62 score means, why this placement scores better than putting the gap opposite K and pairing I with R.

---

## Question 2: A position-specific scoring matrix for a DNA motif (5 p)

A transcription factor binds the following four aligned 5-bp sites:

```
Position:  1 2 3 4 5
Site 1:    G A T T C
Site 2:    G A T A C
Site 3:    G T T T C
Site 4:    G A T A G
```

Build a PSSM with the recipe from Session 5. Add a pseudocount of $+1$ to the count of every base (A, C, G, T) at every position, use the background frequency $q_j = 0.25$ for every base, and compute

$$
S_{i,j} = \log_2 \frac{f_{i,j}}{q_j}
$$

where $f_{i,j}$ is the pseudocount-adjusted frequency of base $j$ at position $i$. You may use $\log_2 1.5 \approx 0.58$ and $\log_2 2.5 \approx 1.32$.

a. **(2 p)** Write down the pseudocount-adjusted frequencies and the PSSM (5 positions × 4 bases). Show how you got the score of one entry.

b. **(1 p)** Score the two candidate sites `GATTG` and `GTTCC` with your PSSM. Which one is the more likely binding site, and roughly how many times more likely is `GATTG` under the motif model than under the background model?

c. **(2 p)** Position 1 is G in all four sites, yet G scores only about 1.3 bits there. Explain why it does not get $\log_2(1/0.25) = 2$ bits, and what would happen to this score if the alignment had 400 sites that all had G at position 1. Then say what the score of `GTTCC` would be *without* pseudocounts, and why that is a problem.

---

## Question 3: Two models with the same RMSD (5 p)

Two predicted models, A and B, of the same 10-residue segment are each superimposed on the experimental structure. After superposition, the distances $d_i$ (in Å) between corresponding Cα atoms are:

| Residue | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Model A | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| Model B | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 4 | 4 |

In model B, residues 9 and 10 form a loop that sits in a different position from the experimental structure.

a. **(2 p)** Compute the RMSD of each model. Give the formula you use.

b. **(1 p)** Compute a TM-score for each model with

$$
\text{TM} = \frac{1}{L} \sum_{i=1}^{L} \frac{1}{1 + (d_i / d_0)^2}
$$

with $L = 10$ and, to keep the numbers simple, $d_0 = 2$ Å. (For real proteins $d_0$ depends on the length of the protein.)

c. **(2 p)** Which model is the better prediction, and why does the RMSD not show this while the TM-score does? A third program reports for model C "RMSD 0.8 Å", but over only 4 of the 10 residues. Is model C better than A and B? Explain.

---

## Question 4: Is it a globin? Sequence and structure evidence (5 p)

A colleague has a 128-residue protein from a soil bacterium. Its UniProtKB entry is unreviewed (TrEMBL) and is annotated as "globin-like protein". A BLASTP search of Swiss-Prot gives no hit with an E-value below 1.

a. **(1 p)** Where does an annotation like "globin-like protein" in an unreviewed entry usually come from, and why should you not take it at face value?

b. **(2 p)** Describe two ways to look for distant relatives that BLAST missed: a PSI-BLAST search, and a structure search with Foldseek using the protein's AlphaFold DB model. For each, say what information it uses and why it can find relationships that a single BLAST search with BLOSUM62 misses.

c. **(2 p)** Your colleague runs both. (The numbers are made up for this exercise.)

- **PSI-BLAST**, inclusion threshold E = 0.005. Round 2: 25 sequences included, all bacterial globins and flavohaemoglobins (E-values $10^{-6}$ to $10^{-3}$). Round 5: 600 sequences included, among them more than 200 myosins and tropomyosins (long coiled-coil proteins).
- **Foldseek**, AlphaFold DB model (mean pLDDT 88) against the PDB. Top hit: a truncated haemoglobin from *Mycobacterium tuberculosis*, TM-score 0.71, RMSD 2.1 Å over 112 aligned residues, 14% sequence identity. Next hit: human β-globin, TM-score 0.55.

What do you conclude about the protein? Which results do you trust, which not, and why? Name one further check you would make.
