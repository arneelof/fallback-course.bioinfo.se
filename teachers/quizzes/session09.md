# Session 9: Backpropagation, Training, and Regularization

## What is backpropagation, precisely?

- [x] The chain rule from calculus, applied systematically layer by layer from the output back to the input
- [ ] A completely different algorithm from the chain rule, specific to deep learning
- [ ] A method for choosing which activation function to use
- [ ] A way to initialize a network's weights before training starts

## Backpropagation computes each layer's error signal once and reuses it for every weight in that layer, rather than re-deriving each weight's gradient independently from scratch. Why does this reuse matter?

- [x] It is the entire reason backpropagation is computationally efficient rather than intractable for a network with many weights
- [ ] It only matters for networks with fewer than 10 weights
- [ ] It has no effect on efficiency, only on numerical accuracy
- [ ] It is required by PyTorch's syntax but not by the underlying mathematics

## Training Session 8's subcellular-localization network with no regularization reaches 100% training accuracy but only 43.8% validation accuracy by the end (after peaking at 48.6% in epoch 5). What does this gap indicate?

- [x] Overfitting — the model has memorized idiosyncrasies of the training examples rather than learning the general signal
- [ ] The model has learned the task perfectly and the validation set must be mislabeled
- [ ] A bug in the forward pass, since training accuracy should never exceed validation accuracy
- [ ] The learning rate is set far too low

## For a softmax classifier, cross-entropy loss for a single example reduces to $-\log p(\text{true class})$. Predicting the true class with probability 0.9 costs about 0.105; predicting it with probability 0.01 costs about 4.6. What does this asymmetry mean in practice?

- [x] A confidently wrong prediction is punished far more heavily than a hedged, uncertain one
- [ ] The loss is symmetric: being wrong always costs the same regardless of confidence
- [ ] A probability of exactly 0.5 always gives the lowest possible loss
- [ ] Cross-entropy loss cannot be computed for probabilities below 0.1

## In the vanishing-gradient demonstration, a 6-layer sigmoid network (on the GB1 inputs) has an input-layer gradient roughly 10,000,000x smaller than its output layer's, while a same-depth ReLU network's shrinks only about 550x. What causes this difference?

- [x] Sigmoid saturates for large |x|, giving near-zero local derivatives that the chain rule multiplies together across layers; ReLU's derivative doesn't shrink on the positive side
- [ ] The sigmoid network in the demonstration has more layers than the ReLU network
- [ ] Sigmoid networks always have more total parameters than ReLU networks of the same shape
- [ ] PyTorch's `autograd` only computes gradients correctly for ReLU, not for sigmoid

## Which of these is NOT a fix for vanishing gradients named on the book page?

- [x] Increasing the learning rate until gradients are large enough to matter
- [ ] Choosing an activation function (like ReLU) that doesn't saturate on one side
- [ ] Weight initialization schemes matched to each layer's size
- [ ] Batch normalization of the activations between layers

## Trained on Session 8's homology-aware split, Session 8's network reaches 100% training accuracy with or without dropout and L2. Its best validation accuracy is 0.486 without them and 0.476 with them; early stopping keeps whichever peak it reached. What does this say about dropout/L2 here?

- [x] With roughly 190,000 parameters and only 486 training examples, the model can memorize the training set even with dropout and L2 active — regularization doesn't fix a fundamental data-to-parameter mismatch
- [ ] Dropout and L2 always make a network worse, so they should never be used
- [ ] Early stopping only works when combined with a larger learning rate
- [ ] The validation set must be mislabeled, since regularization always improves validation accuracy

## On the same homology-aware test set, Session 9's trained network (one hidden layer, ~190,000 weights) scores accuracy 0.514 and MCC 0.394, while plain logistic regression (no hidden layer) scores 0.569 and 0.461. What is the best explanation?

- [x] With only 486 training proteins there is too little data to learn the extra interactions a hidden layer could represent, so the simpler model generalizes better
- [ ] Logistic regression is always better than neural networks
- [ ] The hidden layer was never trained, because backpropagation does not reach it
- [ ] The test set contains homologs of the logistic-regression training set but not of the network's

## In the breast-cancer example, the mean and standard deviation used to standardize each feature are computed on the training biopsies only, then applied to validation and test. Why not compute them on all 569 biopsies?

