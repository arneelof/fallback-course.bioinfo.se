<!-- hand-written: the live quiz for the lecture. A warm-up at the start (three short questions on the
     day's topics, then a word cloud of what students want to learn), one question after each
     of the three blocks (guess alone, see the result, fix and run the discussion notebook, discuss
     with your neighbours, answer again; then one student, drawn at random, explains), and one
     feedback question at the end.
     The block questions are the discussion problems of book/notebooks/session09-discussion-*.ipynb.
     Not anonymous: answering is what counts as attendance; right or wrong is never graded.
     Figures: tools/builders/make_session09_quiz_figures.py. Slides: slides/quiz/session09.yaml.
     scripts/pick_live_quizzes.py leaves this file alone. Format: quizbinf docs/quiz-authoring.md. -->

# Session 9: How a Neural Network Learns, and Why Training Fails

## Warm-up 1 of 3. The chain rule: if y = f(g(x)), then dy/dx is ...

mode: once

- [ ] f′(x) · g′(x)
- [x] f′(g(x)) · g′(x)
- [ ] f′(x) + g′(x)
- [ ] f(g′(x))

## Warm-up 2 of 3. The true label is 1 and the model predicts p = 0.01. The cross-entropy loss is −ln p. About how large is it?

mode: once

- [ ] 0.01
- [ ] 0.99
- [x] 4.6
- [ ] 100

## Warm-up 3 of 3. Training accuracy 100%, validation accuracy 60%. What is this?

mode: once

- [ ] Underfitting
- [x] Overfitting
- [ ] A learning rate that is too small
- [ ] A vanishing gradient

## Before we start: in up to three words, what do you want to learn today?

![](figs/session09-q4-blocks.png){width=85%}

type: word
max words: 3
mode: once

## Block 1. A tiny network: two inputs, one ReLU hidden unit, one sigmoid output. The hidden unit's input is z1 = −0.52. After loss.backward(), what is w1.grad?

![](figs/session09-q1-relu.png){width=100%}

mode: twice

- [ ] About −0.24: the error flows back through w3 to w1
- [x] Exactly 0: ReLU passes no gradient back for a negative input
- [ ] Small but not zero: the gradient shrinks, as with tanh
- [ ] −0.52, the value of z1

## Block 2. On GB1, a linear model on the one-hot encoding of four positions gets test R² = 0.50, and a 64/64 network 0.79. Give the linear model one feature for every pair of residues at every pair of positions (2,480 features). What test R² does it reach?

![](figs/session09-q2-epistasis.png){width=90%}

mode: twice

- [ ] About 0.50: it is still a linear model, so nothing changes
- [x] About 0.74: most of the way to the network
- [ ] About 0.79 or above: it matches the network
- [ ] Below 0.50: 2,480 features overfit 20,000 variants

## Block 3. A trained network with dropout (p = 0.5) predicts the same biopsy five times, without model.eval(). What does it print?

![](figs/session09-q3-dropout.png){width=100%}

mode: twice

- [ ] The same probability five times: the weights do not change
- [x] Five different probabilities: dropout still switches off random units
- [ ] An error: a model with dropout cannot predict
- [ ] 0.5 five times: dropout halves every output

## Before you leave: in up to three words, what was the hardest part of today?

![](figs/session09-q4-blocks.png){width=85%}

type: word
max words: 3
mode: once
