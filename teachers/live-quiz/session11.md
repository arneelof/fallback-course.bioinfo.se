<!-- hand-written: the live quiz for the lecture. A warm-up at the start (three short questions on the
     day's topics, then a word cloud of what students want to learn), one question after each
     of the three blocks (guess alone, see the result, fix and run the discussion notebook and
     discuss with your neighbours, answer again; then one student, drawn at random, explains),
     and one feedback question at the end.
     The block questions are the discussion problems of book/notebooks/session11-discussion-*.ipynb.
     Not anonymous: answering is what counts as attendance; right or wrong is never graded.
     Figures: tools/builders/make_session11_quiz_figures.py. Slides: slides/quiz/session11.yaml.
     scripts/pick_live_quizzes.py leaves this file alone. Format: quizbinf docs/quiz-authoring.md. -->

# Session 11: Sequences, Language Models and SignalP

## Warm-up 1 of 3. During training, a gradient is multiplied by 0.8 at each of 60 steps back along a sequence. What happens to it?

mode: once

- [ ] It stays about the same
- [ ] It grows very large
- [x] It all but vanishes: about one millionth is left
- [ ] It becomes exactly 0.8

## Warm-up 2 of 3. In self-attention, one position gives a weight to every position in the sequence. What is true of these weights?

mode: once

- [ ] They are all equal
- [ ] They are 0 or 1
- [x] They add up to 1
- [ ] They depend only on the distance between the positions

## Warm-up 3 of 3. What does a signal peptide at the N-terminus of a protein do?

mode: once

- [ ] It starts translation
- [x] It sends the protein into the secretory pathway
- [ ] It marks the protein for degradation
- [ ] It binds the protein to DNA

## Before we start: in up to three words, what do you want to learn today?

![](figs/session11-q4-blocks.png){width=85%}

type: word
max words: 3
mode: once

## Block 1. A forward LSTM and a bidirectional LSTM label each of the first 70 residues of 741 test proteins as signal peptide or not. In the proteins that have a signal peptide, where along the sequence is the gap in mislabelled residues between the two models largest?

![](figs/session11-q1-context.png){width=100%}

mode: twice

- [x] At residues 1–5: the forward LSTM has not yet seen the hydrophobic h-region
- [ ] Near the cleavage site: those residues are the hardest for any model
- [ ] Evenly along the sequence: the bidirectional model is simply better everywhere
- [ ] Nowhere: an LSTM's memory makes the reading direction irrelevant

## Block 2. ESM-2 was trained only to fill in masked residues and never saw a structure. From its attention maps, a small predictor picks β-globin's most likely long-range contacts. How does the fraction of these that are real contacts change from the smallest model (8M parameters) to the largest (650M)?

![](figs/session11-q2-contacts.png){width=70%}

mode: twice

- [ ] About 0.9 at every size: the structure is there from the start
- [ ] Near 0 at every size: without structures in training, attention holds no structure
- [x] Near 0 for the smallest model, rising to about 0.9 for the largest
- [ ] Highest for the smallest model: larger models overfit to sequences

## Block 3. Two signal-peptide detectors are trained on eukaryotic proteins only and tested on bacterial proteins: a logistic regression on one-hot encoded residues, and one on frozen ESM-2 embeddings. How do they do on the bacteria?

![](figs/session11-q3-transfer.png){width=90%}

mode: twice

- [ ] Both keep nearly all their performance: a signal peptide is a signal peptide
- [ ] One-hot does better: ESM-2 has learnt mainly eukaryotic proteins
- [x] ESM-2 keeps most of its performance; one-hot loses much more
- [ ] Both fall to near zero: the two kingdoms are too different

## Before you leave: in up to three words, what was the hardest part of today?

![](figs/session11-q4-blocks.png){width=85%}

type: word
max words: 3
mode: once
