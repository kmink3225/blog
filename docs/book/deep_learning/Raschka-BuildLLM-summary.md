---
name: "Build a Large Language Model (From Scratch)"
type: book-summary
source_file: "Raschka-BuildLLM_full.md"
authors: "Sebastian Raschka"
year: 2025
total_pages: 337
language: en
keywords: [LLM, GPT, transformer, attention, pretraining, fine-tuning, tokenization, PyTorch, LoRA, instruction-tuning]
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

### Ch 1: Understanding large language models (pp. 1–16)
**핵심**: LLM은 transformer 아키텍처 기반의 대규모 딥러닝 모델로, next-word prediction을 통해 학습한다. "large"는 모델 파라미터 수(수십~수백억)와 학습 데이터 규모 양쪽을 의미한다. 이전 NLP 모델이 특정 태스크에 특화되었던 반면, LLM은 광범위한 NLP 태스크에서 범용적 역량을 보인다. 본 책은 ChatGPT와 같은 GPT 기반 LLM을 단계별로 직접 구현하는 것을 목표로 한다. LLM 개발은 Stage 1(데이터 준비 + 아키텍처), Stage 2(사전학습), Stage 3(파인튜닝)의 3단계로 구성된다.
**키워드**: `LLM`, `transformer`, `next-word prediction`, `GPT`, `decoder-only`
**상세**: → `source_file` Ch 1 (line 645)

---

### Ch 2: Working with text data (pp. 17–49)
**핵심**: 텍스트를 LLM에 입력하기 위해 토큰화(tokenization) → 정수 ID 변환 → 임베딩 벡터 변환의 파이프라인을 구현한다. BPE(Byte Pair Encoding)는 GPT 계열에서 사용하는 서브워드 토큰화 방식으로, 어휘 외 단어(OOV) 문제를 해결한다. 슬라이딩 윈도우 방식으로 학습용 입력-출력 쌍을 생성하며, 최종 입력은 토큰 임베딩과 위치 임베딩(positional embedding)의 합으로 구성된다. Word2Vec 등 기존 임베딩과 달리, LLM은 학습 과정에서 임베딩을 함께 학습한다.
**키워드**: `BPE`, `tokenization`, `embedding`, `sliding window`, `positional encoding`
**상세**: → `source_file` Ch 2 (line 1589)

---

### Ch 3: Coding attention mechanisms (pp. 50–91)
**핵심**: 4가지 어텐션 변형을 단계적으로 구현한다: (1) 단순 self-attention, (2) 학습 가능한 가중치를 가진 self-attention(Q, K, V 행렬), (3) causal attention(미래 토큰을 마스킹하여 자기회귀 생성 보장), (4) multi-head attention(여러 head를 병렬로 실행하여 다양한 표현 부분공간의 정보를 동시에 포착). Attention score는 softmax(QK^T / sqrt(d_k)) × V로 계산하며, causal mask는 상삼각 행렬을 -inf로 채워 softmax에서 0으로 만든다. Dropout을 어텐션 가중치에 적용하여 과적합을 방지한다.
**키워드**: `self-attention`, `causal attention`, `multi-head attention`, `QKV`, `dropout`
**상세**: → `source_file` Ch 3 (line 3860)

---

### Ch 4: Implementing a GPT model from scratch to generate text (pp. 92–127)
**핵심**: GPT-2 (124M 파라미터) 아키텍처를 직접 구현한다. 핵심 구성은 Token + Position Embedding → N개 Transformer Block → Final LayerNorm → Linear(vocab_size)이다. Transformer Block은 Pre-LayerNorm 방식으로 LayerNorm → Multi-Head Attention → Residual → LayerNorm → FFN(GELU, 4배 확장) → Residual로 구성된다. GPT_CONFIG_124M 설정: vocab_size=50257, context_length=1024, emb_dim=768, n_heads=12, n_layers=12이다. GPT-2와 GPT-3는 동일한 아키텍처이며 스케일(1.5B → 175B)만 다르다.
**키워드**: `GPT-2`, `transformer block`, `LayerNorm`, `GELU`, `residual connection`
**상세**: → `source_file` Ch 4 (line 7049)

---

