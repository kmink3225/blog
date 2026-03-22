---
name: "Build a Large Language Model (From Scratch)"
type: book-summary
authors: "Sebastian Raschka"
year: 2025
total_pages: 337
language: en
keywords: [LLM, GPT, transformer, attention, pretraining, fine-tuning, tokenization, PyTorch, LoRA, instruction-tuning]
sources:
  - file: "Raschka-BuildLLM_marker_full.md"
    tool: Marker
---

# Build a Large Language Model (From Scratch) — Summary

> Sebastian Raschka (2025), Manning Publications, 337 pages, 7 chapters + 5 appendices
> GPT-2 아키텍처를 처음부터 직접 구현하고, 사전학습과 파인튜닝까지 전 과정을 코드로 완성하는 실습서이다.

## Contents

1. Understanding large language models (pp. 1–16)
2. Working with text data (pp. 17–49)
3. Coding attention mechanisms (pp. 50–91)
4. Implementing a GPT model from scratch to generate text (pp. 92–127)
5. Pretraining on unlabeled data (pp. 128–168)
6. Fine-tuning for classification (pp. 169–203)
7. Fine-tuning to follow instructions (pp. 204–250)
- Appendix A: Introduction to PyTorch (pp. 251–288)
- Appendix B: References and further reading (pp. 289–299)
- Appendix C: Exercise solutions (pp. 300–312)
- Appendix D: Adding bells and whistles to the training loop (pp. 313–321)
- Appendix E: Parameter-efficient fine-tuning with LoRA (pp. 322–336)

---

## Chapter Summaries

> Marker 원본: `Raschka-BuildLLM_marker_full.md` | 총 ~11,576 라인 | `L:숫자`로 직접 접근 가능


### Ch 1: Understanding large language models (pp. 1–16)
**핵심**: LLM은 transformer 아키텍처 기반의 대규모 딥러닝 모델로, next-word prediction을 통해 학습한다. "large"는 모델 파라미터 수(수십~수백억)와 학습 데이터 규모 양쪽을 의미한다. 이전 NLP 모델이 특정 태스크에 특화되었던 반면, LLM은 광범위한 NLP 태스크에서 범용적 역량을 보인다. 본 책은 ChatGPT와 같은 GPT 기반 LLM을 단계별로 직접 구현하는 것을 목표로 한다. LLM 개발은 Stage 1(데이터 준비 + 아키텍처), Stage 2(사전학습), Stage 3(파인튜닝)의 3단계로 구성된다.
**키워드**: `LLM`, `transformer`, `next-word prediction`, `GPT`, `decoder-only`
**상세**: → `Raschka-BuildLLM_marker_full.md` Ch 1 (L:264)
LLM은 대규모 텍스트 데이터로 학습된 심층 신경망으로, next-word prediction이라는 자기지도학습(self-supervised learning) 방식을 통해 언어의 구조와 의미를 학습한다. "large"는 모델 파라미터 수(수십~수백억)와 학습 데이터 규모를 모두 의미하며, GPT-3의 경우 CommonCrawl, WebText2, Books, Wikipedia 등 총 499B 토큰 중 300B 토큰으로 학습되었다. 이전 NLP 모델이 스팸 분류 등 특정 태스크에 특화되었던 반면, LLM은 번역, 요약, 코드 생성, 감성 분석 등 광범위한 태스크에서 범용적 역량을 보인다. Transformer 아키텍처(2017, "Attention Is All You Need")가 대부분의 현대 LLM의 기반이며, encoder-decoder 구조에서 self-attention 메커니즘이 핵심이다. BERT는 encoder 기반으로 masked word prediction에 특화되고, GPT는 decoder 기반으로 텍스트 생성에 특화된다. GPT는 zero-shot/few-shot 학습이 가능하며, 명시적으로 학습하지 않은 태스크도 수행할 수 있는 emergent behavior를 보인다. 이전의 RNN 기반 encoder-decoder 모델은 전체 입력을 하나의 hidden state로 압축해야 하는 한계가 있었으나, transformer의 self-attention은 입력의 모든 위치를 직접 참조할 수 있다. LLM 개발은 Stage 1(데이터 준비 + 아키텍처 구현), Stage 2(사전학습), Stage 3(파인튜닝)의 3단계로 구성된다. 파인튜닝은 instruction fine-tuning(다양한 지시 수행)과 classification fine-tuning(특정 분류 태스크)의 두 가지 주요 방식이 있다. GPT-2와 GPT-3는 동일한 아키텍처이며, 스케일만 다르다(GPT-2: 1.5B, GPT-3: 96 transformer layers, 175B parameters). 커스텀 LLM은 데이터 프라이버시, 지연 시간 감소, 도메인 특화 성능 등의 이점을 제공하며, 본 책은 GPT-2 아키텍처를 처음부터 직접 구현하는 것을 목표로 한다.

