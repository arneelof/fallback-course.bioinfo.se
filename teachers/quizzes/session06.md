# Session 6: Protein Structure

## Which level of protein structure describes the sequence of amino acids in a polypeptide chain, with no 3D information at all?

- [x] Primary structure
- [ ] Secondary structure
- [ ] Tertiary structure
- [ ] Quaternary structure

## An alpha helix is stabilized mainly by which interaction?

- [x] Hydrogen bonds between backbone N-H and C=O groups four residues apart
- [ ] Disulfide bonds between cysteine side chains
- [ ] Hydrogen bonds between neighboring beta strands
- [ ] Ionic bonds between the helix's own side chains

## What mainly drives a single protein chain to fold into its compact tertiary structure?

- [x] The hydrophobic effect: water excludes non-polar side chains from its surface, driving them to bury inside the fold
- [ ] Covalent peptide bonds forming between non-adjacent residues
- [ ] The genetic code directly specifying the 3D coordinates of each atom
- [ ] Repulsion between all identically-charged residues

## Hemoglobin is described as a heterotetramer: two alpha chains and two beta chains, each independently folded, arranged with respect to each other. Which level of structure does that description belong to?

- [x] Quaternary structure
- [ ] Primary structure
- [ ] Secondary structure
- [ ] There is no name for this level — it is just "the whole protein"

## Anfinsen showed that unfolded ribonuclease refolds into its active shape on its own. Which conclusion is justified?

- [x] For many globular proteins the sequence contains enough information to specify the native fold under the right conditions, though some proteins also need chaperones, ligands or partners, and some have no single fold
- [ ] Every protein sequence folds into exactly one structure, whatever the conditions
- [ ] Protein folding requires no energy at all
- [ ] Structure prediction from sequence is therefore an easy, already-solved problem

## This is the core of the notebook's quaternary-distance calculation:

<!-- coding-exercise -->

```python
fe_2hhb = {}
for chain in structures["2hhb"][0]:
    for res in chain:
        if res.get_resname() == "HEM":
            fe_2hhb[chain.id] = res["FE"].get_coord()

beta_beta_T = np.linalg.norm(fe_2hhb["B"] - fe_2hhb["D"])
```

`2HHB`'s chain `B` and chain `D` are both beta-globin chains. What does `beta_beta_T` end up holding?

- [x] The straight-line distance, in Angstroms, between the two beta chains' heme iron atoms
- [ ] The number of hydrogen bonds between the two beta chains
- [ ] The root-mean-square deviation between the two beta chains' full coordinates
- [ ] The angle, in degrees, between the two beta chains' helices

## Why does modeling a protein's tertiary structure by directly simulating the physics (de novo / ab initio modeling) struggle to scale to larger proteins?

- [x] It is the most rigorous approach in principle, but computationally so expensive it has mainly been practical only for small proteins
- [ ] It requires an existing structure of a homologous protein to work at all
- [ ] It only works for proteins with no secondary structure
- [ ] It cannot be run on a computer, only performed experimentally

## Comparative modeling (homology modeling / threading) predicts a new protein's structure by assuming it folds like a known template with a similar sequence. What is its main limitation?

- [x] It is structurally useless for a genuinely new fold with no sufficiently similar template already solved
- [ ] It only works for proteins shorter than 20 residues
- [ ] It cannot use any information from multiple sequence alignments
- [ ] It always produces a less accurate model than de novo modeling, even when a good template exists

## Evolutionary (contact-based) structure-prediction methods infer which residues are likely to be close together in 3D from patterns of co-evolution across many homologous sequences. What earlier concept from this course does this directly build on?

- [x] The same evolutionary information behind Session 5's profiles/PSSMs, now used for a 3D geometric question instead of a sequence-scoring one
- [ ] Session 4's dynamic programming alignment algorithm, used unchanged
- [ ] Session 2's tensor operations, with no connection to sequence data
- [ ] Session 1's gradient descent, applied directly to atomic coordinates

