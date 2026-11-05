# KB8029 Bioinformatics: marking guide for the Q&A 2 practice exam (Sessions 7-12)

Q&A 2, Friday 19 March 2027. Draft for review by the course teachers.

**How to mark.** Swap papers with your neighbour. For each part, compare the answer with the model answer and give the points in the table; half points are fine. Wording does not have to match: give the points when the idea is there. In calculations, mark the method as well as the result. If a number from an earlier part is wrong but is then used correctly, give full points for the later part ("follow-through"). When you disagree, ask a TA.

---

## Brain dump (7 minutes, before the practice exam)

Books and notes closed. The teacher picks two or three of these topics. Each student writes everything they remember about them, as keywords, formulas and small sketches. Afterwards, compare with the lists below: these are the points a good brain dump contains, and what is missing is what to reread.

### Topic A: How a neural network learns (Sessions 7 and 9)

- The weighted sum $z = w_1 x_1 + \dots + w_n x_n + b$; the bias moves the decision boundary away from the origin; $z = 0$ is a straight line (hyperplane).
- One weighted sum draws one straight boundary, so it cannot represent XOR. A hidden layer with a **nonlinear** activation can; without the nonlinearity, linear layers collapse into one, $W_2(W_1 x + b_1) + b_2$.
- Activations: step (no useful gradient), sigmoid, tanh, ReLU.
- Loss: mean squared error for regression, cross-entropy $-\log p(\text{true class})$ for classification; confident mistakes are expensive.
- Gradient descent: $w_{\text{new}} = w - \eta\,\partial L/\partial w$; the learning rate $\eta$; too small is slow, too large overshoots.
- Backpropagation: the chain rule from the loss backwards, reusing each layer's error signal.
- The training loop: zero the gradients, forward pass, loss, `loss.backward()`, `optimizer.step()`; mini-batches, epochs, SGD, momentum, Adam.
- Why training fails: equal starting weights (symmetry), vanishing gradients in deep sigmoid networks ($0.25^n$), a bad learning rate or optimiser.
- Overfitting and the remedies: more data, a smaller model or a better architecture, early stopping, L2 (weight decay) and L1, dropout (`model.train()` / `model.eval()`).

### Topic B: Evaluating a model honestly (Session 8)

- Training set fits the weights, validation set makes choices, test set is used once at the end.
- Regression vs. classification, and the output, loss and metrics that go with each (RMSE, Pearson $r$, $R^2$ vs. confusion matrix, precision, recall, $F_1$, MCC, ROC/AUROC).
- Precision $= TP/(TP+FP)$, recall $= TP/(TP+FN)$; the trade-off when the threshold moves.
- Accuracy misleads with unbalanced classes: compare with "always the commonest class"; MCC is 0 for such a baseline.
- Leakage through the samples (homologs in both sets, several samples from one patient), the preprocessing (normalising on all data) and the evaluation (repeatedly looking at the test set).
- Homology partitioning: cluster (e.g. MMseqs2 at 30% identity) and put whole clusters into one set.
- One split is noisy; k-fold cross-validation; always compare with a simple baseline.

### Topic C: How a model uses sequence context (Sessions 10 and 11)

- Convolution: a small kernel reused at every position (weight sharing), far fewer weights than a dense layer; kernel size, padding, stride, pooling, number of filters.
- Equivariance vs. invariance; global pooling gives a position-invariant summary and forgets where a motif was.
- Receptive field grows with depth and pooling; first-layer filters on one-hot DNA or protein are learned PWMs.
- RNN: hidden state $h_t = \tanh(W_{xh} x_t + W_{hh} h_{t-1} + b_h)$; vanishing and exploding gradients through time; the LSTM's additive cell state; a bidirectional LSTM also sees what comes after a position.
- Self-attention: query, key, value; $\text{softmax}(QK^\top/\sqrt{d_k})\,V$; any two positions in one step.
- Transformer block: several heads, feed-forward network, residual connections and layer normalisation, position encoding.
- Masked (BERT-style, ESM-2) vs. next-token (GPT-style) language models; contextual embeddings; foundation models: pretrain, represent, adapt; why they help most when labels are scarce (SignalP 6.0).

---

## Question 1: A forward pass and one gradient-descent step (5 p)