### Ch 5: Pretraining on unlabeled data (pp. 128–168)
**핵심**: Next-token prediction 방식으로 LLM을 사전학습한다. Cross-entropy loss로 예측 분포와 실제 토큰 간 차이를 최소화하며, perplexity(= exp(loss))로 해석한다. AdamW 옵티마이저(lr=0.0004, weight_decay=0.1)를 사용하며, 학습 시 train loss는 9.781에서 0.391로 수렴하지만 validation loss는 6.452에서 정체되어 과적합이 발생한다. Temperature scaling(분포 뾰족함 조절)과 top-k sampling(상위 k개 토큰 중 샘플링) 등 디코딩 전략을 구현한다. OpenAI GPT-2 사전학습 가중치를 직접 구현한 모델에 로딩하는 방법도 다룬다.
**키워드**: `cross-entropy`, `perplexity`, `AdamW`, `temperature`, `top-k sampling`, `pretrained weights`
**상세**: → `source_file` Ch 5 (line 9533)

---

### Ch 6: Fine-tuning for classification (pp. 169–203)
**핵심**: 사전학습된 GPT 모델을 스팸 분류기로 파인튜닝한다. 두 가지 파인튜닝 방식(instruction fine-tuning vs. classification fine-tuning)을 비교하며, classification 방식은 특정 클래스 레이블 예측에 특화되어 더 적은 데이터와 연산으로 학습 가능하다. 원래 출력층(768→50257)을 분류 헤드(768→2)로 교체하며, 마지막 토큰의 hidden state를 분류에 사용한다. 사전학습 모델은 instruction을 따르지 못하므로 classification head를 추가하여 "spam"/"not spam" 이진 분류를 수행한다.
**키워드**: `classification fine-tuning`, `spam detection`, `classification head`, `output layer replacement`
**상세**: → `source_file` Ch 6 (line 12429)

---

### Ch 7: Fine-tuning to follow instructions (pp. 204–250)
**핵심**: Instruction fine-tuning을 통해 LLM이 사람의 지시를 따르도록 학습한다. 데이터는 instruction/input/output 형식의 JSON으로 구성하며, 프롬프트 템플릿("Below is an instruction... ### Instruction: ... ### Response: ...")을 사용한다. 커스텀 collate function으로 패딩 토큰(50256)을 추가하여 배치를 구성하고, 패딩 위치의 loss는 -100 placeholder로 무시한다. 평가는 Ollama를 통해 Llama 3 모델로 0~100점 스코어링하며, 파인튜닝 모델은 평균 50.32점을 달성한다. Preference fine-tuning(DPO)은 선택적 후속 단계로 제시한다.
**키워드**: `instruction fine-tuning`, `prompt template`, `collate function`, `Ollama`, `Llama 3 evaluation`
**상세**: → `source_file` Ch 7 (line 14711)

---

### Appendix A: Introduction to PyTorch (pp. 251–288)
**핵심**: PyTorch 기초(텐서, 자동 미분, GPU 활용)를 다루며, LLM 구현에 필요한 딥러닝 프레임워크 기본기를 제공한다.
**키워드**: `PyTorch`, `tensor`, `autograd`, `GPU`
**상세**: → `source_file` Appendix A (line 17779)

### Appendix D: Adding bells and whistles to the training loop (pp. 313–321)
**핵심**: 학습 루프에 cosine annealing, linear warmup, gradient clipping 등 고급 학습 기법을 추가하는 방법을 다룬다.
**키워드**: `cosine annealing`, `warmup`, `gradient clipping`
**상세**: → `source_file` Appendix D (line 21442)

### Appendix E: Parameter-efficient fine-tuning with LoRA (pp. 322–336)
**핵심**: LoRA(Low-Rank Adaptation)는 가중치 행렬 W의 업데이트 ΔW를 저랭크 행렬 A, B의 곱으로 근사하여, 소수의 파라미터만 학습한다. rank(내부 차원)와 alpha(스케일링 팩터)가 핵심 하이퍼파라미터이며, A는 Kaiming 초기화, B는 0 초기화한다. 스팸 분류(Ch 6) 및 instruction fine-tuning(Ch 7) 모두에 적용 가능하다.
**키워드**: `LoRA`, `low-rank adaptation`, `parameter-efficient`, `rank`, `alpha`
**상세**: → `source_file` Appendix E (line 21966)

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
