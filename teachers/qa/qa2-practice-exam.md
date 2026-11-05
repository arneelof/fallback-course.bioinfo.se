# KB8029 Bioinformatics: practice exam for Q&A 2 (Sessions 7-12)

Q&A 2, Friday 19 March 2027

**Instructions.** You have 37 minutes. Answer on paper, on your own, with the same aids as in the written exam: pen, paper and up to five single-sided pages of your own notes; no computer or phone. There are four questions of 5 points each, so plan for about 9 minutes per question and move on if you get stuck. The numbers are chosen so that you can do every calculation by hand, without a calculator; show your working, because the working earns most of the points. Nothing is collected or graded: after the break you swap papers with a neighbour and mark each other's answers against the marking guide.

---

## Question 1: A forward pass and one gradient-descent step (5 p)

A tiny network has two inputs $x_1, x_2$, one hidden unit with a ReLU activation and one output unit without an activation (a regression output):

$$
z = w_1 x_1 + w_2 x_2 + b, \qquad h = \text{ReLU}(z) = \max(0, z), \qquad \hat y = v\,h
$$

It is trained with the squared-error loss $L = (\hat y - y)^2$. The current weights are

$$
w_1 = 1, \qquad w_2 = 0.5, \qquad b = -1, \qquad v = 2.
$$

The training example is $x = (x_1, x_2) = (1, 2)$ with target $y = 4$.

a. **(1 p)** Do the forward pass: compute $z$, $h$, $\hat y$ and $L$.

b. **(2 p)** Use the chain rule (backpropagation) to compute $\partial L / \partial v$, $\partial L / \partial w_1$, $\partial L / \partial w_2$ and $\partial L / \partial b$. Write out the chain of local slopes for $\partial L / \partial w_1$.

c. **(1 p)** Take one gradient-descent step with learning rate $\eta = 0.025$ on all four weights ($w_{\text{new}} = w - \eta\,\partial L/\partial w$). Give the new weights, then redo the forward pass for the same example with the new weights. Did the loss go down?

d. **(1 p)** Go back to the *original* weights and a second training example, $x = (0, 1)$ with target $y = 1$. Which of the four gradients are zero for this example, and why? What would it mean for training if this happened for every training example?

---

## Question 2: Evaluating a signal-peptide predictor (5 p)

A group trains a classifier that predicts whether a protein has a signal peptide. On their test set of 200 proteins, 20 of which really have a signal peptide, it gives this confusion matrix:

|                           | Predicted: signal peptide | Predicted: no signal peptide |
|---------------------------|---------------------------|------------------------------|
| **True: signal peptide**  | 15                        | 5                            |
| **True: no signal peptide** | 10                      | 170                          |

a. **(2 p)** With "signal peptide" as the positive class, compute the precision, the recall, the $F_1$ score and the accuracy.

b. **(1 p)** A colleague says that the accuracy shows the classifier is excellent. What accuracy and recall does a "classifier" get that always answers "no signal peptide" on the same test set? What does this tell you about accuracy here, and which measure would you report instead?

c. **(1 p)** The classifier outputs a score, and a protein is called positive when the score is above a threshold. Every protein called positive will be tested in an expensive experiment. Should the threshold be raised or lowered, and what happens to precision and recall when it is?

d. **(1 p)** The group split their proteins into training and test sets at random, and they compared 20 network sizes and learning rates and kept the one with the best test-set score. Give two reasons why the reported numbers are probably too optimistic, and say how to fix each.

---

## Question 3: A convolutional network on DNA (5 p)

A network predicts whether a transcription factor binds a 100-bp DNA window. The window is one-hot encoded, so one example is a tensor of shape $4 \times 100$ (channels × length). The network is:

1. `Conv1d(4, 16, kernel_size=9)`, stride 1, no padding, then ReLU;
2. `MaxPool1d(2)` (window 2, stride 2);
3. `Conv1d(16, 32, kernel_size=5)`, stride 1, no padding, then ReLU;
4. global max pooling over the positions, then `Linear(32, 1)` and a sigmoid.

Every convolution has one bias per filter.

a. **(2 p)** Give the shape (channels × length) of the output of steps 1, 2 and 3, and the number of trainable parameters in each of the two convolutional layers.

b. **(1 p)** How many bases of the input window does one output position of the second convolutional layer (step 3) depend on (its receptive field)? Show how you get the number.

c. **(1 p)** One filter of the first layer can be read as a learned position weight matrix (Session 5). What are its dimensions, and what does a high output of this filter at one position of the sequence mean?

d. **(1 p)** You want to augment the training data. For each of the following transformations, say whether it keeps the label (binds / does not bind) and give a one-line reason: (i) the reverse complement of the window; (ii) shuffling the order of the bases in the window; (iii) shifting the window two bases to the left or right.

---

## Question 4: Long-range information for structure prediction: alignments or a language model? (5 p)

You want the structure of a 120-residue protein found in a metagenome. A database search finds only 15 homologous sequences.

a. **(1.5 p)** Explain why two residues that are in contact in the structure tend to co-evolve. Explain why the mutual information between two alignment columns gives false contacts, and what direct coupling analysis (DCA) does about it.

b. **(1 p)** Why does having only 15 homologs hurt contact prediction by DCA, and why does it also hurt AlphaFold2? Refer to how AlphaFold2 turns the alignment into information about residue pairs.

c. **(1.5 p)** ESMFold builds on the protein language model ESM-2 and needs no alignment. Compare the two routes. Where does the information about which residues are in contact come from in DCA and AlphaFold2, and where does it come from in ESM-2? When is that information collected: at prediction time, or before? Give one advantage of each route.

d. **(1 p)** The predicted model has a mean pLDDT of 45. Give two different explanations for the low value that fit this protein, and say what the low pLDDT does *not* tell you.
