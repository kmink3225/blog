---
name: Deep_Learning_GUIDE
type: category
version: 1.0
description: Deep Learning 카테고리 포스트 작성 규칙 — 수학+코드 하이브리드, NLP, 아키텍처 중심
scope: docs/blog/posts/Deep_Learning/
parent: AGENT_GUIDE.md
index: docs/blog/posts/Deep_Learning/index.qmd
book_sources: []
cross_references:
  - docs/blog/posts/Math/GUIDE.md
  - docs/blog/posts/Statistics/GUIDE.md
  - docs/blog/posts/Machine_Learning/GUIDE.md
  - docs/blog/posts/Agent/GUIDE.md
---

# Deep Learning 카테고리 작성 가이드

> 이 문서는 `AGENT_GUIDE.md`의 공통 규칙을 보충하는 **Deep Learning 전용 가이드**이다.
> 공통 규칙(YAML 헤더, 한다 체, index.qmd 패턴 등)은 `AGENT_GUIDE.md`를 따른다.

---

## 카테고리 특성

- **수학 + 코드 하이브리드**: 수식으로 원리를 설명하고 PyTorch 코드로 구현한다
- **아키텍처 중심**: 모델 구조(CNN, RNN, Transformer 등)를 시각적으로 분해한다
- **NLP 시리즈가 핵심**: 31개 파일로 구성된 NLP 시리즈가 가장 큰 비중을 차지한다
- **종단 데이터 연계**: Statistics/Machine_Learning 카테고리와 크로스 레퍼런스가 많다
- **한국어/영어 병기**: 핵심 용어는 `한국어(English)` 형태로 처음 등장 시 병기한다

---

## 포스트 콘텐츠 구조

### 1. 정의 (Definition)

- 모델/기법의 공식적 정의를 callout 블록으로 제시한다
- 입력, 출력, 파라미터를 명확히 한다

```markdown
::: {.callout-note}
## 정의: Self-Attention

Self-Attention은 시퀀스 내 모든 위치 쌍 간의 관련도를 계산하는 메커니즘이다.

$$
\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^\top}{\sqrt{d_k}}\right)V
$$

- $Q, K, V$: 각각 Query, Key, Value 행렬 ($\mathbb{R}^{n \times d_k}$)
- $d_k$: Key 벡터의 차원 (스케일링 팩터)
:::
```

### 2. 개념 및 원리 (Concept & Principles)

- 모델 아키텍처를 컴포넌트 단위로 분해한다
- 순전파(forward pass)와 역전파(backpropagation)의 수학적 과정을 설명한다
- 기존 방법의 한계 → 새로운 방법의 해결 방식으로 동기를 제시한다
- ASCII 다이어그램 또는 Mermaid로 구조를 시각화한다

```markdown
## Transformer 아키텍처

```
입력 토큰 → Embedding + Positional Encoding
    ↓
┌─────────────────────────┐
│   Multi-Head Attention  │ ← Self-Attention × h개 헤드
│   Add & Layer Norm      │
│   Feed Forward          │
│   Add & Layer Norm      │
└─────────────────────────┘ × N layers
    ↓
출력 확률 분포
```
```

### 3. 직관적 설명 (Intuitive Explanation)

- 수식 없이 핵심 아이디어를 전달한다
- 기존 방법과의 비교를 통해 차이를 명확히 한다

```markdown
> **직관**: RNN이 책을 한 글자씩 순서대로 읽는 사람이라면,
> Transformer는 책 전체를 한눈에 펼쳐놓고 관련 있는 부분끼리 연결하는 사람이다.
> 순서에 의존하지 않으므로 병렬 처리가 가능하고, 먼 거리의 단어 간 관계도 직접 파악할 수 있다.
```

### 4. 왜 필요한가 (Why It Matters)

- 선행 모델의 구체적 한계를 제시한다 (예: RNN의 기울기 소실)
- 이 기법이 해결하는 문제를 명시한다
- 성능 비교(벤치마크)를 포함한다

### 5. 응용 분야 (Applications)

```markdown
| 분야 | 모델 | 구체적 예시 |
|---|---|---|
| 자연어처리 | BERT, GPT | 감성 분석, 기계 번역, 질의응답 |
| 컴퓨터 비전 | ViT, ResNet | 이미지 분류, 객체 탐지 |
| 음성 | Whisper, Wav2Vec | 음성 인식, 화자 분리 |
| 시계열 | Temporal Transformer | 수요 예측, 이상 탐지 |
| 생명과학 | AlphaFold | 단백질 구조 예측 |
```

### 6. 예시 (Examples)

- 소규모 데이터로 순전파/역전파 과정을 단계별로 보여준다
- 차원, 형상(shape) 변화를 명시한다 (예: `[batch, seq_len, d_model]`)

### 7. 코드 예시 (Code Examples)

- **2단계 구성**: (1) 순수 Python/NumPy로 알고리즘 원리를 구현 → (2) PyTorch로 실무 코드 제시
- 패키지: `numpy` (low-level), `torch`, `torch.nn`, `transformers` (Hugging Face), `torchvision`
- 모델 정의 → 학습 루프 → 평가 순서를 따른다
- 텐서 shape을 주석으로 표기한다

```markdown
#### Step 1: NumPy 구현 (원리 이해)

```python
import numpy as np

