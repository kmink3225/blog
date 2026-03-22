---
name: "Speech and Language Processing, 3rd Ed."
type: book-summary
authors: "Daniel Jurafsky, James H. Martin"
year: 2026
total_pages: 611
language: en
keywords: [NLP, large language models, transformers, BERT, speech recognition, TTS, parsing, information extraction, coreference, sentiment analysis, machine translation, RAG]
sources:
  - file: "Jurafsky-SLP_marker_full.md"
    tool: Marker
---

# Speech and Language Processing, 3rd Ed. — Summary

> Daniel Jurafsky, James H. Martin (3rd ed. draft, Jan 2026), 611 pages, 25 chapters
> 자연어 처리, 전산 언어학, 음성 인식을 대규모 언어 모델 중심으로 재구성한 종합 교과서이다

## Contents

### Part I: Large Language Models
- Ch 1: Introduction
- Ch 2: Words and Tokens
- Ch 3: N-gram Language Models
- Ch 4: Logistic Regression
- Ch 5: Embeddings
- Ch 6: Neural Networks
- Ch 7: Large Language Models
- Ch 8: Transformers
- Ch 9: Masked Language Models
- Ch 10: Post-training: Instruction Tuning, Alignment, and Test-Time Compute
- Ch 11: Retrieval-based Models
- Ch 12: Machine Translation
- Ch 13: RNNs and LSTMs
- Ch 14: Phonetics and Speech Feature Extraction
- Ch 15: Automatic Speech Recognition

### Part II: Annotating Linguistic Structure
- Ch 16: Text-to-Speech
- Ch 17: Sequence Labeling for Parts of Speech and Named Entities
- Ch 18: Context-Free Grammars and Constituency Parsing
- Ch 19: Dependency Parsing
- Ch 20: Information Extraction: Relations, Events, and Time
- Ch 21: Semantic Role Labeling
- Ch 22: Lexicons for Sentiment, Affect, and Connotation
- Ch 23: Coreference Resolution and Entity Linking
- Ch 24: Discourse Coherence
- Ch 25: Conversation and its Structure

---

## Chapter Summaries

> Marker 원본: `Jurafsky-SLP_marker_full.md` | 총 ~17,811 라인 | `L:숫자`로 직접 접근 가능


### Ch 1: Introduction (p. 3)
**핵심**: NLP, 전산 언어학, 음성 인식 분야의 전체 개관을 제공한다. 이 책이 대규모 언어 모델을 중심으로 재구성되었음을 밝힌다.
**키워드**: `NLP`, `computational linguistics`, `speech recognition`, `language models`
**상세**: → `Jurafsky-SLP_marker_full.md` Ch 1 (L:304)
이 책은 자연어 처리(NLP), 전산 언어학, 음성 인식 분야의 전체 개관을 제공하는 종합 교과서이다. 3판에서는 대규모 언어 모델(LLM)을 중심으로 전체 구조가 재구성되었다. Part I에서는 토큰화, n-그램, 로지스틱 회귀, 임베딩, 신경망, 트랜스포머, BERT, 포스트트레이닝, RAG, 기계 번역, RNN/LSTM, 음성 인식/합성을 다룬다. Part II에서는 시퀀스 레이블링, 구문 분석, 의존 파싱, 정보 추출, 의미역 분석, 감성 사전, 상호 참조 해결, 담화 일관성, 대화 구조를 다룬다. 인코더, 디코더, 인코더-디코더의 세 가지 LM 아키텍처를 비교하고 각각의 적용 과제를 설명한다. 전통적 통계 기법부터 최신 딥러닝 접근법까지 통합적으로 제시하며, 각 주제에 대해 수학적 기초와 실용적 응용을 균형 있게 다룬다. 언어의 시간적 특성, 형태론적 다양성, 언어 간 유형론적 차이도 중요하게 다룬다

### Ch 2: Words and Tokens (pp. 4-37)
**핵심**: 단어의 정의와 형태소 분석부터 시작하여 유니코드 처리를 설명한다. BPE(Byte-Pair Encoding) 서브워드 토크나이제이션을 상세히 다루고, 코퍼스 구성, 정규 표현식, 최소 편집 거리(edit distance)를 설명한다.
**키워드**: `BPE`, `tokenization`, `Unicode`, `morphemes`, `edit distance`, `regular expressions`
**상세**: → `Jurafsky-SLP_marker_full.md` Ch 2 (L:314)
단어의 정의와 형태소(morpheme) 개념에서 출발하여 텍스트 처리의 기초를 다진다. ELIZA 시스템을 통해 패턴 매칭 기반 대화의 역사적 맥락을 소개한다. 유니코드(Unicode)와 UTF-8 인코딩을 설명하고 다국어 텍스트 처리의 기반을 제공한다. BPE(Byte-Pair Encoding) 서브워드 토크나이제이션 알고리즘을 단계별로 상세히 설명하며, 이것이 현대 LLM의 표준 토큰화 방법임을 보여준다. 코퍼스(corpus) 구성과 단어 빈도 분석을 위한 Unix 도구 활용법을 실습한다. 정규 표현식(regular expressions)의 문법과 활용을 체계적으로 제시한다. 규칙 기반 토큰화(Penn Treebank 표준)와 데이터 기반 토큰화를 비교한다. 접어(clitic) 처리, 다단어 표현, 언어별 토큰화 차이를 설명한다. 최소 편집 거리(minimum edit distance) 알고리즘을 동적 프로그래밍으로 유도하고, 이것이 ASR의 WER 평가에 활용됨을 보인다. 셰익스피어 코퍼스를 예시로 단어 빈도 분포와 Zipf 법칙을 소개한다

**Marker 세부 목차** (`Jurafsky-SLP_marker_full.md`):
- 2.2 Morphemes: Parts of Words `L:437`
- 2.3 Unicode `L:487`
- 2.4 Subword Tokenization: Byte-Pair Encoding (p.20) `L:595`
- 2.6 Regular Expressions `L:817`
- 2.6.5 A Simple Example `L:953`
- 2.7 Simple Unix Tools for Word Tokenization `L:1123`
- 2.8 Rule-based tokenization `L:1187`
- 2.9 Minimum Edit Distance `L:1244`
- 2.10 Summary `L:1357`


### Ch 3: N-gram Language Models (pp. 38-61)
**핵심**: N-그램 언어 모델의 기본 원리를 소개한다. 훈련/테스트 셋 분리, 퍼플렉시티 평가, 문장 샘플링을 설명한다. 일반화 vs 과적합 문제에 대해 스무딩, 보간, 백오프 기법을 제시한다. 퍼플렉시티와 엔트로피의 관계를 유도한다.
**키워드**: `n-gram`, `perplexity`, `smoothing`, `interpolation`, `entropy`
**상세**: → `Jurafsky-SLP_marker_full.md` Ch 3 (L:1436)
N-그램 언어 모델의 기본 원리를 확률의 연쇄 법칙(chain rule)으로부터 유도한다. 마르코프 가정(Markov assumption)을 도입하여 바이그램, 트라이그램, 일반 n-그램으로 확장한다. 최대우도추정(MLE)을 통해 n-그램 확률을 코퍼스 빈도로부터 계산하는 방법을 예시와 함께 설명한다. 훈련 셋과 테스트 셋 분리의 중요성과 미등장(unseen) n-그램 문제를 다룬다. 퍼플렉시티(perplexity)를 언어 모델 평가 지표로 정의하고 계산법을 보인다. 문장 샘플링을 통해 언어 모델의 품질을 직관적으로 평가하는 방법을 설명한다. 일반화와 과적합(overfitting) 사이의 긴장 관계를 n-그램 크기별로 비교한다. 라플라스 스무딩, 보간(interpolation), 백오프(backoff) 기법을 제시하여 영의 확률 문제를 해결한다. Kneser-Ney 스무딩의 직관과 수식을 상세히 유도한다. 퍼플렉시티와 엔트로피의 수학적 관계를 정보 이론 관점에서 증명한다