**Marker 세부 목차** (`Raschka-BuildLLM_marker_full.md`):
- 1 Understanding large language models 1 (p.22) `L:64`
- 1.1 What is an LLM? (p.23) `L:286`
- 1.2 Applications of LLMs (p.25) `L:310`
- 1.3 Stages of building and using LLMs (p.26) `L:326`
- 1.4 Introducing the transformer architecture (p.28) `L:356`
- 1.5 Utilizing large datasets (p.31) `L:390`
- 1.6 A closer look at the GPT architecture (p.33) `L:422`
- 1.7 Building a large language model (p.35) `L:448`


---

### Ch 2: Working with text data (pp. 17–49)
**핵심**: 텍스트를 LLM에 입력하기 위해 토큰화(tokenization) → 정수 ID 변환 → 임베딩 벡터 변환의 파이프라인을 구현한다. BPE(Byte Pair Encoding)는 GPT 계열에서 사용하는 서브워드 토큰화 방식으로, 어휘 외 단어(OOV) 문제를 해결한다. 슬라이딩 윈도우 방식으로 학습용 입력-출력 쌍을 생성하며, 최종 입력은 토큰 임베딩과 위치 임베딩(positional embedding)의 합으로 구성된다. Word2Vec 등 기존 임베딩과 달리, LLM은 학습 과정에서 임베딩을 함께 학습한다.
**키워드**: `BPE`, `tokenization`, `embedding`, `sliding window`, `positional encoding`
**상세**: → `Raschka-BuildLLM_marker_full.md` Ch 2 (L:481)
텍스트를 LLM에 입력하기 위해 토큰화 → 정수 ID 변환 → 임베딩 벡터 변환의 3단계 파이프라인을 구현한다. 딥러닝 모델은 원시 텍스트를 직접 처리할 수 없으므로 연속적인 벡터 표현(embedding)으로 변환해야 하며, Word2Vec과 같은 기존 방법과 달리 LLM은 학습 과정에서 임베딩을 함께 최적화한다. 토큰화는 정규표현식 기반의 단순 분할에서 시작하여, 구두점과 특수문자를 별도 토큰으로 분리하는 방식으로 발전한다. 각 토큰에 고유 정수 ID를 부여하고 `<|endoftext|>`, `<|unk|>` 등 특수 토큰을 추가하여 문서 경계 표시와 미등록 단어 처리를 한다. BPE(Byte Pair Encoding)는 GPT-2/3에서 사용하는 서브워드 토큰화 방식으로, 빈도 높은 바이트 쌍을 반복 병합하여 어휘를 구성함으로써 OOV(Out-of-Vocabulary) 문제를 해결한다. tiktoken 라이브러리를 사용하여 GPT-2의 BPE 토크나이저(vocab_size=50,257)를 구현하며, 이 토크나이저는 모든 미등록 단어를 서브워드로 분해할 수 있다. 슬라이딩 윈도우 방식으로 학습용 입력-타겟 쌍을 생성하며, context_length만큼의 토큰을 입력으로 하고 1 위치 이동한 토큰을 타겟으로 사용한다. PyTorch의 Dataset과 DataLoader를 활용하여 효율적인 배치 처리를 구현하며, stride 파라미터로 윈도우 이동 간격을 조절한다. 토큰 임베딩 레이어(nn.Embedding)는 각 토큰 ID를 768차원 벡터로 변환하며, 위치 임베딩(positional embedding)을 더하여 토큰의 순서 정보를 인코딩한다. GPT-2의 위치 임베딩은 절대 위치를 학습하는 방식으로, context_length(1024) × emb_dim(768) 크기의 학습 가능한 행렬이다. 최종 입력 표현은 토큰 임베딩과 위치 임베딩의 합이며, 이것이 transformer 블록으로 전달된다.

**Marker 세부 목차** (`Raschka-BuildLLM_marker_full.md`):
- 2 Working with text data 17 (p.38) `L:74`
- 2.1 Understanding word embeddings (p.39) `L:501`
- 2.2 Tokenizing text (p.42) `L:531`
- 2.3 Converting tokens into token IDs (p.45) `L:667`
- 2.4 Adding special context tokens (p.50) `L:812`
- 2.5 Byte pair encoding (p.54) `L:943`
- 2.6 Data sampling with a sliding window (p.56) `L:1017`
- 2.7 Creating token embeddings (p.62) `L:1273`
- 2.8 Encoding word positions (p.64) `L:1357`


---

