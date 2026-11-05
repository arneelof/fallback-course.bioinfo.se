# Session 5: Advanced Database Search & Profile Methods

## Why can't BLAST simply run Session 4's full dynamic programming against every sequence in a database?

- [x] Dynamic programming's cost grows with the product of the two sequences' lengths, which becomes infeasible multiplied across hundreds of millions of database sequences
- [ ] Dynamic programming only produces correct results for sequences shorter than 100 residues
- [ ] Databases store sequences in a binary format dynamic programming cannot parse
- [ ] BLAST does run full dynamic programming against every sequence; there is no heuristic shortcut

## What is the correct order of BLAST's three main stages?

- [x] Seeding (find short high-scoring word matches) -> Extension (grow into a full alignment) -> Evaluation (statistical significance)
- [ ] Evaluation -> Seeding -> Extension
- [ ] Extension -> Evaluation -> Seeding
- [ ] BLAST has only one stage: direct pairwise alignment

## For the query word LWG scored against BLOSUM62, the word AWG scores 16 while IWG scores 19. Both clear a threshold of T=12, so both go into the lookup table BLAST builds from the query. What does this table let BLAST do efficiently?

- [x] Scan each database sequence once and, with a single table lookup per 3-letter word, find every word that seeds a match to the query, including similar words and not only exact ones
- [ ] Skip the extension stage entirely for any word scoring above the threshold
- [ ] Guarantee that the final reported alignment is globally optimal
- [ ] Replace the need for a substitution matrix during extension

## During extension, the running score reaches a peak of 9, then falls to 3 (a drop-off of 6) with a drop-off threshold X=5. What does BLAST report?

- [x] It stops extending, and trims the reported alignment back to where the running score was actually at its peak of 9
- [ ] It stops extending, and reports the alignment up to the point where the score fell to 3
- [ ] It keeps extending regardless, since some drop is always expected
- [ ] It discards the seed entirely, since any drop-off means the seed was spurious

## An alignment gets E-value 10^-6 against a small custom database of 500 sequences. What would you expect if you ran the same alignment's score against the whole of GenBank instead?

- [x] A much larger (worse) E-value, since E is proportional to database size and a bigger database gives chance more opportunities to produce an equally good false hit
- [ ] Exactly the same E-value, since E-value doesn't depend on database size
- [ ] A smaller (better) E-value, since bigger databases are always more statistically reliable
- [ ] E-values are undefined for databases larger than 10,000 sequences

## A local BLASTP search of HBB against five other human globins reports myoglobin only as a weak alignment (E = 63). Rerun with the two-hit rule switched off, BLAST finds a 145-residue alignment at 25.5% identity with E = 5x10^-11. What does this show?

- [x] The first E-value only evaluated the alignment BLAST happened to find; its seeding heuristic skipped the good alignment, which is the price of speed
- [ ] Switching off the two-hit rule makes BLAST report false positives, so the second result should be ignored
- [ ] Myoglobin is unrelated to hemoglobin, since the default search found no significant hit
- [ ] E-values are random, so two runs of the same search can disagree

## Why can bit scores be compared directly across two BLAST searches that used different substitution matrices, when raw scores cannot?

- [x] The bit score formula normalizes the raw score using that search's own K and lambda constants, removing the scoring-system-specific part
- [ ] Bit scores are always computed using BLOSUM62, regardless of what matrix the search actually used
- [ ] Bit scores ignore the alignment entirely and depend only on sequence length
- [ ] Raw scores and bit scores are the same number under two different names

## This cell builds a PSSM from a 5-sequence toy alignment and finds its highest-scoring sequence. What does it print?

<!-- coding-exercise -->

This cell from `notebooks/session05-blast-and-profiles-in-code.ipynb` builds a PSSM from a 5-sequence toy alignment, with a uniform pseudocount of +1 added to every residue's count at every position:

```python
def pssm(pseudocount):
    matrix = []
    for pos in range(n_pos):
        c = counts_at(pos)
        total = sum(c.values()) + pseudocount * len(residues)
        freqs = {r: (c[r] + pseudocount) / total for r in residues}
        matrix.append({r: math.log2(freqs[r] / background[r]) if freqs[r] > 0 else float("-inf") for r in residues})
    return matrix

pssm_pseudo = pssm(pseudocount=1)
best_seq, best_score = best_sequence(pssm_pseudo)
print(best_seq)
```

The alignment's own consensus sequence (majority residue at every position) is `AGLSP`. What does this cell print?

- [x] AGLSP -- the PSSM's highest-scoring sequence recovers the alignment's own consensus
- [ ] It raises a ZeroDivisionError, since some residues never appear at some positions
- [ ] A sequence made entirely of the single most common residue overall, ignoring position
- [ ] RGISQ -- the rarest residue at each position, since rare residues get the most "surprising" scores