## The notebook assigns HBB's secondary structure with PyMOL's own `dss` algorithm, from the atomic coordinates. How does the result compare with the PDB entry's own annotation (117 of 146 residues in helices)?

- [x] 118 of 146 residues (80.8%) in a helix, 0% strand: essentially the same answer from a different method
- [ ] A completely different result, showing the annotation is wrong
- [ ] That HBB has no secondary structure at all
- [ ] That HBB is roughly half helix and half sheet

## The notebook measures the beta1-beta2 heme iron-to-iron distance in both deoxyhemoglobin (2HHB, ~39.5A) and oxyhemoglobin (1HHO, ~34.6A). What does this ~5A change represent?

- [x] A real, measured geometric signature of hemoglobin's T-to-R quaternary allosteric transition between its two functional states
- [ ] A measurement error, since a protein's quaternary structure cannot physically change
- [ ] A change in hemoglobin's primary structure caused by oxygen binding
- [ ] The distance between two alpha chains, not two beta chains

## Getting `1HHO`'s second alpha/beta chain pair required applying the file's own `REMARK 350` symmetry operation to the first pair, rather than reading it directly from the file. What general operation does this represent?

- [x] A rigid-body transformation: a rotation (plus, in general, a translation) that moves an object in 3D space without changing its own shape
- [ ] A sequence alignment between the two chains
- [ ] A change to the protein's secondary structure assignment
- [ ] A rescaling of the atomic coordinates to a different unit of distance

## SCOP, CATH, ECOD, and TED all classify protein domains by their solved or predicted 3D structure. How does this differ from Session 3/5's InterPro/Pfam domain classification?

- [x] InterPro/Pfam classify by sequence similarity; SCOP/CATH/ECOD/TED classify by actual 3D structural similarity, which can survive long after sequence similarity is no longer detectable
- [ ] They classify completely unrelated things, with no overlap in what counts as a "domain"
- [ ] SCOP/CATH/ECOD/TED are strictly newer, more accurate replacements for InterPro/Pfam
- [ ] InterPro/Pfam only classify RNA domains, while the structural databases only classify protein

## Foldseek can search a query structure against hundreds of millions of real and predicted structures in seconds — roughly BLAST's role, but for structure. What makes this possible?

- [x] Encoding each residue's local 3D neighborhood into a small discrete alphabet (3Di), turning structure comparison into fast sequence-like alignment instead of expensive geometric superposition
- [ ] Foldseek only compares backbone atoms, ignoring every side chain
- [ ] Foldseek skips statistical significance testing entirely
- [ ] Foldseek is limited to proteins under 100 residues, which keeps every search fast

## A real Foldseek comparison of alpha- vs. beta-globin chains (2HHB vs. 1HHO, ~43% sequence identity) gives a TM-score around 0.90-0.91; comparing hemoglobin to an unrelated fold (GFP, 1EMA) returns zero hits. What does the alpha-vs-beta-globin result demonstrate?

- [x] Structural similarity remains clearly detectable well after sequence identity has dropped a long way — structure is more conserved than sequence
- [ ] Foldseek cannot reliably distinguish related folds from unrelated ones
- [ ] Alpha- and beta-globin are in fact identical in sequence
- [ ] TM-score can only be computed for two copies of the exact same protein

<!-- coding-exercise -->
## This is a real result from running Foldseek locally on this page's own structures:

```
foldseek easy-search 2HHB.pdb targets/ result.tsv tmp \
    --format-output "query,target,alntmscore,rmsd,fident"
```

For the `2HHB.pdb_A` vs. `1HHO.pdb_A` row (same alpha-globin chain, two
different oxygenation states), Foldseek reports a TM-score around 0.98
and an RMSD around 0.7 Angstrom. What does this tell you?

- [x] The two structures are about as similar as two independently solved structures of the same protein get — Foldseek correctly reports very high structural similarity
- [ ] The two chains have completely different folds
- [ ] Foldseek failed to align the two structures
- [ ] A TM-score of 0.98 means the sequences are 98% identical

