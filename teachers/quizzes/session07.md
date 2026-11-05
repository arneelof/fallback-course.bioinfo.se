# Session 7: Linear Models, Gradient Descent, the XOR Problem & Secondary Structure Prediction

## In a perceptron's weighted sum z = w1x1 + ... + wnxn + b, what does the bias term b let the model do?

- [x] Let the decision threshold sit somewhere other than zero, instead of being forced through the origin
- [ ] Scale the learning rate up or down during training
- [ ] Act as the activation function itself
- [ ] Set a hard upper limit on how large z can get

## A profile score (Session 5) and a perceptron share the same mathematical core. What is it, and how do they differ?

- [x] A weighted sum (dot product); a profile reports it as a score, a perceptron passes it through an activation (a threshold) to classify
- [ ] A matrix inversion; they differ only in the matrix size
- [ ] A simple average of the inputs; they are identical
- [ ] A probability density function; only the perceptron uses it

## A perceptron has one input, no bias (z = wx), an initial weight w0 = 0, a training example (x, y) = (3, 9), a squared-error loss L(w) = (wx - y)^2, and a learning rate η = 0.02. Using dL/dw = 2(wx - y)x, what is w1 after one gradient descent step?

At w=0: dL/dw = 2(0 - 9)(3) = -54, so w1 = 0 - 0.02×(-54).

- [x] 1.08
- [ ] 0.54
- [ ] -1.08
- [ ] 9.0

## This session's lab implements gradient descent directly with raw tensors and autograd, deliberately without using `nn.Module`. Why?

- [x] To see every step of the training mechanics directly, rather than use a convenient shortcut around them
- [ ] Because `nn.Module` cannot represent a single perceptron
- [ ] Because raw tensors train measurably faster than `nn.Module`
- [ ] Because `nn.Module` does not support gradient descent

## Geometrically, why can no single perceptron represent the XOR function?

- [x] XOR's two "1" outputs sit on opposite corners of the input square, and no single straight line can separate both of them from both "0" outputs
- [ ] XOR requires three or more inputs to even be defined
- [ ] A perceptron's sign activation function can only ever output positive numbers
- [ ] XOR's inputs and outputs are not integers

## The algebraic proof that no perceptron can solve XOR derives a contradiction between which two facts?

- [x] w1 + w2 + b must be both greater than 0 (from the two "1" rows) and less than or equal to 0 (from a "0" row) — impossible at once
- [ ] The bias b must be simultaneously positive and negative
- [ ] The weights w1 and w2 must both equal exactly zero
- [ ] The sign function must output a value strictly between 0 and 1

## Bulyk, Johnson & Church's protein-binding microarray study found that a zinc-finger transcription factor's binding affinity depended on its binding site's nucleotides in a specific way. What did they find that directly violates the assumption behind a simple profile/perceptron score?

- [x] Binding-site positions do not contribute independently — the effect of one position's identity depends on what's at another position
- [ ] Transcription factors never bind DNA in a sequence-specific way
- [ ] All positions in a binding site contribute exactly equally to binding
- [ ] Binding affinity is unrelated to the nucleotide sequence

## A network has a hidden layer but no activation function: h = W1 x + b1, z = W2 h + b2. Can it solve XOR?

- [x] No: W2(W1 x + b1) + b2 = (W2 W1) x + (W2 b1 + b2) is again a single linear function
- [ ] Yes: any hidden layer is enough
- [ ] Yes, with enough hidden units
- [ ] Only with a smaller learning rate

## In gradient descent on a simple quadratic loss, the steps shrink on their own as the weight approaches the minimum. What can go wrong if the learning rate is too large?

- [x] The update overshoots the minimum and can oscillate or diverge
- [ ] Nothing: any learning rate converges
- [ ] The model stops after one step
- [ ] The loss becomes negative

## Minsky and Papert's 1969 book *Perceptrons* proved a real limitation of single-layer perceptrons. What effect is this proof widely credited with contributing to?

- [x] A sharp drop in funding and interest in neural-network research — the first "AI winter"
- [ ] The invention of the transistor
- [ ] The immediate invention of backpropagation that same year
- [ ] A formal ban on perceptron research by funding agencies

## What later development made it practical to train multi-layer networks, resolving the XOR limitation?

