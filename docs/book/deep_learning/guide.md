# Deep Learning — Book Guide

이 디렉토리의 교재 소스를 빠르게 탐색하기 위한 가이드.

## 소스 파일 목록

### Goodfellow-DeepLearning
| 파일 | 변환 도구 |
|---|---|
| Goodfellow-DeepLearning-summary.md | 요약 |
| Goodfellow-DeepLearning_azure_full.md | Document Intelligence |

### Goodfellow-DeepLearning_azure
| 파일 | 변환 도구 |
|---|---|
| Goodfellow-DeepLearning_azure_full.md | Document Intelligence |

### Jurafsky-SLP
| 파일 | 변환 도구 |
|---|---|
| Jurafsky-SLP-summary.md | 요약 |
| Jurafsky-SLP_marker_full.md | Marker |

### Raschka-BuildLLM
| 파일 | 변환 도구 |
|---|---|
| Raschka-BuildLLM-summary.md | 요약 |
| Raschka-BuildLLM_marker_full.md | Marker |

### Sutton-RL
| 파일 | 변환 도구 |
|---|---|
| Sutton-RL-summary.md | 요약 |
| Sutton-RL_marker_full.md | Marker |

### Zhang-D2L
| 파일 | 변환 도구 |
|---|---|
| Zhang-D2L-summary.md | 요약 |
| Zhang-D2L_azure_full.md | Document Intelligence |

### Zhang-D2L_azure
| 파일 | 변환 도구 |
|---|---|
| Zhang-D2L_azure_full.md | Document Intelligence |

## 챕터 목차 (Marker 기준)

> `L:숫자`는 원본 md 파일의 라인 번호. `Read(file, offset=L, limit=N)`으로 해당 구간을 직접 읽을 수 있음.

### Jurafsky-SLP
- **파일**: `Jurafsky-SLP_marker_full.md`
- **총 라인 수**: ~17,811
- **주요 섹션** (202개):
- Volume I (p.8) `L:294`
  - 2.2 Morphemes: Parts of Words `L:437`
  - 2.3 Unicode `L:487`
  - 2.4 Subword Tokenization: Byte-Pair Encoding (p.20) `L:595`
  - 2.6 Regular Expressions `L:817`
  - 2.6.5 A Simple Example `L:953`
  - 2.7 Simple Unix Tools for Word Tokenization `L:1123`
  - 2.8 Rule-based tokenization `L:1187`
  - 2.9 Minimum Edit Distance `L:1244`
  - 2.10 Summary `L:1357`
  - 3.1 N-Grams `L:1436`
  - 3.2 Evaluating Language Models: Training and Test Sets `L:1621`
  - 3.3 Evaluating Language Models: Perplexity `L:1659`
  - 3.4 Sampling sentences from a language model `L:1743`
  - 3.5 Generalizing vs. overfitting the training set `L:1759`
  - 3.6 Smoothing, Interpolation, and Backoff `L:1793`
  - 3.7 Advanced: Perplexity's Relation to Entropy `L:1948`
  - 3.8 Summary `L:2053`
