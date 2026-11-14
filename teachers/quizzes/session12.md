# Session 12: AlphaFold and Generative Models of Protein Structure

## Why do residues that are in contact tend to co-evolve across a protein family, and why were early mutual-information scores not enough?

- [x] A destabilising mutation at one residue is often compensated at its partner; but correlations also arise indirectly (A-B and B-C make A-C look coupled), which global models such as DCA/plmDCA separate out
- [ ] Residues in contact are always identical, so mutual information is exact
- [ ] Coevolution only happens between residues far apart in sequence
- [ ] Mutual information requires a known structure

## In eight real structures, a neighbouring residue pair is in contact 23-42% of the time when the centre pair is, against a 3% base rate. Why does this matter for contact prediction?

- [x] A predictor that looks at a neighbourhood of the map (PconsC2's random forests, then deep residual CNNs) can clean up and complete noisy pair-by-pair predictions
- [ ] It means contact maps are random
- [ ] Only the diagonal of a contact map carries information
- [ ] It shows coevolution is unnecessary

## What did AlphaFold 1 and trRosetta predict that earlier methods did not?

- [x] Distributions of distances (and, in trRosetta, orientations) between residue pairs, rather than binary contacts
- [ ] Full atomic coordinates directly from one sequence
- [ ] Secondary structure only
- [ ] Binding affinities

## An AlphaFold model has pLDDT above 90 in two domains but high PAE between them. What is the right interpretation?

- [x] Each domain is probably accurate, but their relative orientation is uncertain
- [ ] The whole model is accurate
- [ ] Both domains are wrong
- [ ] The protein must be disordered

## In the AlphaFold DB model of p53, the DNA-binding domain has mean pLDDT about 95 while the N-terminal region has about 48. What is the best explanation?

- [x] The model is not confident there; for p53 this matches experiments showing that the N-terminal transactivation region is intrinsically disordered on its own (it folds on binding partners such as MDM2)
- [ ] AlphaFold ran out of memory for the N-terminus
- [ ] p53 has no homologs
- [ ] The DNA-binding domain was copied from a template and the rest was guessed

## ESMFold predicted Ephrin-A5 (1SHW chain A) from its single sequence with TM-score 0.941 against the crystal structure. What replaces the multiple sequence alignment in ESMFold?

- [x] The ESM-2 protein language model's internal representation of the sequence
- [ ] A template from the PDB
- [ ] A physics-based force field
- [ ] Nothing: it folds by molecular dynamics

## FoldDock gave acceptable models (DockQ >= 0.23) for 63% of dimers. What was the key trick for using AlphaFold2 on complexes?

- [x] Concatenate the chains and give AlphaFold2 paired and unpaired alignments of both proteins, then score interfaces with pDockQ (interface pLDDT and number of contacts)
- [ ] Retrain AlphaFold2 from scratch on docked complexes
- [ ] Dock rigid monomer models with a physics-based program
- [ ] Use only one chain's alignment

## For antibody-antigen complexes, the best of 200 AlphaFold3 models is much better than the top-ranked one. What is the main bottleneck?

- [x] Ranking: AlphaFold's own confidence estimates often fail to identify the best model it generated
- [ ] AlphaFold3 cannot generate any correct models
- [ ] DockQ cannot score antibodies
- [ ] More sampling makes results worse

## For CheY, mutual information (with APC) finds 49% true contacts among its top-L pairs; mean-field DCA on the same alignment finds 73%. Why?

- [x] DCA fits one global model, so a correlation passed along a chain of contacts (A-B, B-C) is not mistaken for a direct A-C contact
- [ ] DCA uses more sequences
- [ ] DCA uses the known structure
- [ ] Mutual information cannot be computed for proteins

## In AlphaFold2's Evoformer, what does the "outer product mean" do?

- [x] It passes information from the MSA to the pair representation: how two columns vary together across the sequences updates their pair, a learned form of coevolution
- [ ] It averages the five AlphaFold models
- [ ] It computes the final coordinates
- [ ] It removes gaps from the alignment

## Why can ipTM be low for a correct interface, and how does ipSAE address this?

- [x] ipTM is diluted by non-interacting or disordered regions of full-length constructs; ipSAE counts only residue pairs with good PAE
- [ ] ipTM ignores the interface completely
- [ ] ipSAE uses the experimental structure
- [ ] ipTM only works for homodimers

## In the four-regions heuristic, which region is an interaction between an intrinsically disordered transactivation domain and its partner, and why is structure prediction a poor tool there?

- [x] Region IV (missing context or dynamics): the interaction is transient and conditional, and a single static structure does not capture it; high confidence may reflect memorised training structures
- [ ] Region I, because it has strong coevolution
- [ ] Region II, because the partner is ambiguous
- [ ] Region III, because antibodies are involved

## A toy diffusion model trained on only 20 ring points generates samples closer to its training points (median 0.27) than a perfect ring sampler would be (0.54). With 4,000 training points the two agree. What does this illustrate?

- [x] With little training data a generative model partly memorises its examples; with enough data it learns the underlying distribution, the same question raised for AlphaFold3 on antibodies and RNA
- [ ] Diffusion models cannot learn rings
- [ ] More training data always causes memorisation
- [ ] The perfect sampler is wrong

## At CASP16, how did AlphaFold3 compare with AlphaFold2 for protein complexes?

- [x] Slightly better, but the difference disappeared when AlphaFold2 was run with massive sampling
- [ ] Much worse on all targets
- [ ] It solved all complex targets
- [ ] It was not tested

## In AlphaFold's Evoformer, what do row-wise and column-wise attention each operate over?

- [x] Row-wise attends across positions within one sequence; column-wise attends across different sequences at a fixed position
- [ ] Row-wise and column-wise are two names for the exact same computation
- [ ] Row-wise attention only runs during training, column-wise only during inference
- [ ] They operate directly on 3D coordinates, not on the MSA representation

## What does AlphaFold3's "Pairformer" represent, relative to AlphaFold2's Evoformer?

- [x] A related but simplified architecture that leans more on the pairwise representation and less on the raw MSA — evidence the specific attention pattern is still being iterated on, not a settled final design
- [ ] The exact same architecture, just renamed for AlphaFold3
- [ ] A return to the pre-attention, CNN-based contact-prediction approach
- [ ] A component that removes attention from AlphaFold entirely

## Diffusion models have a forward process and a reverse process. Which one requires training?

- [x] Only the reverse process — the forward process is a fixed, pre-specified noise schedule with no learned parameters
- [ ] Only the forward process
- [ ] Both require training, in alternation
- [ ] Neither requires training; diffusion is a purely analytical technique

## Why is RFdiffusion always paired with ProteinMPNN, rather than used alone?

- [x] RFdiffusion generates a protein backbone (3D coordinates) with no amino acid identities; ProteinMPNN separately solves the inverse-folding problem of designing a sequence for that backbone
- [ ] ProteinMPNN makes RFdiffusion's diffusion process converge faster
- [ ] RFdiffusion cannot produce valid 3D coordinates without ProteinMPNN's help
- [ ] They are two different names released for the same underlying model

## This is the reverse-diffusion sampling loop from the notebook, run once per timestep from pure noise down to real data:

<!-- coding-exercise -->

```python
@torch.no_grad()
def reverse_sample(n=1000):
    x = torch.randn(n, 2, device=device)
    for t in reversed(range(T2)):
        tt = torch.full((n,), t, device=device, dtype=torch.long)
        pred_noise = dnet(x, tt)
        alpha, alpha_bar, beta = alphas2[t], alpha_bars2[t], betas2[t]
        noise = torch.randn_like(x) if t > 0 else torch.zeros_like(x)
        x = (1 / torch.sqrt(alpha)) * (x - (beta / torch.sqrt(1 - alpha_bar)) * pred_noise) + torch.sqrt(beta) * noise
    return x
```

Why does the loop add fresh random `noise` at every step except the very last one (`t == 0`)?

- [x] Each reverse step is itself a sample from a learned Gaussian distribution, not a deterministic point estimate — adding noise at every step except the final one matches the stochastic process being reversed, while the last step returns the final clean sample with no more noise to add
- [ ] It's a bug — the noise term should not be there at all
- [ ] The noise is only for visualization purposes and has no effect on the mathematics
- [ ] Adding noise speeds up computation by allowing larger batch sizes

## Best long-range contact precision (top L/5, free-modelling targets) was 27% in CASP11, 47% in CASP12 and over 70% in CASP13. What was the key methodological change?

- [x] The whole contact map was predicted as an image by deep residual CNNs over coevolution features, instead of scoring each residue pair separately
- [ ] CASP13 targets were much easier
- [ ] Multiple sequence alignments were abandoned
- [ ] The contact cutoff was changed from 8 to 12 Angstrom

## A region of an AlphaFold model has pLDDT below 50. What does that tell you?

- [x] The model is not confident about that region; disorder is one common reason, but too few homologs, several conformations or an uncertain domain orientation can also cause it
- [ ] The region is certainly intrinsically disordered
- [ ] The region has been shown experimentally to be unstructured
- [ ] The whole model is wrong

## AlphaFold3 returns a confident model for two proteins you submitted together. What does that establish?

- [x] How the two could interact if they do; not whether they actually interact in the cell, or when
- [ ] That they interact in the cell
- [ ] That their interaction has been measured experimentally
- [ ] That neither protein has any other partner

## What is the idea behind AlphaFold2's triangle updates of the pair representation?

- [x] Pair (i, j) is updated with information passing through every third residue k, because residue-pair relationships constrain each other; the updates are learned, not rules that enforce geometry
- [ ] They enforce the triangle inequality on predicted distances exactly
- [ ] They split the protein into triangles of three residues
- [ ] They align three homologous sequences at a time

## A designed protein sequence is refolded with AlphaFold2 and matches the intended backbone closely. What has been shown?

- [x] That the design is computationally self-consistent; whether it folds and works must still be tested by experiment
- [ ] That the protein has been validated experimentally
- [ ] That the protein binds its intended target
- [ ] Nothing, because AlphaFold2 cannot fold designed proteins

## How accurate is AlphaFold2 for a typical well-folded, single-domain protein?

- [x] Often close to experimental accuracy: in CASP14 its median backbone error was about 1 Å
- [ ] Rarely better than 5 Å backbone error; useful only for the overall fold
- [ ] Accurate only if a template with more than 90% sequence identity exists
- [ ] It cannot predict single domains, only complexes

## AlphaFold3 was designed to model several molecule types jointly with proteins, which the original AlphaFold2 network does not. Which?

- [x] Small-molecule ligands, DNA and RNA
- [ ] Only other protein chains, in complexes
- [ ] Only single protein chains, more accurately
- [ ] None: AlphaFold3 differs from AlphaFold2 only in its training data

## What do ColabFold (with MMseqs2) and the AlphaFold Server (with its own database searches) search for before predicting a structure?

- [x] Homologous sequences (a multiple sequence alignment) and structural templates, which AlphaFold uses as input
- [ ] The best of the input sequences, so that only that one is predicted
- [ ] Free GPU memory for the prediction
- [ ] The input sequence itself, in UniProt

## DockQ combines interface contacts, interface RMSD and ligand RMSD into one score between 0 and 1. How is a complex model with DockQ = 0.30 classed?

- [x] Acceptable
- [ ] Incorrect
- [ ] Medium quality
- [ ] High quality
