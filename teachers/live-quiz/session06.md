<!-- hand-written: the live quiz for the lecture. A warm-up at the start (three short questions on the
     day's topics, then a word cloud of what students want to learn), one question after each
     of the three blocks (guess alone, see the result, fix and run the discussion notebook, discuss
     with your neighbours, answer again; then one student, drawn at random, explains), and one
     feedback question at the end.
     A starting draft for Petras Kundrotas, whose lecture this is: change anything.
     The block questions are the discussion problems of book/notebooks/session06-discussion-*.ipynb.
     Not anonymous: answering is what counts as attendance; right or wrong is never graded.
     Figures: tools/builders/make_session06_quiz_figures.py. Slides: slides/quiz/session06.yaml.
     scripts/pick_live_quizzes.py leaves this file alone. Format: quizbinf docs/quiz-authoring.md. -->

# Session 6: Protein Structure

## Warm-up 1 of 3. An α-helix is held together mainly by ...

mode: once

- [ ] Disulphide bonds
- [x] Backbone hydrogen bonds, from residue i to residue i + 4
- [ ] Salt bridges between side chains
- [ ] Hydrogen bonds between neighbouring strands

## Warm-up 2 of 3. What does a protein's contact map show?

mode: once

- [x] Which residues are close to each other in 3D
- [ ] Which proteins interact in the cell
- [ ] The hydrophobicity along the sequence
- [ ] Where in the cell the protein is found

## Warm-up 3 of 3. During evolution, which usually changes more slowly?

mode: once

- [ ] The sequence
- [ ] Both change equally fast
- [x] The structure
- [ ] Neither changes

## Before we start: in up to three words, what do you want to learn today?

![](figs/session06-q4-blocks.png){width=85%}

type: word
max words: 3
mode: once

## Block 1. PyMOL's dss finds haemoglobin's β chain 80.8% helix and 0% strand. Haemoglobin works only as four chains; myoglobin (1MBN) has the same globin fold but works alone, as one chain. What does dss find for myoglobin?

![](figs/session06-q1-myoglobin.png){width=80%}

mode: twice

- [x] About 80% helix and 0% strand: the same as the β chain
- [ ] About 50% helix: without partner chains, some helices unfold
- [ ] About 40% helix and 30% strand: one chain alone needs strands to be stable
- [ ] Hardly any helix or strand: a chain without partners stays mostly loop

## Block 2. The globins are about 80% helix and 0% strand. Green fluorescent protein (GFP, 1EMA) is a barrel of β-strands wrapped around one central helix. What does dss find for GFP?

![](figs/session06-q2-gfp.png){width=80%}

mode: twice

- [ ] About 80% helix and 0% strand, like the globins
- [ ] About 50% helix and 50% strand
- [x] About 10% helix and 54% strand
- [ ] About 0% helix and 100% strand

## Block 3. From deoxy (T, 2HHB) to oxy (R, 1HHO) haemoglobin, each chain hardly changes shape, but the distance between the irons of the two β chains shrinks by about 5 Å. Which of the four iron–iron distances changes the least?

![](figs/session06-q3-tetramer.png){width=80%}

mode: twice

- [ ] α1–β1, the "fixed" interface
- [ ] α1–β2, the "sliding" interface
- [x] α1–α2
- [ ] None: all shrink by about 5 Å, because the whole tetramer contracts

## Before you leave: in up to three words, what was the hardest part of today?

![](figs/session06-q4-blocks.png){width=85%}

type: word
max words: 3
mode: once