| Part | Points |
|---|---|
| a. Forward pass | 1 |
| b. Gradients by the chain rule | 2 |
| c. One update and the new loss | 1 |
| d. The example with zero gradients | 1 |

### Model answer

**a.** $z = 1 \cdot 1 + 0.5 \cdot 2 - 1 = 1$, so $h = \max(0, 1) = 1$, $\hat y = v h = 2 \cdot 1 = 2$, and $L = (2 - 4)^2 = 4$.

**b.** Start from the loss and move backwards:

- $\partial L / \partial \hat y = 2(\hat y - y) = 2(2 - 4) = -4$
- $\partial L / \partial v = \partial L / \partial \hat y \cdot h = -4 \cdot 1 = -4$
- $\partial L / \partial h = \partial L / \partial \hat y \cdot v = -4 \cdot 2 = -8$
- $\partial h / \partial z = 1$, because $z = 1 > 0$ (ReLU passes positive values unchanged)
- $\partial L / \partial w_1 = \dfrac{\partial L}{\partial \hat y}\,\dfrac{\partial \hat y}{\partial h}\,\dfrac{\partial h}{\partial z}\,\dfrac{\partial z}{\partial w_1} = (-4)(2)(1)(x_1 = 1) = -8$
- $\partial L / \partial w_2 = (-8)(x_2 = 2) = -16$
- $\partial L / \partial b = (-8)(1) = -8$

All four gradients are negative: increasing any weight would lower the loss, which makes sense because the prediction (2) is below the target (4).

**c.** With $\eta = 0.025$:

| Weight | Old | $-\eta \cdot$ gradient | New |
|---|---|---|---|
| $v$ | 2 | $-0.025 \cdot (-4) = +0.1$ | 2.1 |
| $w_1$ | 1 | $-0.025 \cdot (-8) = +0.2$ | 1.2 |
| $w_2$ | 0.5 | $-0.025 \cdot (-16) = +0.4$ | 0.9 |
| $b$ | −1 | $-0.025 \cdot (-8) = +0.2$ | −0.8 |

New forward pass: $z = 1.2 \cdot 1 + 0.9 \cdot 2 - 0.8 = 2.2$, $h = 2.2$, $\hat y = 2.1 \cdot 2.2 = 4.62$, $L = (4.62 - 4)^2 = 0.62^2 \approx 0.38$. The loss fell from 4 to about 0.38. (The prediction overshoots the target a little, but it is much closer than before.)

**d.** $z = 1 \cdot 0 + 0.5 \cdot 1 - 1 = -0.5$, so $h = 0$, $\hat y = 0$ and $L = (0 - 1)^2 = 1$. **All four gradients are zero.** For $w_1$, $w_2$ and $b$ the chain passes through $\partial h / \partial z$, which is 0 because ReLU is flat for $z < 0$. For $v$, $\partial L / \partial v = \partial L / \partial \hat y \cdot h = -2 \cdot 0 = 0$. So this example cannot change any weight, even though its prediction is wrong. If $z < 0$ for every training example, the unit never gets a gradient and never recovers: it is a "dead" ReLU, and this network would output 0 for everything.

### Partial credit

- **a.** 0.5 for $z$ and $h$, 0.5 for $\hat y$ and $L$.
- **b.** 0.5 for $\partial L/\partial v$; 0.5 for the written chain for $w_1$ with the right value; 0.5 each for $w_2$ and $b$. A consistent error carried through (for example a missing factor 2, giving $-2, -4, -8, -4$) loses 0.5 once, not on every gradient.
- **c.** 0.5 for the four new weights (0.25 if one or two are wrong), 0.5 for the new forward pass and the conclusion that the loss went down. Follow-through from b.
- **d.** 0.5 for "all four are zero" with $z = -0.5$; 0.5 for the reason (flat ReLU; $h = 0$ for $v$) and what it means for training. Saying only that the three hidden-layer gradients are zero, and missing $v$, gets 0.75 in all.

### Common mistakes

