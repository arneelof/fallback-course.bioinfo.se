<!-- hand-written: the live quiz for the lecture. A warm-up at the start (three short questions on the
     day's topics, then a word cloud of what students want to learn), one question after each
     of the three blocks (guess alone, see the result, fix and run the discussion notebook, discuss
     with your neighbours, answer again; then one student, drawn at random, explains), and one
     feedback question at the end.
     The block questions are the discussion problems of book/notebooks/session10-discussion-*.ipynb.
     Not anonymous: answering is what counts as attendance; right or wrong is never graded.
     Figures: tools/builders/make_session10_quiz_figures.py. Slides: slides/quiz/session10.yaml.
     scripts/pick_live_quizzes.py leaves this file alone. Format: quizbinf docs/quiz-authoring.md. -->

# Session 10: CNNs, Classic & Modern

## Warm-up 1 of 3. A 3 × 3 kernel slides over a 6 × 6 image, without padding, one step at a time. How large is the output?

mode: once

- [ ] 6 × 6
- [x] 4 × 4
- [ ] 3 × 3
- [ ] 2 × 2

## Warm-up 2 of 3. A filter, 8 bases wide, slides along one-hot encoded DNA. What is it most like?

mode: once

- [ ] A BLAST alignment
- [ ] A phylogenetic tree
- [x] A position weight matrix
- [ ] A restriction enzyme

## Warm-up 3 of 3. What does transfer learning mean?

mode: once

- [ ] Moving the model from the CPU to a GPU
- [x] Starting from a network trained on another, larger data set
- [ ] Copying labels from similar proteins
- [ ] Training two networks and averaging them

## Before we start: in up to three words, what do you want to learn today?

![](figs/session10-q4-blocks.png){width=85%}

type: word
max words: 3
mode: once

## Block 1. A convolutional layer, nn.Conv2d(3, 64, kernel_size=3, bias=False), is applied to a 224 × 224 RGB image, and then to a 448 × 448 one. How many weights does it have?

![](figs/session10-q1-conv-weights.png){width=100%}

mode: twice

- [x] 1,728 for both images
- [ ] 1,728, then 6,912: the larger image has four times as many pixels
- [ ] 9,633,792, then 38,535,168: one weight per pixel, channel and filter
- [ ] 576 for both images

## Block 2. One filter, 7 residues wide, responds to L, I, V and F. Protein A has a hydrophobic stretch at residues 2–10, protein B the same stretch at residues 81–89. After global max pooling, what does the filter report?

![](figs/session10-q2-pooling.png){width=90%}

mode: twice

- [x] The same value for both proteins
- [ ] A higher value for A: the stretch is at the N-terminus
- [ ] A higher value for B: the filter has more sequence before the stretch
- [ ] Zero for both: pooling removes the signal

## Block 3. A tile goes through 16 random 3 × 3 filters and global max pooling. Shift the tile by 8 pixels, or turn it by 90°: which of the two changes the 16 pooled features?

![](figs/session10-q3-turn.png){width=90%}

mode: twice

- [ ] Only the shift
- [x] Only the turn
- [ ] Both
- [ ] Neither: a CNN ignores both

## Before you leave: in up to three words, what was the hardest part of today?

![](figs/session10-q4-blocks.png){width=85%}

type: word
max words: 3
mode: once
