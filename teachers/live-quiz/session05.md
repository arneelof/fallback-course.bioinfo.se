<!-- hand-written: the live quiz for the lecture. A warm-up at the start (three short questions on the
     day's topics, then a word cloud of what students want to learn), one question after each
     of the three blocks (guess alone, see the result, fix and run the discussion notebook, discuss
     with your neighbours, answer again; then one student, drawn at random, explains), and one
     feedback question at the end.
     A starting draft for Petras Kundrotas, whose lecture this is: change anything.
     The block questions are the discussion problems of book/notebooks/session05-discussion-*.ipynb.
     Not anonymous: answering is what counts as attendance; right or wrong is never graded.
     Figures: tools/builders/make_session05_quiz_figures.py. Slides: slides/quiz/session05.yaml.
     scripts/pick_live_quizzes.py leaves this file alone. Format: quizbinf docs/quiz-authoring.md. -->

# Session 5: Advanced Database Search & Profile Methods

## Warm-up 1 of 3. BLAST reports a hit with E-value 0.001. What does that mean?

mode: once

- [ ] The hit is homologous with 99.9% probability
- [x] About 0.001 hits this good are expected by chance in this search
- [ ] The two sequences differ at 0.1% of their positions
- [ ] The alignment has 0.001 gaps per residue

## Warm-up 2 of 3. In one column of an alignment, 4 of 5 sequences have A. Without pseudocounts, what is the frequency of A?

mode: once

- [ ] 4
- [ ] 0.25
- [ ] 0.2
- [x] 0.8

## Warm-up 3 of 3. In a Markov chain, the next state depends on ...

mode: once

- [x] only the current state
- [ ] all the earlier states
- [ ] nothing: it is random
- [ ] the final state

## Before we start: in up to three words, what do you want to learn today?

![](figs/session05-q4-blocks.png){width=85%}

type: word
max words: 3
mode: once

## Block 1. BLAST's neighbour words: every word that scores at least T = 12 against a query word with BLOSUM62. LWG has 49. At the same threshold, how many does GKV have, the word right next to it in haemoglobin beta?

![](figs/session05-q1-words.png){width=100%}

mode: twice

- [ ] About as many as LWG: same length, same threshold
- [ ] More than LWG: G, K and V have many similar residues
- [x] Far fewer: GKV starts from a much lower self-score
- [ ] None: no other word can reach 12

## Block 2. A PSSM is built from five aligned proteins, with a pseudocount of +1 for every residue at every position. The new sequence GGLSP has a G at position 1, where none of the five has one. What happens to its score, compared with the consensus AGLSP?

![](figs/session05-q2-pseudocounts.png){width=90%}

mode: twice

- [ ] Minus infinity: G was never seen at position 1
- [x] Lower than AGLSP, but finite and still positive
- [ ] The same as AGLSP: one position hardly matters
- [ ] Higher than AGLSP: G is common in the alignment

## Block 3. BRCA1 has three real Pfam domains. Which of the three matches has the smallest E-value, that is, the most significant match?

![](figs/session05-q3-domains.png){width=100%}

mode: twice

- [ ] The RING finger: the best-known of the three
- [ ] The BRCT domain: the family is named after BRCA1
- [x] The serine-rich domain
- [ ] About the same: all three domains are real

## Before you leave: in up to three words, what was the hardest part of today?

![](figs/session05-q4-blocks.png){width=85%}

type: word
max words: 3
mode: once