- [x] Statistics computed on all data would let information from the validation and test sets leak into training (Session 8)
- [ ] The training set is always larger, so its statistics are more accurate
- [ ] PyTorch cannot standardize a validation set
- [ ] Standardizing the test set would change its labels

## On the breast-cancer data, 5-fold cross-validation gives logistic regression (31 weights) and a 16-unit network (513 weights) the same accuracy, 0.979. What is the most reasonable conclusion?

- [x] The classes are separated almost linearly by the nucleus measurements, so the hidden layer has little to add
- [ ] The network was not trained, because the accuracies are identical
- [ ] Cross-validation always makes two models look equal
- [ ] Logistic regression and a one-hidden-layer network are the same model

## Examples per weight: breast cancer 0.78 (tie), GB1 fitness 2.1 (network wins), localization 0.003 (linear wins). Which statement best summarizes when a hidden layer pays off?

- [x] When the relationship is not additive and there are enough data to learn it (few examples per weight is a warning sign, not a strict rule); with too little data a non-additive problem can still favour the simpler model
- [ ] Whenever the dataset has more than 1,000 examples
- [ ] Only for regression problems
- [ ] Only when the inputs are standardized

## L1 regularization (Lasso) penalizes the sum of the absolute values of the weights, while L2 (weight decay/Ridge) penalizes the sum of their squares. Which one tends to push some weights all the way to exactly zero, rather than just shrinking every weight a little?

- [x] L1
- [ ] L2
- [ ] Both push weights to exactly zero equally often
- [ ] Neither — both only ever shrink weights toward zero without reaching it

## This is from the notebook's early-stopping training loop:

<!-- coding-exercise -->

```python
best_val_acc, best_epoch, best_state = 0.0, 0, None
history_reg = []
for epoch in range(100):
    model_reg.train()
    optimizer.zero_grad()
    logits = model_reg(X_train_t)
    loss = loss_fn(logits, y_train_t)
    loss.backward()
    optimizer.step()

    model_reg.eval()
    with torch.no_grad():
        train_acc = (model_reg(X_train_t).argmax(1).numpy() == y_train).mean()
        val_acc = (model_reg(X_val_t).argmax(1).numpy() == y_val).mean()
    history_reg.append((epoch, train_acc, val_acc))
    if val_acc > best_val_acc:
        best_val_acc, best_epoch = val_acc, epoch
        best_state = {k: v.clone() for k, v in model_reg.state_dict().items()}

print(f"best validation accuracy: {best_val_acc:.3f}, reached at epoch {best_epoch}")
model_reg.load_state_dict(best_state)
```

After this loop finishes, what does `model_reg.load_state_dict(best_state)` actually do to the model?

- [x] Rolls the model's weights back to whichever epoch had the best validation accuracy during training, discarding whatever it learned afterward — this is early stopping
- [ ] Resets the model to its randomly-initialized starting weights before any training happened
- [ ] Has no effect, since `model_reg` was already at its final (epoch-99) weights
- [ ] Retrains the model for 100 more epochs starting from `best_state`

## Rost & Sander's PHD method (already introduced on Session 7) is described as combining several pieces introduced across Sessions 5-9. Which combination is it?

- [x] Profile input from an alignment (Session 5) feeding a hidden layer (Session 7) with three outputs for helix/strand/loop (Session 8), trained by backpropagation (Session 9) and evaluated on test sets purged of similar sequences (Session 8)
- [ ] Raw one-hot sequence encoding, with no profile input at all
- [ ] A single perceptron with no hidden layer, trained on Session 5's profile scores directly
- [ ] An approach unrelated to the profile/PSSM methods introduced on Session 5

## In the training loop, what does `loss.backward()` do?

- [x] Computes the gradient of the loss with respect to every weight, by backpropagation
- [ ] Updates every weight
- [ ] Clears the old gradients
- [ ] Computes the predictions

## A 64/64 network starts with every weight equal to 0.1. After training, all 64 first-layer units are identical. Why?

- [x] Identical units receive identical gradients and stay identical; random initialization breaks the symmetry
- [ ] The learning rate was too large
- [ ] ReLU units cannot learn from equal weights
- [ ] The network has too few parameters

## A six-layer sigmoid network trained with plain SGD stays at the error of predicting the mean, while the same network with ReLU learns. Why?

