<!-- hand-written: the live quiz for the lecture. A warm-up at the start (three short questions on the
     day's topics, then a word cloud of what students want to learn), one question after each
     of the three blocks (guess alone, see the result, fix and run the discussion notebook, discuss
     with your neighbours, answer again; then one student, drawn at random, explains), and one
     feedback question at the end.
     The block questions are the discussion problems of book/notebooks/session12-discussion-*.ipynb.
     Not anonymous: answering is what counts as attendance; right or wrong is never graded.
     Figures: tools/builders/make_session12_quiz_figures.py. Slides: slides/quiz/session12.yaml.
     scripts/pick_live_quizzes.py leaves this file alone. Format: quizbinf docs/quiz-authoring.md. -->

# Session 12: AlphaFold and Generative Models of Protein Structure

## Warm-up 1 of 3. Two residues that touch in the structure tend to mutate together over evolution. What is this called?

mode: once

- [ ] Conservation
- [ ] Homology
- [x] Coevolution
- [ ] Convergent evolution

## Warm-up 2 of 3. A region of an AlphaFold model has pLDDT 30. What does that mean?

mode: once

- [ ] 30% of its atoms are wrong
- [ ] It is a β-strand
- [ ] It is predicted very accurately
- [x] AlphaFold is unsure of its local structure; often it is disordered

## Warm-up 3 of 3. How does a diffusion model generate a new example?

mode: once

- [ ] It copies the nearest training example
- [x] It starts from random noise and removes it step by step
- [ ] It folds the chain with a physics force field
- [ ] It searches the PDB for a match

## Before we start: in up to three words, what do you want to learn today?

![](figs/session12-q4-blocks.png){width=85%}

type: word
max words: 3
mode: once

## Block 1. Two antiparallel β-strands pair up, and residue i is in contact with residue j. Which neighbouring pair is then most likely to be in contact too?

The two strands run in opposite directions, as the arrows show.

![](figs/session12-q1-strands.png){width=80%}

mode: twice

- [ ] (i + 1, j + 1): contacts continue along the diagonal of the map
- [x] (i + 1, j − 1): contacts continue across the diagonal of the map
- [ ] (i + 1, j) and (i, j + 1) most: the residues right next to the contact
- [ ] All neighbouring pairs equally: contacts are independent of each other

## Block 2. MDM2 binds p53 and marks it for degradation. The AlphaFold DB model of full-length human MDM2 (491 residues) has a mean pLDDT of 63. What is the mean pLDDT of its p53-binding domain, residues 25–109?

![](figs/session12-q2-plddt.png){width=100%}

mode: twice

- [ ] About 63: the same as the whole chain
- [x] About 95: the domain is very confident, and the rest pulls the mean down
- [ ] About 40: with a mean of 63, no part of the model can be trusted
- [ ] It cannot be said without a crystal structure

## Block 3. A toy diffusion model trained on 4000 points of a ring generates points spread evenly along the ring. What does it generate when it is trained on only 20 points?

![](figs/session12-q3-ring.png){width=100%}

mode: twice

- [ ] Points spread evenly along the ring, as with 4000 points
- [x] Points on the ring, but bunched around the 20 training points
- [ ] Exact copies of the 20 training points, and nothing else
- [ ] Noise: 20 points are too few to learn anything

## Before you leave: in up to three words, what was the hardest part of today?

![](figs/session12-q4-blocks.png){width=85%}

type: word
max words: 3
mode: once