- Forgetting the factor 2 in $\partial L / \partial \hat y = 2(\hat y - y)$.
- Using $x$ instead of $h$ in $\partial L / \partial v$, or forgetting $v$ in the gradients of the hidden-layer weights.
- Using $x_2 = 1$ instead of $x_2 = 2$ for $\partial L / \partial w_2$: each weight's gradient is multiplied by *its own* input.
- Adding the gradient instead of subtracting it: the weights then move away from the target and the loss rises.
- Ignoring the ReLU, either treating it as the identity in d (then the gradients are not zero) or putting $\partial h / \partial z = 0$ in b.

---

## Question 2: Evaluating a signal-peptide predictor (5 p)

| Part | Points |
|---|---|
| a. Precision, recall, $F_1$, accuracy | 2 |
| b. The "always no" baseline | 1 |
| c. Moving the threshold | 1 |
| d. Why the numbers are too optimistic | 1 |

### Model answer

**a.** From the table: $TP = 15$, $FN = 5$, $FP = 10$, $TN = 170$.

- Precision $= TP/(TP+FP) = 15/25 = 0.60$
- Recall $= TP/(TP+FN) = 15/20 = 0.75$
- $F_1 = \dfrac{2 \cdot 0.60 \cdot 0.75}{0.60 + 0.75} = \dfrac{0.90}{1.35} = 2/3 \approx 0.67$
- Accuracy $= (TP+TN)/200 = 185/200 = 0.925$

**b.** "Always no" gets accuracy $180/200 = 0.90$ and recall $0/20 = 0$: it finds no signal peptide at all. The classifier's 0.925 is only 2.5 percentage points above a model that has learned nothing, because 90% of the test proteins are negatives. Accuracy is dominated by the large class and says little here. Report precision and recall (or $F_1$), or MCC, which is 0 for the "always no" baseline and about 0.63 for this classifier.

**c.** Raise the threshold. Fewer proteins are called positive, so there are fewer false positives and fewer wasted experiments: precision usually goes up. More true signal peptides now fall below the threshold, so recall goes down. (Lowering it does the opposite, which is what you would want in a screen where missing a positive is worse.)

**d.** Two reasons, each with its fix:

1. **Homologs on both sides of a random split.** Proteins come in families; a test protein with a close homolog in the training set can be classified by recognising the family rather than the signal peptide. Fix: homology partitioning: cluster the proteins (for example with MMseqs2 at 30% identity) and put whole clusters into training, validation or test.
2. **The test set was used to choose the model.** Picking the best of 20 settings on the test set turns it into a validation set, and the best of 20 noisy scores is partly luck (selection bias). Fix: make the choices on a separate validation set (or by cross-validation within the training data) and use the test set once, at the end.

Also accept: normalisation or feature selection fitted on all data before the split (fit it on the training set only); only 20 positives in the test set, so the numbers are very uncertain (report the uncertainty, use more data or cross-validation); a test set that does not look like the proteins the tool will be used on.

### Partial credit

- **a.** 0.5 for each of the four numbers. Fractions such as $15/25$ are fine. Follow-through for $F_1$ if precision or recall is wrong.
- **b.** 0.5 for both numbers (0.90 and 0), 0.5 for the explanation and a better measure.
- **c.** 0.5 for "raise", 0.5 for the effect on both precision and recall.
- **d.** 0.5 per reason with its fix; 0.25 for a reason without a fix.

### Common mistakes

- Swapping precision and recall. Precision divides by the predicted positives (the column), recall by the true positives (the row).
- Reading the confusion matrix by columns instead of rows: here rows are the true class and columns the prediction, as on the Session 8 page.
- Taking $F_1$ as the plain mean of precision and recall (0.675) instead of the harmonic mean (0.667).
- In b, saying that the baseline's precision is 0. It is undefined ($0/0$), since it never predicts a positive; its recall is 0.
- In d, giving "overfitting" as the reason without saying how the test set lets information in. Overfitting is visible on an honest test set; the problem here is that the test set is not honest.

---

## Question 3: A convolutional network on DNA (5 p)

| Part | Points |
|---|---|
| a. Shapes and parameter counts | 2 |
| b. Receptive field | 1 |
| c. A filter as a PWM | 1 |
| d. Which augmentations keep the label | 1 |

### Model answer

**a.** Without padding and with stride 1, the output length is $L - k + 1$.

