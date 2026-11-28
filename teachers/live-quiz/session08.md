<!-- hand-written: the live quiz for the lecture. A warm-up at the start (three short questions on the
     day's topics, then a word cloud of what students want to learn), one question after each
     of the three blocks (guess alone, see the result, fix and run the discussion notebook and
     discuss with your neighbours, answer again; then one student, drawn at random, explains),
     and one feedback question at the end. The block questions are the discussion problems of
     book/notebooks/session08-discussion-*.ipynb.
     Not anonymous: answering is what counts as attendance; right or wrong is never graded.
     Figures: tools/builders/make_session08_quiz_figures.py. Slides: slides/quiz/session08.yaml.
     scripts/pick_live_quizzes.py leaves this file alone. Format: quizbinf docs/quiz-authoring.md. -->

# Session 8: Machine Learning Foundations & Practical PyTorch

## Warm-up 1 of 3. Predicting a protein's melting temperature from its sequence is ...

mode: once

- [ ] classification
- [x] regression
- [ ] clustering
- [ ] unsupervised learning

## Warm-up 2 of 3. 95 of 100 proteins are not membrane proteins. A model always says “not membrane”. What is its accuracy?

mode: once

- [ ] 0%
- [ ] 5%
- [ ] 50%
- [x] 95%

## Warm-up 3 of 3. In a PyTorch training step, what does `loss.backward()` do?

mode: once

- [ ] Updates the weights
- [x] Computes the gradients
- [ ] Computes the loss
- [ ] Sets the gradients to zero

## Before we start: in up to three words, what do you want to learn today?

![](figs/session08-q4-blocks.png){width=85%}

type: word
max words: 3
mode: once

## Block 1. We have 55 proteins and want to predict a yes/no label: is the protein mostly helical (helix fraction above 0.5)? The only feature is the fraction of helix-forming residues. Which way of predicting the label gives the higher accuracy?

The two ways:

- (a) train a classifier (logistic regression) directly on the yes/no labels;
- (b) train a regression model (linear regression) on the helix fraction itself, and call a protein "helical" when its predicted fraction is above 0.5.

Accuracy is measured by 5-fold cross-validation.

![](figs/session08-q1-helix.png){width=90%}

mode: twice

- [ ] (a) The classifier: it is trained on exactly the yes/no question
- [ ] (b) The regression: the numbers keep information that the labels throw away
- [x] About the same: both end up drawing one threshold on one feature
- [ ] Neither: one feature cannot separate helical from non-helical proteins

## Block 2. The 700 localisation proteins are clustered at 30%, 50%, 70% and 90% sequence identity. As the cutoff rises, what happens to the share of validation proteins with a homolog in training, and to the accuracy advantage those proteins get?

![](figs/session08-q2-leakage.png){width=90%}

mode: twice

- [x] Both fall, and the advantage is already gone at 50%
- [ ] The share falls, but the advantage grows: closer relatives help more
- [ ] Both stay about the same: a homolog is a homolog
- [ ] The share rises: a stricter cutoff finds more homologs

## Block 3. A one-hot protein sequence (L residues × 20) goes into either nn.Linear(L · 20, 64) or nn.Conv1d(20, 64, kernel_size=7). How do the two layers' parameter counts change from L = 150 to L = 1000?

![](figs/session08-q3-layers.png){width=90%}

mode: twice

- [ ] Both grow about seven times
- [x] nn.Linear grows about seven times; nn.Conv1d stays the same
- [ ] Both stay the same: each has 64 units either way
- [ ] nn.Conv1d grows; nn.Linear stays the same

## Before you leave: in up to three words, what was the hardest part of today?

![](figs/session08-q4-blocks.png){width=85%}

type: word
max words: 3
mode: once
