# Session 10: CNNs, Classic & Modern

## Why does a convolutional layer use far fewer parameters than a fully connected layer processing the same input?

- [x] It reuses the same small kernel at every position (weight sharing), instead of learning an independent weight per position
- [ ] It only looks at half of the input
- [ ] It automatically discards the least useful input positions
- [ ] It uses 16-bit instead of 32-bit weights

## A randomly-initialized (untrained) 1D convolution kernel is applied to a signal, and separately to the same signal shifted by 10 positions. What does this actually show about the two outputs?

- [x] They match exactly (away from the edges) once you shift one of them by 10 positions — equivariance is a property of weight sharing itself, not something the network has to learn
- [ ] They are completely unrelated, since the kernel was never trained
- [ ] They only match after training the kernel for many epochs
- [ ] They match only if the kernel size equals the shift amount

## A convolutional layer is translation-*equivariant* by itself. What additional operation turns that into translation-*invariance* (the same output value regardless of where a feature appears)?

- [x] Global pooling (e.g. taking the max or mean over the whole feature map), which discards the remaining position information
- [ ] Adding more convolutional layers of the same kind
- [ ] Increasing the kernel size until it covers the whole input
- [ ] Nothing else is needed — equivariance and invariance are the same property

## On Session 10's real measured comparison, how did the 1D-CNN's test accuracy compare to Session 9's trained flat MLP, on the identical homology-aware subcellular-localization test set?

- [x] Higher (0.587 vs. 0.514), and better on MCC and AUROC too, despite using about 10x fewer parameters
- [ ] Lower (0.514 vs. 0.587), because a CNN needs far more parameters to reach the same accuracy
- [ ] Identical to three decimal places
- [ ] The CNN could not be trained on this data at all

## This is the core architecture from the notebook's subcellular-localization case study:

<!-- coding-exercise -->

```python
class LocalizationCNN(nn.Module):
    def __init__(self, n_classes=5, n_channels=20):
        super().__init__()
        self.conv1 = nn.Conv1d(n_channels, 32, kernel_size=7, padding=3)
        self.conv2 = nn.Conv1d(32, 64, kernel_size=7, padding=3)
        self.pool = nn.MaxPool1d(2)
        self.classifier = nn.Linear(64, n_classes)

    def forward(self, x):                      # x: (batch, 20, 150)
        x = torch.relu(self.conv1(x))
        x = self.pool(x)
        x = torch.relu(self.conv2(x))
        x = torch.adaptive_avg_pool1d(x, 1).squeeze(-1)   # global average pool -> (batch, 64)
        return self.classifier(x)               # raw logits, (batch, n_classes)
```

What does the `torch.adaptive_avg_pool1d(x, 1).squeeze(-1)` line do to the sequence-length dimension, right before the final classification layer?

- [x] It collapses the whole sequence-length dimension down to a single value per channel by averaging — global average pooling, which is what makes the final prediction position-independent
- [ ] It doubles the sequence length by upsampling
- [ ] It selects only the first residue's features and discards the rest
- [ ] It removes the channel dimension instead of the sequence-length dimension

## Why is a fully connected layer a particularly poor fit for a 224x224x3 image specifically, compared to a small text-classification input?

- [x] The input has over 150,000 values, so even a modest hidden layer needs millions of independently-learned weights, with no structural notion that nearby pixels are related
- [ ] Images cannot be represented as numbers at all
- [ ] A fully connected layer can only accept grayscale (single-channel) input
- [ ] 224x224x3 images are too small for a fully connected layer to process

## What specifically made it possible to train networks over 100 layers deep (ResNet, 2015), where simply stacking more layers onto a plain CNN had previously made training worse, not better?

- [x] Skip (residual) connections, letting a layer's input pass through unchanged alongside its transformed output
- [ ] Using a bigger GPU
- [ ] Removing all activation functions from the network
- [ ] Training for 10x more epochs on the same architecture

## AlexNet's 2012 ImageNet result is widely credited with starting the current deep-learning era. What made it such a striking result at the time, beyond simply winning the competition?

- [x] Its top-5 error (16.4% on the provided data, 15.3% with extra data) beat the runner-up's 26.2% by about 10 percentage points, a margin large enough to change what the field considered worth trying
- [ ] It was the very first convolutional neural network ever built
- [ ] It achieved 0% error on the ImageNet test set
- [ ] It required no training data at all

## Why is transfer learning (fine-tuning a pretrained ImageNet model) the practical default for most new image tasks, rather than training a deep CNN from scratch?

- [x] Early layers of an image classifier tend to learn generic, reusable features (edges, textures, simple shapes) regardless of the original task, so only a small new head needs training for the new task
- [ ] Training a CNN from scratch is technically impossible
- [ ] A pretrained model automatically achieves perfect accuracy on any new dataset with zero adaptation
- [ ] It removes the need for any labeled data at all in the new task

## A fully-connected model predicting a full contact map (every output pixel from every input pixel) for a protein of length L needs on the order of L^4 weights, not L^2. Why L^4 rather than L^2?

- [x] Both the input and the output are themselves L^2-sized (an L x L grid), and a fully connected layer needs one weight per (input, output) pair, i.e. L^2 x L^2
- [ ] Because contact maps are always stored as 4-dimensional arrays
- [ ] Because L^4 is simply a typo for L^2 in the original description
- [ ] Because four separate models are needed, one per spatial dimension

## A 2D convolutional layer is applied to a contact map with `padding` chosen so the output has the same height and width as the input. Why does this specific property matter for contact-map prediction?