- Logistic Regression and Text Classification (p.69) `L:2127`
  - 4.1 Machine learning and classification `L:2164`
  - 4.2 The sigmoid function `L:2217`
  - 4.3 Classification with Logistic Regression `L:2292`
  - 4.4 Learning in Logistic Regression `L:2422`
  - 4.5 The cross-entropy loss function `L:2434`
  - 4.7 Multinomial logistic regression `L:2669`
  - 4.8 Learning in Multinomial Logistic Regression `L:2752`
  - 4.9 Evaluation: Precision, Recall, F-measure `L:2788`
  - 4.10 Test sets and Cross-validation `L:2870`
  - 4.11 Statistical Significance Testing `L:2888`
  - 4.12 Avoiding Harms in Classification `L:2952`
  - 4.13 Interpreting models (p.98) `L:2990`
  - 4.14 Advanced: Regularization (p.98) `L:2996`
  - 4.15 Advanced: Deriving the Gradient Equation `L:3050`
  - 4.16 Summary `L:3092`
  - 5.1 Lexical Semantics `L:3157`
  - 5.2 Vector Semantics: The Intuition `L:3235`
  - 5.3 Simple count-based embeddings `L:3273`
  - 5.4 Cosine for measuring similarity `L:3341`
  - 5.5 Word2vec `L:3401`
  - 5.6 Visualizing Embeddings `L:3584`
  - 5.8 Bias and Embeddings `L:3654`
  - 5.9 Evaluating Vector Models `L:3672`
  - 5.10 Summary `L:3686`
  - 6.1 Units `L:3766`
  - 6.2 The XOR problem `L:3842`
  - 6.4 Feedforward networks for NLP: Classification `L:4041`
  - 6.5 Embeddings as the input to neural net classifiers `L:4083`
  - 6.6 Training Neural Nets `L:4193`
  - 6.7 Summary `L:4412`
  - 7.1 Three architectures for language models `L:4503`
  - 7.2 Conditional Generation of Text: The Intuition `L:4525`
  - 7.3 Prompting `L:4561`
  - 7.4 Generation and Sampling `L:4657`
  - 7.5 Training Large Language Models `L:4767`
  - 7.6 Evaluating Large Language Models `L:4862`
  - 7.7 Ethical and Safety Issues with Language Models `L:4960`
  - 7.8 Summary `L:4994`
  - 8.1 Attention `L:5062`
  - 8.2 Transformer Blocks `L:5222`
  - 8.4 The input: embeddings for token and position `L:5383`
  - 8.5 The Language Modeling Head `L:5433`
  - 8.7 Training `L:5511`
  - 8.8 Dealing with Scale `L:5523`
  - 8.9 Interpreting the Transformer `L:5598`
  - 8.10 Summary `L:5634`
  - 9.1 Bidirectional Transformer Encoders `L:5676`
  - 9.2 Training Bidirectional Encoders `L:5731`
  - 9.3 Contextual Embeddings `L:5831`
  - 9.4 Fine-Tuning for Classification `L:5927`
- 9.5 Fine-Tuning for Sequence Labeling: Named Entity Recognition (p.220) `L:5990`
  - 9.6 Summary `L:6109`
- Post-training: Instruction Tuning, Alignment, and Test-Time Compute (p.225) `L:6127`
  - 10.1 Instruction Tuning (p.226) `L:6153`
  - 10.2 Learning from Preferences `L:6265`
  - 10.3 LLM Alignment via Preference-Based Learning `L:6385`
- 11 Information Retrieval and Retrieval-Augmented Generation `L:6530`
  - 11.1 Information Retrieval `L:6578`
  - 11.2 Evaluation of Information-Retrieval Systems `L:6804`
  - 11.3 Information Retrieval with Dense Vectors `L:6903`
  - 11.4 Retrieval-Augmented Generation (RAG) `L:6958`
  - 11.5 Datasets `L:7017`
  - 11.6 Evaluating Question Answering `L:7083`
  - 11.7 Summary `L:7093`
- 12 Machine Translation `L:7170`
  - 12.1 Language Divergences and Typology `L:7228`
  - 12.2 Machine Translation using Encoder-Decoder `L:7328`
  - 12.3 Details of the Encoder-Decoder Model `L:7423`
  - 12.4 Decoding in MT: Beam Search `L:7459`
  - 12.5 Translating in low-resource situations `L:7579`
  - 12.6 MT Evaluation `L:7619`
  - 12.8 Summary `L:7762`
- 13 RNNs and LSTMs `L:7827`
  - 13.1 Recurrent Neural Networks `L:7835`
  - 13.1.1 Inference in RNNs (p.292) `L:7857`
  - 13.2 RNNs as Language Models `L:7903`
  - 13.3 RNNs for other NLP tasks `L:7984`
  - 13.4 Stacked and Bidirectional RNN architectures `L:8048`
  - 13.5 The LSTM `L:8102`
  - 13.6 Summary: Common RNN NLP Architectures `L:8181`
  - 13.7 The Encoder-Decoder Model with RNNs `L:8191`
  - 13.9 Summary `L:8358`