**Marker 세부 목차** (`Jurafsky-SLP_marker_full.md`):
- 3.1 N-Grams `L:1436`
- 3.2 Evaluating Language Models: Training and Test Sets `L:1621`
- 3.3 Evaluating Language Models: Perplexity `L:1659`
- 3.4 Sampling sentences from a language model `L:1743`
- 3.5 Generalizing vs. overfitting the training set `L:1759`
- 3.6 Smoothing, Interpolation, and Backoff `L:1793`
- 3.7 Advanced: Perplexity's Relation to Entropy `L:1948`
- 3.8 Summary `L:2053`


### Ch 4: Logistic Regression (pp. 62-95)
**핵심**: 머신러닝 분류의 기본 모델로 로지스틱 회귀를 소개한다. 시그모이드 함수, 교차 엔트로피 손실, 경사 하강법을 설명한다. 다항 로지스틱 회귀(소프트맥스)로 확장하고, 정밀도/재현율/F-measure, 교차 검증, 통계적 유의성 검정, 정규화를 다룬다. 분류기의 해석 가능성과 편향 회피 문제를 논의한다.
**키워드**: `logistic regression`, `cross-entropy`, `gradient descent`, `softmax`, `F-measure`, `regularization`
**상세**: → `Jurafsky-SLP_marker_full.md` Ch 4 (L:2164)
머신러닝 분류의 기본 모델로 로지스틱 회귀를 소개하며, 관찰(observation), 특징(feature), 클래스(class)의 개념을 정의한다. 감성 분석과 언어 식별을 예시 과제로 사용한다. 시그모이드 함수를 가중합에 적용하여 확률을 출력하는 과정을 수식으로 유도한다. 가중치(weight)와 편향(bias)의 역할, 내적(dot product) 표기법을 설명한다. 교차 엔트로피(cross-entropy) 손실 함수를 정의하고, 이를 최소화하는 학습 원리를 제시한다. 확률적 경사 하강법(SGD)의 알고리즘을 단계별로 설명하고, 학습률과 배치 크기의 영향을 논의한다. 다항 로지스틱 회귀(소프트맥스)로 확장하여 다중 클래스 분류를 다룬다. 정밀도(precision), 재현율(recall), F-measure 평가 지표를 정의하고 혼동 행렬과 매크로/마이크로 평균을 설명한다. 교차 검증(cross-validation)과 통계적 유의성 검정(부트스트랩, 순열 검정)을 다룬다. 분류기의 편향 회피와 해석 가능성, L1/L2 정규화를 논의하며 경사 방정식의 수학적 유도를 부록으로 제공한다

**Marker 세부 목차** (`Jurafsky-SLP_marker_full.md`):
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


### Ch 5: Embeddings (pp. 96-119)
**핵심**: 어휘 의미론에서 출발하여 벡터 의미론의 직관을 설명한다. 빈도 기반 임베딩(공기행렬, TF-IDF, PPMI)과 코사인 유사도를 다룬다. Word2vec(Skip-gram)의 학습 원리를 설명하고, 임베딩의 의미적 속성, 편향 문제, 시각화 방법을 논의한다.
**키워드**: `word2vec`, `cosine similarity`, `TF-IDF`, `PPMI`, `embedding bias`, `vector semantics`
**상세**: → `Jurafsky-SLP_marker_full.md` Ch 5 (L:3157)
어휘 의미론(lexical semantics)에서 출발하여 레마(lemma), 단어 의미(word sense), 다의성(polysemy), 동의어(synonym), 유사성(similarity), 관련성(relatedness)의 개념을 체계적으로 정의한다. 의미장(semantic field)과 함축(connotation)의 3차원 모델(쾌락가, 각성도, 지배도)을 소개하며, 이것이 벡터 의미론의 기원임을 설명한다. 분포 가설(distributional hypothesis)에 기반한 벡터 의미론의 직관을 ongchoi(공심채) 예시로 설명한다. 빈도 기반 임베딩으로 공기 행렬(co-occurrence matrix), TF-IDF 가중치, PPMI(Positive Pointwise Mutual Information)를 다룬다. 코사인 유사도를 벡터 간 의미적 유사성 측정 도구로 정의하고 계산법을 보인다. Word2vec Skip-gram 모델의 학습 원리를 분류기 관점에서 설명하며, 네거티브 샘플링을 통한 효율적 학습을 다룬다. 임베딩의 의미적 속성(유추 관계, 선형 부분 구조)을 분석한다. 임베딩에 내재된 성별, 인종 편향 문제와 디바이어싱(debiasing) 기법을 논의한다. t-SNE 등을 이용한 임베딩 시각화 방법을 소개한다. SimLex-999 등의 평가 데이터셋으로 벡터 모델의 품질을 평가하는 방법을 제시한다

**Marker 세부 목차** (`Jurafsky-SLP_marker_full.md`):
- 5.1 Lexical Semantics `L:3157`
- 5.2 Vector Semantics: The Intuition `L:3235`
- 5.3 Simple count-based embeddings `L:3273`
- 5.4 Cosine for measuring similarity `L:3341`
- 5.5 Word2vec `L:3401`
- 5.6 Visualizing Embeddings `L:3584`
- 5.8 Bias and Embeddings `L:3654`
- 5.9 Evaluating Vector Models `L:3672`
- 5.10 Summary `L:3686`


### Ch 6: Neural Networks (pp. 120-145)
**핵심**: 뉴럴 유닛(ReLU, sigmoid, tanh)과 XOR 문제를 통해 비선형성의 필요성을 보여준다. 순전파 신경망의 구조를 정의하고, NLP 분류와 임베딩 입력 활용법을 설명한다. 역전파, 드롭아웃, 정규화 등 학습 기법을 다룬다.
**키워드**: `feedforward network`, `backpropagation`, `XOR`, `dropout`, `NLP classification`
**상세**: → `Jurafsky-SLP_marker_full.md` Ch 6 (L:3766)
뉴럴 유닛(neural unit)의 기본 구조를 가중합과 비선형 활성화 함수로 정의한다. 시그모이드, tanh, ReLU 세 가지 활성화 함수의 수학적 정의와 각각의 장단점을 비교한다. ReLU가 기울기 소실 문제(vanishing gradient problem)를 완화하는 이유를 설명한다. XOR 문제를 통해 단일 뉴런의 한계와 비선형성의 필요성, 히든 레이어의 역할을 증명한다. 순전파 신경망(feedforward neural network)의 다층 구조를 행렬 표기법으로 정의한다. NLP 분류 과제에 순전파 네트워크를 적용하는 방법을 감성 분석 예시로 설명한다. 사전 학습된 임베딩을 신경망 입력으로 사용하는 방법과 임베딩 레이어의 학습을 다룬다. 역전파(backpropagation) 알고리즘의 연쇄 법칙 기반 유도를 상세히 제시한다. 드롭아웃(dropout), 배치 정규화 등 학습 시 정규화 기법을 설명한다. 자동 미분(automatic differentiation)과 계산 그래프의 원리를 소개한다

**Marker 세부 목차** (`Jurafsky-SLP_marker_full.md`):
- 6.1 Units `L:3766`
- 6.2 The XOR problem `L:3842`
- 6.4 Feedforward networks for NLP: Classification `L:4041`
- 6.5 Embeddings as the input to neural net classifiers `L:4083`
- 6.6 Training Neural Nets `L:4193`
- 6.7 Summary `L:4412`