- [x] Contact-map prediction is a dense, pixel-to-pixel task — every input residue pair needs a corresponding output prediction, so the spatial dimensions must be preserved through the network
- [ ] It makes the network train faster, with no effect on what the network can predict
- [ ] It is required for any convolution to work at all, regardless of the task
- [ ] It only matters for square images, not for rectangular ones

## With only 40 labelled histology tiles per class, a small CNN from scratch, the same CNN with augmentation, a frozen ImageNet ResNet-18 and a frozen DINOv2 (each with a new last layer) were tested on tiles from 50 new patients. Which ranking did the notebook measure?

- [x] DINOv2 best (0.832); ResNet-18 (0.780) and the augmented CNN (0.792) close together; the CNN from scratch last (0.745)
- [ ] The CNN from scratch best, because it is adapted to tissue only
- [ ] ResNet-18 far ahead of everything else, because it was trained with labels
- [ ] All four within one percentage point

## DINOv2 was trained on 142 million images without a single label, yet its features classify tissue tiles it has never seen. What kind of model is this?

- [x] A self-supervised foundation model: pretrained once on huge unlabelled data, then reused for many tasks with a small model on top
- [ ] A model trained specifically on colorectal cancer slides
- [ ] A CNN with more convolution layers than ResNet-18
- [ ] A model that memorized the test tiles during pretraining

## Every model scored clearly higher on validation tiles (from the same slides as the training tiles) than on test tiles (from 50 other patients). What is the lesson?

- [x] Tiles from the same patient share staining, scanner and tissue features, so the honest split is by patient, just as Session 8 split proteins by homology
- [ ] The test tiles must be mislabelled
- [ ] Validation accuracy is always higher than test accuracy, whatever the split
- [ ] The models should have been trained on the test patients

## Rotating a tissue tile by 90° changed the predicted class for 18% of test tiles with the CNN trained without augmentation, but shifting it by 8 pixels changed only 5%. Why?

- [x] Shared kernels plus pooling give tolerance to shifts by construction; nothing in the architecture gives rotation invariance, so it has to be learned, for example from rotated training copies
- [ ] Rotated tiles contain black corners that confuse the network
- [ ] The network was trained on rotated tiles only
- [ ] Rotation changes the colours of the stain

## Training the CNN with rotated and mirrored copies of every tile roughly halved the fraction of test tiles whose prediction changed under a 90° rotation (18% → 9%). What did augmentation do?

- [x] It taught the network, from data, a symmetry that tissue really has (a section has no "up") but that the architecture cannot provide
- [ ] It made the network rotation invariant by construction
- [ ] It increased the number of weights in the network
- [ ] It removed the need for a test set

## The localization CNN's first-layer filter most selective for secreted proteins has its largest weights on L, I, V and F and fires around residues 10-13 of secreted proteins. What has it learned?

- [x] A detector for the hydrophobic core of the N-terminal signal peptide: effectively a learned position weight matrix
- [ ] A detector for nuclear localization signals
- [ ] Nothing: first-layer weights stay random
- [ ] The average length of secreted proteins

## Basset (2016) and DanQ (2016) report that many of their first-layer convolution filters match known transcription-factor motifs in CIS-BP or JASPAR. Why is that expected?

- [x] A first-layer filter on one-hot DNA is a 4 x k weight matrix scanned along the sequence, the form of a PWM, so training on binding or chromatin data tends to recover the motifs that explain it
- [ ] The motif databases were used to initialize the filters
- [ ] Convolution filters can only represent known motifs
- [ ] It is a coincidence

## DeepSEA predicts 919 chromatin features from 1,000 bp of DNA. How can such a model score the effect of a single non-coding variant?

- [x] Predict the chromatin profile for the reference sequence and for the sequence carrying the variant, and compare the two
- [ ] Look the variant up in a database of known disease mutations
- [ ] Count how often the variant occurs in the population
- [ ] It cannot score single variants

## In the contact map of an all-beta protein (the FNIII domain 1TEN), many contacts form lines running perpendicular to the main diagonal. What do they correspond to?

- [x] Pairs of antiparallel beta-strands: as one strand runs forward, its partner runs backward
- [ ] Alpha-helices
- [ ] Parallel beta-strands
- [ ] Disulfide bonds

## Three stacked 1D convolutions with kernel size 3, stride 1 and no pooling: how many input positions does one unit of the third layer depend on?

- [x] 7: each layer adds kernel size − 1 = 2 positions (3, 5, 7)
- [ ] 3: every layer sees only its own kernel
- [ ] 9: three layers times three positions
- [ ] 27: the receptive field multiplies by the kernel size in every layer

## A CNN trained on blood cells pasted into one corner reaches 0.86 accuracy on corner cells but about 0.2 on cells at random positions. Which change to the architecture would most directly help?

- [x] Replace the final Flatten + Linear layer by global average pooling, so the output no longer depends on where in the image a feature was found
- [ ] Add more local max-pooling layers of size 2
- [ ] Use a larger learning rate
- [ ] Remove the convolutional layers and use a dense network

## Which augmentation would be wrong for its task?

- [x] Rotating handwritten digits by 180° during training, because a rotated 6 becomes a 9
- [ ] Rotating blood-cell images by 90°, because a cell on a slide has no "up"
- [ ] Mirroring tissue tiles from a histology slide
- [ ] Small colour changes of H&E-stained tiles, imitating staining differences between labs

## The localization CNN averages each filter's output over the whole sequence before classifying (global average pooling). Why can this be a limitation for signal peptides?

- [x] It discards where the filter fired, although a hydrophobic stretch means a signal peptide at the N-terminus but may be a transmembrane helix in the middle of a protein
- [ ] It makes the filters forget which amino acids they respond to
- [ ] It doubles the number of weights in the network
- [ ] It only works for DNA, not for proteins
