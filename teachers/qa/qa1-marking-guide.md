# KB8029 Bioinformatics: marking guide for Q&A 1 (Sessions 1-6)

Q&A 1, Wednesday 10 March 2027

**How to mark.** Each question is worth 5 points. Give the points listed for each part, and use the partial-credit notes when an answer is only partly right. Give credit for correct reasoning even if an arithmetic slip makes the final number wrong, and do not take points off twice for one mistake that is carried forward (if an error in part a makes part b wrong, but part b is done correctly from the wrong numbers, part b gets full points). Answers in other words than the model answer are fine if they contain the same points. Where you and your partner disagree, ask a TA.

---

## Brain dump (7 minutes, before the practice exam)

Books and notes closed. Write everything you remember about these three topics. Afterwards, compare with the lists below: what you could not recall is what to revise first.

**1. Aligning two sequences by dynamic programming (Session 4).** A good brain dump contains:

- homology (orthologs, paralogs) as the reason to align, and an alignment as a hypothesis about which residues correspond;
- the matrix $V(i,j)$ and the recurrence (diagonal + $s(x_i,y_j)$, or a gap from above or the left), the first row and column, traceback;
- Needleman-Wunsch (global) versus Smith-Waterman (local: negative cells set to 0, traceback from the highest cell until a 0), and when to use which;
- linear versus affine gap penalties, $g(n) = g_{\text{op}} + (n-1)\,g_{\text{ext}}$;
- substitution matrices as log-odds scores; PAM (closely related, explicit evolutionary model, extrapolated; higher number = more distant) versus BLOSUM (conserved blocks of distant proteins; higher number = closer);
- a raw score alone is not evidence of homology.

**2. From BLAST to profiles (Session 5, with the logarithms of Session 1).** A good brain dump contains:

- why a database search cannot run full dynamic programming on every entry;
- BLAST's seed (words, neighbour words above threshold $T$), extend (X-drop), evaluate stages;
- $E = K m n\, e^{-\lambda S}$: the expected number of chance hits with score $\ge S$; it grows with database size and falls exponentially with score; bit scores;
- PSI-BLAST: iterate, inclusion threshold, PSSM, convergence, profile drift;
- building a PSSM: count, pseudocounts, background, $S_{i,j} = \log_2(f_{i,j}/q_j)$, score a sequence by summing;
- profile HMMs: match, insert and delete states; position-specific gaps; Pfam.

**3. Comparing protein structures (Session 6).** A good brain dump contains:

- the four levels of structure; secondary structure elements; hydrophobic effect; Anfinsen;
- distance maps and contact maps (rotation-invariant; local versus long-range contacts);
- structure is more conserved than sequence;
- RMSD (after superposition; length-dependent; sensitive to outliers; give the number of aligned residues) versus TM-score (0 to 1, length-normalised, about 0.5 = same fold);
- DALI (distance maps), TM-align, Foldseek (3Di alphabet, fast search);
- domains and CATH (Class, Architecture, Topology, Homologous superfamily), other classifications.

---

## Question 1: A global alignment with BLOSUM62 (5 p)

### a. The matrix (2 p)

| | – | W | R | E |
|---|---|---|---|---|
| **–** | 0 | -4 | -8 | -12 |
| **W** | -4 | **11** | 7 | 3 |
| **K** | -8 | 7 | **13** | 9 |
| **I** | -12 | 3 | **9** | 10 |
| **E** | -16 | -1 | 5 | **14** |

The first row and column are multiples of the gap penalty ($0, -4, -8, \dots$). Two example cells:

- $V(2,2)$ (K against R): $\max(V(1,1) + s(K,R),\ V(1,2) - 4,\ V(2,1) - 4) = \max(11 + 2,\ 7 - 4,\ 7 - 4) = 13$.
- $V(4,3)$ (E against E): $\max(V(3,2) + 5,\ V(3,3) - 4,\ V(4,2) - 4) = \max(14,\ 6,\ 1) = 14$.