### Ch 7: Large Language Models (pp. 146-172)
**핵심**: 언어 모델의 세 가지 아키텍처(인코더-온리, 인코더-디코더, 디코더-온리)를 비교한다. 조건부 텍스트 생성의 직관, 프롬프팅, 샘플링 전략(top-k, top-p, temperature)을 설명한다. LLM 학습 과정과 평가 방법론, 윤리적/안전성 이슈를 다룬다.
**키워드**: `LLM`, `prompting`, `top-k sampling`, `temperature`, `ethics`, `evaluation`
**상세**: → `Jurafsky-SLP_marker_full.md` Ch 7 (L:4503)
언어 모델의 세 가지 아키텍처(인코더, 디코더, 인코더-디코더)를 정의하고 각각의 정보 흐름과 적용 과제를 비교한다. 디코더는 GPT/Claude/Llama 등의 생성 모델에, 인코더는 BERT 등의 분류 모델에, 인코더-디코더는 번역/ASR에 사용된다. 조건부 텍스트 생성(conditional generation)의 직관을 감성 분석과 질의응답 예시로 설명한다. 프롬프팅(prompting)과 프롬프트 엔지니어링의 원리를 소개하며, 인스트럭션 튜닝이 모델의 지시 따르기 능력을 향상시키는 메커니즘을 설명한다. 인컨텍스트 학습(in-context learning)과 체인 오브 소트(chain-of-thought) 프롬프팅을 다룬다. 샘플링 전략(top-k, top-p/nucleus, temperature)의 수학적 정의와 생성 품질에 미치는 영향을 분석한다. LLM 학습 과정에서 데이터 규모, 모델 크기, 스케일링 법칙(scaling laws)의 관계를 논의한다. LLM 평가 방법론으로 자동 벤치마크와 인간 평가를 비교한다. 환각(hallucination), 편향, 독성 등 윤리적/안전성 이슈와 완화 전략을 논의한다. 파인튜닝과 파라미터 효율적 적응(LoRA)을 소개한다

**Marker 세부 목차** (`Jurafsky-SLP_marker_full.md`):
- 7.1 Three architectures for language models `L:4503`
- 7.2 Conditional Generation of Text: The Intuition `L:4525`
- 7.3 Prompting `L:4561`
- 7.4 Generation and Sampling `L:4657`
- 7.5 Training Large Language Models `L:4767`
- 7.6 Evaluating Large Language Models `L:4862`
- 7.7 Ethical and Safety Issues with Language Models `L:4960`
- 7.8 Summary `L:4994`


### Ch 8: Transformers (pp. 173-198)
**핵심**: 어텐션 메커니즘을 QKV 프레임워크로 정의하고, 멀티헤드 어텐션, 트랜스포머 블록(잔차 연결, 레이어 정규화, FFN)을 설명한다. 토큰/위치 임베딩, 언어 모델링 헤드, 행렬 병렬화를 다룬다. 학습 시 스케일링 전략과 트랜스포머 해석 가능성을 논의한다.
**키워드**: `attention`, `multi-head`, `transformer block`, `layer normalization`, `positional embedding`
**상세**: → `Jurafsky-SLP_marker_full.md` Ch 8 (L:5062)
어텐션 메커니즘을 문맥 의존적 단어 의미(contextual embeddings) 계산의 핵심 도구로 소개한다. "chicken/road" 대명사 해소 예시를 통해 문맥 정보의 중요성을 설명한다. 단순화된 어텐션(가중합)에서 출발하여 QKV(Query-Key-Value) 프레임워크로 발전시킨다. 쿼리, 키, 값 행렬(W^Q, W^K, W^V)의 역할과 스케일드 닷프로덕트 어텐션 수식을 유도한다. 멀티헤드 어텐션(multi-head attention)의 구조와 다양한 관점의 정보 포착 능력을 설명한다. 트랜스포머 블록의 전체 구성(잔차 연결, 레이어 정규화, 순전파 네트워크 FFN)을 상세히 다룬다. 토큰 임베딩과 위치 임베딩(절대적/회전적 위치 인코딩)을 설명한다. 언어 모델링 헤드의 구조와 가중치 공유(weight tying) 기법을 소개한다. 행렬 병렬화(KV 캐시, 모델 병렬리즘)를 통한 대규모 모델의 효율적 처리를 다룬다. 트랜스포머 해석 가능성(어텐션 패턴 분석, 프로빙)을 논의한다

**Marker 세부 목차** (`Jurafsky-SLP_marker_full.md`):
- 8.1 Attention `L:5062`
- 8.2 Transformer Blocks `L:5222`
- 8.4 The input: embeddings for token and position `L:5383`
- 8.5 The Language Modeling Head `L:5433`
- 8.7 Training `L:5511`
- 8.8 Dealing with Scale `L:5523`
- 8.9 Interpreting the Transformer `L:5598`
- 8.10 Summary `L:5634`


### Ch 9: Masked Language Models (pp. 199-217)
**핵심**: 양방향 트랜스포머 인코더(BERT)의 구조와 사전학습 방법(MLM, NSP)을 설명한다. 문맥 의존 임베딩(contextual embeddings)의 개념을 소개하고, 분류와 시퀀스 레이블링(NER)에 대한 파인튜닝 방법을 다룬다.
**키워드**: `BERT`, `masked language model`, `contextual embeddings`, `fine-tuning`, `NER`
**상세**: → `Jurafsky-SLP_marker_full.md` Ch 9 (L:5676)
양방향 트랜스포머 인코더(BERT)의 구조를 인과적(causal) 디코더와 비교하여 설명한다. 양방향 어텐션은 단순히 인과적 마스킹을 제거하여 구현되며, 미래 토큰도 참조할 수 있게 된다. BERT의 구체적 사양(30K WordPiece 어휘, 512 토큰 윈도우, 12레이어, 약 100M 파라미터)과 다국어 XLM-RoBERTa(250K 어휘, 24레이어, 550M 파라미터)를 비교한다. 마스크드 언어 모델링(MLM) 학습: 15% 토큰을 선택하여 80%는 [MASK]로, 10%는 랜덤 토큰으로, 10%는 원본 유지하는 전략을 설명한다. 디노이징(denoising) 학습의 일반 원리(마스킹, 치환, 재배열, 삭제)를 소개한다. 문맥 의존 임베딩(contextual embeddings)이 정적 임베딩과 달리 동일 단어에 문맥별 다른 벡터를 부여함을 설명한다. 분류 과제를 위한 파인튜닝: [CLS] 토큰 위에 분류 헤드를 추가하는 방법을 다룬다. 시퀀스 레이블링을 위한 파인튜닝: 각 토큰 위치에 분류기를 배치하여 NER 등을 수행하는 방법을 설명한다. BIO/BIOES 태깅 스키마를 소개하고 개체명 경계 인식에 활용한다. 인코더 모델은 생성이 아닌 해석적(interpretive) 과제에 특화되어 있음을 강조한다

**Marker 세부 목차** (`Jurafsky-SLP_marker_full.md`):
- 9.1 Bidirectional Transformer Encoders `L:5676`
- 9.2 Training Bidirectional Encoders `L:5731`
- 9.3 Contextual Embeddings `L:5831`
- 9.4 Fine-Tuning for Classification `L:5927`
- 9.5 Fine-Tuning for Sequence Labeling: Named Entity Recognition (p.220) `L:5990`
- 9.6 Summary `L:6109`


