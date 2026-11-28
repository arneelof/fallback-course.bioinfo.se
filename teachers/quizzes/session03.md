# Session 3: Biological Databases

## Why do the INSDC partners exchange public nucleotide sequence records daily?

- [x] To make shared public records accessible through all three partner interfaces under shared accessions; release and indexing can delay a particular record's appearance
- [ ] Because only one of the three is allowed to accept new submissions
- [ ] So that each database can give the same sequence its own, different accession number
- [ ] Because local copies of the combined data are cheaper to maintain than synchronization

## Since the 1990s, most major scientific journals have required new sequence data to be deposited in an INSDC database before publication. What does this policy make possible?

- [x] Anyone can retrieve essentially the underlying sequence data behind a published paper, for free and with no restrictions on reuse
- [ ] It guarantees every paper's sequence data is manually reviewed by NCBI before publication
- [ ] It means all published sequences are automatically added to Swiss-Prot
- [ ] It restricts sequence data to non-commercial use only

## The DNA/RNA/protein levels of sequence databases mirror which biological concept?

- [x] The central dogma (DNA is transcribed to RNA, RNA is translated to protein)
- [ ] The taxonomic hierarchy of species
- [ ] The chronological order in which the databases were founded
- [ ] The size, in bytes, of each database

## UniProtKB's Swiss-Prot currently holds around 576,000 entries; TrEMBL holds around 149 million. What's the key practical difference between them?

- [x] Swiss-Prot entries are manually reviewed by curators; TrEMBL entries are automatically annotated and unreviewed
- [ ] Swiss-Prot only contains human proteins; TrEMBL contains every other species
- [ ] TrEMBL is more accurate because it has far more entries to cross-check against
- [ ] TrEMBL entries are checked by two independent curators, Swiss-Prot entries by one

## What does UniParc store that neither Swiss-Prot nor TrEMBL does on its own?

- [x] Every unique protein sequence in the world exactly once, under a stable identifier, regardless of which source database it originally came from
- [ ] Only sequences that have never appeared in any other database
- [ ] 3D structural coordinates for every known protein
- [ ] Only proteins with no known function

## A colleague gives you the accession number NP_000509.1 with no other context. From the prefix alone, what do you know?

- [x] It's a protein-level RefSeq record, and the .1 marks a specific version of it
- [ ] It's a raw, unassembled sequencing read
- [ ] It's a non-coding RNA record
- [ ] It's a predicted, not yet directly confirmed, protein

## Why does an X-prefixed RefSeq accession (e.g. XM_ or XP_) mean something different from the equivalent N-prefixed one (NM_, NP_)?

- [x] X-prefixed accessions are computational models predicted by NCBI's annotation pipeline, while N-prefixed records are the non-predicted class (many curated or supported by transcript evidence)
- [ ] X-prefixed accessions belong only to non-human organisms
- [ ] X-prefixed accessions are always longer sequences than N-prefixed ones
- [ ] There is no real difference; the letters are chosen arbitrarily

## Why isn't an accession number like NM_000518.5 a good universal "name" for a gene, the way the approved symbol HBB is?

- [x] It's only unique within RefSeq — the same gene has a different accession number in Ensembl, UniProt, and DDBJ, while the HGNC-approved symbol is widely shared across databases
- [ ] Accession numbers are randomly reassigned to different genes every year
- [ ] Accession numbers can only ever refer to proteins, never to genes or transcripts
- [ ] Official gene symbols have no governing body and are chosen informally by each lab

## Searching NCBI's or EBI's top-level, everything-at-once search for "hemoglobin beta" returns a long, mixed list spanning genome, gene, and protein records. What's the more effective alternative?

- [x] Search directly inside a level-specific database (e.g. NCBI Gene, or UniProt) once you know which level — DNA, RNA, or protein — you actually need
- [ ] Always use the exact accession number instead of any text search
- [ ] Switch to a completely different search engine outside NCBI/EBI
- [ ] There is no more effective alternative; a long results list is unavoidable

## Searching PubMed for `hemoglobin` returns 288,577 results and `malaria` returns 125,442. `hemoglobin AND malaria` returns 4,458. About how many results should `hemoglobin OR malaria` return?

<!-- coding-exercise -->

