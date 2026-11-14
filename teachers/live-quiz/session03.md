<!-- hand-written: ten short conceptual questions aligned with the revised Session 3.
     Correct-answer positions balanced and randomized; distractors shuffled reproducibly with xorshift32 seed 20261113.
     Run the ten questions once each in the final 10 minutes.
     A new title preserves any previously used quiz and its recorded answers.
     Local source only: this file does not update the running quiz service.
     scripts/pick_live_quizzes.py leaves hand-written files alone. -->

# Session 3: Biological Databases (2027 review)

## 1. You find the same HBB accession and sequence through NCBI and ENA. What have you found?

mode: once

- [ ] Proof that every annotation in the record is correct
- [x] Two access routes to one shared archival record
- [ ] Two genes that happen to have the same name
- [ ] Two independent experiments confirming the annotation

## 2. Which identifier specifies the version of the HBB mRNA sequence used in an analysis?

mode: once

- [ ] NCBI Gene ID 3043
- [x] NM_000518.5
- [ ] HBB
- [ ] NP_000509.1

## 3. You have an HBB transcript sequence. What else is needed to estimate HBB RNA abundance in a blood sample?

mode: once

- [x] Expression measurements from the relevant sample or condition
- [ ] The same sequence shown at a second archive website
- [ ] Only the amino-acid sequence of beta-globin
- [ ] Only the transcript sequence length

## 4. A reviewed UniProt entry describes a protein function. How should you assess support for that particular claim?

mode: once

- [ ] Assume every claim in a reviewed entry was demonstrated experimentally
- [ ] Use the number of linked databases as the measure of experimental support
- [ ] Reject the claim unless a three-dimensional structure is available
- [x] Inspect the evidence attached to the claim and its linked references

## 5. You want to examine an intronic HBB variant. Which sequence export retains its position within the selected transcript region?

mode: once

- [ ] The encoded protein sequence
- [ ] The mature spliced transcript only
- [x] The genomic span containing the exons and intervening introns
- [ ] The coding sequence only

## 6. In a genome browser, what best helps locate a ClinVar variant relative to an HBB exon?

mode: once

- [ ] Change the assembly until the variant looks closer to an exon
- [ ] Hide the transcript annotation and inspect only the variant colour
- [x] Display the ClinVar and transcript annotation tracks on the same assembly and interval
- [ ] Count every overlapping track as independent evidence for the variant

## 7. You need sequences and selected metadata for 200 supplied accessions, and must repeat the task next month. Which route is most suitable?

mode: once

- [ ] Manually copy each record page into a document
- [x] A script using a documented programmatic interface, with record checks and saved retrieval details
- [ ] Download a file without checking which records it contains
- [ ] Take a screenshot of the first record and reuse it

## 8. You want papers about either HBB or beta globin, and every result should also concern splicing. Which query expresses that grouping?

mode: once

- [ ] HBB AND "beta globin" AND splicing
- [ ] HBB OR ("beta globin" AND splicing)
- [x] (HBB OR "beta globin") AND splicing
- [ ] HBB NOT splicing

## 9. A paper has a PubMed record. What can you conclude about access to its full text?

mode: once

- [ ] The complete paper is always stored in PubMed
- [ ] The paper is necessarily available free in PubMed Central
- [ ] Only the abstract can ever be read
- [x] Full-text availability must be checked separately through the record links, a repository or university access

## 10. An illustrative AI summary says an HBB treatment corrected 8.25% of cells. The paper reports 8.25% correctly spliced HBB RNA in cultured cells. What is the problem?

mode: once

- [x] The summary changes an RNA measurement into a percentage of corrected cells
- [ ] Any result from cultured cells establishes a treatment effect in patients
- [ ] The two percentages necessarily describe the same biological outcome
- [ ] A real paper with a valid DOI makes the summary automatically reliable