### Ch 3: Coding attention mechanisms (pp. 50–91)
**핵심**: 4가지 어텐션 변형을 단계적으로 구현한다: (1) 단순 self-attention, (2) 학습 가능한 가중치를 가진 self-attention(Q, K, V 행렬), (3) causal attention(미래 토큰을 마스킹하여 자기회귀 생성 보장), (4) multi-head attention(여러 head를 병렬로 실행하여 다양한 표현 부분공간의 정보를 동시에 포착). Attention score는 softmax(QK^T / sqrt(d_k)) × V로 계산하며, causal mask는 상삼각 행렬을 -inf로 채워 softmax에서 0으로 만든다. Dropout을 어텐션 가중치에 적용하여 과적합을 방지한다.
**키워드**: `self-attention`, `causal attention`, `multi-head attention`, `QKV`, `dropout`
**상세**: → `Raschka-BuildLLM_marker_full.md` Ch 3 (L:1514)
Self-attention 메커니즘을 단계별로 구현하며, 이전 RNN 기반 모델의 한계(전체 입력을 하나의 hidden state로 압축)를 극복하는 과정을 설명한다. 2014년 Bahdanau attention이 RNN에 선택적 접근을 가능하게 했고, 2017년 transformer는 RNN 없이 self-attention만으로 구성된 아키텍처를 제안했다. 먼저 학습 가능한 가중치 없이 dot product 기반의 단순 self-attention을 구현하여 context vector의 개념을 이해한다. 각 입력 토큰에 대해 다른 모든 토큰과의 attention score를 계산하고, softmax로 정규화하여 attention weight를 얻은 뒤, 입력 벡터의 가중합으로 context vector를 생성한다. 학습 가능한 self-attention에서는 Query(Q), Key(K), Value(V) 가중치 행렬을 도입하여, 입력 x를 각각 q=xW_q, k=xW_k, v=xW_v로 변환한다. Attention score는 softmax(QK^T / sqrt(d_k)) × V로 계산하며, sqrt(d_k) 스케일링은 큰 내적값으로 인한 gradient vanishing을 방지한다. Causal attention은 상삼각 행렬을 -inf로 마스킹하여 softmax에서 미래 토큰의 가중치를 0으로 만들어, 자기회귀 생성 시 미래 정보 유출을 방지한다. Dropout을 attention weight에 적용하여 특정 토큰에 대한 과도한 의존을 방지하고 과적합을 줄인다. CausalAttention 클래스로 causal mask와 dropout이 포함된 self-attention을 하나의 PyTorch 모듈로 구현한다. Multi-head attention은 여러 attention head를 병렬로 실행하여 다양한 표현 부분공간의 정보를 동시에 포착하며, 각 head의 출력을 연결(concatenate)한 뒤 출력 projection을 적용한다. 효율적 구현에서는 하나의 큰 가중치 행렬로 모든 head를 동시에 계산하고 reshape/transpose로 분할한다. GPT-2 124M 모델의 경우 12개 head, 각 head 차원 64(768/12)로 구성된다.

**Marker 세부 목차** (`Raschka-BuildLLM_marker_full.md`):
- 3.1 The problem with modeling long sequences (p.73) `L:1514`
- 3.2 Capturing data dependencies with attention mechanisms (p.75) `L:1542`
- 3.3 Attending to different parts of the input with self-attention (p.76) `L:1562`
- 3.3.1 A simple self-attention mechanism without trainable weights (p.77) `L:1574`
- 3.3.2 Computing attention weights for all input tokens (p.82) `L:1730`
- 3.4 Implementing self-attention with trainable weights (p.85) `L:1853`
- 3.4.1 Computing the attention weights step by step (p.86) `L:1867`
- 3.4.2 Implementing a compact self-attention Python class (p.91) `L:2045`
- 3.5 Hiding future words with causal attention (p.95) `L:2166`
- 3.5.1 Applying a causal attention mask (p.96) `L:2178`
- 3.5.2 Masking additional attention weights with dropout (p.99) `L:2326`
- 3.5.3 Implementing a compact causal attention class (p.101) `L:2385`
- 3.6 Extending single-head attention to multi-head attention (p.103) `L:2482`
- 3.6.2 Implementing multi-head attention with weight splits (p.107) `L:2570`


---