### Ch 10: Post-training (pp. 218-234)
**핵심**: 인스트럭션 튜닝으로 LLM의 응답 품질을 향상시키는 방법을 설명한다. 선호도 기반 학습(RLHF, DPO)을 통한 LLM 정렬(alignment) 기법을 다룬다. 테스트 시점 연산(test-time compute)의 활용도 소개한다.
**키워드**: `instruction tuning`, `RLHF`, `DPO`, `alignment`, `test-time compute`
**상세**: → `Jurafsky-SLP_marker_full.md` Ch 10 (L:6153)
인스트럭션 튜닝(instruction tuning)은 사전학습된 LLM을 지시-응답 데이터셋으로 추가 학습하여 지시 따르기 능력을 향상시키는 SFT(supervised fine-tuning) 방법이다. 도메인 적응, 파라미터 효율적 파인튜닝(LoRA), 과제 기반 파인튜닝(분류 헤드 추가)과의 차이를 명확히 구분한다. 인스트럭션 데이터셋 구축 방법으로 인간 직접 작성(Aya 503M 인스턴스, 114개 언어), 기존 NLP 데이터셋 템플릿 변환(SuperNatural Instructions, Flan), 어노테이션 가이드라인 활용, 합성 데이터 생성의 네 가지를 소개한다. 선호도 기반 학습(learning from preferences)의 원리를 설명하며, 보상 모델 학습과 선호 데이터 수집 방법을 다룬다. RLHF(Reinforcement Learning from Human Feedback)의 전체 파이프라인을 제시한다. DPO(Direct Preference Optimization)가 보상 모델 없이 직접 선호도를 최적화하는 더 단순한 대안임을 설명한다. LLM 정렬(alignment)의 목표로 유용성(helpfulness), 무해성(harmlessness), 정직성(honesty)을 정의한다. 테스트 시점 연산(test-time compute)의 개념과 활용 방법을 소개한다. 인스트럭션 튜닝은 기본 모델 학습 비용의 극히 일부만 소요됨을 강조한다

**Marker 세부 목차** (`Jurafsky-SLP_marker_full.md`):
- 10.1 Instruction Tuning (p.226) `L:6153`
- 10.2 Learning from Preferences `L:6265`
- 10.3 LLM Alignment via Preference-Based Learning `L:6385`


### Ch 11: Retrieval-based Models (pp. 235-257)
**핵심**: TF-IDF 기반 정보 검색부터 밀집 벡터 검색(dense retrieval)까지 다룬다. IR 시스템 평가(정밀도, 재현율, MAP)를 설명하고, 검색 증강 생성(RAG)의 원리를 소개한다. QA 데이터셋과 평가 방법을 다룬다.
**키워드**: `information retrieval`, `RAG`, `dense retrieval`, `TF-IDF`, `QA evaluation`
**상세**: → `Jurafsky-SLP_marker_full.md` Ch 11 (L:6530)
LLM의 환각(hallucination) 문제, 독점 데이터 접근 불가, 정보의 시간적 한계를 LLM 단독 사용의 세 가지 핵심 문제로 제시한다. 검색 증강 생성(RAG)을 이 문제들의 해결책으로 소개하며, IR 기반 문서 검색과 LLM 기반 답변 생성을 결합한다. 정보 검색(IR)의 기본 구조로 쿼리, 문서, 컬렉션, 관련성 개념을 정의한다. 희소 검색(sparse retrieval): 백오브워즈 모델, 벡터 공간 모델, TF-IDF 가중치, BM25 스코어링을 설명한다. 역색인(inverted index)의 구조와 효율적 검색 방법을 다룬다. IR 평가: 정밀도, 재현율, MAP(Mean Average Precision), MRR, NDCG 지표를 정의한다. 밀집 검색(dense retrieval): BERT 등 인코더 모델로 쿼리와 문서를 밀집 벡터로 인코딩하여 유사도를 계산한다. 바이인코더(bi-encoder)와 크로스인코더(cross-encoder) 아키텍처를 비교한다. RAG 파이프라인의 전체 구조(검색→컨텍스트 결합→생성)를 설명한다. QA 데이터셋(SQuAD 등)과 EM/F1 기반 평가 방법을 다룬다

**Marker 세부 목차** (`Jurafsky-SLP_marker_full.md`):
- 11 Information Retrieval and Retrieval-Augmented Generation `L:6530`
- 11.1 Information Retrieval `L:6578`
- 11.2 Evaluation of Information-Retrieval Systems `L:6804`
- 11.3 Information Retrieval with Dense Vectors `L:6903`
- 11.4 Retrieval-Augmented Generation (RAG) `L:6958`
- 11.5 Datasets `L:7017`
- 11.6 Evaluating Question Answering `L:7083`
- 11.7 Summary `L:7093`


### Ch 12: Machine Translation (pp. 258-283)
**핵심**: 언어 간 발산과 유형론적 차이를 설명한다. 인코더-디코더 모델을 MT에 적용하는 방법, 빔 서치 디코딩을 다룬다. 저자원 번역, BLEU/COMET 기반 MT 평가, 편향과 윤리적 문제를 논의한다.
**키워드**: `encoder-decoder`, `beam search`, `BLEU`, `low-resource`, `language typology`
**상세**: → `Jurafsky-SLP_marker_full.md` Ch 12 (L:7170)
기계 번역(MT)의 실용적 응용으로 정보 접근, 포스트에디팅(CAT), 실시간 통역, 이미지 기반 번역을 소개한다. 언어 간 발산과 유형론(typology)을 설명하며, 어순(SVO/SOV/VSO), 형태론적 유형(교착어/굴절어/고립어), 대명사 탈락, 격 표지 등의 차이를 영어-일본어-중국어 예시로 보인다. 인코더-디코더 모델을 MT의 표준 아키텍처로 제시하며, 소스 언어 인코딩과 타겟 언어 디코딩의 분리를 설명한다. 토크나이제이션 전략(다국어 BPE, SentencePiece)과 병렬 코퍼스 구축 방법을 다룬다. 교차 어텐션(cross-attention)과 교사 강제(teacher forcing) 학습을 설명한다. 빔 서치(beam search) 디코딩의 알고리즘과 빔 크기의 영향을 분석한다. 저자원 번역(low-resource translation): 역번역(back-translation), 전이 학습, 다국어 모델 접근법을 소개한다. MT 평가: chrF(문자 F-점수), BLEU, COMET 지표의 정의와 한계를 비교한다. 번역에서의 성별 편향과 문화적 편향 문제를 논의한다. 인코더-디코더와 디코더 전용 LLM의 번역 성능을 비교한다

**Marker 세부 목차** (`Jurafsky-SLP_marker_full.md`):
- 12 Machine Translation `L:7170`
- 12.1 Language Divergences and Typology `L:7228`
- 12.2 Machine Translation using Encoder-Decoder `L:7328`
- 12.3 Details of the Encoder-Decoder Model `L:7423`
- 12.4 Decoding in MT: Beam Search `L:7459`
- 12.5 Translating in low-resource situations `L:7579`
- 12.6 MT Evaluation `L:7619`
- 12.8 Summary `L:7762`


### Ch 13: RNNs and LSTMs (pp. 284-309)
**핵심**: RNN의 기본 구조와 언어 모델링 적용을 설명한다. 스택/양방향 RNN, LSTM의 게이트 메커니즘을 다룬다. RNN 기반 인코더-디코더 모델과 어텐션 메커니즘을 소개한다.
**키워드**: `RNN`, `LSTM`, `gated units`, `encoder-decoder`, `attention`
**상세**: → `Jurafsky-SLP_marker_full.md` Ch 13 (L:7827)
RNN(순환 신경망)의 기본 구조를 Elman 네트워크로 소개하며, 히든 상태의 재귀적 연결이 가변 길이 문맥을 표현하는 메커니즘을 설명한다. 순전파 추론에서 h_t = g(Uh_{t-1} + Wx_t), y_t = f(Vh_t) 공식을 유도하고 행렬 차원을 명시한다. 시간을 통한 역전파(BPTT: Backpropagation Through Time)의 원리와 그래프 전개(unrolling) 기법을 설명한다. RNN을 언어 모델링에 적용하여 고정 길이 n-그램의 한계를 극복하는 방법을 보인다. 텍스트 분류(감성 분석)에서 최종 히든 상태를 사용하는 방법과 풀링 기법을 설명한다. 시퀀스 레이블링(품사 태깅)에 RNN을 적용하는 방법을 다룬다. 스택 RNN(깊은 RNN)과 양방향 RNN(BiRNN)의 구조와 장점을 설명한다. LSTM의 게이트 메커니즘(망각 게이트, 입력 게이트, 출력 게이트)을 수식과 함께 상세히 설명하며, 장기 의존성 학습 능력을 분석한다. RNN 기반 인코더-디코더 모델의 구조와 컨텍스트 벡터의 역할을 설명한다. RNN 기반 어텐션 메커니즘을 소개하며, 이것이 트랜스포머 어텐션의 전신임을 보인다