**Points.** 0.5 p for the correct first row and column. 1.5 p for the interior: full points if all 12 cells are right, 1 p for one or two wrong cells, 0.5 p if the method is clearly right but there are more errors.

**Common mistakes.** Initialising the first row and column with zeros (that is the local, Smith-Waterman, initialisation). Adding the substitution score to the cell above or to the left instead of the diagonal one. Reading $s(x_i,y_j)$ from the wrong row or column of the BLOSUM62 table. Taking the minimum instead of the maximum.

### b. Traceback, alignment and score (2 p)

The traceback starts in the bottom-right cell, $V(4,3) = 14$, because the alignment is global. The path is $V(4,3) \to V(3,2)$ (diagonal, E–E) $\to V(2,2)$ (up: I against a gap) $\to V(1,1)$ (diagonal, K–R) $\to V(0,0)$ (diagonal, W–W). The alignment is

```
W K I E
W R - E
```

Score check: $s(W,W) + s(K,R) + g + s(E,E) = 11 + 2 - 4 + 5 = 14$, which equals $V(4,3)$. This optimal alignment is unique.

**Points.** 0.5 p for starting the traceback in the bottom-right cell. 1 p for the correct alignment. 0.5 p for the score check that adds up to 14.

**Common mistakes.** Starting the traceback in the highest cell of the matrix (that is the local rule; here it happens to be the same cell, so accept it only if the student says why the bottom-right cell is used). Writing the alignment backwards. Forgetting the gap penalty in the score check.

### c. Why K is paired with R (1 p)

**Model answer.** A BLOSUM62 score is a (scaled) log-odds score: the log of how often two residues are aligned in related proteins, divided by how often they would be paired by chance. K–R scores $+2$, so lysine and arginine (both positively charged) replace each other in related proteins more often than chance, and pairing them is evidence for the alignment. I–R scores $-3$, so that pairing is seen less often than chance. The alternative alignment `WKIE` / `W-RE` scores $11 - 4 - 3 + 5 = 9$, five less than 14.

**Points.** 0.5 p for explaining that a positive score means the pair is seen more often than by chance in related proteins (a conservative substitution) and a negative score less often. 0.5 p for the comparison: either the score of the alternative (9 against 14), or the argument that both alignments pay one gap, so the difference is $s(K,R) - s(I,R) = 2 - (-3) = 5$.

**Common mistakes.** "K and R are similar" without saying what the score measures. Saying that K and R are identical or that the score is a probability.

---

## Question 2: A position-specific scoring matrix for a DNA motif (5 p)

### a. Frequencies and PSSM (2 p)

With 4 sites and a pseudocount of $+1$ for each of the 4 bases, every column has $4 + 4 = 8$ counts in total, so $f_{i,j} = (n_{i,j} + 1)/8$, where $n_{i,j}$ is the observed count. The score is then

$$
S_{i,j} = \log_2 \frac{(n_{i,j}+1)/8}{0.25} = \log_2 \frac{n_{i,j}+1}{2}
$$

so only five different values occur:

| Count $n$ | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| $f = (n+1)/8$ | 0.125 | 0.25 | 0.375 | 0.5 | 0.625 |
| $S = \log_2(f/0.25)$ | -1 | 0 | 0.58 | 1 | 1.32 |

The counts are: position 1 G4; position 2 A3, T1; position 3 T4; position 4 A2, T2; position 5 C3, G1. The PSSM is

| Position | A | C | G | T |
|---|---|---|---|---|
| 1 | -1 | -1 | **1.32** | -1 |
| 2 | **1** | -1 | -1 | 0 |
| 3 | -1 | -1 | -1 | **1.32** |
| 4 | **0.58** | -1 | -1 | **0.58** |
| 5 | -1 | **1** | 0 | -1 |

Example entry: position 2, base A: $n = 3$, $f = 4/8 = 0.5$, $S = \log_2(0.5/0.25) = \log_2 2 = 1$.

