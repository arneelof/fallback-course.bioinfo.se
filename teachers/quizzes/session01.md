# Session 1: Math Prerequisites

## What is the length (norm) of the vector (5, 12)?

- [ ] 17
- [x] 13
- [ ] 60
- [ ] 8.5

## What is the Frobenius norm of the matrix [[3, 0], [0, 4]]?

Treat every entry as part of one long vector: √(3² + 0² + 0² + 4²).

- [ ] 7
- [x] 5
- [ ] 12
- [ ] 25

## What is the dot product of (3, 2) and (-1, 4)?

- [ ] -11
- [x] 5
- [ ] 11
- [ ] -5

## Two nonzero vectors have a dot product of exactly zero. What must be true about the angle between them?

- [ ] It must be 0°
- [x] It must be 90°
- [ ] It must be 180°
- [ ] Nothing — a zero dot product doesn't constrain the angle

## Two nonzero vectors point in broadly opposite directions (the angle between them exceeds 90°). Without computing anything, what can you say about their dot product?

- [ ] It must be positive
- [x] It must be negative
- [ ] It must be exactly zero
- [ ] Its sign can't be determined from the angle alone

## What is the unit vector in the same direction as (6, 8)?

- [x] (0.6, 0.8)
- [ ] (6, 8)
- [ ] (0.75, 1)
- [ ] (3, 4)

## A matrix X holds 1,000 proteins × 20 features, and a classifier has one weight per feature. What is the shape of X w?

- [x] (1000,): one score per protein
- [ ] (20,): one score per feature
- [ ] (1000, 20)
- [ ] It cannot be computed

## X has shape (500, 20). Which product can NOT be computed?

- [x] X u, for a vector u with 500 entries
- [ ] Xᵀ u, for a vector u with 500 entries
- [ ] X w, for a vector w with 20 entries
- [ ] Xᵀ X

## X has shape (1000, 20). What is the shape of Xᵀ X, and what does it compare?

- [x] (20, 20): every feature with every other feature, summed over the proteins
- [ ] (1000, 1000): every protein with every feature
- [ ] (1000, 20): the same as X
- [ ] (20, 1000): the transpose again

## For A = [[2,1],[1,2]], which of the following is an eigenvector of A?

A(1,1) = (2·1+1·1, 1·1+2·1) = (3,3) — the same direction as (1,1), just scaled.

- [x] (1, 1)
- [ ] (1, 0)
- [ ] (0, 1)
- [ ] (2, 1)

## If Av = λv for some nonzero vector v, what does λ represent?

- [x] The factor v is scaled by under the transformation A, with its direction left unchanged
- [ ] The determinant of A
- [ ] The number of dimensions of v
- [ ] The angle between v and Av

## For f(x0, x1) = x0^2 * x1 + 3*x1, what is the gradient at the point (2, 1)?

The partial derivatives are df/dx0 = 2*x0*x1 and df/dx1 = x0^2 + 3.

- [x] (4, 7)
- [ ] (2, 7)
- [ ] (4, 3)
- [ ] (7, 4)

## In Session 1's gradient descent worked example, x_n moves toward the minimum in ever-smaller steps, even though the learning rate η never changes. Why?

- [x] Because the derivative itself shrinks as x_n approaches the minimum, so η times a smaller number is a smaller step
- [ ] Because η automatically decays after each step behind the scenes
- [ ] Because the function f(x) changes shape near the minimum
- [ ] Because gradient descent always takes geometrically decreasing steps, regardless of the function

## Gradient descent updates a parameter by moving in the direction *opposite* the gradient. Why opposite, rather than the same direction?

- [x] Because the gradient points toward steepest increase, so its opposite points toward steepest decrease
- [ ] Because the gradient is always a negative number
- [ ] Because moving in the gradient's own direction is mathematically undefined
- [ ] Because the learning rate η is always negative

## For a composite function y = f(g(x)), the chain rule gives dy/dx as:

- [x] (df/dg) · (dg/dx)
- [ ] df/dx + dg/dx
- [ ] df/dg + dg/dx
- [ ] df/dx · dg/dx

## A 10-base fragment has 7 G or C. Under a model where each base is G/C with probability p, which p gives the highest likelihood p^7 (1-p)^3?

