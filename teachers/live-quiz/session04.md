<!-- hand-written: the live quiz for the lecture. A warm-up at the start (three short questions on the
     day's topics, then a word cloud of what students want to learn), one question after each
     of the three blocks (guess alone, see the result, fix and run the discussion notebook and
     discuss with your neighbours, answer again; then one student, drawn at random, explains),
     and one feedback question at the end.
     A starting draft for Petras Kundrotas, who gives this lecture: change anything you like.
     The block questions are the discussion problems of book/notebooks/session04-discussion-*.ipynb.
     Not anonymous: answering is what counts as attendance; right or wrong is never graded.
     Figures: tools/builders/make_session04_quiz_figures.py. Slides: slides/quiz/session04.yaml.
     scripts/pick_live_quizzes.py leaves this file alone. Format: quizbinf docs/quiz-authoring.md. -->

# Session 4: Sequence Alignment

## Warm-up 1 of 3. Two genes in different species descend from one gene in their last common ancestor, split by speciation. They are ...

mode: once

- [ ] paralogs
- [x] orthologs
- [ ] analogs
- [ ] unrelated

## Warm-up 2 of 3. An affine gap penalty has g_open = −10 and g_ext = −1. What does one gap of length 3 cost?

mode: once

- [x] −12
- [ ] −13
- [ ] −30
- [ ] −3

## Warm-up 3 of 3. A column of a multiple alignment has the same amino acid in every sequence. What is its entropy?

mode: once

- [x] 0
- [ ] 1
- [ ] log₂ 20, the largest possible
- [ ] It depends on the amino acid

## Before we start: in up to three words, what do you want to learn today?

![](figs/session04-q4-blocks.png){width=85%}

type: word
max words: 3
mode: once

## Block 1. Align x = ATCG against y = TCG, with match +1, mismatch −1 and gap −1. Which scores higher, global (Needleman-Wunsch) or local (Smith-Waterman) alignment, and what are the scores?

![](figs/session04-q1-local-global.png){width=80%}

mode: twice

- [x] Global 2, local 3: local can leave out the leading A
- [ ] Both 3: the best alignment is TCG against TCG either way
- [ ] Global 3, local 2: global uses more of the sequence
- [ ] Both 2: the leading A costs a gap either way

## Block 2. A gap of four residues sits in an alignment as one block, or as four single gaps. A linear penalty (g = −1) charges −4 either way. What does an affine penalty (g_open = −8, g_ext = −1) charge?

![](figs/session04-q2-gaps.png){width=90%}

mode: twice

- [x] −11 for the block, −32 for the scattered gaps
- [ ] −11 for both: like linear, it only counts the gap length
- [ ] −32 for the block, −11 for the scattered gaps
- [ ] −8 for the block, −32 for the scattered gaps

## Block 3. Four sequences have the true history ((A, B), (C, D)), but B evolved much faster than the others. Progressive alignment builds its guide tree from these distances by UPGMA. What does UPGMA do?

![](figs/session04-q3-guide-tree.png){width=85%}

mode: twice

- [ ] It merges A and B first: they share the most recent ancestor
- [ ] It merges C and D first, then joins A and B as relatives
- [x] It merges C and D first, then A joins them; B is added last
- [ ] It merges B first: it is the most different

## Before you leave: in up to three words, what was the hardest part of today?

![](figs/session04-q4-blocks.png){width=85%}

type: word
max words: 3
mode: once