**Points.** 0.5 p for the right denominator (8, not 4 or 5) and the pseudocount-adjusted frequencies. 0.5 p for the worked example entry. 1 p for the PSSM: full points if all 20 entries are right, 0.5 p for up to three wrong entries.

**Common mistakes.** Dividing by 4 + 1 = 5 (adding one pseudocount per column instead of one per base). Adding the pseudocount only to the bases that were not seen. Using $\log_{10}$ or $\ln$ instead of $\log_2$. Forgetting to divide by the background $q_j$, which gives negative scores everywhere.

### b. Scoring two sites (1 p)

- `GATTG`: $1.32 + 1 + 1.32 + 0.58 + 0 = 4.22$ bits.
- `GTTCC`: $1.32 + 0 + 1.32 + (-1) + 1 = 2.64$ bits.

`GATTG` is the more likely binding site. A score of $S$ bits means that the site is $2^S$ times more likely under the motif model than under the background, so `GATTG` is about $2^{4.22} \approx 19$ times more likely (exactly $2.5 \times 2 \times 2.5 \times 1.5 \times 1 = 18.75$, multiplying the ratios $f/q$ instead of adding their logs). `GTTCC` is about $2^{2.64} \approx 6$ times more likely, so `GATTG` is about 3 times more likely than `GTTCC`.

**Points.** 0.5 p for both scores (one position looked up wrongly: 0.25 p). 0.5 p for choosing `GATTG` and for the $2^S$ interpretation; accept any value from 16 to 20.

**Common mistakes.** Multiplying the scores instead of adding them (the scores are logs, so they add, as in Session 1). Reading $4.22$ bits as "4.22 times more likely".

### c. Pseudocounts and small samples (2 p)

**Model answer.** Without pseudocounts, G at position 1 would have $f = 4/4 = 1$ and score $\log_2(1/0.25) = 2$ bits. The pseudocounts add one count to every base, so G gets $5/8 = 0.625$ and the score falls to $\log_2 2.5 \approx 1.32$. The pseudocount acts as a prior ("every base is possible"), and with only four sites the prior has a large influence: four observations are not strong evidence that the other bases never occur there. With 400 sites that all have G, $f = 401/404 \approx 0.99$ and the score is $\log_2(0.99/0.25) \approx 1.99$ bits, close to 2: the observed counts swamp the prior.

Without pseudocounts, `GTTCC` has a C at position 4, where no site has a C. Then $f = 0$, $\log_2 0 = -\infty$, and the whole site scores $-\infty$, however well the other four positions match. One unseen base vetoes the site, although with only four sites its absence may be bad luck rather than biology. Pseudocounts prevent this.

**Points.** 0.5 p for the 2 bits without pseudocounts and why the pseudocounts lower it. 0.5 p for the idea that with few sequences the prior (pseudocount) matters, and that with many sequences the score approaches 2 bits (an exact value is not needed). 0.5 p for $-\infty$ (or "minus infinity", "log of zero") for `GTTCC`. 0.5 p for why that is a problem (a single unseen base rules the site out; absence in four sites is weak evidence).

**Common mistakes.** Saying that a fully conserved position has 0 bits (that is its *entropy*; its information content is high). Saying the score with 400 sites would be much larger than 2 bits: the maximum is $\log_2(1/0.25) = 2$ bits for DNA with a uniform background. Answering "0" for `GTTCC` without pseudocounts.

---

## Question 3: Two models with the same RMSD (5 p)

### a. RMSD (2 p)

$$
\text{RMSD} = \sqrt{\frac{1}{N} \sum_{i=1}^{N} d_i^2}
$$

- Model A: $\sum d_i^2 = 10 \times 4 = 40$, so $\text{RMSD} = \sqrt{40/10} = \sqrt{4} = 2.0$ Å.
- Model B: $\sum d_i^2 = 8 \times 1 + 2 \times 16 = 40$, so $\text{RMSD} = \sqrt{4} = 2.0$ Å.

Both models have the same RMSD.

**Points.** 0.5 p for the formula (square, mean, root, in that order). 0.75 p for each model.

