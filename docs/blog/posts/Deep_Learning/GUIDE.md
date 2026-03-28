---
name: Deep_Learning_GUIDE
type: category
version: 1.0
description: "LOAD when writing posts about neural networks, CNN, RNN, Transformer, NLP, GAN, or reinforcement learning. Covers theory-to-code pipeline with PyTorch implementations and architecture comparisons."
scope: docs/blog/posts/Deep_Learning/
parent: AGENT_GUIDE.md
index: docs/blog/posts/Deep_Learning/index.qmd
book_sources:
  - docs/book/deep_learning/
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
- 추상적이거나 이해하기 어려운 개념에는 비유, 기존 방법과의 비교 등 직관적 설명을 적재적소에 포함한다 (필요시 별도 섹션으로 분리 가능)
- 각 개념 또는 원리에 데이터 사이언스 실무에 어떻게 적용될 수 있는지 설명한다

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

### 3. 왜 필요한가 (Why It Matters)

- 선행 모델의 구체적 한계를 제시한다 (예: RNN의 기울기 소실)
- 이 기법이 해결하는 문제를 명시한다
- 성능 비교(벤치마크)를 포함한다

### 4. 응용 분야 (Applications)

```markdown
| 분야 | 모델 | 구체적 예시 |
|---|---|---|
| 자연어처리 | BERT, GPT | 감성 분석, 기계 번역, 질의응답 |
| 컴퓨터 비전 | ViT, ResNet | 이미지 분류, 객체 탐지 |
| 음성 | Whisper, Wav2Vec | 음성 인식, 화자 분리 |
| 시계열 | Temporal Transformer | 수요 예측, 이상 탐지 |
| 생명과학 | AlphaFold | 단백질 구조 예측 |
```

### 5. 예시 (Examples)

- 소규모 데이터로 순전파/역전파 과정을 단계별로 보여준다
- 차원, 형상(shape) 변화를 명시한다 (예: `[batch, seq_len, d_model]`)

### 6. 코드 예시 (Code Examples)

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

### 7. 관련 주제 (Related Topics)

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

---

## 교재 레퍼런스

이 카테고리의 포스트 작성 시 다음 교재를 **논리적 뼈대**로 활용한다. 교재의 체계를 참고하되, agent의 최신 사전지식으로 outdated된 내용은 수정하고 부족한 부분은 보완한다.

| 교재 | Summary 경로 | 활용 영역 |
|---|---|---|
| Goodfellow et al. — Deep Learning (2016) | `docs/book/deep_learning/Goodfellow-DeepLearning-summary.md` | DL 이론, CNN, RNN, 생성모델 |
| Zhang et al. — Dive into Deep Learning (2023) | `docs/book/deep_learning/Zhang-D2L-summary.md` | DL 실습, PyTorch, Transformer |
| Raschka — Build a Large Language Model (2025) | `docs/book/deep_learning/Raschka-BuildLLM-summary.md` | LLM 구현, Attention, 파인튜닝 |
| Sutton & Barto — Reinforcement Learning (2018) | `docs/book/deep_learning/Sutton-RL-summary.md` | 강화학습, Q-Learning, Policy Gradient |
| Jurafsky & Martin — Speech and Language Processing (2024) | `docs/book/deep_learning/Jurafsky-SLP-summary.md` | NLP, Transformer, 감정분석, 대화시스템 |

**활용 절차**: Summary 읽기 → 논리 구조 파악 → Full MD에서 수식/정의 확인 → 교재 내용 중 유효한 부분은 유지, outdated된 부분은 agent 지식으로 수정·보완 → 블로그 스타일로 재작성 + `(저자, 연도, Ch.N)` 인용

---

## 자주 발생하는 오류 패턴 (fix blocks)

<fix-architecture-without-math>

**WRONG** — 수식 없이 한 줄 비유로 끝내는 설명:

> "Transformer uses attention"
> "Attention은 중요한 부분에 집중하는 메커니즘이다"

**CORRECT** — 수식 → 직관 → 코드 3단계:

1. **수식**: $\text{Attention}(Q,K,V) = \text{softmax}\!\left(\frac{QK^\top}{\sqrt{d_k}}\right)V$
2. **직관**: 왜 $\sqrt{d_k}$로 스케일링하는가? — $d_k$가 클수록 내적 분산이 커져 softmax가 극단값으로 수렴하기 때문이다. 스케일링 없이는 gradient가 사라진다.
3. **코드**: NumPy low-level 구현 → PyTorch `nn.MultiheadAttention` 순서로 제시한다.

아키텍처 설명 시 반드시 이 3단계(수식 → 직관 → 코드)를 거친다. 비유는 직관 단계의 **보조 수단**일 뿐, 수식을 대체하지 않는다.

</fix-architecture-without-math>

<fix-code-without-shapes>

**WRONG** — 텐서 연산 코드만 나열하고 shape 정보가 없는 경우:

```python
q = self.W_q(x).view(B, T, self.n_heads, self.d_k).transpose(1, 2)
attn = (q @ k.transpose(-2, -1)) / (self.d_k ** 0.5)
out = attn @ v
```

**CORRECT** — 각 레이어의 입출력 shape를 주석으로 명시:

```python
# x: [batch, seq_len, d_model] = [32, 128, 512]
q = self.W_q(x)                          # [batch, seq_len, d_model]
q = q.view(B, T, self.n_heads, self.d_k) # [batch, seq_len, n_heads, d_k] = [32, 128, 8, 64]
q = q.transpose(1, 2)                    # [batch, n_heads, seq_len, d_k] = [32, 8, 128, 64]

attn = (q @ k.transpose(-2, -1))         # [batch, n_heads, seq_len, seq_len] = [32, 8, 128, 128]
attn = attn / (self.d_k ** 0.5)          # 스케일링, shape 동일
out = attn @ v                           # [batch, n_heads, seq_len, d_k] = [32, 8, 128, 64]
```

모든 DL 코드 블록에서 **입력 shape → 중간 shape → 출력 shape**를 주석으로 추적한다. 구체적인 숫자 예시(예: `[32, 128, 512]`)를 병기하면 더 좋다.

</fix-code-without-shapes>

---

## 경계 (Boundaries)

<boundaries>

### CAN (이 카테고리에서 해야 하는 것)

- 교재 기반 수학적 유도 (손실 함수 미분, backprop chain rule 전개 등)
- PyTorch 구현 (모델 정의 → 학습 루프 → 평가 파이프라인)
- 아키텍처 비교표 (파라미터 수, 연산 복잡도, 장단점을 표로 정리)
- **low-level → 프레임워크 2단계 코드**: NumPy/순수 Python으로 원리 구현 → PyTorch로 실무 코드
- 텐서 shape 변환 추적 (입력부터 출력까지 모든 중간 shape 명시)
- 선행 모델 한계 → 새 모델 해결 방식의 동기 서술

### CANNOT (이 카테고리에서 하지 말아야 하는 것)

- 수식 없이 "attention은 중요한 부분에 집중하는 것" 식의 비유만으로 설명하는 것
- shape 주석 없는 텐서 연산 코드
- 아키텍처 이름만 나열하고 내부 구조를 분해하지 않는 것
- low-level 구현 없이 프레임워크 API 호출만으로 끝내는 것

</boundaries>