### Ch 4: Implementing a GPT model from scratch to generate text (pp. 92–127)
**핵심**: GPT-2 (124M 파라미터) 아키텍처를 직접 구현한다. 핵심 구성은 Token + Position Embedding → N개 Transformer Block → Final LayerNorm → Linear(vocab_size)이다. Transformer Block은 Pre-LayerNorm 방식으로 LayerNorm → Multi-Head Attention → Residual → LayerNorm → FFN(GELU, 4배 확장) → Residual로 구성된다. GPT_CONFIG_124M 설정: vocab_size=50257, context_length=1024, emb_dim=768, n_heads=12, n_layers=12이다. GPT-2와 GPT-3는 동일한 아키텍처이며 스케일(1.5B → 175B)만 다르다.
**키워드**: `GPT-2`, `transformer block`, `LayerNorm`, `GELU`, `residual connection`
**상세**: → `Raschka-BuildLLM_marker_full.md` Ch 4 (L:2814)
GPT-2 124M 파라미터 모델의 전체 아키텍처를 처음부터 PyTorch로 구현한다. GPT_CONFIG_124M 설정: vocab_size=50257, context_length=1024, emb_dim=768, n_heads=12, n_layers=12, drop_rate=0.1, qkv_bias=False이다. 모델의 전체 구조는 Token Embedding + Position Embedding → Dropout → N개 Transformer Block → Final LayerNorm → Linear(vocab_size)이다. LayerNorm은 각 레이어의 활성화를 정규화하여 학습 안정성을 높이며, Pre-LayerNorm 방식(attention/FFN 이전에 적용)을 사용한다. Feed Forward Network(FFN)는 GELU 활성화 함수를 사용하며, 내부 차원을 4배(768→3072)로 확장한 후 다시 원래 차원으로 축소한다. GELU는 ReLU와 달리 음수 입력에 대해서도 작은 gradient를 허용하여 0 부근에서 부드러운 전환을 제공한다. Shortcut(residual) connection은 레이어의 입력을 출력에 직접 더하여 gradient flow를 개선하고 깊은 네트워크의 학습을 가능하게 한다. Transformer Block은 LayerNorm → Multi-Head Attention → Residual → LayerNorm → FFN → Residual의 순서로 구성된다. GPTModel 클래스에서 12개 transformer block을 순차적으로 쌓고, 최종 LayerNorm 후 Linear layer로 각 위치의 50,257 차원 logit을 출력한다. generate_text_simple 함수로 텍스트 생성을 구현하며, 매 스텝마다 마지막 토큰의 logit에서 argmax로 다음 토큰을 선택한다. GPT-2와 GPT-3는 동일한 아키텍처이며 스케일만 다르고(GPT-3: 96 layers, 175B params), Lambda Labs 추정에 따르면 GPT-3 학습에 단일 V100 GPU로 355년이 소요된다. 124M 모델의 총 파라미터 수를 layer별로 계산하면 약 163M이며, 이 중 weight tying(embedding과 output layer 공유)을 적용하면 124M이 된다.

**Marker 세부 목차** (`Raschka-BuildLLM_marker_full.md`):
- 4.1 Coding an LLM architecture (p.114) `L:2814`
- 4.2 Normalizing activations with layer normalization (p.120) `L:2992`
- 4.3 Implementing a feed forward network with GELU activations (p.126) `L:3160`
- 4.4 Adding shortcut connections (p.130) `L:3273`
- 4.5 Connecting attention and linear layers in a transformer block (p.134) `L:3414`
- 4.6 Coding the GPT model (p.138) `L:3500`
- 4.7 Generating text (p.143) `L:3669`


---

### Ch 5: Pretraining on unlabeled data (pp. 128–168)
**핵심**: Next-token prediction 방식으로 LLM을 사전학습한다. Cross-entropy loss로 예측 분포와 실제 토큰 간 차이를 최소화하며, perplexity(= exp(loss))로 해석한다. AdamW 옵티마이저(lr=0.0004, weight_decay=0.1)를 사용하며, 학습 시 train loss는 9.781에서 0.391로 수렴하지만 validation loss는 6.452에서 정체되어 과적합이 발생한다. Temperature scaling(분포 뾰족함 조절)과 top-k sampling(상위 k개 토큰 중 샘플링) 등 디코딩 전략을 구현한다. OpenAI GPT-2 사전학습 가중치를 직접 구현한 모델에 로딩하는 방법도 다룬다.
**키워드**: `cross-entropy`, `perplexity`, `AdamW`, `temperature`, `top-k sampling`, `pretrained weights`
**상세**: → `Raschka-BuildLLM_marker_full.md` Ch 5 (L:3826)
Next-token prediction 방식으로 GPT-2 모델을 사전학습하는 전체 과정을 구현한다. 학습 전 모델은 무의미한 텍스트("Every effort moves you rentingetic wasn?")를 생성하며, 학습을 통해 coherent한 텍스트 생성 능력을 갖추게 된다. Cross-entropy loss를 사용하여 모델의 예측 확률 분포와 실제 다음 토큰 간의 차이를 최소화하며, perplexity(= exp(loss))로 해석하면 모델이 각 위치에서 고려하는 후보 토큰 수를 직관적으로 이해할 수 있다. 학습용 데이터는 Edith Wharton의 "The Verdict" 단편소설(20,479자)을 사용하며, 90:10 비율로 train/validation을 분할한다. AdamW 옵티마이저(lr=0.0004, weight_decay=0.1)로 학습하며, context_length를 256으로 줄여 소비자 하드웨어에서 실행 가능하게 한다. 학습 루프에서 train loss는 약 9.8에서 0.4로 수렴하지만, validation loss는 약 6.5에서 정체되어 소규모 데이터셋에서의 과적합이 발생한다. Temperature scaling은 logit을 temperature 값으로 나누어 확률 분포의 뾰족함을 조절하며, temperature > 1이면 더 다양하고, < 1이면 더 결정적인 출력을 생성한다. Top-k sampling은 확률이 가장 높은 k개의 토큰만 후보로 남기고 나머지를 -inf로 마스킹하여, 확률이 극히 낮은 비합리적 토큰의 선택을 방지한다. 모델 가중치는 torch.save/torch.load로 저장/로딩하며, optimizer state도 함께 저장하여 학습 재개를 가능하게 한다. OpenAI의 GPT-2 사전학습 가중치를 직접 구현한 모델에 로딩하는 방법을 상세히 다루며, TensorFlow 체크포인트의 가중치를 PyTorch 텐서로 변환하여 대응하는 레이어에 할당한다. 124M, 355M, 774M, 1558M 4개 GPT-2 변형 모두 로딩 가능하며, 사전학습된 모델은 즉시 coherent한 텍스트를 생성한다.