**Common mistakes.** Taking the mean of the distances without squaring (model B would then get 1.6 Å). Taking the root before the mean, or forgetting the root (giving 4).

### b. TM-score (1 p)

With $d_0 = 2$ Å the terms are $1/(1 + (d/2)^2)$: for $d = 1$, $1/1.25 = 0.8$; for $d = 2$, $1/2 = 0.5$; for $d = 4$, $1/5 = 0.2$.

- Model A: $(10 \times 0.5)/10 = 0.50$.
- Model B: $(8 \times 0.8 + 2 \times 0.2)/10 = (6.4 + 0.4)/10 = 0.68$.

**Points.** 0.5 p for each model.

**Common mistakes.** Forgetting to square $d_i/d_0$. Dividing by the number of terms with a large deviation instead of by $L$.

### c. Which model is better, and model C (2 p)

**Model answer.** Model B is better: eight of its ten residues are within 1 Å of the experimental structure, and only the two-residue loop is wrong. Model A has every residue 2 Å off. The RMSD cannot tell them apart because it squares the deviations, so the two loop residues ($4^2 = 16$ each) contribute 32 of model B's sum of 40, four times as much as its eight good residues together. One badly placed region can thus inflate the RMSD even when the rest of the structure fits well. The TM-score gives each residue a term between 0 and 1: a residue that fits closely contributes nearly 1, and a badly placed one contributes close to 0 rather than a large penalty. A few outliers therefore cost little, and the many residues that fit closely are rewarded. It is also normalised by length, so it can be compared between proteins of different sizes.

Model C is not better on this evidence. An RMSD over 4 of 10 residues says nothing about the other six: a superposition can be restricted to the residues that fit well, so an RMSD should always be given with the number of aligned residues. Counted over all 10 residues, with the six unaligned residues contributing nothing, model C would have a TM-score of at most $4 \times 0.86 / 10 \approx 0.34$, below both A and B.

**Points.** 0.5 p for choosing B with a reason. 0.5 p for why the RMSD misses it (squaring, outliers dominate). 0.5 p for how the TM-score differs (bounded per residue, length-normalised). 0.5 p for model C: the RMSD covers only 4 residues, so it must be reported with the number of aligned residues (the TM-score estimate is not required).

**Common mistakes.** "Same RMSD, so equally good." "Model C has the lowest RMSD, so it is best." Saying that a TM-score of 0.5 for model A proves the same fold: the 0.5 rule of thumb applies to whole proteins with the real, length-dependent $d_0$, not to this 10-residue toy example.

---

## Question 4: Is it a globin? Sequence and structure evidence (5 p)

### a. The annotation (1 p)

**Model answer.** An unreviewed TrEMBL entry is annotated automatically, by programs, mostly by transfer from similar sequences or family signatures (for example a match to a family model); no curator has checked it. Its protein-existence level is usually "inferred from homology" or "predicted". Automatic annotation can be wrong, for example when it is copied from a sequence that was itself annotated automatically, so errors spread from entry to entry, and "-like" signals that the evidence is indirect. Check the evidence before relying on it.

**Points.** 0.5 p for "automatic / predicted, not curated". 0.5 p for a reason for caution (transfer by similarity, error propagation, no experimental evidence).

**Common mistakes.** Saying TrEMBL entries are experimentally verified, or that Swiss-Prot is a subset of TrEMBL.

### b. Two ways to find distant relatives (2 p)

**Model answer.**

- **PSI-BLAST** starts with an ordinary BLAST search, aligns the hits that pass the inclusion threshold to the query, and builds a PSSM from them. It then searches again with the PSSM instead of BLOSUM62, and repeats until no new sequences are included (convergence) or a set number of rounds is reached. It uses the *sequence* information of the whole family: which positions are conserved and which residues are allowed at each. A single BLAST search scores every position with the same general-purpose matrix, so a faint but real family signal is lost; the PSSM gives high weight to the conserved positions and therefore detects more remote homologs.
- **Foldseek** uses the 3D structure (here a predicted model). It converts the structure into a string of 3Di letters, one per residue, describing the local 3D environment of each residue, and searches structure databases with fast sequence-search methods. Structure is more conserved than sequence, so two proteins whose sequences have diverged beyond recognition can still have the same fold and be found.