| Step | Output shape (channels × length) | Trainable parameters |
|---|---|---|
| 1. `Conv1d(4, 16, 9)` | $16 \times 92$ ($100 - 9 + 1$) | $9 \cdot 4 \cdot 16 + 16 = 592$ |
| 2. `MaxPool1d(2)` | $16 \times 46$ (pooling halves the length, keeps the channels) | 0 |
| 3. `Conv1d(16, 32, 5)` | $32 \times 42$ ($46 - 5 + 1$) | $5 \cdot 16 \cdot 32 + 32 = 2{,}592$ |

(For reference: global max pooling gives 32 numbers, and `Linear(32, 1)` adds 33 parameters, 3,217 in all.)

**b.** **18 bases.** One output position of step 3 reads 5 neighbouring positions of the pooled map. Each pooled position covers 2 neighbouring positions of the step-1 output, so together they cover $5 \cdot 2 = 10$ neighbouring step-1 positions. Neighbouring step-1 positions are one base apart and each reads 9 bases, so 10 of them read $10 + 9 - 1 = 18$ bases. (Layer by layer: 9 after step 1; $9 + 1 = 10$ after pooling, where one step now moves 2 bases; $10 + (5 - 1) \cdot 2 = 18$ after step 3.)

**c.** One filter is a $4 \times 9$ matrix (plus one bias): one weight for each of the four bases at each of the nine positions, just like a PWM over a 9-bp site. A high output at a position means that the 9-bp stretch there matches the pattern the filter has learned, for example the transcription factor's binding motif, in the same way that a high PWM score marks a likely site. The difference from Session 5's PWM is that the weights are learned from labelled windows by gradient descent, not counted from aligned sites.

**d.**

- (i) **Reverse complement: keeps the label.** DNA is double-stranded, and the factor binds the double helix; the same site read from the other strand is the reverse complement.
- (ii) **Shuffling the bases: does not keep the label.** It destroys the motif and keeps only the base composition, so the shuffled window would usually not bind. (Shuffled sequences are often used as *negatives*, never as copies of positives.)
- (iii) **Shifting by two bases: keeps the label**, as long as the binding site stays inside the window; it teaches the network that the exact position in the window does not matter.

### Partial credit

- **a.** 1 for the three shapes (0.5 if two are right); 0.5 for each parameter count. A count without the biases ($576$ and $2{,}560$) gets 0.25 each.
- **b.** 1 for 18 with a reason. 0.5 for 13 ($9 + 5 - 1$) with a correct stacking argument that forgets the pooling, or for a correct method with an arithmetic slip.
- **c.** 0.5 for $4 \times 9$, 0.5 for the meaning of a high output.
- **d.** 1 for all three right with reasons; 0.5 for two right.

### Common mistakes

- Forgetting the input channels in the parameter count ($9 \cdot 16 + 16$), or multiplying by the sequence length. A convolution's weights do not depend on the length of the input.
- Changing the number of channels at the pooling step, or forgetting that pooling halves the length.
- Adding the kernel sizes ($9 + 5 = 14$) for the receptive field, or ignoring the pooling.
- In c, giving the filter's size as $9 \times 16$ (that is the number of filters, not the size of one).
- In d, rejecting the reverse complement because "the sequence is different". The molecule the factor binds is the same.

---

## Question 4: Long-range information for structure prediction: alignments or a language model? (5 p)

| Part | Points |
|---|---|
| a. Coevolution, mutual information and DCA | 1.5 |
| b. Why 15 homologs are too few | 1 |
| c. Comparing the alignment route and the language-model route | 1.5 |
| d. Interpreting a mean pLDDT of 45 | 1 |

### Model answer

**a.** Two residues in contact interact. A mutation in one can break the contact, and it is often tolerated only if the other residue changes too (a compensating mutation). Across a large family of homologs, the two alignment columns therefore change together: they co-evolve. Mutual information scores each pair of columns on its own, so it also picks up **indirect** couplings (if A touches B and B touches C, A and C look coupled although they are not in contact) and correlations caused by **phylogeny** (closely related sequences share many residues). Direct coupling analysis fits **one global statistical model to the whole alignment**, so the coupling of each pair is estimated while all the others are taken into account. This separates direct from indirect couplings. (On CheY, the precision of the top-$L$ contacts rose from 0.49 with mutual information to 0.73 with DCA.)