**Marker 세부 목차** (`Raschka-BuildLLM_marker_full.md`):
- 5.1 Evaluating generative text models (p.150) `L:3826`
- 5.1.1 Using GPT to generate text (p.151) `L:3834`
- 5.1.2 Calculating the text generation loss (p.153) `L:3914`
- 5.1.3 Calculating the training and validation set losses (p.161) `L:4176`
- 5.2 Training an LLM (p.167) `L:4392`
- 5.3 Decoding strategies to control randomness (p.172) `L:4600`
- 5.3.1 Temperature scaling (p.173) `L:4634`
- 5.3.2 Top-k sampling (p.176) `L:4757`
- 5.3.3 Modifying the text generation function (p.178) `L:4824`
- 5.4 Loading and saving model weights in PyTorch (p.180) `L:4913`
- 5.5 Loading pretrained weights from OpenAI (p.181) `L:4967`


---

### Ch 6: Fine-tuning for classification (pp. 169–203)
**핵심**: 사전학습된 GPT 모델을 스팸 분류기로 파인튜닝한다. 두 가지 파인튜닝 방식(instruction fine-tuning vs. classification fine-tuning)을 비교하며, classification 방식은 특정 클래스 레이블 예측에 특화되어 더 적은 데이터와 연산으로 학습 가능하다. 원래 출력층(768→50257)을 분류 헤드(768→2)로 교체하며, 마지막 토큰의 hidden state를 분류에 사용한다. 사전학습 모델은 instruction을 따르지 못하므로 classification head를 추가하여 "spam"/"not spam" 이진 분류를 수행한다.
**키워드**: `classification fine-tuning`, `spam detection`, `classification head`, `output layer replacement`
**상세**: → `Raschka-BuildLLM_marker_full.md` Ch 6 (L:5278)
사전학습된 GPT 모델을 스팸 분류기로 파인튜닝하는 전체 과정을 구현한다. Instruction fine-tuning은 다양한 태스크를 수행하는 범용 모델을 만들지만 대규모 데이터와 연산이 필요하고, classification fine-tuning은 특정 분류 태스크에 특화되어 더 적은 리소스로 학습 가능하다. SMS Spam Collection 데이터셋(5,574개 메시지, spam 747개/ham 4,827개)을 사용하며, 클래스 불균형을 해결하기 위해 다수 클래스를 소수 클래스 수에 맞춰 언더샘플링한다. 데이터를 train(70%)/validation(10%)/test(20%)로 분할하고, 배치 내 시퀀스 길이 통일을 위해 가장 긴 시퀀스에 맞춰 패딩 토큰(50256)을 추가한다. custom collate function에서 max_length를 설정하여 지나치게 긴 시퀀스를 잘라내며, 이는 메모리 효율과 학습 안정성을 위함이다. OpenAI GPT-2 사전학습 가중치를 로딩한 뒤, 원래 출력층(768→50257)을 분류 헤드(768→2)로 교체한다. 분류에는 시퀀스의 마지막 토큰의 hidden state만 사용하며, 이 토큰이 전체 시퀀스의 문맥 정보를 집약하고 있기 때문이다. 학습 시 전체 모델을 파인튜닝할 수도 있고, 마지막 transformer block과 분류 헤드만 학습할 수도 있으며, 후자가 더 빠르고 과적합에 강하다. AdamW(lr=5e-5, weight_decay=0.1)로 5 에포크 학습하며, train accuracy 97.5%, validation accuracy 97.5%, test accuracy 95.67%를 달성한다. 최종 모델은 새로운 텍스트 메시지에 대해 "spam" 또는 "not spam"을 예측할 수 있으며, softmax 확률로 예측 확신도를 확인할 수 있다.

**Marker 세부 목차** (`Raschka-BuildLLM_marker_full.md`):
- 6.1 Different categories of fine-tuning (p.191) `L:5278`
- 6.2 Preparing the dataset (p.193) `L:5304`
- 6.3 Creating data loaders (p.196) `L:5477`
- 6.4 Initializing a model with pretrained weights (p.202) `L:5659`
- 6.5 Adding a classification head (p.204) `L:5760`
- 6.6 Calculating the classification loss and accuracy (p.211) `L:5933`
- 6.7 Fine-tuning the model on supervised data (p.216) `L:6114`
- 6.8 Using the LLM as a spam classifier (p.221) `L:6332`