## At a position where alanine (background frequency 7.4%) appears in 4 of 5 sequences and tryptophan (background frequency 1.3%) appears in just 1, which gets the HIGHER log-odds score WITHOUT pseudocounts?

- [x] Tryptophan -- its much rarer background frequency makes even one occurrence look far more surprising than chance would predict
- [ ] Alanine, because it appears more often in the alignment
- [ ] They get exactly the same score, since log-odds only depends on alignment counts
- [ ] Neither can be scored without first adding pseudocounts

## What does PSI-BLAST do differently from ordinary BLAST?

- [x] It builds a position-specific scoring matrix (PSSM) from the hits that pass an inclusion threshold, then re-searches using that PSSM instead of a fixed substitution matrix, repeating over several iterations
- [ ] It only ever runs once, exactly like ordinary BLAST, but with a stricter E-value cutoff
- [ ] It searches by exact keyword match only, ignoring sequence similarity entirely
- [ ] It replaces the seed-and-extend heuristic with full Needleman-Wunsch dynamic programming

## What does a profile HMM model that a PSSM, used in ordinary gapped alignment, does not?

- [x] Position-specific insertion and deletion behaviour, as Insert/Delete states with their own transition probabilities at each position, instead of the same gap penalties everywhere
- [ ] Log-odds scores of individual residues
- [ ] Background amino acid frequencies
- [ ] Nothing -- a PSSM and a profile HMM are mathematically identical

## In a profile HMM, why are the Match/Insert/Delete states called "hidden"?

- [x] Given an observed residue, the model doesn't directly tell you which state produced it -- that has to be inferred from which path through the model best explains the whole sequence
- [ ] The states are literally invisible in any diagram of the model
- [ ] Insert and Delete states never actually appear in real biological sequences
- [ ] Profile HMMs are only used for confidential, unpublished sequences

## A live Pfam search on HBB finds domain PF00042 ("Globin") at residues 27-142 with E-value 1.3x10^-29. On BRCA1, three domains match with E-values from 1.6x10^-6 (the 41-residue RING finger) to 2.8x10^-77 (a 164-residue BRCA1-specific domain). How should you read the RING finger's weaker E-value?

- [x] It is still significant; the evidence from sequence alone is weaker because the domain is short and the RING family is diverse, not because the domain is "less real"
- [ ] It means that domain almost certainly isn't real, since it's far less extreme than the others
- [ ] It means the Pfam database has an error for that specific domain
- [ ] All three E-values should be identical if the domains are all genuinely present

## Classic BLAST builds a lookup table from the query's words. MMseqs2 instead builds a k-mer index of the target database. Why does that help at the scale of billions of sequences?

- [x] The database index is built once and reused, so each query only looks up its own (similar) k-mers instead of reading through every database sequence
- [ ] MMseqs2 replaces alignment with a neural network, so no index of the query is needed
- [ ] Indexing the database makes the results exactly optimal, unlike BLAST
- [ ] It removes the need for a substitution matrix

## MMseqs2 only keeps a database sequence for further scoring when two similar k-mers fall on the same diagonal. Why is that a good filter?

- [x] Two hits at the same offset between query and target are consistent with one ungapped stretch of alignment, which is much less likely by chance than a single isolated k-mer match
- [ ] Diagonal hits are the only ones that can contain gaps
- [ ] It guarantees that the final alignment has no gaps
- [ ] The diagonal holds the database sequences with the highest identity to each other

## In round 2 of a PSI-BLAST search, an unrelated protein with a long low-complexity region passes the inclusion threshold. What is the most likely consequence in later rounds?

- [x] The next PSSM shifts towards the intruder, so later rounds pull in more unrelated proteins like it (profile drift)
- [ ] Nothing: PSI-BLAST automatically removes false positives in the next round
- [ ] The search stops immediately because the profile can no longer converge
- [ ] Only the E-values change; the list of hits stays the same

## Why do real profile tools remove or down-weight near-identical sequences before building a PSSM?

- [x] So that an over-represented subfamily does not dominate the column statistics and make the profile describe that subfamily rather than the whole family
- [ ] Because BLAST cannot align sequences that are too similar
- [ ] Only to save memory
- [ ] Because identical sequences give negative log-odds scores

## Which BLAST program takes a protein query and searches a nucleotide database, translating the database sequences in all six frames as it searches?

- [x] tblastn
- [ ] blastx
- [ ] blastp
- [ ] tblastx

## Which BLAST program compares a protein query directly with a protein database, with no translation involved?

- [x] blastp
- [ ] blastn
- [ ] blastx
- [ ] tblastx

## A 120-residue protein query produces a PSSM. How many position-specific amino-acid scores does it contain?

- [x] 2,400 (120 positions × 20 amino acids; whether it is stored as 120 × 20 or 20 × 120 is only a convention)
- [ ] 120
- [ ] 20
- [ ] 14,400 (120 × 120)
