# Session 11: Sequences, Language Models and SignalP

## An RNN's hidden state update is h_t = tanh(W_xh x_t + W_hh h_t-1 + b_h). What lets the same RNN process sequences of any length with a fixed number of parameters?

- [x] The same weight matrices (W_xh, W_hh) are reused at every position in the sequence, rather than having separate weights per position
- [ ] The sequence is always padded to a single fixed length before training
- [ ] Longer sequences automatically get more hidden units allocated to them
- [ ] RNNs cannot actually handle variable-length sequences in practice

## The gradient that backpropagation through time sends to an early position is a product of many factors, one per step (recurrent weights and activation derivatives). What decides whether it vanishes or explodes?

- [x] Whether the effective size of those factors is repeatedly below 1 (it tends to vanish) or above 1 (it can explode)
- [ ] The number of residues in the amino acid alphabet
- [ ] Whether the model uses PyTorch or another framework
- [ ] The batch size used during training

## Why does a bidirectional LSTM (BiLSTM) suit signal-peptide detection better than a forward-only LSTM, architecturally?

- [x] Whether an N-terminal residue belongs to a signal peptide is decided by the h-region that follows it, and a forward-only model can only see what came before
- [ ] BiLSTM always has fewer parameters than a forward-only LSTM
- [ ] BiLSTM does not use gates, avoiding the vanishing-gradient problem entirely
- [ ] Forward-only LSTMs cannot process protein sequences at all

## In the session's per-residue signal-peptide comparison on the homology-aware test set, the sliding window reached MCC 0.539, the simple RNN 0.620, the LSTM 0.631 and the bidirectional LSTM 0.820. What is the most important lesson?

- [x] Seeing the residues after a position matters more than extra memory: going bidirectional gave far more than going from RNN to LSTM
- [ ] More parameters always win
- [ ] Recurrent networks are no better than a sliding window
- [ ] The LSTM failed to train

## SignalP's versions run from feed-forward networks (1.0, 1997) through an HMM (2.0), transmembrane negatives (4.0), a deep network with an LSTM and a CRF (5.0, 2019) to 6.0 (2022). What was new in 6.0?

- [x] A pretrained Transformer protein language model (ProtBERT), fine-tuned, with a CRF on top; five signal-peptide types and n/h/c regions
- [ ] It returned to hand-designed scoring rules
- [ ] It replaced machine learning with sequence alignment to known signal peptides
- [ ] It added the organism group as a new required input

## Why does the session's dataset keep only signal peptides with experimental evidence (ECO:0000269)?

- [x] Many UniProt signal peptides are predicted, often by SignalP itself; training on them would teach a model to imitate SignalP
- [ ] Experimental annotations are always longer
- [ ] Predicted features cannot be downloaded from UniProt
- [ ] It makes the dataset larger

## What distinguishes a BERT-style language model (like ESM-2 and ProtBERT) from a GPT-style one?

- [x] BERT fills in masked tokens using context on both sides; GPT predicts the next token and may only attend to earlier positions
- [ ] BERT uses recurrence, GPT uses attention
- [ ] GPT has no attention
- [ ] BERT can only be used for proteins

## In self-attention, each position's query is compared with every key, the scores go through a softmax, and the result weights the values. What does one row of the resulting attention matrix represent?

- [x] How much each position contributes to the new representation of one position; the row sums to one
- [ ] The probability of the next token
- [ ] The gradient of the loss for that position
- [ ] A fixed weight shared by all sequences

## The Transformer (2017) removed recurrence entirely. Which advantage did that bring?

- [x] All positions can be processed in parallel, and any two positions are connected in one step, however far apart
- [ ] It no longer needs training data
- [ ] It uses fewer parameters than any RNN
- [ ] It cannot overfit

## With only 20 labelled training proteins, logistic regression on frozen ESM-2 embeddings reached MCC 0.762 on signal-peptide detection, while one-hot models stayed near zero. Which SignalP 6.0 finding does this mirror?

- [x] Protein language models enable few-shot learning: SignalP 6.0 made Tat/SPII (36 examples) and Sec/SPIII (113) predictable for the first time
- [ ] Language models remove the need for any labels
- [ ] One-hot encoding is always wrong for proteins
- [ ] SignalP 6.0 was trained on only 20 proteins

## On test proteins with no close homolog (<30% identity) in the training set, one-hot classifiers dropped to MCC 0.68-0.78, while frozen ESM-2 embeddings kept 0.96. On >90% identity, all were perfect. What does this show?

- [x] Pretrained representations help most where there is nothing close to copy from, the same pattern SignalP 6.0 reported below 60% identity
- [ ] Language models are worse on close homologs
- [ ] Homology partitioning is no longer needed
- [ ] The test set was too small to say anything

## ESM-2's attention-derived contact predictions for beta-globin had top-L/5 long-range precision 0.00 (8M parameters), 0.17 (35M), 0.62 (150M) and 0.90 (650M). What do these numbers suggest?

- [x] Knowledge about 3D structure emerges from masked-residue training only as models get larger, even though no structures were used in training
- [ ] Small models are better at structure
- [ ] The contact predictor was trained on beta-globin
- [ ] Attention maps cannot contain structural information