---

### Ch 7: Fine-tuning to follow instructions (pp. 204–250)
**핵심**: Instruction fine-tuning을 통해 LLM이 사람의 지시를 따르도록 학습한다. 데이터는 instruction/input/output 형식의 JSON으로 구성하며, 프롬프트 템플릿("Below is an instruction... ### Instruction: ... ### Response: ...")을 사용한다. 커스텀 collate function으로 패딩 토큰(50256)을 추가하여 배치를 구성하고, 패딩 위치의 loss는 -100 placeholder로 무시한다. 평가는 Ollama를 통해 Llama 3 모델로 0~100점 스코어링하며, 파인튜닝 모델은 평균 50.32점을 달성한다. Preference fine-tuning(DPO)은 선택적 후속 단계로 제시한다.
**키워드**: `instruction fine-tuning`, `prompt template`, `collate function`, `Ollama`, `Llama 3 evaluation`
**상세**: → `Raschka-BuildLLM_marker_full.md` Ch 7 (L:6448)
Instruction fine-tuning을 통해 사전학습된 LLM이 사람의 자연어 지시를 이해하고 원하는 응답을 생성하도록 학습한다. 1,100개의 instruction-response 쌍으로 구성된 JSON 데이터셋을 사용하며, 각 항목은 instruction, input(선택), output 필드로 구성된다. 프롬프트 템플릿("Below is an instruction that describes a task. Write a response... ### Instruction: {instruction} ### Response: {output}")을 사용하여 학습 데이터를 포맷팅한다. input 필드가 있는 경우 "### Input:" 섹션을 추가하여 추가 컨텍스트를 제공한다. 커스텀 collate function으로 배치 내 시퀀스 길이를 통일하며, 패딩 토큰(50256)을 추가하고 instruction 부분의 loss는 -100 placeholder로 마스킹하여 응답 생성 부분만 학습한다. 이 selective loss masking은 모델이 instruction을 단순히 복사하는 것이 아니라 적절한 응답을 생성하는 데 집중하게 한다. 데이터를 train(85%)/validation(5%)/test(10%)로 분할하고, OpenAI GPT-2 355M 사전학습 가중치를 로딩하여 파인튜닝한다. AdamW(lr=0.00005, weight_decay=0.1)로 2 에포크 학습하며, train loss 0.194, validation loss 0.668을 달성한다. 모델 평가는 Ollama를 통해 Llama 3 8B 모델이 0~100점으로 자동 스코어링하며, 파인튜닝 모델은 평균 50.32점을 달성한다. extract_response 함수로 생성된 전체 텍스트에서 "### Response:" 이후 부분만 추출하여 최종 응답으로 사용한다. 추가적인 성능 향상을 위해 DPO(Direct Preference Optimization) 등의 preference fine-tuning 기법을 후속 단계로 제안한다.

**Marker 세부 목차** (`Raschka-BuildLLM_marker_full.md`):
- 7.1 Introduction to instruction fine-tuning (p.226) `L:6448`
- 7.2 Preparing a dataset for supervised instruction fine-tuning (p.228) `L:6462`
- 7.3 Organizing data into training batches (p.232) `L:6635`
- 7.4 Creating data loaders for an instruction dataset (p.244) `L:6975`
- 7.5 Loading a pretrained LLM (p.247) `L:7082`
- 7.6 Fine-tuning the LLM on instruction data (p.250) `L:7196`
- 7.7 Extracting and saving responses (p.254) `L:7334`
- 7.8 Evaluating the fine-tuned LLM (p.259) `L:7508`
- 7.9 Conclusions (p.268) `L:7864`
- 7.9.1 What's next? (p.268) `L:7868`
- 7.9.2 Staying up to date in a fast-moving field (p.269) `L:7878`
- 7.9.3 Final words (p.269) `L:7882`


---