**Marker 세부 목차** (`Jurafsky-SLP_marker_full.md`):
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


### Ch 14: Phonetics and Speech Feature Extraction (pp. 310-338)
**핵심**: 음성학적 전사와 조음 음성학(자음/모음 분류)을 설명한다. 운율(강세, 억양)과 음향 음성학(파형, 스펙트럼, 포르만트)을 다룬다. 로그 멜 스펙트럼과 MFCC 특징 추출 과정을 상세히 유도한다.
**키워드**: `phonetics`, `mel spectrum`, `MFCC`, `spectrogram`, `prosody`, `articulation`
**상세**: → `Jurafsky-SLP_marker_full.md` Ch 14 (L:8391)
음성학(phonetics)을 음성 인식과 음성 합성의 계산적 기초로 소개한다. 문자 체계의 역사(수메르 설형문자, 중국 갑골문, 서셈어 문자)를 통해 음성 단위의 추상화 과정을 추적한다. IPA(국제 음성 기호)와 ARPAbet 음성 전사 체계를 비교하며, 영어 자음/모음의 전체 체계를 표로 제시한다. TIMIT, CMU Pronouncing Dictionary 등 음성 자원과 음성 전사 코퍼스를 소개한다. 조음 음성학(articulatory phonetics): 자음의 조음 위치(양순, 치경, 연구개 등)와 조음 방법(파열, 마찰, 비음 등), 모음의 혀 높이와 전후 위치에 따른 분류를 체계적으로 설명한다. 운율(prosody): 강세(stress), 억양(intonation), 음조(tone)의 정의와 역할을 다룬다. 음향 음성학: 파형(waveform), 주파수, 스펙트럼, 스펙트로그램, 포르만트(formant)의 개념을 수학적으로 정의한다. 로그 멜 스펙트럼 추출 과정(프리엠퍼시스, 윈도잉, DFT, 멜 필터뱅크, 로그 압축)을 단계별로 유도한다. MFCC(Mel Frequency Cepstral Coefficients) 특징 추출의 DCT 기반 알고리즘을 설명한다. 이 특징들이 ASR과 TTS 시스템의 입력으로 사용됨을 강조한다

**Marker 세부 목차** (`Jurafsky-SLP_marker_full.md`):
- 14 Phonetics and Speech Feature Extraction `L:8391`
- 14.1 Speech Sounds and Phonetic Transcription `L:8405`
- 14.2 Articulatory Phonetics (p.319) `L:8473`
- 14.3 Prosody `L:8563`
- 14.4 Acoustic Phonetics and Signals `L:8639`
- 14.4.1 Waves `L:8643`
- 14.5 Feature Extraction for Speech Recognition: Log Mel Spectrum (p.336) `L:8856`
- 14.6 MFCC: Mel Frequency Cepstral Coefficients `L:8975`
- 14.7 Summary `L:9022`


### Ch 15: Automatic Speech Recognition (pp. 339-364)
**핵심**: ASR 태스크를 정의하고, CNN 기반 음향 모델을 설명한다. 인코더-디코더 ASR 아키텍처와 자기지도 모델(HuBERT)을 소개한다. CTC(Connectionist Temporal Classification) 알고리즘과 WER(단어 오류율) 평가를 다룬다.
**키워드**: `ASR`, `CTC`, `HuBERT`, `WER`, `encoder-decoder`, `CNN acoustic model`
**상세**: → `Jurafsky-SLP_marker_full.md` Ch 15 (L:9070)
ASR 태스크의 변이 차원(어휘 크기, 화자 유형, 채널/잡음, 방언/화자 특성)을 체계적으로 분류한다. 주요 ASR 코퍼스(LibriSpeech, Switchboard, CALLHOME, CHiME, AMI, CORAAL, Common Voice, FLEURS)를 소개하고 각각의 WER 성능을 비교한다. 읽기 음성(2% WER)부터 다화자 만찬 대화(25.5% WER)까지 난이도별 성능 차이를 보인다. CNN(합성곱 신경망)을 음성 특징 추출의 초기 레이어로 소개하며, 1D 합성곱의 커널, 스트라이드, 다운샘플링 연산을 설명한다. 인코더-디코더 ASR: Listen Attend and Spell 아키텍처와 교차 어텐션 메커니즘을 다룬다. Whisper 시스템의 구조(680K시간 다국어 학습, 멀티태스크 프레임워크)를 소개한다. 자기지도 모델 HuBERT: 마스크된 음성 구간의 이산 라벨을 예측하는 학습 방식을 설명하며, k-means 클러스터링으로 의사(pseudo) 라벨을 생성하는 과정을 다룬다. CTC(Connectionist Temporal Classification): 정렬 없이 시퀀스 레이블링을 수행하는 알고리즘을 수학적으로 유도한다. WER(단어 오류율) 평가 지표의 정의(삽입/삭제/치환 기반)와 계산법을 제시한다. 아프리카계 미국인 영어 등 비표준 방언에서의 ASR 성능 격차와 공정성 문제를 논의한다

**Marker 세부 목차** (`Jurafsky-SLP_marker_full.md`):
- 15 Automatic Speech Recognition (p.346) `L:9070`
- 15.1 The Automatic Speech Recognition Task `L:9096`
- 15.2 Convolutional Neural Networks `L:9143`
- 15.3 The Encoder-Decoder Architecture for ASR `L:9210`
- 15.4 Self-supervised models: HuBERT `L:9315`
- 15.5 CTC `L:9407`
- 15.6 ASR Evaluation: Word Error Rate (p.366) `L:9516`
- 15.7 Summary `L:9593`


### Ch 16: Text-to-Speech (pp. 365-378)
**핵심**: TTS 시스템의 전체 파이프라인을 설명한다. 오디오 코덱을 이용한 이산 오디오 토큰 학습, VALL-E의 2단계 LM 기반 음성 생성을 다룬다. TTS 평가와 음성 언어 모델(spoken language models)을 소개한다.
**키워드**: `TTS`, `VALL-E`, `audio codec`, `spoken language models`, `speech synthesis`
**상세**: → `Jurafsky-SLP_marker_full.md` Ch 16 (L:9632)
TTS(텍스트-음성 합성)의 역사를 폰 켐펠렌(1769년)의 기계적 음성 합성기에서부터 추적한다. 현대 TTS의 패러다임 전환을 설명한다: 과거의 단일 화자 수백 시간 학습에서 수천 화자의 수만 시간 데이터로 화자 독립적(speaker-independent) 모델을 학습하는 방식으로 변화했다. 제로샷 TTS: 학습 시 보지 못한 새 화자의 3초 음성만으로 해당 화자의 음성을 생성하는 과제를 정의한다. 오디오 코덱(codec) 기반 이산 오디오 토큰 학습의 전체 파이프라인(인코더→벡터 양자화기→디코더)을 설명한다. 벡터 양자화(VQ): 코드북 기반 이산 토큰 생성과 잔여 벡터 양자화(RVQ)의 다계층 구조를 다룬다. EnCodec 등 신경 오디오 코덱의 학습 손실 함수(재구성 손실, 적대적 손실, 코드북 손실)를 소개한다. VALL-E: 2단계 LM 기반 음성 생성 시스템의 구조를 설명하며, 자기회귀 모델(AR)과 비자기회귀 모델(NAR)의 조합을 다룬다. TTS 평가: MOS(Mean Opinion Score)와 화자 유사도 측정 방법을 소개한다. 음성 언어 모델(Spoken Language Models): 텍스트와 음성 토큰을 통합적으로 처리하는 모델의 가능성을 논의한다. 음성 번역, 화자 분리(diarization) 등 추가 음성 과제를 소개한다