def self_attention(X, W_q, W_k, W_v):
    """
    순수 NumPy로 Self-Attention 구현 — 행렬 연산의 원리를 직접 확인
    X: [seq_len, d_model]
    """
    Q = X @ W_q  # [seq_len, d_k] — Query 생성
    K = X @ W_k  # [seq_len, d_k] — Key 생성
    V = X @ W_v  # [seq_len, d_v] — Value 생성

    d_k = K.shape[-1]
    scores = Q @ K.T / np.sqrt(d_k)  # [seq_len, seq_len] — 유사도 점수

    # softmax (수치 안정성을 위해 max를 뺌)
    scores_exp = np.exp(scores - scores.max(axis=-1, keepdims=True))
    attn_weights = scores_exp / scores_exp.sum(axis=-1, keepdims=True)

    output = attn_weights @ V  # [seq_len, d_v] — 가중 합
    return output, attn_weights

# 예시: seq_len=3, d_model=4
np.random.seed(42)
X = np.random.randn(3, 4)
W_q = np.random.randn(4, 4)
W_k = np.random.randn(4, 4)
W_v = np.random.randn(4, 4)

out, weights = self_attention(X, W_q, W_k, W_v)
print(f"Attention weights:\n{weights.round(3)}")
print(f"Output shape: {out.shape}")
```

#### Step 2: PyTorch 구현 (실무 활용)

```python
import torch
import torch.nn as nn

class SelfAttention(nn.Module):
    def __init__(self, d_model, n_heads):
        super().__init__()
        self.n_heads = n_heads
        self.d_k = d_model // n_heads
        self.W_q = nn.Linear(d_model, d_model)
        self.W_k = nn.Linear(d_model, d_model)
        self.W_v = nn.Linear(d_model, d_model)

    def forward(self, x):
        # x: [batch, seq_len, d_model]
        B, T, C = x.shape
        q = self.W_q(x).view(B, T, self.n_heads, self.d_k).transpose(1, 2)
        k = self.W_k(x).view(B, T, self.n_heads, self.d_k).transpose(1, 2)
        v = self.W_v(x).view(B, T, self.n_heads, self.d_k).transpose(1, 2)
        # [batch, n_heads, seq_len, d_k]

        attn = (q @ k.transpose(-2, -1)) / (self.d_k ** 0.5)
        attn = torch.softmax(attn, dim=-1)
        out = attn @ v  # [batch, n_heads, seq_len, d_k]
        return out.transpose(1, 2).contiguous().view(B, T, C)
```
```

### 8. 관련 주제 (Related Topics)

- 포스트 끝에 관련 개념과 블로그 내 링크를 목록으로 제시한다
- 선행 지식(prerequisite)과 후속 주제(next)를 구분한다
- **파일이 아직 존재하지 않더라도 논리적으로 필요한 주제는 placeholder 링크로 포함한다.** 이를 통해 향후 채워야 할 콘텐츠를 체계적으로 파악할 수 있다. Placeholder 링크는 경로를 미리 지정하되, 해당 파일이 생성되면 자연스럽게 연결된다.

```markdown
## 관련 주제

**선행 지식**

- [선형대수: 행렬 곱](../../Math/linear_algebra/05.matrix_multiplication.qmd)
- [최적화: 경사하강법](../../Math/optimization.qmd) ← 파일 미존재, placeholder

**후속 주제**

- [BERT와 사전학습](./NLP/22.plm_bert.qmd)
- [LLM의 구조적 한계](./NLP/31.llm-structural-limitations.qmd)

**다른 카테고리 연결**

- [임베딩과 벡터 저장소](../Agent/08-Embeddings/) — DL 임베딩의 RAG 활용
- [종단 데이터 DL](./13-mixed-model-dl-longitudinal.qmd) — Statistics 크로스 레퍼런스
```

---

## 하위 카테고리별 추가 지침

### NLP (NLP/)

- 31개 파일로 구성된 핵심 시리즈이다
- 파일명 패턴: `번호.토픽명.qmd` (예: `1.nlp_overview.qmd`, `20.transformer.qmd`)
- 전처리(토큰화) → 벡터화(TF-IDF, Word2Vec) → 신경망(RNN, LSTM) → Transformer → PLM(BERT, GPT) → LLM 순서를 따른다
- Hugging Face `transformers` 라이브러리 활용 코드를 포함한다

### CNN (cnn/)

- 합성곱 연산의 수학적 정의와 시각적 설명을 병행한다
- 커널, 스트라이드, 패딩, 풀링 등 기본 연산을 상세히 다룬다

### 종단 데이터 DL (루트 레벨 13~31번 파일)

- Statistics/LDA 시리즈와 크로스 레퍼런스된다
- LSTM, TCN, Temporal Transformer, Neural ODE를 다룬다
- 통계 모델(Mixed Model)과의 비교를 항상 포함한다
- 파일명 패턴: `번호-mixed-model-dl-토픽.qmd`

---

## 수식 작성 규칙

- Statistics/Math 카테고리와 동일한 표기법을 따른다
- 텐서 shape은 `[batch, seq_len, d_model]` 형태로 대괄호 표기한다
- 손실 함수, 활성화 함수 등은 정의와 그래프를 함께 제시한다
- 기울기(gradient) 유도 시 chain rule 단계를 명시한다