### Appendix A: Introduction to PyTorch (pp. 251–288)
**핵심**: PyTorch 기초(텐서, 자동 미분, GPU 활용)를 다루며, LLM 구현에 필요한 딥러닝 프레임워크 기본기를 제공한다.
**키워드**: `PyTorch`, `tensor`, `autograd`, `GPU`
**상세**: → `Raschka-BuildLLM_marker_full.md` Appendix A (L:7902)
PyTorch의 3가지 핵심 구성요소인 텐서 라이브러리, 자동 미분 엔진(autograd), 딥러닝 유틸리티를 소개한다. AI → Machine Learning → Deep Learning의 계층 구조를 설명하며, LLM이 deep neural network의 한 종류임을 명확히 한다. 텐서는 스칼라(0차원), 벡터(1차원), 행렬(2차원), 다차원 배열의 일반화이며, NumPy 배열과 유사하지만 GPU 가속을 지원한다. 텐서 연산으로 reshape, transpose, matmul 등의 기본 연산과 broadcasting 규칙을 다루며, dtype과 device 관리를 설명한다. Computation graph 개념을 통해 forward pass와 backward pass(역전파)의 관계를 시각화하고, autograd가 gradient를 자동 계산하는 과정을 보여준다. nn.Module을 상속하여 다층 신경망(입력→은닉→출력)을 구현하며, nn.Linear, nn.ReLU 등의 빌딩 블록을 소개한다. Dataset과 DataLoader를 사용하여 데이터를 효율적으로 배치 처리하며, shuffle, drop_last 등의 옵션을 설명한다. 전형적인 학습 루프는 forward pass → loss 계산 → backward pass → optimizer step → zero_grad의 순서로 구성된다. 모델 저장(torch.save)과 로딩(torch.load + load_state_dict)을 다루며, state_dict가 학습 가능한 파라미터의 딕셔너리임을 설명한다. GPU 사용을 위해 .to(device)로 모델과 텐서를 이동하며, torch.cuda.is_available()로 GPU 사용 가능 여부를 확인한다. 다중 GPU 학습을 위해 PyTorch의 DistributedDataParallel(DDP)을 소개하며, torch.distributed를 사용한 설정 방법을 다룬다.

**Marker 세부 목차** (`Raschka-BuildLLM_marker_full.md`):
- appendix A Introduction to PyTorch (p.272) `L:7902`
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


### Appendix D: Adding bells and whistles to the training loop (pp. 313–321)
**핵심**: 학습 루프에 cosine annealing, linear warmup, gradient clipping 등 고급 학습 기법을 추가하는 방법을 다룬다.
**키워드**: `cosine annealing`, `warmup`, `gradient clipping`
**상세**: → `Raschka-BuildLLM_marker_full.md` Appendix D (L:10208)
Chapter 5~7의 학습 루프에 3가지 고급 학습 기법을 추가하여 학습 안정성과 성능을 향상시킨다. Learning rate warmup은 학습 초기에 매우 낮은 learning rate(initial_lr=0.0001)에서 시작하여 지정된 스텝 수(전체의 약 20%) 동안 점진적으로 peak_lr(0.01)까지 증가시키며, 초기에 큰 가중치 업데이트로 인한 불안정을 방지한다. Cosine decay는 warmup 이후 learning rate를 코사인 곡선을 따라 점차 감소시켜 min_lr(initial_lr의 10%)에 도달하게 하며, 학습 후반에 loss minima를 overshoot하는 위험을 줄인다. Gradient clipping은 gradient의 전체 norm이 지정된 max_norm(1.0)을 초과할 때 비례적으로 축소하여 exploding gradient 문제를 방지하며, torch.nn.utils.clip_grad_norm_으로 구현한다. 이 3가지 기법을 결합한 수정된 train_model_simple 함수를 구현하며, optimizer의 param_groups에서 learning rate를 매 스텝마다 동적으로 업데이트한다. 수정된 학습 함수로 GPT-2 124M 모델을 "The Verdict" 데이터셋에서 재학습하면, train loss 0.361, validation loss 6.365를 달성한다. 이 기법들은 대규모 모델 학습에서 표준적으로 사용되며, GPT-3 논문에서도 cosine decay와 warmup을 사용했음을 명시하고 있다.

**Marker 세부 목차** (`Raschka-BuildLLM_marker_full.md`):
- appendix D Adding bells and whistles to the training loop (p.334) `L:10208`
- D.4 The modified training function `L:10490`