**Marker 세부 목차** (`Jurafsky-SLP_marker_full.md`):
- 16 Text-to-Speech `L:9632`
- 16.2 Using a codec to learn discrete audio tokens `L:9690`
- 16.3 VALL-E: Generating audio with 2-stage LM `L:9824`
- 16.4 TTS Evaluation `L:9875`
- 16.5 Other speech tasks `L:9887`
- 16.6 Spoken Language Models `L:9905`
- 16.7 Summary `L:9909`


### Ch 17: Sequence Labeling (pp. 382-405)
**핵심**: 품사 태깅과 개체명 인식(NER)을 위한 시퀀스 레이블링을 다룬다. HMM 기반 품사 태깅(비터비 알고리즘)과 CRF(조건부 랜덤 필드)를 설명한다. NER 평가 방법을 제시한다.
**키워드**: `POS tagging`, `NER`, `HMM`, `Viterbi`, `CRF`, `sequence labeling`
**상세**: → `Jurafsky-SLP_marker_full.md` Ch 17 (L:9956)
품사(POS)의 역사를 기원전 100년 디오니시우스 트라크스의 8품사 체계에서부터 추적한다. Universal Dependencies(UD) 17개 품사 태그셋을 표로 제시하며, 개방 클래스(명사, 동사, 형용사, 부사)와 폐쇄 클래스(전치사, 관사, 접속사 등)를 구분한다. 각 품사의 문법적 정의와 형태론적 특성을 영어 예시와 함께 설명한다. 품사 태깅의 실용적 중요성(파싱, 의존 관계, 정보 추출의 전제조건)을 강조한다. 개체명 인식(NER): 사람, 장소, 조직 등의 개체명 범주와 BIO/IOB 태깅 스키마를 정의한다. HMM(은닉 마르코프 모델) 기반 품사 태깅: 전이 확률과 방출 확률의 정의, 비터비(Viterbi) 알고리즘의 동적 프로그래밍 유도를 상세히 다룬다. 비터비 디코딩의 시간 복잡도(O(N²T))와 역추적(backtrace) 과정을 설명한다. CRF(조건부 랜덤 필드): 판별 모델로서의 장점, 특징 함수(feature function), 전역 정규화를 HMM과 비교한다. NER 평가: 엔티티 단위 정밀도/재현율/F1과 경계 오류 유형을 설명한다. 신경망 기반 시퀀스 레이블링(BiLSTM-CRF, 트랜스포머)과의 연결을 소개한다

**Marker 세부 목차** (`Jurafsky-SLP_marker_full.md`):
- 17 Sequence Labeling for Parts of Speech and Named Entities `L:9956`
- 17.1 (Mostly) English Word Classes `L:9978`
- 17.2 Part-of-Speech Tagging `L:10077`
- 17.3 Named Entities and Named Entity Tagging `L:10117`
- 17.4 HMM Part-of-Speech Tagging `L:10182`
- 17.5 Conditional Random Fields (CRFs) (p.403) `L:10430`
- 17.6 Evaluation of Named Entity Recognition `L:10619`
- 17.7 Further Details `L:10629`
- 17.8 Summary `L:10662`


### Ch 18: Context-Free Grammars and Constituency Parsing (pp. 407-429)
**핵심**: 구성소(constituency)와 문맥 자유 문법(CFG)의 형식적 정의를 제공한다. 트리뱅크, 문법 동치와 정규형, 구조적 모호성을 설명한다. CKY 동적 프로그래밍 파싱과 신경망 기반 구간(span) 파서를 다룬다.
**키워드**: `CFG`, `CKY parsing`, `treebank`, `constituency`, `ambiguity`, `span-based parsing`
**상세**: → `Jurafsky-SLP_marker_full.md` Ch 18 (L:10723)
구성소(constituency) 개념을 명사구(NP)의 분포적 증거를 통해 도입한다. 문맥 자유 문법(CFG)의 형식적 정의: 규칙(production), 단말/비단말 기호, 어휘(lexicon), 시작 기호를 제시한다. CFG를 문장 생성 장치와 구조 부여 장치의 두 관점에서 설명하며, 유도(derivation)와 파스 트리(parse tree)를 정의한다. 영어의 주요 구문 구조(NP, VP, PP, S, SBAR)를 예시 규칙으로 제시한다. 트리뱅크(treebank): Penn Treebank, Universal Dependencies 코퍼스를 소개하며, 코퍼스 기반 문법 추출 방법을 설명한다. 문법 동치와 촘스키 정규형(CNF)을 정의하고, 임의의 CFG를 CNF로 변환하는 알고리즘을 제시한다. 구조적 모호성(structural ambiguity): PP 부착 모호성, 접속 모호성 등의 예시와 그 조합적 폭발을 보인다. CKY(Cocke-Kasami-Younger) 파싱 알고리즘: 동적 프로그래밍 표의 구성과 O(n³|G|) 시간 복잡도를 유도한다. 신경망 기반 구간(span) 파서: 각 구간에 점수를 부여하고 CKY로 최적 트리를 찾는 방법을 설명한다. 파서 평가: PARSEVAL 지표(레이블 정밀도/재현율, 교차 괄호)와 헤드 찾기(head-finding) 규칙을 다룬다

**Marker 세부 목차** (`Jurafsky-SLP_marker_full.md`):
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


### Ch 19: Dependency Parsing (pp. 431-454)
**핵심**: 의존 관계(dependency relations)를 정의하고, 전이 기반(transition-based) 파싱(아크 표준 시스템, 신경망 분류기)을 설명한다. 그래프 기반(graph-based) 파싱(최대 스패닝 트리)을 다루고, UAS/LAS 평가 지표를 소개한다.
**키워드**: `dependency parsing`, `transition-based`, `graph-based`, `UAS`, `LAS`
**상세**: → `Jurafsky-SLP_marker_full.md` Ch 19 (L:11452)
의존 문법(dependency grammar)을 구구조 문법과 비교하며, 구문소(phrasal constituent) 없이 단어 간 직접적인 핵어-의존어(head-dependent) 관계로 문장 구조를 표현한다. 의존 구조가 술어-논항 의미 관계의 좋은 근사임을 설명하며, 이것이 NLP에서 의존 문법이 더 널리 쓰이는 이유임을 강조한다. 자유 어순 언어(체코어 등)에서 의존 문법의 장점을 보인다. Universal Dependencies(UD) 프로젝트의 37개 의존 관계를 소개하고, NSUBJ, OBJ, NMOD, AMOD, DET, CASE 등 핵심 관계를 예시와 함께 설명한다. 의존 구조의 형식적 정의(방향 그래프, 연결성, 비순환성, 사영성)를 제시한다. 전이 기반(transition-based) 파싱: 아크 표준(arc-standard) 시스템의 설정(스택, 버퍼, SHIFT/LEFT-ARC/RIGHT-ARC 연산)을 단계별로 추적한다. 오라클(oracle) 학습과 신경망 분류기(Chen & Manning 2014)를 이용한 전이 예측을 설명한다. 그래프 기반(graph-based) 파싱: 최대 스패닝 트리 알고리즘(Chu-Liu/Edmonds)을 소개한다. 신경망 기반 간선 점수 계산(biaffine attention)을 설명한다. 평가: UAS(비레이블 부착 점수)와 LAS(레이블 부착 점수)의 정의와 계산법을 제시한다