- [x] Backpropagation multiplies one sigmoid derivative (at most 0.25) per layer, so the first layers receive almost no gradient
- [ ] Sigmoid outputs cannot be negative, so the network cannot predict prices
- [ ] SGD cannot train networks with more than one layer
- [ ] ReLU networks have more weights

## A linear model on the one-hot encoding of four GB1 positions explains 50% of the variance in fitness, and a 64/64 network 79%. What does the linear model fail to capture?

- [x] Epistasis: the effect of a mutation at one position depends on the residues at the other positions, and a sum of per-position weights cannot represent that
- [ ] The amino-acid composition of the variants
- [ ] Measurement noise
- [ ] Nothing: R² values cannot be compared between models

## With 500 GB1 training variants the linear model and the network are equally good; with 20,000 the network is far better. Why?

- [x] The interactions exist in both cases, but learning them needs many examples; the additive model cannot use more data to represent interactions
- [ ] The network only works for large datasets
- [ ] Small datasets have no epistasis
- [ ] The linear model overfits large datasets

## In a long, narrow valley of the loss surface, plain SGD zigzags from wall to wall. How does momentum help?

- [x] It steps along a running average of recent gradients: the components across the valley alternate in sign and cancel, while those along the valley add up
- [ ] It makes every step exactly the same length
- [ ] It computes the exact gradient on the whole training set instead of a mini-batch
- [ ] It lowers the learning rate automatically every epoch

## Which of these is a remedy for vanishing gradients, rather than for slow or noisy optimization?

- [x] Residual connections, which give the gradient a direct path through many layers
- [ ] Momentum
- [ ] Choosing a smaller learning rate
- [ ] Using larger mini-batches

## L2 regularization adds $\lambda \sum_j w_j^2$ to the loss, L1 adds $\lambda \sum_j |w_j|$. Why does L1 set many weights to exactly zero while L2 only shrinks them?

- [x] L2's pull on a weight is proportional to its size and fades as the weight gets small; L1 pulls with the same force however small the weight is, so weights that help little are pushed all the way to zero
- [ ] L1 uses a larger learning rate than L2
- [ ] L2 sets weights to zero only for the output layer
- [ ] L1 deletes the features with the smallest variance before training

## With the penalty chosen on the validation set, L1 logistic regression on the 30 breast-cancer biopsy features kept only a handful of non-zero weights, with almost the same test accuracy as L2 with all 30. When is that most useful?

- [x] When there are many features and few examples, or when we want a model whose few remaining features a biologist or pathologist can read
- [ ] Only when every feature is equally important
- [ ] When the network has many hidden layers
- [ ] Never: a model with fewer weights is always less accurate

## Why is L2 regularization also called "weight decay"?

- [x] Its gradient, $2\lambda w$, makes every update shrink each weight by the same small fraction, so weights decay towards zero unless the data keep them large
- [ ] Because the weights are deleted one by one during training
- [ ] Because the learning rate decays over time
- [ ] Because it only applies to the weights of the last layer

## Dropout switches off a random half of the hidden units in every training step. Why does this reduce overfitting?

- [x] No unit can rely on particular partners being present, so information is spread over many units, and the full network at test time acts like an average of many thinned networks
- [ ] It permanently removes half of the weights, making the network smaller
- [ ] It makes training faster, so there is less time to overfit
- [ ] It removes noisy examples from the training set

## Why does every PyTorch training loop in this course call `model.train()` before training and `model.eval()` before evaluating?

- [x] Dropout (and batch normalization) behave differently in the two modes: dropout is only active in training mode, so evaluation must switch it off
- [ ] `model.eval()` computes the gradients and `model.train()` applies them
- [ ] `model.eval()` deletes the training data from memory
- [ ] They only change the printed output, not the predictions

## The training loss keeps falling, but the validation loss has levelled off and started to rise. Which statement is correct?

- [x] Optimization is still working, but further training no longer helps generalization; early stopping keeps the weights from the best validation epoch
- [ ] The optimizer has failed and must be replaced
- [ ] The validation set is too small to be used
- [ ] The model is underfitting and needs more epochs

## Early stopping chooses the epoch on the validation set. What does that mean for the validation score of the chosen model?

- [x] It is slightly optimistic, because it was used to make a choice; only the test set, used once, gives an honest estimate
- [ ] It is exactly as reliable as a test score
- [ ] It is always lower than the test score
- [ ] It cannot be computed after early stopping
