# Session 8: Machine Learning Foundations & Practical PyTorch

## Which of these is a *regression* problem rather than a classification problem?

- [ ] Predicting whether a missense variant is pathogenic or benign
- [x] Predicting the change in melting temperature (in °C) that a point
      mutation causes
- [ ] Predicting helix / strand / coil for every residue of a protein
- [ ] Predicting which of five compartments a protein localizes to

## Logistic regression computes $z = w_1x_1 + w_2x_2 + b$ and outputs $\sigma(z)$. Despite its name, what kind of model is it, and where is its decision boundary?

- [x] A classifier: $\sigma(z)$ estimates a class probability, and the
      boundary ($\sigma(z) = 0.5$) is the straight line $z = 0$ — the same line Session 7's
      perceptron draws
- [ ] A regression model: $\sigma(z)$ predicts a continuous target, and it
      has no decision boundary
- [ ] A classifier with a curved boundary, because the sigmoid is nonlinear
- [ ] A regression model whose boundary is where $\sigma(z) = 0$

## On the secreted-vs-nuclear example, logistic regression gives N-terminal hydrophobicity a weight of 4.26 and lysine+arginine content a weight of −0.20. What is the most sensible biological reading?

- [x] Secreted proteins start with a hydrophobic signal peptide, and the
      model found that single feature carries almost all of the signal; K+R
      content barely separates the two classes
- [ ] Nuclear proteins are more hydrophobic than secreted ones
- [ ] K+R content is the more important feature, since its weight is negative
- [ ] The weights are arbitrary and cannot be interpreted at all

## On the 3×3 problem, the number of training epochs was chosen by looking at validation accuracy, and the chosen model was then measured once on the test set (0.895). Why not simply report the best validation accuracy instead?

- [ ] The validation set is always smaller than the test set
- [x] The validation set was used to make a choice, so its best score is
      slightly optimistic; only a set that played no part in any decision
      gives an honest estimate
- [ ] Validation accuracy can only be computed during training, not after
- [ ] There is no difference: validation and test accuracy are always equal

## In the 3×3 test-set confusion matrix, 9 true "cross" patterns were predicted as "vertical". Which per-class metrics do these 9 errors lower?

- [x] Recall of "cross" (0.75) and precision of "vertical" (0.76)
- [ ] Precision of "cross" and recall of "vertical"
- [ ] Only overall accuracy, not any per-class metric
- [ ] Recall of "vertical" and recall of "cross"

## Before balancing, the localization data has 424 / 497 / 140 / 488 / 338 proteins per class. A "classifier" that always answers *nucleus* reaches accuracy 0.263. What is its MCC, and why?

- [x] 0 — MCC measures agreement beyond chance, and a constant prediction
      has none, however high its accuracy
- [ ] 0.263 — MCC equals accuracy for multi-class problems
- [ ] 0.20 — the chance level for five classes
- [ ] 1 — it never misclassifies a nuclear protein

## In ten random splits of the 700 localization proteins, 31.3% of validation proteins had a ≥30%-identity homolog in the training set. The baseline classified those correctly 67.5% of the time, versus 50.9% for the rest. What does this show?

- [x] A random split lets the model exploit family-specific similarity, so
      it overestimates performance on genuinely new families; clusters of
      homologs should be kept on one side of the split
- [ ] Homologs confuse the model, so they should be removed from the test
      set only
- [ ] Proteins with homologs are intrinsically easier to localize, so
      nothing is wrong with the split
- [ ] The MMseqs2 clustering must be wrong, since training and validation
      proteins are never related

## Averaged over ten splits of each kind, the baseline scored 0.553 on random splits and 0.536 on homology-aware splits — a small drop. Why is the overall drop so much smaller than the per-protein effect (0.675 vs 0.509)?

- [ ] Homology partitioning removes most of the training data
- [x] Most proteins in this dataset (476 of 700) have no ≥30% homolog in the
      set at all, so only a minority ever benefited from leakage; in more
      redundant data (a whole proteome, the PDB) the gap can be much larger
- [ ] The per-protein effect was measured incorrectly
- [ ] Homology-aware splits always give the same accuracy as random splits

## Ten random 70/15/15 splits gave validation accuracies from 0.505 to 0.610 for the same model and data. What does 5-fold cross-validation give you that a single split does not?

- [x] Every protein is used for validation exactly once, so the estimate
      no longer depends on one arbitrary draw of the split
- [ ] A guaranteed higher accuracy
- [ ] A test set that can be reused for tuning
- [ ] The ability to skip having a separate test set for the final number

## The 3×3 perceptrons give one misclassified noisy "horizontal" pattern the scores $(-2.19, -0.80, -2.35, -2.61, 0.16)$ for (horizontal, vertical, diagonal, anti-diagonal, cross). What does applying softmax change?

- [ ] It changes the prediction from "cross" to "horizontal"
- [x] Nothing about which class wins (still "cross", 0.62); it rescales the
      scores into positive numbers that sum to 1, which should not be read as
      reliable probabilities for scores not trained with cross-entropy
