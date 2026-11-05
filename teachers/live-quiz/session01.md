<!-- hand-written: the live quiz for the lecture. A warm-up at the start (three short questions on the
     day's topics, then a word cloud of what students want to learn), one question after each
     of the three blocks (answer alone, see the result, discuss with your neighbours, answer
     again; then one student, drawn at random, explains), and one feedback question at the end.
     The block questions are the discussion problems of book/notebooks/session01-discussion-*.ipynb.
     Not anonymous: answering is what counts as attendance; right or wrong is never graded.
     Figures: tools/builders/make_session01_quiz_figures.py. The slides follow the same steps.
     scripts/pick_live_quizzes.py leaves this file alone. Format: quizbinf docs/quiz-authoring.md. -->

# Session 1: Math Prerequisites

## Warm-up 1 of 3. A is a 3 × 2 matrix and v is a vector of 2 numbers. What is A v?

mode: once

- [x] A vector of 3 numbers
- [ ] A vector of 2 numbers
- [ ] A 3 × 2 matrix
- [ ] Not defined

## Warm-up 2 of 3. What is the derivative of eˣ?

mode: once

- [ ] x eˣ⁻¹
- [x] eˣ
- [ ] ln x
- [ ] 1/x

## Warm-up 3 of 3. What is log₂ 8?

mode: once

- [x] 3
- [ ] 4
- [ ] 2.08
- [ ] 16

## Before we start: in up to three words, what do you want to learn today?

![](figs/session01-q4-blocks.png){width=85%}

type: word
max words: 3
mode: once

## Block 1. Which of the vectors a, b and c points in the most similar direction to x = (2, 1), that is, makes the smallest angle with it?

The figure shows the three vectors and their dot products with x.

![](figs/session01-q1-vectors.png){width=70%}

mode: twice

- [ ] b: its dot product with x is ten times larger than the others
- [ ] a and b equally: they point in the same direction
- [x] c: it points exactly along x
- [ ] a and c equally: they have the same dot product with x

## Block 2. The loss is L(w) = (w − 4)², and we start at w = 0. With learning rate η = 0.5, one gradient descent step lands exactly on the minimum. What happens with η = 2 if we keep stepping?

![](figs/session01-q2-learning-rate.png){width=80%}

mode: twice

- [ ] It lands on the minimum in one step, like η = 0.5
- [ ] It overshoots a little, then settles at w = 4 after a few zig-zags
- [x] Each step overshoots further, on alternating sides: it moves away from the minimum
- [ ] It overshoots once to w = 8 and stays there

## Block 3. Every submitted assignment is checked by an automatic plagiarism detector. Your assignment gets flagged. How likely is it that it really is plagiarised?

The detector is good but not perfect:

- it flags 85% of the assignments that are plagiarised,
- and it also wrongly flags 8% of the genuine ones.

In this course, 3% of all assignments are plagiarised. The tree shows 10 000 assignments.

![](figs/session01-q3-plagiarism.png){width=85%}

mode: twice

- [ ] About 85%: that is how often the detector catches plagiarism
- [ ] About 92%: the detector is wrong only 8% of the time
- [x] About 25%: most flags come from the many genuine assignments
- [ ] About 3%: the flag says nothing beyond the base rate

## Before you leave: in up to three words, what was the hardest part of today?

![](figs/session01-q4-blocks.png){width=85%}

type: word
max words: 3
mode: once