- [x] 0.7, the observed fraction
- [ ] 0.5, since all bases are equally likely
- [ ] 1.0, since most bases are G/C
- [ ] 0.3

## A sequence scores -2 bits in a log-odds comparison of a family model against a background model. What does that mean?

- [x] It is 4 times more likely under the background model than under the family model
- [ ] It is 2 times more likely under the family model
- [ ] It certainly does not belong to the family
- [ ] The score is invalid, since log-odds cannot be negative

## Among 200 proteins, 60 are membrane proteins and 30 of those have a signal peptide; 20 of the other 140 have one too. What is P(membrane | signal peptide)?

- [x] 30/50 = 0.6
- [ ] 30/60 = 0.5
- [ ] 60/200 = 0.3
- [ ] 50/200 = 0.25

## mRNA levels (1, 2, 3, 4, 100) and protein levels (2, 4, 6, 8, 10) rise together, but one mRNA value is extreme. Which is true?

- [x] Spearman's rho is 1, and Pearson's r is lower (0.72), because the extreme value is off the straight line
- [ ] Both are exactly 1
- [ ] Pearson's r is 1, and Spearman's rho is lower
- [ ] Both are close to 0

## What does Spearman's rank correlation measure that Pearson's r does not?

- [x] Whether y tends to increase with x (a monotonic relationship), even if not along a straight line
- [ ] Whether x causes y
- [ ] A U-shaped relationship
- [ ] The slope of the regression line

## What does a p-value actually represent?

- [x] P(data at least this extreme | the null hypothesis is true)
- [ ] P(the null hypothesis is true | the data)
- [ ] The probability that the null hypothesis is false
- [ ] The probability the experiment was conducted correctly

## A researcher runs a two-sample t-test comparing gene expression in 4 control replicates vs. 4 treatment replicates. The means are far apart and both groups have very little variability among their replicates. What does this predict about the resulting t-statistic and p-value?

- [x] A large |t| and a very small p-value
- [ ] A small |t| and a large p-value
- [ ] |t| and p-value are unrelated to how far apart the means are
- [ ] The t-test cannot be run with only 4 replicates per group

## You test 1000 genes, and in truth NONE of them are differentially expressed. Using p<0.05 with no correction for multiple testing, about how many genes will appear "significant" just by chance?

- [ ] 0
- [ ] 5
- [x] 50
- [ ] 1000

## Why is controlling the false discovery rate (e.g. with the Benjamini-Hochberg procedure) usually preferred over Bonferroni correction when testing thousands of genes at once?

- [x] It controls the expected proportion of false discoveries rather than the chance of any single false positive, giving more power to detect real effects among many tests
- [ ] FDR ignores the multiple-testing problem entirely, which is simpler
- [ ] Bonferroni correction only works for continuous-valued data
- [ ] FDR requires testing fewer genes than Bonferroni does

## In a volcano plot (log2 fold change on the x-axis, -log10(p-value) on the y-axis), which genes are the most interesting?

- [x] Genes far from the center (large effect) AND high up (strong statistical evidence)
- [ ] Only genes far from the center, regardless of height
- [ ] Only genes high up, regardless of horizontal position
- [ ] Genes exactly at the center of the plot

## What is log10(0.0001)?

- [x] -4
- [ ] 4
- [ ] 0.0001
- [ ] -0.0001

## Why are substitution-matrix and profile scores (Sessions 4 and 5) computed as SUMS of log-odds terms rather than PRODUCTS of odds ratios?

- [x] Because log(xy) = log(x) + log(y), so summing logs is equivalent to multiplying the underlying probabilities, while avoiding numerical underflow
- [ ] Because sums are always more biologically meaningful than products
- [ ] Because logarithms make small probabilities larger
- [ ] Because addition is only possible for positive numbers

## What range of values does the sigmoid function σ(z) = 1/(1+e^-z) always produce, no matter what z is?

- [x] (0, 1)
- [ ] (-1, 1)
- [ ] (0, ∞)
- [ ] Any real number

## This cell simulates 100 genes that are all truly non-differentially-expressed (drawn from the exact same distribution) and tests each one:

<!-- coding-exercise -->

```python
false_positives = 0
for _ in range(100):
    g1 = rng.normal(0, 1, size=6)
    g2 = rng.normal(0, 1, size=6)
    _, p = stats.ttest_ind(g1, g2)
    if p < 0.05:
        false_positives += 1
print(false_positives)
```