- [ ] It makes every probability equal to 0.2
- [ ] It turns the scores into a regression output

<!-- coding-exercise -->
## In the notebook's homology-leakage check below, what does `has.mean()` measure for one split?

```python
tr, tmp = train_test_split(idx_all, test_size=0.30, stratify=y, random_state=seed)
va, te = train_test_split(tmp, test_size=0.5, stratify=y[tmp], random_state=seed)
pred = LogisticRegression(max_iter=2000, random_state=0).fit(X[tr], y[tr]).predict(X[va])
train_groups = set(groups[tr])
has = np.array([groups[i] in train_groups for i in va])
leak_frac.append(has.mean())
```

- [x] The fraction of validation proteins whose MMseqs2 cluster also has a
      member in the training set
- [ ] The fraction of validation proteins the classifier gets right
- [ ] The fraction of training proteins that are singletons
- [ ] The number of clusters in the validation set

## The 3×3 classifier is rewritten as `PatternClassifier`, a single `nn.Linear(9, 5)` inside an `nn.Module`, and the trained perceptron weights are copied into it. What happens?

- [x] It makes exactly the same predictions as the NumPy perceptrons: it has
      50 parameters (5 × 9 weights + 5 biases) and computes the same five
      weighted sums
- [ ] It predicts differently, because `nn.Linear` applies softmax internally
- [ ] It cannot be used until it has been trained with backpropagation
- [ ] It has 45 parameters, because `nn.Linear` has no bias by default

## Predictions correlate with the truth at r = 0.95, but each prediction is about twice the true value plus 5. Which is true?

- [x] The correlation is high, but the RMSE is large and R² can be negative: r measures whether predictions track the trend, not whether they are numerically right
- [ ] r = 0.95 means the predictions are accurate to within 5%
- [ ] The RMSE must be small because r is close to 1
- [ ] R² always equals r² for any predictor

## A classifier's softmax output is 0.9 for "secreted". What can you conclude without further checks?

- [x] Only that "secreted" has the highest score; whether 0.9 means a 90% chance depends on training and calibration
- [ ] The protein is secreted with 90% probability
- [ ] The model is 90% accurate
- [ ] Softmax outputs are random

## You standardize all features with the mean and standard deviation of the whole dataset, then split it. What kind of leakage is this?

- [x] Leakage through preprocessing: test-set statistics have entered the model
- [ ] Leakage through the samples, like homologs on both sides of the split
- [ ] Evaluation leakage: inspecting the test set while choosing models
- [ ] No leakage, because the labels were not used

## Why is a PSSM built by counting residues in an alignment not a clean example of supervised learning?

- [x] It is estimated from family members by counting, not fitted to labelled positive and negative examples to predict a label
- [ ] Because it uses no numbers
- [ ] Because it has no weights
- [ ] Because alignments are unsupervised clustering

## You train for 50 epochs and record validation accuracy (100 examples) after each. It fluctuates between 0.84 and 0.94 around 0.89, peaking once at 0.94. Why is reporting 0.94 as the model's expected accuracy optimistic?

- [x] With 100 examples each value is uncertain by about ±0.03, so picking the maximum of 50 noisy values partly selects luck
- [ ] Because validation accuracy is always lower than test accuracy
- [ ] Because the model was trained on the validation set
- [ ] It is not optimistic: the highest value is the true accuracy

## A 1-nearest-neighbour model, trained and evaluated on the same 55 proteins, predicts their helix fractions perfectly (R² = 1.00). On 14 held-out proteins its R² is 0.03. What does this show?

- [x] Evaluating on the training data measures memorization, not generalization: every protein's nearest neighbour is itself
- [ ] The model is perfect and the held-out proteins are mislabelled
- [ ] R² cannot be computed on held-out data
- [ ] 1-nearest-neighbour always beats a linear model

## What does it mean that a neural network is **overfitting**?

- [x] It fits the training data very well but performs clearly worse on data it has not seen, because it has learned details specific to the training examples
- [ ] It performs badly on both the training data and new data, because it is too simple
- [ ] It has been trained for too few epochs
- [ ] Its validation accuracy is higher than its training accuracy

## After standardizing with the training-set statistics, the training images have mean 0 and standard deviation 1 exactly, but the validation images only approximately. Why?

- [x] The statistics were computed from the training images, and a different sample of images has a slightly different mean and spread
- [ ] A bug in the code
- [ ] The validation images were not standardized
- [ ] Standardization only works on the training set

## A PyTorch classifier's last layer outputs raw scores (logits), with no softmax layer. Why?

- [x] `nn.CrossEntropyLoss` combines log-softmax with the negative log-likelihood in one numerically stable operation, so the model should output raw logits
- [ ] Softmax cannot be computed for more than two classes
- [ ] Logits are already probabilities
- [ ] Softmax would change which class gets predicted