- 14 Phonetics and Speech Feature Extraction `L:8391`
  - 14.1 Speech Sounds and Phonetic Transcription `L:8405`
  - 14.2 Articulatory Phonetics (p.319) `L:8473`
  - 14.3 Prosody `L:8563`
  - 14.4 Acoustic Phonetics and Signals `L:8639`
  - 14.4.1 Waves `L:8643`
  - 14.5 Feature Extraction for Speech Recognition: Log Mel Spectrum (p.336) `L:8856`
  - 14.6 MFCC: Mel Frequency Cepstral Coefficients `L:8975`
  - 14.7 Summary `L:9022`
- 15 Automatic Speech Recognition (p.346) `L:9070`
  - 15.1 The Automatic Speech Recognition Task `L:9096`
  - 15.2 Convolutional Neural Networks `L:9143`
  - 15.3 The Encoder-Decoder Architecture for ASR `L:9210`
  - 15.4 Self-supervised models: HuBERT `L:9315`
  - 15.5 CTC `L:9407`
  - 15.6 ASR Evaluation: Word Error Rate (p.366) `L:9516`
  - 15.7 Summary `L:9593`
- 16 Text-to-Speech `L:9632`
  - 16.2 Using a codec to learn discrete audio tokens `L:9690`
  - 16.3 VALL-E: Generating audio with 2-stage LM `L:9824`
  - 16.4 TTS Evaluation `L:9875`
  - 16.5 Other speech tasks `L:9887`
  - 16.6 Spoken Language Models `L:9905`
  - 16.7 Summary `L:9909`
- Volume II (p.386) `L:9940`
- 17 Sequence Labeling for Parts of Speech and Named Entities `L:9956`
  - 17.1 (Mostly) English Word Classes `L:9978`
  - 17.2 Part-of-Speech Tagging `L:10077`
  - 17.3 Named Entities and Named Entity Tagging `L:10117`
  - 17.4 HMM Part-of-Speech Tagging `L:10182`
  - 17.5 Conditional Random Fields (CRFs) (p.403) `L:10430`
  - 17.6 Evaluation of Named Entity Recognition `L:10619`
  - 17.7 Further Details `L:10629`
  - 17.8 Summary `L:10662`
- 18 Context-Free Grammars and Constituency Parsing `L:10723`
  - 18.1 Constituency (p.415) `L:10741`
  - 18.2 Context-Free Grammars `L:10757`
  - 18.3 Treebanks `L:10953`
  - 18.4 Grammar Equivalence and Normal Form `L:11018`
  - 18.6 CKY Parsing: A Dynamic Programming Approach `L:11124`
  - 18.7 Span-Based Neural Constituency Parsing `L:11265`
  - 18.7.1 Computing Scores for a Span `L:11271`
  - 18.8 Evaluating Parsers `L:11338`
  - 18.9 Heads and Head-Finding `L:11365`
  - 18.10 Summary `L:11399`
- 19 Dependency Parsing `L:11452`
  - 19.1 Dependency Relations `L:11480`
  - 19.2 Transition-Based Dependency Parsing `L:11592`
  - 19.3 Graph-Based Dependency Parsing `L:11913`
  - 19.4 Evaluation `L:12060`
  - 19.5 Summary `L:12082`
- 20 Information Extraction: Relations, Events, and Time `L:12121`
  - 20.1 Relation Extraction `L:12159`
  - 20.2 Relation Extraction Algorithms `L:12226`
  - 20.3 Extracting Events `L:12560`
  - 20.4 Representing Time `L:12587`
  - 20.5 Representing Aspect `L:12641`
  - 20.6 Temporally Annotated Datasets: TimeBank `L:12705`
  - 20.7 Automatic Temporal Analysis `L:12737`
  - 20.8 Template Filling `L:12868`
  - 20.9 Summary `L:12966`
