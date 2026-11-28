<!-- hand-written: the live quiz for the lecture. A warm-up at the start (three short questions on the
     day's topics, then a word cloud of what students want to learn), one question after each
     of the three blocks (answer alone, see the result, discuss with your neighbours, answer
     again; then one student, drawn at random, explains), and one feedback question at the end.
     Not anonymous: answering is what counts as attendance; right or wrong is never graded.
     Figures: tools/builders/make_session07_quiz_figures.py. Slides: slides/quiz/session07.yaml.
     scripts/pick_live_quizzes.py leaves this file alone. Format: quizbinf docs/quiz-authoring.md. -->

# Session 7: Linear Models, Gradient Descent, the XOR Problem & Secondary Structure Prediction

## Warm-up 1 of 3. In gradient descent, each step moves the weights ...

mode: once

- [ ] along the gradient: uphill
- [x] against the gradient: downhill
- [ ] towards zero
- [ ] at random

## Warm-up 2 of 3. Which logic function is true when exactly one of two inputs is true?

mode: once

- [ ] AND
- [ ] OR
- [x] XOR
- [ ] NAND

## Warm-up 3 of 3. Which structure is held together by hydrogen bonds from residue i to residue i + 4?

mode: once

- [ ] β-strand
- [x] α-helix
- [ ] Coil
- [ ] Disulphide bond

## Before we start: in up to three words, what do you want to learn today?

![](figs/session07-q4-blocks.png){width=85%}

type: word
max words: 3
mode: once

## Block 1. Two training examples, (2, 6) and (3, 3), and one weight: prediction = w · x. No single w fits both. Starting at w = 0 with η = 0.02, where does gradient descent take w?

![](figs/session07-q1-disagree.png){width=80%}

mode: twice

- [ ] To w = 3: it fits the first example
- [ ] To w = 2: halfway between the two
- [x] To about w = 1.6: closer to w = 1, which fits the second example
- [ ] Nowhere: w keeps jumping, because the two examples pull in opposite directions

## Block 2. A network with two hidden units: h₁ = ReLU(x₁ + x₂), h₂ = ReLU(x₁ + x₂ − 1), z = h₁ − 2h₂. Which logic function of x₁ and x₂ does z compute?

![](figs/session07-q2-network.png){width=80%}

mode: twice

- [ ] AND
- [ ] OR
- [x] XOR
- [ ] None: without training, the weights compute nothing useful

## Block 3. The two pictures of today. Which of these methods are picture 2: a hidden layer with a nonlinear activation? Tick all that apply.

![](figs/session07-q3-pictures.png){width=90%}

type: multi
mode: twice

- [ ] PSSM
- [ ] Perceptron
- [ ] Logistic regression
- [ ] GOR
- [x] MLP
- [x] PHD

## Before you leave: in up to three words, what was the hardest part of today?

![](figs/session07-q4-blocks.png){width=85%}

type: word
max words: 3
mode: once