- [x] Backpropagation — an efficient way to apply the chain rule through a network with hidden layers
- [ ] A new activation function that only single perceptrons could use
- [ ] Increasing the bias term to a very large fixed value
- [ ] Removing the sign function from the perceptron entirely

## What changes between a single perceptron and a network with one hidden layer that lets the network represent XOR?

- [x] Several weighted sums, each followed by a nonlinear activation, each draw their own boundary, and a final weighted sum combines them
- [ ] The network uses a smaller learning rate
- [ ] The network adds a bias term, which the perceptron lacks
- [ ] The network has more inputs than the perceptron

## Methods predicting secondary structure from single sequences, including an early neural network (Qian & Sejnowski 1988, 64.3%), stayed around 60-65% accuracy. What did Rost & Sander's PHD method change to reach about 71%?

- [x] Its input: a profile from a multiple alignment of homologs instead of a single sequence, which added six to eight percentage points
- [ ] A much larger single-sequence database, with no change to the model
- [ ] Removing the bias term from the perceptron entirely
- [ ] Switching from BLOSUM62 to PAM250 as the scoring matrix

## A model predicts HBB's helix fraction (0.80) from its amino-acid composition. What can it never tell you?

- [x] Which residues are in helices, and where each helix starts and stops
- [ ] Whether HBB is mostly helical
- [ ] How many alanines HBB contains
- [ ] Anything at all about HBB

## This is the training loop from the notebook's linear model:

<!-- coding-exercise -->

```python
for epoch in range(epochs):
    z = X @ w + b
    pred = torch.sigmoid(z)
    loss = torch.nn.functional.binary_cross_entropy(pred, y)
    loss.backward()
    with torch.no_grad():
        w -= lr * w.grad
        b -= lr * b.grad
        w.grad.zero_()
        b.grad.zero_()
```

What would go wrong if the two `.zero_()` calls at the end of the loop were removed?

- [x] Gradients would accumulate (add up) across iterations instead of being recomputed fresh each step, corrupting the updates
- [ ] The model would train identically, just somewhat more slowly
- [ ] PyTorch would raise an error on the very next `.backward()` call
- [ ] The weights would never update at all

## The ten residues QGTAVVVSAA form a helix in one protein and a strand in another. What does this show?

- [x] Local sequence alone cannot determine secondary structure; information from outside the window, such as the protein family, is needed
- [ ] The secondary structures in the PDB are unreliable
- [ ] Helices and strands are the same structure
- [ ] Ten residues are too few to form any secondary structure

## In the hand-built XOR network (h₁ = OR, h₂ = NAND, y = AND of the two), what are h₁, h₂ and y for the input (1, 1)?

- [x] h₁ = 1, h₂ = 0, y = 0
- [ ] h₁ = 1, h₂ = 1, y = 1
- [ ] h₁ = 0, h₂ = 1, y = 0
- [ ] h₁ = 0, h₂ = 0, y = 0

## PHD combined networks in three levels. What does the second level (the structure-to-structure network) add?

- [x] It reads the first level's predictions for a window of neighbouring residues and learns that helices and strands come in segments of plausible length
- [ ] It aligns the sequence to its homologs
- [ ] It predicts the 3D coordinates of each residue
- [ ] It removes the hidden layer from the first network

## Homologous proteins often keep the same structure even when their sequences have diverged. Why does this help secondary-structure prediction?

- [x] A profile of the family shows which substitutions each position tolerates, which reflects its structure better than the single sequence does
- [ ] Homologs always have identical sequences in helices
- [ ] It means a single sequence contains all the information needed
- [ ] It lets the predictor skip the training step

## Why are amino acids one-hot encoded (20 numbers, a single 1) rather than numbered A = 1, C = 2, ..., Y = 20?

- [x] Numbering implies a false order and distance between amino acids; one-hot makes every amino acid equally different and lets the network learn a weight for each
- [ ] One-hot encoding uses fewer numbers
- [ ] Neural networks can only read zeros and ones
- [ ] Numbering would change the protein's sequence

## An embedding layer gives each amino acid a trainable vector. How is it related to one-hot encoding?

- [x] It is a linear layer applied to the one-hot vector: multiplying a one-hot vector by a weight matrix picks out one row
- [ ] It replaces the sequence with its amino-acid composition
- [ ] It is the same as a profile from a multiple alignment
- [ ] It sorts the amino acids by hydrophobicity