**Marker 세부 목차** (`Jurafsky-SLP_marker_full.md`):
- 19 Dependency Parsing `L:11452`
- 19.1 Dependency Relations `L:11480`
- 19.2 Transition-Based Dependency Parsing `L:11592`
- 19.3 Graph-Based Dependency Parsing `L:11913`
- 19.4 Evaluation `L:12060`
- 19.5 Summary `L:12082`


### Ch 20: Information Extraction (pp. 455-480)
**핵심**: 관계 추출(패턴, 지도 학습, 반지도, 원격 감독)과 이벤트 추출을 다룬다. 시간 표현(TimeML, TimeBank)과 양상(aspect) 표현을 설명한다. 템플릿 채우기 과제를 소개한다.
**키워드**: `relation extraction`, `event extraction`, `temporal analysis`, `distant supervision`, `template filling`
**상세**: → `Jurafsky-SLP_marker_full.md` Ch 20 (L:12121)
정보 추출(IE)을 비정형 텍스트에서 구조화된 데이터를 추출하는 과제로 정의하며, 항공 요금 인상 뉴스 기사를 도입 예시로 사용한다. 관계 추출(relation extraction): ACE의 17개 관계 유형(Physical, Part-Whole, Person-Social 등)과 UMLS의 의료 관계를 소개한다. 관계 추출 알고리즘: 패턴 기반(Hearst 패턴), 지도 학습(특징 기반 분류기), 반지도 학습(부트스트래핑), 원격 감독(distant supervision, Freebase/Wikipedia 활용)을 체계적으로 비교한다. 지식 그래프와 RDF 트리플(주어-술어-목적어) 표현, Wikipedia 인포박스로부터의 관계 추출을 다룬다. 이벤트 추출: 이벤트의 정의(트리거, 논항, 참여자)와 ACE/ERE 이벤트 온톨로지를 설명한다. 시간 표현(temporal expression): TimeML 표준과 시간 정규화(절대/상대 시간을 달력 날짜로 변환)를 다룬다. 양상(aspect) 표현: 상태, 활동, 달성, 성취의 구분을 설명한다. TimeBank 코퍼스와 시간 관계(BEFORE, AFTER, SIMULTANEOUS 등) 주석 체계를 소개한다. 자동 시간 분석: 시간 표현 인식, 시간 정규화, 사건 간 시간 순서 결정의 파이프라인을 다룬다. 템플릿 채우기(template filling): 반복적 상황에서 슬롯을 자동으로 채우는 과제를 설명한다

**Marker 세부 목차** (`Jurafsky-SLP_marker_full.md`):
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


### Ch 21: Semantic Role Labeling (pp. 481-500)
**핵심**: 의미역(thematic roles)과 태도 교체(diathesis alternation)를 설명한다. PropBank과 FrameNet의 구조를 비교하고, 신경망 기반 SRL 시스템을 소개한다. 선택 제약과 술어 분해도 다룬다.
**키워드**: `semantic roles`, `PropBank`, `FrameNet`, `SRL`, `selectional restrictions`
**상세**: → `Jurafsky-SLP_marker_full.md` Ch 21 (L:12997)
의미역(semantic roles)의 기원을 기원전 파니니의 카라카(kāraka) 체계에서부터 추적한다. "누가 누구에게 무엇을 했는가"라는 핵심 질문을 XYZ Corporation 주식 매입의 다양한 표면 실현(능동, 수동, 명사화)으로 설명한다. 주제역(thematic roles): AGENT, THEME, EXPERIENCER, INSTRUMENT, BENEFICIARY, SOURCE, GOAL 등 약 12개 역할을 정의하고 예시를 제시한다. 태도 교체(diathesis alternation): 동일 동사가 다른 논항 구조를 취하는 현상(능격, 사역, 장소/위치 교체 등)을 설명하며, 의미역이 표면 구문을 넘어 일반화하는 도구임을 보인다. PropBank: 동사별 프레임셋(frameset)과 Arg0-Arg5 역할 체계를 소개하며, 트리뱅크 위에 의미역을 주석한 구조를 설명한다. FrameNet: 프레임(frame) 기반 의미 표현을 PropBank과 비교하며, 프레임 요소(FE)와 어휘 단위(LU)의 개념을 다룬다. 신경망 기반 SRL 시스템: end-to-end 의미역 레이블링의 구조를 설명한다. 선택 제약(selectional restrictions): 술어가 논항에 대해 갖는 의미적 선호(예: eat의 THEME은 먹을 수 있는 것)를 설명한다. 술어 분해(primitive decomposition): 의미 원소(CAUSE, BECOME, BE 등)로 동사 의미를 분석하는 접근법을 소개한다. 의미역이 QA, 기계 번역, 정보 추출의 중간 표현으로 활용됨을 강조한다

**Marker 세부 목차** (`Jurafsky-SLP_marker_full.md`):
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


### Ch 22: Lexicons for Sentiment, Affect, and Connotation (pp. 501-520)
**핵심**: 감정의 정의(기본 감정, 차원 모델)와 감성/정서 사전을 소개한다. 인간 레이블링, 반지도/지도 학습을 통한 사전 구축 방법을 설명한다. 사전 기반 감성/정서 인식과 함축 프레임(connotation frames)을 다룬다.
**키워드**: `sentiment lexicon`, `affect`, `connotation frames`, `emotion`, `opinion mining`
**상세**: → `Jurafsky-SLP_marker_full.md` Ch 22 (L:13617)
감정(affect)의 다섯 가지 유형(emotion, mood, interpersonal stance, attitude, personality traits)을 Scherer 분류법으로 구분한다. 감정의 두 가지 이론적 전통을 비교한다: 기본 감정론(Ekman의 6가지, Plutchik의 8가지 감정 바퀴)과 차원 모델(쾌락가-각성도-지배도 3차원 공간). 감성(sentiment)을 쾌락가(valence) 차원의 특수한 경우로 정의한다. 주요 감성/정서 사전을 소개한다: General Inquirer(1966, 긍정 1915/부정 2291개), MPQA(2718/4912개), Hu-Liu 극성 사전, NRC VAD 사전(20,000 단어). 인간 레이블링을 통한 사전 구축: Best-Worst Scaling 방법과 크라우드소싱 절차를 설명한다. 반지도 학습 기반 사전 구축: 시드 단어에서 출발하여 WordNet 동의어/반의어 관계나 공기 패턴으로 확장하는 부트스트래핑 방법을 다룬다. 지도 학습 기반 사전 구축: 단어 임베딩과 분류기를 결합하는 방법을 설명한다. 사전 기반 감성/정서 인식: 문서의 단어별 점수를 집계하여 전체 감성을 판단하는 방법을 다룬다. 엔티티 중심 정서 분석: 특정 대상에 대한 감정을 추적하는 기법을 소개한다. 함축 프레임(connotation frames): 동사가 주어와 목적어에 대해 함축하는 감정적 태도를 구조화한 의미 자원을 설명한다

**Marker 세부 목차** (`Jurafsky-SLP_marker_full.md`):
- 22 Lexicons for Sentiment, Affect, and Connotation `L:13617`
- 22.1 Defining Emotion `L:13651`
- 22.2 Available Sentiment and Affect Lexicons `L:13679`
- 22.3 Creating Affect Lexicons by Human Labeling (p.512) `L:13736`
- 22.5 Supervised Learning of Word Sentiment `L:13886`
- 22.6 Using Lexicons for Sentiment Recognition `L:14016`
- 22.7 Using Lexicons for Affect Recognition `L:14033`
- 22.8 Lexicon-based methods for Entity-Centric Affect `L:14067`
- 22.9 Connotation Frames (p.524) `L:14084`