## Trained on eukaryotic proteins only, a one-hot classifier reached MCC 0.647 on bacterial proteins; ESM-2 embeddings reached 0.952. What does this suggest?

- [x] The ESM-2 representation transfers across kingdoms much better, consistent with SignalP 6.0 working without organism input; concluding that organism information is never needed would require more evidence, such as other organism groups and signal-peptide types
- [ ] Bacterial and eukaryotic signal peptides are identical
- [ ] One-hot encoding cannot represent bacterial proteins
- [ ] SignalP 6.0 requires the organism group more than ever

## Why did the SignalP authors call their SignalP 5.0 homology partitioning with CD-HIT "actually not valid"?

- [x] Assigning CD-HIT clusters to folds only controls identity to cluster centres; other pairs across folds stayed well above the 20% cutoff, so performance was overestimated
- [ ] CD-HIT cannot handle protein sequences
- [ ] There were too many folds
- [ ] The clusters were too small

## UniRep is described as a protein language model built on an LSTM rather than a Transformer. What does it actually learn to do during pretraining?

- [x] Predict the next amino acid given the ones before it, on millions of unlabeled UniRef50 sequences -- no labels or annotations required
- [ ] Predict a protein's exact 3D structure directly from its sequence
- [ ] Classify proteins into a fixed set of functional categories using labeled training data
- [ ] Translate protein sequences into a different organism's genetic code

## This is the shared tagger class from the session's notebook, switched between architectures via its `kind` argument:

<!-- coding-exercise -->

```python
class SeqTagger(nn.Module):
    def __init__(self, vocab_size, emb_dim=24, hid_dim=48, kind="rnn"):
        super().__init__()
        self.emb = nn.Embedding(vocab_size, emb_dim)
        bidirectional = (kind == "bilstm")
        if kind in ("lstm", "bilstm"):
            self.rnn = nn.LSTM(emb_dim, hid_dim, batch_first=True, bidirectional=bidirectional)
        elif kind == "gru":
            self.rnn = nn.GRU(emb_dim, hid_dim, batch_first=True)
        else:
            self.rnn = nn.RNN(emb_dim, hid_dim, batch_first=True, nonlinearity="tanh")
        out_dim = hid_dim * (2 if bidirectional else 1)
        self.out = nn.Linear(out_dim, 1)

    def forward(self, x):
        z = self.emb(x)
        h, _ = self.rnn(z)
        return self.out(h).squeeze(-1)
```

Why does `out_dim` need to double (`hid_dim * 2`) specifically when `kind="bilstm"`, but not for `"lstm"`, `"gru"`, or `"rnn"`?

- [x] A bidirectional LSTM concatenates the forward and backward hidden states at every position, so the final linear layer receives twice as many features as a single-direction model produces
- [ ] `bilstm` always uses twice as many embedding dimensions as the other options
- [ ] It is a bug in the code -- all four options should use the same `out_dim`
- [ ] Doubling `out_dim` is required by PyTorch's `nn.LSTM` regardless of directionality

## Besides self-attention, a Transformer block contains a feed-forward network, residual connections, layer normalization, and (before the first block) a position encoding. What would go wrong without the position encoding?

- [x] Attention by itself ignores order: shuffling the tokens would just shuffle the outputs, so "ACDE" and "EDCA" would look the same
- [ ] The model could not be trained on a GPU
- [ ] The attention weights would no longer sum to 1
- [ ] The feed-forward network would have no weights

## Why does every Transformer block add each step's output to its input (a residual connection), as ResNet did?

- [x] It gives the gradient a direct path through dozens of blocks, so it does not vanish, the same problem Session 9 met in deep sigmoid networks
- [ ] It doubles the number of attention heads
- [ ] It lets the model see future tokens
- [ ] It replaces the need for training data

## ESM-2, DINOv2 and the ProtBERT inside SignalP 6.0 are all called foundation models. What do they have in common?

- [x] Each was pretrained once on huge amounts of unlabelled data with a self-supervised task, and is then reused for many tasks via its embeddings plus a small model, or light fine-tuning
- [ ] Each was trained on labelled protein structures
- [ ] Each is a recurrent network
- [ ] Each must be retrained from scratch for every new task

## Which statement correctly describes language models of proteins?

- [x] They learn sequence regularities without biological labels, either by predicting the next residue (autoregressive) or by predicting hidden residues from both sides (masked, like ESM-2)
- [ ] They always predict the next residue from the previous ones only
- [ ] They need experimentally labelled proteins for training
- [ ] They assign one fixed vector to each amino acid type

## In one-hot encoding every leucine is the same vector. What is different in an ESM-2 embedding?

- [x] Each leucine gets its own vector, computed from the sequence around it, so leucines in signal peptides are represented differently from leucines in cytoplasmic proteins
- [ ] All leucines still get exactly the same vector
- [ ] Leucines are removed from the sequence before embedding
- [ ] ESM-2 encodes only the hydrophobicity of each residue

## A high attention weight connects residue 12 to residue 87 in one head of a protein language model. What does it show?

- [x] That residue 87 contributes strongly when residue 12 is updated in that head; it does not by itself prove a 3D contact or explain the biology
- [ ] That the two residues are in contact in the folded protein
- [ ] That residue 87 is functionally essential
- [ ] That the model has made an error