This cell from `notebooks/session03-databases-in-code.ipynb` computes the real, live counts and checks a prediction against them:

```python
a = pubmed_count("hemoglobin")           # 288,577
b = pubmed_count("malaria")              # 125,442
a_and_b = pubmed_count("hemoglobin AND malaria")   # 4,458
a_or_b = pubmed_count("hemoglobin OR malaria")

print(a_or_b, "vs predicted:", a + b - a_and_b)
```

- [x] Both numbers printed are 409,561 — set-theory inclusion-exclusion (|A| + |B| − |A ∩ B|) predicts the real PubMed count exactly
- [ ] The predicted number is far smaller than the real one, because OR only loosely approximates a set union in PubMed
- [ ] The cell raises an error, since `pubmed_count` requires a database connection string
- [ ] 414,019 — simply adding the two individual counts together

## What is the practical effect of wrapping a two-word PubMed search in quotation marks, e.g. searching `"hemoglobin beta"` instead of `hemoglobin beta`?

- [x] It requires the exact phrase, adjacent and in that order, instead of matching both words anywhere in the record in any order
- [ ] It searches only the title field and ignores the abstract
- [ ] It is exactly equivalent to using the NOT operator
- [ ] It has no effect on PubMed search results

## PubMed Central (PMC) currently holds about 12.6 million records out of PubMed's roughly 41 million. What does this tell you about free full-text access to the biomedical literature?

- [x] Only a minority (roughly a third) of PubMed-indexed papers have a free full text available directly through PMC
- [ ] Every PubMed record has a free full text available through PMC
- [ ] PMC and PubMed index completely different, non-overlapping sets of papers
- [ ] PMC only contains papers published before the year 2000

## Pfam's own standalone website was retired in 2023. Where do you look up a Pfam family today?

- [x] InterPro — Pfam was merged directly into it as one of its member databases
- [ ] UniProt — Pfam families are now listed there instead, with no separate database
- [ ] Pfam families were discontinued and no longer exist anywhere
- [ ] Rfam — Pfam and Rfam were merged into a single resource

## Rfam classifies non-coding RNA families using a covariance model rather than a plain profile HMM, the way InterPro/Pfam classifies protein families. Why does RNA specifically need that extra step?

- [x] A covariance model scores conserved secondary structure (base-pairing) together with sequence, since a non-coding RNA's function usually depends on the shape it folds into as much as its exact sequence
- [ ] Covariance models are just a faster algorithm for computing the same thing a profile HMM computes
- [ ] RNA sequences are too short for a profile HMM to ever work
- [ ] Covariance models only work on protein-coding sequences, not RNA

## PDB entry 2HHB (human deoxyhemoglobin, solved by X-ray diffraction) and the AlphaFold DB model for the same protein (P68871) both exist. What's the actual difference between them?

<!-- coding-exercise -->

This pair of cells from `notebooks/session03-databases-in-code.ipynb` queries both, live:

```python
r = requests.get("https://www.ebi.ac.uk/pdbe/api/pdb/entry/summary/2hhb", timeout=30)
pdbe_summary = r.json()["2hhb"][0]
print("Experimental method:", pdbe_summary["experimental_method"])

r = requests.get("https://alphafold.ebi.ac.uk/api/prediction/P68871", timeout=30)
af_entry = r.json()[0]
print("Mean pLDDT confidence:", af_entry["globalMetricValue"])
```

- [x] 2HHB is an experimentally determined structure (X-ray diffraction); the AlphaFold model is a computational prediction, with its own confidence score rather than an experimental method
- [ ] They're both predictions, just made by different software packages
- [ ] They're both experimentally solved structures, just deposited by different labs
- [ ] 2HHB is the prediction; the AlphaFold model is the experimentally confirmed structure

## Complex Portal's entry CPX-2158 ("Hemoglobin HbA complex": 2× HBA1, 2× HBB, 4× heme) and PDB entry 2HHB both describe the same real hemoglobin tetramer. What does each database record actually capture?

- [x] Complex Portal records composition and stoichiometry (which molecules, how many copies of each); PDB records atomic-resolution 3D geometry
- [ ] They contain completely unrelated information about two different molecules
- [ ] Complex Portal only lists predicted complexes, never curated real ones
- [ ] PDB only stores raw sequence, never 3D coordinates