### Ch 23: Coreference Resolution and Entity Linking (pp. 521-550)
**핵심**: 상호 참조 현상(대명사, 명사구 조응)의 언어학적 배경을 설명한다. 멘션 검출, 신경망 기반 멘션 랭킹 알고리즘, 엔티티 링킹을 다룬다. 상호 참조에서의 성별 편향 문제와 위노그래드 스키마를 논의한다.
**키워드**: `coreference resolution`, `entity linking`, `mention ranking`, `Winograd schema`, `gender bias`
**상세**: → `Jurafsky-SLP_marker_full.md` Ch 23 (L:14147)
상호 참조 해결(coreference resolution)을 담화 모델(discourse model) 내에서 멘션(mention)과 담화 엔티티(discourse entity)를 연결하는 과제로 정의한다. Victoria Chen 예시를 통해 멘션, 참조 표현(referring expression), 조응(anaphora), 선행사(antecedent), 상호 참조 체인(coreference chain)의 개념을 소개한다. 상호 참조의 언어학적 배경: 대명사(인칭, 재귀, 지시), 명사구 조응, 영대명사(zero anaphora)의 유형을 설명한다. 문법적 제약(결속 이론의 원리), 담화적 제약(최근성, 현저성), 의미적 제약(선택 제약, 세계 지식)을 다룬다. 멘션 검출: 명사구, 대명사, 고유 명사를 후보 멘션으로 식별하고 필터링하는 방법을 설명한다. 신경망 기반 멘션 랭킹 알고리즘: 각 멘션에 대해 가능한 선행사를 점수화하고 최적의 쌍을 선택하는 end-to-end 모델을 다룬다. 스팬 표현(span representation)과 멘션 쌍 점수 함수의 구조를 설명한다. 엔티티 링킹(entity linking): 멘션을 Wikipedia 등 온톨로지의 실세계 엔티티에 매핑하는 과제를 다룬다. 후보 생성과 엔티티 소거(entity disambiguation)의 두 단계를 설명한다. 위노그래드 스키마: 세계 지식이 필요한 난해한 대명사 해소 문제와 NLP 도전 과제로서의 의미를 논의한다. 상호 참조에서의 성별 편향 문제(WinoBias, WinoGender 데이터셋)를 다룬다

**Marker 세부 목차** (`Jurafsky-SLP_marker_full.md`):
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


### Ch 24: Discourse Coherence (pp. 551-572)
**핵심**: 담화 일관성 관계(수사 구조 이론 등)와 담화 구조 파싱을 설명한다. 센터링 이론과 엔티티 기반 일관성, 표현 학습 기반 지역/전역 일관성 모델을 다룬다.
**키워드**: `discourse coherence`, `RST`, `centering theory`, `entity-based coherence`
**상세**: → `Jurafsky-SLP_marker_full.md` Ch 24 (L:14991)
담화 일관성(discourse coherence)을 문장들 사이의 체계적 관계로 정의하며, 비일관적 텍스트("John took a train... He likes spinach")와 일관적 텍스트("She had to attend a conference")를 대비한다. 지역 일관성(local coherence)의 세 가지 차원: 일관성 관계(coherence relations), 엔티티 기반 일관성, 주제적 일관성(어휘 결속)을 구분한다. 수사 구조 이론(RST): 핵(nucleus)과 위성(satellite) 사이의 일관성 관계(Reason, Elaboration, Contrast, Condition 등)를 정의하고 RST 트리 구조를 설명한다. Penn Discourse TreeBank(PDTB): 명시적/암시적 담화 접속사(discourse connective)와 4계층 관계 분류(Temporal, Contingency, Comparison, Expansion)를 소개한다. RST와 PDTB의 차이점(트리 구조 vs 지역적 관계, 핵-위성 vs 대칭적 논항)을 비교한다. 담화 구조 파싱: 전이 기반 RST 파서의 SHIFT-REDUCE 알고리즘을 설명한다. 센터링 이론(Centering Theory): 발화별 현저한 엔티티를 추적하며, CONTINUE/RETAIN/SHIFT 전이의 일관성 차이를 분석한다. 엔티티 격자(entity grid) 모델: 문서를 엔티티×문장 행렬로 표현하여 일관성을 정량화하는 방법을 설명한다. 표현 학습 기반 일관성 모델: 문장 쌍의 순서 판별 과제로 신경망을 학습하는 방법을 다룬다. 전역 일관성: 장르별 담화 구조(학술 논문의 IMRaD, 설득적 에세이의 주장-근거 구조)를 소개한다

**Marker 세부 목차** (`Jurafsky-SLP_marker_full.md`):
- 24 Discourse Coherence `L:14991`
- 24.1 Coherence Relations `L:15047`
- 24.2 Discourse Structure Parsing `L:15145`
- 24.3 Centering and Entity-Based Coherence (p.567) `L:15266`
- 24.4 Representation learning models for local coherence `L:15405`
- 24.5 Global Coherence `L:15460`
- 24.6 Summary `L:15534`


### Ch 25: Conversation and its Structure (pp. 573-580)
**핵심**: 인간 대화의 속성(턴 테이킹, 인접 쌍, 기반 형성)을 분석한다. 대화 행위(dialog acts)와 대화 코퍼스를 소개한다.
**키워드**: `dialog acts`, `turn-taking`, `adjacency pairs`, `grounding`, `conversation structure`
**상세**: → `Jurafsky-SLP_marker_full.md` Ch 25 (L:15575)
대화(conversation)를 복잡한 공동 활동(joint activity)으로 정의하며, 인간-인간 대화와 인간-LLM 대화 모두에 구조가 있음을 강조한다. 여행사-고객 전화 대화 전사를 도입 예시로 사용한다. 턴(turn)의 정의와 턴 테이킹(turn-taking): 화자가 교대하는 메커니즘, 끝점 검출(endpointing)의 과제를 설명한다. 화행(speech acts/dialogue acts): Wittgenstein-Austin의 전통을 따라 발화를 행위로 분석하며, Constatives(진술), Directives(지시), Commissives(약속), Acknowledgments(인정)의 4가지 분류를 소개한다. 인접 쌍(adjacency pairs): 질문-답변, 제안-수락/거절, 인사-인사 등 대화의 구조적 쌍을 정의한다. 선호 구조(preference structure): 수락이 거절보다 선호되는 비대칭적 응답 패턴을 설명한다. 기반 형성(grounding): 대화 참여자가 상호 이해를 확인하는 메커니즘(명시적 확인, 반복, "OK" 등)을 다룬다. 대화 행위 코퍼스: Switchboard DAMSL, ATIS, MultiWOZ 등의 대화 코퍼스와 태그셋을 소개한다. 인간-LLM 대화에서도 동일한 대화 구조 분석이 적용됨을 논의한다. 이 장은 초기 초안(stub) 상태로, 향후 대화 구조의 전산적 주석 방법이 추가될 예정이다

**Marker 세부 목차** (`Jurafsky-SLP_marker_full.md`):
- 25 Conversation and its Structure (p.580) `L:15575`
- 25.1 Properties of Human Conversation `L:15581`
- 25.2 Dialog Acts and Corpora `L:15763`



### 기타 섹션 (Marker)

- Volume I (p.8) `L:294`
- Logistic Regression and Text Classification (p.69) `L:2127`
- Post-training: Instruction Tuning, Alignment, and Test-Time Compute (p.225) `L:6127`
- Volume II (p.386) `L:9940`

---

## Marker 세부 목차

> `L:숫자`는 `Jurafsky-SLP_marker_full.md`의 라인 번호.

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
