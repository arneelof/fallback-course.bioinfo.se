<!-- hand-written: the live quiz for the lecture. A warm-up at the start (three short questions on the
     day's topics, then a word cloud of what students want to learn), one question after each
     of the three blocks (answer alone, see the result, discuss with your neighbours, answer
     again; then one student, drawn at random, explains), and one feedback question at the end.
     The block questions are the discussion problems of book/notebooks/session02-discussion-*.ipynb.
     Not anonymous: answering is what counts as attendance; right or wrong is never graded.
     Figures: tools/builders/make_session02_quiz_figures.py. Slides: slides/quiz/session02.yaml.
     scripts/pick_live_quizzes.py leaves this file alone. Format: quizbinf docs/quiz-authoring.md. -->

# Session 2: Working like a computational biologist in Python

## Warm-up 1 of 3. `x = [1, 2]; y = x; y.append(3)`. What is `x` now?

mode: once

- [ ] [1, 2]
- [x] [1, 2, 3]
- [ ] [3]
- [ ] An error

## Warm-up 2 of 3. `df` has one row per gene. What does `df["padj"] < 0.05` give?

mode: once

- [ ] The genes with padj below 0.05
- [ ] The number of such genes
- [x] True or False for every gene
- [ ] An error

## Warm-up 3 of 3. Python reports an error on line 12. Where is the mistake?

mode: once

- [ ] On line 12
- [x] On line 12 or earlier
- [ ] After line 12
- [ ] In a library, not in your code

## Before we start: in up to three words, what do you want to learn today?

![](figs/session02-q4-blocks.png){width=85%}

type: word
max words: 3
mode: once

## Block 1. Two classmates look for "the most changed gene" in the RNA-seq table df (one row per gene). Both snippets run without errors. What do they return?

In log2_FoldChange, a positive value means the gene goes up, a negative value that it goes down.

![](figs/session02-q1-most-changed.png){width=100%}

mode: twice

- [ ] The same gene: both find the largest change
- [x] A: the most down-regulated gene; B: the largest change, up or down
- [ ] A: the most up-regulated gene; B: the largest change, up or down
- [ ] A: the most down-regulated gene; B: the most up-regulated gene

## Block 2. A classmate wants the average length of the globins in a compressed FASTA file. Which line contains the mistake?

![](figs/session02-q2-gzip-error.png){width=100%}

mode: twice

- [x] Line 3
- [ ] Line 4
- [ ] Line 5
- [ ] None: the code runs and prints the average length

## Block 3. In PyTorch, x = 3 and y = x². After y.backward(), x.grad is 6. Without zeroing anything, you compute y2 = x² and call y2.backward(). What does x.grad show now?

![](figs/session02-q3-backward.png){width=100%}

mode: twice

- [ ] 6: the new gradient replaces the old one
- [x] 12: the new gradient is added to the old one
- [ ] 36: the two gradients are multiplied
- [ ] An error: backward() can only be called once

## Before you leave: in up to three words, what was the hardest part of today?

![](figs/session02-q4-blocks.png){width=85%}

type: word
max words: 3
mode: once