Which of the following is the most accurate prediction for what this prints?

- [x] A number close to 5, varying somewhat each run due to randomness — not exactly 0
- [ ] Exactly 0, since none of the genes are truly different
- [ ] Exactly 100, since the test always rejects the null hypothesis
- [ ] It will raise an error, since g1 and g2 are identical distributions

## A fair eight-sided die (values 1-8) is rolled once. What is P(even | X > 5)?

X > 5 means the outcome is 6, 7, or 8 — three equally likely outcomes, of which two (6 and 8) are even.

- [ ] 1/3
- [ ] 1/2
- [x] 2/3
- [ ] 3/4

## This cell from notebooks/session01-math-in-code.ipynb runs gradient descent on f(x) = (x-3)^2:

<!-- coding-exercise -->

```python
def f(x):
    return (x - 3)**2

def fprime(x):
    return 2*(x - 3)

x = 0.0
eta = 0.3
for n in range(4):
    print(f"n={n}  x_n={x:.3f}  f(x_n)={f(x):.3f}  f'(x_n)={fprime(x):.3f}")
    x = x - eta * fprime(x)
print(f"n=4  x_n={x:.3f}  (converging toward the true minimum at x=3)")
```

Without running it: how many lines does this cell print in total, and does the final printed x_n equal exactly 3.0?

- [x] 5 lines total; the final x_n is very close to 3.0 but not exactly equal
- [ ] 4 lines total; the final x_n equals exactly 3.0
- [ ] 5 lines total; the final x_n equals exactly 3.0
- [ ] 4 lines total; the final x_n is very close to 3.0 but not exactly equal

## Using the derivative cheat sheet, what is the derivative of ln(x)?

- [x] 1/x
- [ ] x
- [ ] 1/x²
- [ ] ln(x)

## The sigmoid function's derivative is conventionally written σ(z)(1-σ(z)) rather than re-expanded in terms of e^-z. Why is that form actually useful in practice?

- [x] Because a network's forward pass already computes σ(z), so the derivative costs nothing extra to get from it
- [ ] Because it's the only mathematically correct way to write the derivative
- [ ] Because e^-z cannot be differentiated directly
- [ ] Because σ(z)(1-σ(z)) is always equal to zero

## If f'(x) = 2(x-3), what is ∫f'(x)dx?

- [x] (x-3)² + C
- [ ] 2(x-3)² + C
- [ ] x² - 3 + C
- [ ] 2x - 6

## Starting Session 8, "area under the ROC curve" (AUROC) is a standard classifier-evaluation metric. In what sense is this literally an integral?

- [x] It's the area under a curve, computed numerically (e.g. the trapezoidal rule) rather than solved symbolically, since a real ROC curve isn't a tidy algebraic function
- [ ] It isn't really an integral, "area under the curve" is just a figure of speech
- [ ] It's an integral only when the classifier is a neural network
- [ ] It's the derivative of the ROC curve, not its integral

## A fair six-sided die has mean 3.5. What is its variance?

- [ ] 3.5
- [x] 35/12 ≈ 2.92
- [ ] 1.71
- [ ] 6

## For a normal distribution with mean μ and standard deviation σ, roughly what fraction of values fall within one standard deviation of the mean?

- [x] 68%
- [ ] 95%
- [ ] 99.7%
- [ ] 50%

## An alignment column contains only A, in every sequence. What is its entropy?

- [x] 0 bits: the outcome is certain, so there is no surprise
- [ ] 2 bits, the maximum for DNA
- [ ] 1 bit
- [ ] It cannot be computed from a single column

## Which alignment column has the highest entropy?

- [x] A, C, G and T in 25% of the sequences each
- [ ] A in 70% of the sequences, C, G and T in 10% each
- [ ] A and G in 50% each
- [ ] A in every sequence

## Why does minimizing cross-entropy give the same model as maximum likelihood?

- [x] The cross-entropy between the observed frequencies and the model is the negative log-likelihood per observation
- [ ] Cross-entropy is always zero at the maximum-likelihood parameters
- [ ] They only agree when all outcomes are equally likely
- [ ] Cross-entropy ignores the model's probabilities