- 21 Semantic Role Labeling (p.488) `L:12997`
  - 21.1 Semantic Roles `L:13023`
  - 21.2 Diathesis Alternations `L:13051`
  - 21.3 Semantic Roles: Problems with Thematic Roles `L:13118`
  - 21.4 The Proposition Bank `L:13141`
  - 21.5 FrameNet `L:13201`
  - 21.6 Semantic Role Labeling `L:13285`
  - 21.7 Selectional Restrictions `L:13382`
  - 21.8 Primitive Decomposition of Predicates `L:13515`
  - 21.9 Summary `L:13573`
- 22 Lexicons for Sentiment, Affect, and Connotation `L:13617`
  - 22.1 Defining Emotion `L:13651`
  - 22.2 Available Sentiment and Affect Lexicons `L:13679`
  - 22.3 Creating Affect Lexicons by Human Labeling (p.512) `L:13736`
  - 22.5 Supervised Learning of Word Sentiment `L:13886`
  - 22.6 Using Lexicons for Sentiment Recognition `L:14016`
  - 22.7 Using Lexicons for Affect Recognition `L:14033`
  - 22.8 Lexicon-based methods for Entity-Centric Affect `L:14067`
  - 22.9 Connotation Frames (p.524) `L:14084`
- 23 Coreference Resolution and Entity Linking `L:14147`
  - 23.1 Coreference Phenomena: Linguistic Background `L:14230`
  - 23.3 Mention Detection `L:14449`
  - 23.4 Architectures for Coreference Algorithms `L:14518`
  - 23.5 Classifiers using hand-built features `L:14580`
  - 23.6 A neural mention-ranking algorithm `L:14628`
  - 23.7 Entity Linking (p.547) `L:14715`
  - 23.8 Evaluation of Coreference Resolution `L:14838`
  - 23.9 Winograd Schema problems `L:14864`
  - 23.10 Gender Bias in Coreference `L:14905`
  - 23.11 Summary `L:14924`
- 24 Discourse Coherence `L:14991`
  - 24.1 Coherence Relations `L:15047`
  - 24.2 Discourse Structure Parsing `L:15145`
  - 24.3 Centering and Entity-Based Coherence (p.567) `L:15266`
  - 24.4 Representation learning models for local coherence `L:15405`
  - 24.5 Global Coherence `L:15460`
  - 24.6 Summary `L:15534`
- 25 Conversation and its Structure (p.580) `L:15575`
  - 25.1 Properties of Human Conversation `L:15581`
  - 25.2 Dialog Acts and Corpora `L:15763`