## STRING builds a functional-association network by combining curated interaction databases (like IntAct), computational predictions, and literature text-mining into one score per protein pair. How is this different from IntAct alone?

- [x] IntAct records only direct physical interactions with real experimental evidence; STRING's score also includes indirect/predicted/text-mined relationships, not just confirmed physical binding
- [ ] STRING and IntAct store exactly the same information, just with a different web interface
- [ ] IntAct only covers human proteins, while STRING covers every species
- [ ] STRING is only about gene expression, not interactions at all

## You have new nucleotide sequence data to deposit in the INSDC. Which submission approach is appropriate?

- [x] Submit once through the appropriate route at one partner; the partners exchange the public records
- [ ] Submit the same data separately to all three partners to make it internationally accessible
- [ ] Submit only to NCBI because the other partners cannot accept new data
- [ ] Use three different project descriptions so each partner can create an independent experiment

## An HBB sequencing investigation has linked project, sample, read-run and assembly records. Which description of their roles is correct?

- [x] The project describes the investigation, the sample describes the biological material, the read run holds sequencing reads and qualities, and the assembly records a reconstructed sequence
- [ ] The four records are different names for the same DNA sequence file
- [ ] The project stores protein sequences, the sample stores transcripts, and the read run stores genes
- [ ] The archive constructs an assembly automatically whenever researchers submit a sample description

## An old paper links to a Trace Archive page that no longer opens. What is the best next step?

- [x] Keep the accession and consult the provider's current archive or migration guidance, then verify the retrieved record's identity and metadata
- [ ] Conclude that the experiment and its underlying data have been deleted
- [ ] Replace the accession with the first record returned by a search for the gene name
- [ ] Treat a record at a new website as an independent experiment, even if the accession is unchanged

## Which of these identifies one exact sequence, rather than a gene or a record that may change?

- [x] NM_000518.5
- [ ] HBB
- [ ] NM_000518
- [ ] 3043 (the NCBI Gene ID)

## UniProtKB consists of Swiss-Prot and TrEMBL. Which statement is correct?

- [x] They are two separate sections; when curators review a TrEMBL entry, it is integrated into Swiss-Prot
- [ ] Swiss-Prot is a manually annotated subset of TrEMBL
- [ ] TrEMBL is a manually annotated subset of Swiss-Prot
- [ ] Swiss-Prot accepts direct submissions of new sequences from researchers

## Rank these records from least to most checked: a GenBank submission, an XP_ RefSeq record, a Swiss-Prot entry. Which description fits the XP_ record?

- [x] Predicted by NCBI's annotation pipeline: computed, not curated, and not itself an experimental observation
- [ ] Curated by NCBI staff from the literature
- [ ] The raw sequence exactly as the original submitters deposited it
- [ ] Experimentally confirmed by mass spectrometry

## What provides the strongest evidence in UniProt that a protein has been experimentally observed?

- [x] Protein-existence level 1, "Experimental evidence at protein level"
- [ ] Its sequence can be found in UniProtKB
- [ ] A gene encoding it is annotated in the genome
- [ ] An AlphaFold model of it exists

## An experimental structure has a resolution of 1.74 Å; an AlphaFold model has a mean pLDDT of 97. Which statement is correct?

- [x] Resolution describes the detail in the experimental data on a real molecule; pLDDT is the model's own estimate of how reliable its prediction is
- [ ] Both measure the same thing, on different scales
- [ ] A higher resolution number means a more detailed structure
- [ ] pLDDT measures how well the model fits X-ray data

## Why does it matter whether a protein-protein "interaction" comes from IntAct or from STRING?

- [x] IntAct curates physical interactions from published experiments; STRING scores functional associations that also include co-expression, predictions and text mining
- [ ] STRING lists only interactions confirmed by crystal structures
- [ ] IntAct is predicted entirely by computer
- [ ] They contain the same data in different layouts

## Which statement about protein domains is correct?

- [x] A domain is a conserved part of a protein that can fold and function largely on its own, and one protein chain can contain several
- [ ] Domains are the least conserved part of a protein
- [ ] Only a stretch of at least 300 residues can be a domain
- [ ] Each domain occurs in only one protein family