## In a contact map of a mostly helical protein, what does a stripe of contacts far from the diagonal represent?

- [x] Long-range contacts: residues far apart in sequence but close in space, for example two helices packed against each other
- [ ] Hydrogen bonds within one helix, between residues i and i+4
- [ ] Residues that are identical in sequence
- [ ] Errors in the structure

## Why are distance and contact maps useful for comparing two structures?

- [x] They do not change when a structure is rotated or moved, so two proteins can be compared without first superimposing them
- [ ] They contain the amino-acid sequence, so sequence alignment can be used directly
- [ ] They are always smaller than the coordinate file
- [ ] They show which atoms are hydrogen-bonded

## The bacterial truncated hemoglobin (1IDR) aligns to beta-globin with a sequence-only score no better than shuffled sequences, yet TM-align finds a shared fold over more than 100 residues (TM-score 0.57). What does this show?

- [x] Structure can remain recognizably similar after sequence similarity has become undetectable: structure is more conserved than sequence
- [ ] The two proteins cannot be related, since their sequences show no signal
- [ ] TM-align finds a match between any two proteins
- [ ] The sequence alignment must contain a bug

## Neuroglobin's sequence alignment to beta-globin has a clear signal (score well above shuffled), but only 66% of its residue pairs agree with the structure alignment. What has gone wrong?

- [x] The sequence alignment recognizes the relationship but places some gaps in the wrong positions, so part of the residue correspondence is wrong
- [ ] The two proteins have different folds
- [ ] The structure alignment is unreliable whenever sequence identity is below 30%
- [ ] Nothing: 66% agreement means the alignment is perfect

## Why is the TM-score usually preferred over RMSD for asking whether two proteins share a fold?

- [x] It weights close residue pairs fully and distant ones hardly at all, and normalizes by length, so one misplaced loop or a longer protein does not dominate it
- [ ] It does not need the structures to be aligned
- [ ] It is always exactly 1 for proteins with the same fold
- [ ] RMSD can only be computed for proteins of the same length

## How does DALI compare two structures?

- [x] It looks for residue correspondences that make the two proteins' patterns of internal residue-residue distances agree
- [ ] It compares the amino-acid sequences with BLOSUM62
- [ ] It counts how many helices and strands each protein has
- [ ] It compares the proteins' molecular weights

## Foldseek's 3Di alphabet was derived with a variational autoencoder. Why is that a useful idea to remember for the rest of the course?

- [x] It is an example of a useful representation being learned from data instead of designed by hand
- [ ] It means Foldseek predicts structures from sequence
- [ ] It means Foldseek's results cannot be trusted
- [ ] It means every structure needs to be retrained before searching

## CATH puts beta-globin and the M. tuberculosis truncated hemoglobin in the same homologous superfamily (Globins), while Pfam puts them in two different families. Why can this happen?

- [x] CATH groups domains by 3D structure, which can stay similar after sequence similarity has faded too far for one sequence family to cover both
- [ ] Pfam is wrong and should be replaced by CATH
- [ ] CATH only uses protein names
- [ ] The two proteins have identical sequences

## Deoxy (2HHB) and oxy (1HHO) hemoglobin give a TM-score of 0.98 chain against chain, yet the beta-beta heme iron distance differs by about 5 Angstrom. What is the general lesson?

- [x] A PDB entry is one snapshot of one state; a protein can occupy several conformational states, here differing mainly in how the chains are arranged
- [ ] One of the two structures must be wrong
- [ ] The chains themselves unfold when oxygen binds
- [ ] TM-score cannot be computed for hemoglobin

## Secondary-structure prediction stated as a supervised learning problem: what are the input and the target?

- [x] Input: the sequence (or its profile) around each residue. Target: helix, strand or coil for every residue, taken from solved structures
- [ ] Input: the 3D coordinates. Target: the amino-acid sequence
- [ ] Input: helix, strand or coil labels. Target: the protein's name
- [ ] Input: the contact map. Target: the PDB identifier