### Appendix E: Parameter-efficient fine-tuning with LoRA (pp. 322–336)
**핵심**: LoRA(Low-Rank Adaptation)는 가중치 행렬 W의 업데이트 ΔW를 저랭크 행렬 A, B의 곱으로 근사하여, 소수의 파라미터만 학습한다. rank(내부 차원)와 alpha(스케일링 팩터)가 핵심 하이퍼파라미터이며, A는 Kaiming 초기화, B는 0 초기화한다. 스팸 분류(Ch 6) 및 instruction fine-tuning(Ch 7) 모두에 적용 가능하다.
**키워드**: `LoRA`, `low-rank adaptation`, `parameter-efficient`, `rank`, `alpha`
**상세**: → `Raschka-BuildLLM_marker_full.md` Appendix E (L:10614)
LoRA(Low-Rank Adaptation)는 대규모 모델의 가중치 행렬 W의 업데이트 ΔW를 두 개의 작은 행렬 A와 B의 곱(AB)으로 근사하여, 전체 파라미터 대신 소수의 파라미터만 학습하는 parameter-efficient fine-tuning 기법이다. "low-rank"는 모델 조정을 전체 가중치 공간의 작은 차원 부분공간으로 제한하는 것을 의미하며, rank r이 핵심 하이퍼파라미터로 내부 차원을 결정한다. 수학적으로 W_updated = W + AB이며, 분배법칙에 의해 x(W + AB) = xW + xAB로 분리하여 원본 가중치를 변경하지 않고 LoRA 행렬만 별도로 관리할 수 있다. 이를 통해 하나의 사전학습 모델에 고객/태스크별 LoRA 행렬만 교체하여 사용할 수 있어 저장 공간과 확장성이 크게 개선된다. A 행렬은 Kaiming 초기화(nn.init.kaiming_uniform_)를, B 행렬은 0으로 초기화하여 학습 시작 시 ΔW = AB = 0이 되도록 한다. LoRALayer 클래스를 구현하여 기존 nn.Linear를 대체하며, alpha(스케일링 팩터)를 rank로 나눈 값을 출력에 곱한다. replace_linear_with_lora 함수로 모델 내 모든 Linear 레이어를 자동으로 LoRA 버전으로 교체하며, 원본 가중치는 freeze(requires_grad=False)한다. Chapter 6의 스팸 분류 태스크에 적용하면, rank=8 설정으로 전체 대비 극소수의 파라미터만 학습하면서도 test accuracy 95.67%로 전체 파인튜닝과 동등한 성능을 달성한다. LoRA는 Chapter 7의 instruction fine-tuning에도 동일하게 적용 가능하며, 대규모 모델에서 특히 연산 비용 절감 효과가 크다. rank 값을 높이면 표현력이 증가하지만 학습 파라미터도 늘어나므로, 태스크 복잡도에 맞게 적절히 설정해야 한다.

**Marker 세부 목차** (`Raschka-BuildLLM_marker_full.md`):
- appendix E Parameter-efficient fine-tuning with LoRA (p.343) `L:10614`
- E.4 Parameter-efficient fine-tuning with LoRA `L:10865`


---

## 핵심 하이퍼파라미터 (GPT-2 124M 설정)

| 파라미터 | 값 |
|---|---|
| vocab_size | 50,257 (BPE) |
| context_length | 1,024 |
| emb_dim | 768 |
| n_heads | 12 |
| n_layers | 12 |
| drop_rate | 0.1 |
| qkv_bias | False |


### 기타 섹션 (Marker)

- Build a Large Language Model (From Scratch) `L:13`
- Exercise 2.1 Byte pair encoding of unknown words `L:1011`
- Exercise 2.2 Data loaders with different strides and context sizes (p.60) `L:1217`
- Weight parameters vs. attention weights `L:1923`
- Why query, key, and value? (p.91) `L:2035`
- Exercise 3.1 Comparing SelfAttention\_v1 and SelfAttention\_v2 (p.94) `L:2156`
- Exercise 3.2 Returning two-dimensional embedding vectors (p.106) `L:2564`
- Exercise 3.3 Initializing GPT-2 size attention modules `L:2778`
- Implementing a GPT model from scratch to generate text (p.113) `L:2796`
- Layer normalization vs. batch normalization `L:3154`
- Exercise 4.1 Number of parameters in feed forward and attention modules (p.142) `L:3638`
- Exercise 4.2 Initializing larger GPT models (p.143) `L:3665`
- Exercise 4.3 Using separate dropout parameters `L:3793`
- The cost of pretraining LLMs `L:4188`
- Exercise 6.1 Increasing the context length `L:5585`
- Fine-tuning selected layers vs. all layers `L:5810`
- Exercise 6.2 Fine-tuning the whole model `L:5847`
- The initial loss values are `L:6104`
- Choosing the number of epochs `L:6288`
- Exercise 7.1 Changing prompt styles `L:6543`
- Exercise 7.2 Instruction and input masking `L:6971`
- Exercise 7.3 Fine-tuning on the original Alpaca dataset `L:7328`
- Using larger LLMs via web APIs `L:7520`
- Running the code in a new Python session (p.263) `L:7606`
- Exercise 7.4 Parameter-efficient fine-tuning with LoRA (p.268) `L:7860`
- PyTorch with a NumPy-like API (p.279) `L:8050`
- SELECTING AVAILABLE GPUS ON A MULTI-GPU MACHINE `L:9169`
- Alternative PyTorch APIs for multi-GPU training (p.309) `L:9238`
- Chapter 1 (p.310) `L:9256`
- Chapter 2 `L:9300`
- Chapter 3 `L:9329`
- Chapter 4 `L:9360`
- Chapter 5 `L:9398`
- Chapter 6 `L:9455`
- Chapter 7 `L:9493`
- Appendix A `L:9540`
- On the CPU this resulted in `L:10187`
- Hands-on projects for learning your way `L:11510`

---

## Marker 세부 목차

> `L:숫자`는 `Raschka-BuildLLM_marker_full.md`의 라인 번호.

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