**b.** DCA estimates statistics for every pair of columns ($20 \times 20$ combinations of residues each), and this needs hundreds to thousands of effective sequences; with 15, the noise swamps the signal. AlphaFold2 also builds its long-range information from the alignment: the MSA representation updates the pair representation, from how two columns vary together across the sequences (the outer product mean, a learned version of coevolution). With a shallow alignment the pair representation gets little evolutionary signal, and the accuracy drops.

**c.**

- **DCA and AlphaFold2:** the information comes from **this protein's own family**. It is collected **at prediction time**, by searching databases and building an alignment, and it is read out as coevolution between columns.
- **ESM-2 (ESMFold):** the information comes from the **hundreds of millions of sequences** the model saw in **pretraining**, where it learned to fill in masked residues from the context on both sides. To do that well it had to learn which positions constrain each other, and this is stored in its weights. At prediction time it reads only the single sequence; its contextual embeddings (and attention maps) then carry information about contacts.
- **An advantage of the alignment route:** it uses direct evidence from the protein's own family, and with a deep alignment it is usually the more accurate. **An advantage of the language-model route:** no search or alignment is needed, so it is fast and works for single sequences, such as orphan or metagenomic proteins with few homologs. (Also accept: it can use what it learned from related families even when the alignment is shallow.)

**d.** Any two of:

- too little evolutionary information (only 15 homologs), so the model cannot place the residues with confidence;
- the protein, or large parts of it, is intrinsically disordered;
- it folds only with a partner, a ligand or in a membrane, which the prediction did not include;
- it has several conformations.

What it does **not** tell you: that the protein is disordered. Low pLDDT means low confidence, not necessarily disorder. More generally, pLDDT is the model's own estimate of its local accuracy, not a measurement: confidence is not correctness. (Also accept: pLDDT is local and says nothing about the relative position of domains; that is what PAE is for.)

### Partial credit

- **a.** 0.5 for why contacts co-evolve (compensating mutations), 0.5 for why mutual information gives false contacts (indirect couplings or phylogeny), 0.5 for what DCA does (a global model of all pairs at once). "DCA is better" without saying why gets 0.
- **b.** 0.5 for DCA (too few sequences for the pair statistics), 0.5 for AlphaFold2 (its pair representation is fed from the alignment).
- **c.** 0.5 for the source and timing in the alignment route, 0.5 for the source and timing in the language-model route, 0.5 for one advantage of each (0.25 each).
- **d.** 0.25 for each explanation (0.5 for two), 0.5 for what pLDDT does not tell you.

### Common mistakes

- Describing coevolution as "conserved residues". Conservation is one column that does not change; coevolution is two columns that change together.
- Saying that AlphaFold2 does not use coevolution because it is "deep learning": its pair representation is built from the alignment.
- Saying that ESM-2 was trained on structures. It was trained only on sequences, by masked language modelling; ESMFold adds a structure module on top.
- Treating pLDDT 45 as proof of disorder, or as proof that the protein does not fold.

---

## Note for the teacher

**Likely hardest: Question 1b-d** (the chain rule through the hidden unit). Students who can do the one-weight example on the Session 7 page often stop at $\partial L/\partial v$, because they do not see how the error reaches a weight behind the hidden unit. If most of the room fails it, the key point to explain at the board is: **the gradient for a weight is the product of the local slopes along the path from the loss back to that weight** ($\partial L/\partial \hat y \to \cdot\, v \to \cdot\, \text{ReLU}'(z) \to \cdot\, x_i$). The first part of that product, $\partial L/\partial h = -8$, is computed once and reused for $w_1$, $w_2$ and $b$, which is all backpropagation is. Then show that ReLU's slope is 0 for $z < 0$, which is why part d gives zeros. If time allows, redo part c with $\eta = 0.05$: the step goes in the right direction ($v = 2.2$, $w_1 = 1.4$, $w_2 = 1.3$, $b = -0.6$), but $\hat y = 2.2 \cdot 3.4 = 7.48$ is now further from 4 than before and the loss rises to about 12.1. This is Session 9's "learning rate too large" in one line.

**Second most likely: Question 3b** (receptive field with pooling). The usual wrong answer is 13. Draw three rows of boxes (input bases, step-1 outputs, pooled outputs) and colour the inputs that one step-3 output depends on; the pooling layer doubles the distance that each later kernel position covers.