### Raschka-BuildLLM
- **파일**: `Raschka-BuildLLM_marker_full.md`
- **총 라인 수**: ~11,576
- **주요 섹션** (125개):
  - Build a Large Language Model (From Scratch) `L:13`
  - 1 Understanding large language models 1 (p.22) `L:64`
  - 2 Working with text data 17 (p.38) `L:74`
  - 1.1 What is an LLM? (p.23) `L:286`
  - 1.2 Applications of LLMs (p.25) `L:310`
  - 1.3 Stages of building and using LLMs (p.26) `L:326`
  - 1.4 Introducing the transformer architecture (p.28) `L:356`
  - 1.5 Utilizing large datasets (p.31) `L:390`
  - 1.6 A closer look at the GPT architecture (p.33) `L:422`
  - 1.7 Building a large language model (p.35) `L:448`
  - 2.1 Understanding word embeddings (p.39) `L:501`
  - 2.2 Tokenizing text (p.42) `L:531`
  - 2.3 Converting tokens into token IDs (p.45) `L:667`
  - 2.4 Adding special context tokens (p.50) `L:812`
  - 2.5 Byte pair encoding (p.54) `L:943`
  - Exercise 2.1 Byte pair encoding of unknown words `L:1011`
  - 2.6 Data sampling with a sliding window (p.56) `L:1017`
  - Exercise 2.2 Data loaders with different strides and context sizes (p.60) `L:1217`
  - 2.7 Creating token embeddings (p.62) `L:1273`
  - 2.8 Encoding word positions (p.64) `L:1357`
  - 3.1 The problem with modeling long sequences (p.73) `L:1514`
  - 3.2 Capturing data dependencies with attention mechanisms (p.75) `L:1542`
  - 3.3 Attending to different parts of the input with self-attention (p.76) `L:1562`
  - 3.3.1 A simple self-attention mechanism without trainable weights (p.77) `L:1574`
  - 3.3.2 Computing attention weights for all input tokens (p.82) `L:1730`
  - 3.4 Implementing self-attention with trainable weights (p.85) `L:1853`
  - 3.4.1 Computing the attention weights step by step (p.86) `L:1867`
  - Weight parameters vs. attention weights `L:1923`
  - Why query, key, and value? (p.91) `L:2035`
  - 3.4.2 Implementing a compact self-attention Python class (p.91) `L:2045`
  - Exercise 3.1 Comparing SelfAttention\_v1 and SelfAttention\_v2 (p.94) `L:2156`
  - 3.5 Hiding future words with causal attention (p.95) `L:2166`
  - 3.5.1 Applying a causal attention mask (p.96) `L:2178`
  - 3.5.2 Masking additional attention weights with dropout (p.99) `L:2326`
  - 3.5.3 Implementing a compact causal attention class (p.101) `L:2385`
  - 3.6 Extending single-head attention to multi-head attention (p.103) `L:2482`
  - Exercise 3.2 Returning two-dimensional embedding vectors (p.106) `L:2564`
  - 3.6.2 Implementing multi-head attention with weight splits (p.107) `L:2570`
  - Exercise 3.3 Initializing GPT-2 size attention modules `L:2778`
  - Implementing a GPT model from scratch to generate text (p.113) `L:2796`
  - 4.1 Coding an LLM architecture (p.114) `L:2814`
  - 4.2 Normalizing activations with layer normalization (p.120) `L:2992`
  - Layer normalization vs. batch normalization `L:3154`
  - 4.3 Implementing a feed forward network with GELU activations (p.126) `L:3160`
  - 4.4 Adding shortcut connections (p.130) `L:3273`
  - 4.5 Connecting attention and linear layers in a transformer block (p.134) `L:3414`
  - 4.6 Coding the GPT model (p.138) `L:3500`
  - Exercise 4.1 Number of parameters in feed forward and attention modules (p.142) `L:3638`
  - Exercise 4.2 Initializing larger GPT models (p.143) `L:3665`
  - 4.7 Generating text (p.143) `L:3669`
  - Exercise 4.3 Using separate dropout parameters `L:3793`
  - 5.1 Evaluating generative text models (p.150) `L:3826`
  - 5.1.1 Using GPT to generate text (p.151) `L:3834`
  - 5.1.2 Calculating the text generation loss (p.153) `L:3914`
  - 5.1.3 Calculating the training and validation set losses (p.161) `L:4176`
  - The cost of pretraining LLMs `L:4188`
  - 5.2 Training an LLM (p.167) `L:4392`
  - 5.3 Decoding strategies to control randomness (p.172) `L:4600`
  - 5.3.1 Temperature scaling (p.173) `L:4634`
  - 5.3.2 Top-k sampling (p.176) `L:4757`
  - 5.3.3 Modifying the text generation function (p.178) `L:4824`
  - 5.4 Loading and saving model weights in PyTorch (p.180) `L:4913`
  - 5.5 Loading pretrained weights from OpenAI (p.181) `L:4967`
  - 6.1 Different categories of fine-tuning (p.191) `L:5278`
  - 6.2 Preparing the dataset (p.193) `L:5304`
  - 6.3 Creating data loaders (p.196) `L:5477`
  - Exercise 6.1 Increasing the context length `L:5585`
  - 6.4 Initializing a model with pretrained weights (p.202) `L:5659`
  - 6.5 Adding a classification head (p.204) `L:5760`
  - Fine-tuning selected layers vs. all layers `L:5810`
  - Exercise 6.2 Fine-tuning the whole model `L:5847`
  - 6.6 Calculating the classification loss and accuracy (p.211) `L:5933`
  - The initial loss values are `L:6104`
  - 6.7 Fine-tuning the model on supervised data (p.216) `L:6114`
  - Choosing the number of epochs `L:6288`
  - 6.8 Using the LLM as a spam classifier (p.221) `L:6332`
  - 7.1 Introduction to instruction fine-tuning (p.226) `L:6448`
  - 7.2 Preparing a dataset for supervised instruction fine-tuning (p.228) `L:6462`
  - Exercise 7.1 Changing prompt styles `L:6543`
  - 7.3 Organizing data into training batches (p.232) `L:6635`
  - Exercise 7.2 Instruction and input masking `L:6971`
  - 7.4 Creating data loaders for an instruction dataset (p.244) `L:6975`
  - 7.5 Loading a pretrained LLM (p.247) `L:7082`
  - 7.6 Fine-tuning the LLM on instruction data (p.250) `L:7196`
  - Exercise 7.3 Fine-tuning on the original Alpaca dataset `L:7328`
  - 7.7 Extracting and saving responses (p.254) `L:7334`
  - 7.8 Evaluating the fine-tuned LLM (p.259) `L:7508`
  - Using larger LLMs via web APIs `L:7520`
  - Running the code in a new Python session (p.263) `L:7606`
  - Exercise 7.4 Parameter-efficient fine-tuning with LoRA (p.268) `L:7860`
  - 7.9 Conclusions (p.268) `L:7864`
  - 7.9.1 What's next? (p.268) `L:7868`
  - 7.9.2 Staying up to date in a fast-moving field (p.269) `L:7878`
  - 7.9.3 Final words (p.269) `L:7882`
  - appendix A Introduction to PyTorch (p.272) `L:7902`
  - PyTorch with a NumPy-like API (p.279) `L:8050`
  - A.2.1 Scalars, vectors, matrices, and tensors `L:8054`
  - A.2.3 Common PyTorch tensor operations `L:8117`
  - A.3 Seeing models as computation graphs `L:8214`
  - A.4 Automatic differentiation made easy `L:8236`
  - A.5 Implementing multilayer neural networks `L:8303`
  - A.6 Setting up efficient data loaders `L:8502`
  - A.7 A typical training loop `L:8668`
  - A.8 Saving and loading models `L:8868`
  - A.9 Optimizing training performance with GPUs `L:8889`
  - A.9.1 PyTorch computations on GPU devices `L:8893`
  - A.9.3 Training with multiple GPUs `L:9026`
  - SELECTING AVAILABLE GPUS ON A MULTI-GPU MACHINE `L:9169`
  - Alternative PyTorch APIs for multi-GPU training (p.309) `L:9238`
  - appendix B References and further reading `L:9254`
  - Chapter 1 (p.310) `L:9256`
  - Chapter 2 `L:9300`
  - Chapter 3 `L:9329`
  - Chapter 4 `L:9360`
  - Chapter 5 `L:9398`
  - Chapter 6 `L:9455`
  - Chapter 7 `L:9493`
  - Appendix A `L:9540`
  - appendix C Exercise solutions `L:9569`
  - On the CPU this resulted in `L:10187`
  - appendix D Adding bells and whistles to the training loop (p.334) `L:10208`
  - D.4 The modified training function `L:10490`
  - appendix E Parameter-efficient fine-tuning with LoRA (p.343) `L:10614`
  - E.4 Parameter-efficient fine-tuning with LoRA `L:10865`
  - Hands-on projects for learning your way `L:11510`

### Sutton-RL
- **파일**: `Sutton-RL_marker_full.md`
- **총 라인 수**: ~4,412
- **주요 섹션** (10개):
- Part I Tabular Solution Methods `L:467`
- 3.4 Unified Notation for Episodic and Continuing Tasks `L:866`
- \*5.8 Importance Sampling on Truncated Returns `L:1947`
- 7.7 Off-policy Eligibility Traces using Importance Sampling `L:2766`
- Planning and Learning with Tabular Methods `L:2836`
- Part II Approximate Solution Methods `L:3141`
- On-policy Approximation of Action Values `L:3143`
- 9.1 Value Prediction with Function Approximation `L:3151`
- Off-policy Approximation of Action Values `L:3573`
- 11.3 R-Learning and the Average-Reward Setting `L:3644`