**Points.** 1 p per method: 0.5 p for how it works (PSI-BLAST: iterate, PSSM from included hits; Foldseek: structure turned into a 3Di string and searched quickly, or a correct description of structural comparison with DALI or TM-align), 0.5 p for why it finds what BLAST misses (position-specific family information; structure more conserved than sequence).

**Common mistakes.** Describing PSI-BLAST as "BLAST run several times" without the PSSM. Saying Foldseek compares amino-acid sequences. Saying a profile HMM and PSI-BLAST are the same thing (related ideas, different models; accept a correct mention of profile HMMs as an alternative).

### c. Interpreting the results (2 p)

**Model answer.** The protein is very probably a globin, most likely a truncated (2-on-2) haemoglobin. The early PSI-BLAST rounds and the structure search agree:

- PSI-BLAST round 2 includes only bacterial globins and flavohaemoglobins with good E-values, so the family signal is consistent.
- Round 5 is not trustworthy. Myosins and tropomyosins are long coiled-coil proteins with no relationship to globins. This is **profile drift**: once an unrelated, probably helical or low-complexity sequence passes the inclusion threshold, it shifts the PSSM towards itself, and later rounds pull in more of its kind. Use the profile from the early rounds, keep the threshold strict, and check late hits independently.
- Foldseek gives a TM-score of 0.71 to a truncated haemoglobin over 112 of 128 residues, well above the about 0.5 that usually means the same fold, and the model is confident (pLDDT 88), so the structure evidence is meaningful. The 14% sequence identity is too low to show homology by itself, which is why BLAST failed, but the structure and the early PSI-BLAST rounds point the same way. The lower TM-score to β-globin (0.55) fits a more distant relationship within the globins.

A further check (any one): look for the conserved haem-binding residues, such as the proximal histidine, in an alignment with known globins; search Pfam or InterPro with a profile HMM; look up the CATH classification of the top structural hits, where truncated haemoglobins and β-globin share the Globins homologous superfamily (1.10.490.10); check the pLDDT of the aligned region; express the protein and test haem binding.

**Points.** 0.5 p for the overall conclusion (a globin, most likely a truncated haemoglobin). 0.5 p for trusting round 2 and the Foldseek hit, with a reason. 0.5 p for recognising profile drift in round 5. 0.5 p for a sensible further check.

**Common mistakes.** Concluding that the protein is a myosin because round 5 has the most hits. Treating 14% identity as evidence against homology (low identity does not exclude it). Treating a TM-score above 0.5 as proof of common ancestry: the same fold can in principle arise more than once, so structure evidence is strongest when, as here, it agrees with sequence evidence.

---

## Note for the teacher

**Likely hardest: Question 2 (the PSSM), especially parts a and c.** Students tend to divide by the number of sequences instead of the number of sequences plus the pseudocounts, and many do not see why a fully conserved column scores less than the maximum. If most of the room fails it, the key point is that a PSSM entry compares two probabilities: $f_{i,j}$, the frequency of base $j$ at position $i$ estimated from the alignment *after* adding a prior count to every base (so the denominator is $N + 4$ for DNA, $N + 20$ for proteins), with $q_j$, the background. The score is the log of that ratio, so it is 0 when the column looks like the background, positive when the base is enriched, and capped at $\log_2(1/q_j)$. With few sequences the prior pulls every frequency towards the background, which is why four sites give 1.32 bits instead of 2 and why an unseen base costs $-1$ instead of $-\infty$. A quick board demonstration is to write the column G4 with 4, 40 and 400 sequences and show the score climbing from 1.32 towards 2 bits.

Question 4c is the most likely second problem, because it asks for a judgement rather than a calculation. If many students take the round-5 hits at face value, go back to profile drift: the model chooses its own training data, so one wrong inclusion reinforces itself.
