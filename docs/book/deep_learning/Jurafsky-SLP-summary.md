---
name: "Speech and Language Processing, 3rd Ed."
type: book-summary
source_file: "Jurafsky-SLP_full.md"
authors: "Daniel Jurafsky, James H. Martin"
year: 2026
total_pages: 611
language: en
keywords: [NLP, large language models, transformers, BERT, speech recognition, TTS, parsing, information extraction, coreference, sentiment analysis, machine translation, RAG]
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

### Ch 1: Introduction (p. 3)
**핵심**: NLP, 전산 언어학, 음성 인식 분야의 전체 개관을 제공한다. 이 책이 대규모 언어 모델을 중심으로 재구성되었음을 밝힌다.
**키워드**: `NLP`, `computational linguistics`, `speech recognition`, `language models`
**상세**: → `Speech and Language Processing, 3rd Ed_jan26_full.md` Ch 1 (line 1134)

### Ch 2: Words and Tokens (pp. 4-37)
**핵심**: 단어의 정의와 형태소 분석부터 시작하여 유니코드 처리를 설명한다. BPE(Byte-Pair Encoding) 서브워드 토크나이제이션을 상세히 다루고, 코퍼스 구성, 정규 표현식, 최소 편집 거리(edit distance)를 설명한다.
**키워드**: `BPE`, `tokenization`, `Unicode`, `morphemes`, `edit distance`, `regular expressions`
**상세**: → `Speech and Language Processing, 3rd Ed_jan26_full.md` Ch 2 (line 1150)

### Ch 3: N-gram Language Models (pp. 38-61)
**핵심**: N-그램 언어 모델의 기본 원리를 소개한다. 훈련/테스트 셋 분리, 퍼플렉시티 평가, 문장 샘플링을 설명한다. 일반화 vs 과적합 문제에 대해 스무딩, 보간, 백오프 기법을 제시한다. 퍼플렉시티와 엔트로피의 관계를 유도한다.
**키워드**: `n-gram`, `perplexity`, `smoothing`, `interpolation`, `entropy`
**상세**: → `Speech and Language Processing, 3rd Ed_jan26_full.md` Ch 3 (line 130)

### Ch 4: Logistic Regression (pp. 62-95)
**핵심**: 머신러닝 분류의 기본 모델로 로지스틱 회귀를 소개한다. 시그모이드 함수, 교차 엔트로피 손실, 경사 하강법을 설명한다. 다항 로지스틱 회귀(소프트맥스)로 확장하고, 정밀도/재현율/F-measure, 교차 검증, 통계적 유의성 검정, 정규화를 다룬다. 분류기의 해석 가능성과 편향 회피 문제를 논의한다.
**키워드**: `logistic regression`, `cross-entropy`, `gradient descent`, `softmax`, `F-measure`, `regularization`
**상세**: → `Speech and Language Processing, 3rd Ed_jan26_full.md` Ch 4 (line 173)

### Ch 5: Embeddings (pp. 96-119)
**핵심**: 어휘 의미론에서 출발하여 벡터 의미론의 직관을 설명한다. 빈도 기반 임베딩(공기행렬, TF-IDF, PPMI)과 코사인 유사도를 다룬다. Word2vec(Skip-gram)의 학습 원리를 설명하고, 임베딩의 의미적 속성, 편향 문제, 시각화 방법을 논의한다.
**키워드**: `word2vec`, `cosine similarity`, `TF-IDF`, `PPMI`, `embedding bias`, `vector semantics`
**상세**: → `Speech and Language Processing, 3rd Ed_jan26_full.md` Ch 5 (line 289)

### Ch 6: Neural Networks (pp. 120-145)
**핵심**: 뉴럴 유닛(ReLU, sigmoid, tanh)과 XOR 문제를 통해 비선형성의 필요성을 보여준다. 순전파 신경망의 구조를 정의하고, NLP 분류와 임베딩 입력 활용법을 설명한다. 역전파, 드롭아웃, 정규화 등 학습 기법을 다룬다.
**키워드**: `feedforward network`, `backpropagation`, `XOR`, `dropout`, `NLP classification`
**상세**: → `Speech and Language Processing, 3rd Ed_jan26_full.md` Ch 6 (line 358)

### Ch 7: Large Language Models (pp. 146-172)
**핵심**: 언어 모델의 세 가지 아키텍처(인코더-온리, 인코더-디코더, 디코더-온리)를 비교한다. 조건부 텍스트 생성의 직관, 프롬프팅, 샘플링 전략(top-k, top-p, temperature)을 설명한다. LLM 학습 과정과 평가 방법론, 윤리적/안전성 이슈를 다룬다.
**키워드**: `LLM`, `prompting`, `top-k sampling`, `temperature`, `ethics`, `evaluation`
**상세**: → `Speech and Language Processing, 3rd Ed_jan26_full.md` Ch 7 (line 391)

### Ch 8: Transformers (pp. 173-198)
**핵심**: 어텐션 메커니즘을 QKV 프레임워크로 정의하고, 멀티헤드 어텐션, 트랜스포머 블록(잔차 연결, 레이어 정규화, FFN)을 설명한다. 토큰/위치 임베딩, 언어 모델링 헤드, 행렬 병렬화를 다룬다. 학습 시 스케일링 전략과 트랜스포머 해석 가능성을 논의한다.
**키워드**: `attention`, `multi-head`, `transformer block`, `layer normalization`, `positional embedding`
**상세**: → `Speech and Language Processing, 3rd Ed_jan26_full.md` Ch 8 (line 433)

### Ch 9: Masked Language Models (pp. 199-217)
**핵심**: 양방향 트랜스포머 인코더(BERT)의 구조와 사전학습 방법(MLM, NSP)을 설명한다. 문맥 의존 임베딩(contextual embeddings)의 개념을 소개하고, 분류와 시퀀스 레이블링(NER)에 대한 파인튜닝 방법을 다룬다.
**키워드**: `BERT`, `masked language model`, `contextual embeddings`, `fine-tuning`, `NER`
**상세**: → `Speech and Language Processing, 3rd Ed_jan26_full.md` Ch 9 (line 487)

### Ch 10: Post-training (pp. 218-234)
**핵심**: 인스트럭션 튜닝으로 LLM의 응답 품질을 향상시키는 방법을 설명한다. 선호도 기반 학습(RLHF, DPO)을 통한 LLM 정렬(alignment) 기법을 다룬다. 테스트 시점 연산(test-time compute)의 활용도 소개한다.
**키워드**: `instruction tuning`, `RLHF`, `DPO`, `alignment`, `test-time compute`
**상세**: → `Speech and Language Processing, 3rd Ed_jan26_full.md` Ch 10 (line 519)

### Ch 11: Retrieval-based Models (pp. 235-257)
**핵심**: TF-IDF 기반 정보 검색부터 밀집 벡터 검색(dense retrieval)까지 다룬다. IR 시스템 평가(정밀도, 재현율, MAP)를 설명하고, 검색 증강 생성(RAG)의 원리를 소개한다. QA 데이터셋과 평가 방법을 다룬다.
**키워드**: `information retrieval`, `RAG`, `dense retrieval`, `TF-IDF`, `QA evaluation`
**상세**: → `Speech and Language Processing, 3rd Ed_jan26_full.md` Ch 11 (line 537)

### Ch 12: Machine Translation (pp. 258-283)
**핵심**: 언어 간 발산과 유형론적 차이를 설명한다. 인코더-디코더 모델을 MT에 적용하는 방법, 빔 서치 디코딩을 다룬다. 저자원 번역, BLEU/COMET 기반 MT 평가, 편향과 윤리적 문제를 논의한다.
**키워드**: `encoder-decoder`, `beam search`, `BLEU`, `low-resource`, `language typology`
**상세**: → `Speech and Language Processing, 3rd Ed_jan26_full.md` Ch 12 (line 578)

### Ch 13: RNNs and LSTMs (pp. 284-309)
**핵심**: RNN의 기본 구조와 언어 모델링 적용을 설명한다. 스택/양방향 RNN, LSTM의 게이트 메커니즘을 다룬다. RNN 기반 인코더-디코더 모델과 어텐션 메커니즘을 소개한다.
**키워드**: `RNN`, `LSTM`, `gated units`, `encoder-decoder`, `attention`
**상세**: → `Speech and Language Processing, 3rd Ed_jan26_full.md` Ch 13 (line 611)

### Ch 14: Phonetics and Speech Feature Extraction (pp. 310-338)
**핵심**: 음성학적 전사와 조음 음성학(자음/모음 분류)을 설명한다. 운율(강세, 억양)과 음향 음성학(파형, 스펙트럼, 포르만트)을 다룬다. 로그 멜 스펙트럼과 MFCC 특징 추출 과정을 상세히 유도한다.
**키워드**: `phonetics`, `mel spectrum`, `MFCC`, `spectrogram`, `prosody`, `articulation`
**상세**: → `Speech and Language Processing, 3rd Ed_jan26_full.md` Ch 14 (line 638)

### Ch 15: Automatic Speech Recognition (pp. 339-364)
**핵심**: ASR 태스크를 정의하고, CNN 기반 음향 모델을 설명한다. 인코더-디코더 ASR 아키텍처와 자기지도 모델(HuBERT)을 소개한다. CTC(Connectionist Temporal Classification) 알고리즘과 WER(단어 오류율) 평가를 다룬다.
**키워드**: `ASR`, `CTC`, `HuBERT`, `WER`, `encoder-decoder`, `CNN acoustic model`
**상세**: → `Speech and Language Processing, 3rd Ed_jan26_full.md` Ch 15 (line 687)

### Ch 16: Text-to-Speech (pp. 365-378)
**핵심**: TTS 시스템의 전체 파이프라인을 설명한다. 오디오 코덱을 이용한 이산 오디오 토큰 학습, VALL-E의 2단계 LM 기반 음성 생성을 다룬다. TTS 평가와 음성 언어 모델(spoken language models)을 소개한다.
**키워드**: `TTS`, `VALL-E`, `audio codec`, `spoken language models`, `speech synthesis`
**상세**: → `Speech and Language Processing, 3rd Ed_jan26_full.md` Ch 16 (line 732)

### Ch 17: Sequence Labeling (pp. 382-405)
**핵심**: 품사 태깅과 개체명 인식(NER)을 위한 시퀀스 레이블링을 다룬다. HMM 기반 품사 태깅(비터비 알고리즘)과 CRF(조건부 랜덤 필드)를 설명한다. NER 평가 방법을 제시한다.
**키워드**: `POS tagging`, `NER`, `HMM`, `Viterbi`, `CRF`, `sequence labeling`
**상세**: → `Speech and Language Processing, 3rd Ed_jan26_full.md` Ch 17 (line 779)

### Ch 18: Context-Free Grammars and Constituency Parsing (pp. 407-429)
**핵심**: 구성소(constituency)와 문맥 자유 문법(CFG)의 형식적 정의를 제공한다. 트리뱅크, 문법 동치와 정규형, 구조적 모호성을 설명한다. CKY 동적 프로그래밍 파싱과 신경망 기반 구간(span) 파서를 다룬다.
**키워드**: `CFG`, `CKY parsing`, `treebank`, `constituency`, `ambiguity`, `span-based parsing`
**상세**: → `Speech and Language Processing, 3rd Ed_jan26_full.md` Ch 18 (line 819)

### Ch 19: Dependency Parsing (pp. 431-454)
**핵심**: 의존 관계(dependency relations)를 정의하고, 전이 기반(transition-based) 파싱(아크 표준 시스템, 신경망 분류기)을 설명한다. 그래프 기반(graph-based) 파싱(최대 스패닝 트리)을 다루고, UAS/LAS 평가 지표를 소개한다.
**키워드**: `dependency parsing`, `transition-based`, `graph-based`, `UAS`, `LAS`
**상세**: → `Speech and Language Processing, 3rd Ed_jan26_full.md` Ch 19 (line 875)

### Ch 20: Information Extraction (pp. 455-480)
**핵심**: 관계 추출(패턴, 지도 학습, 반지도, 원격 감독)과 이벤트 추출을 다룬다. 시간 표현(TimeML, TimeBank)과 양상(aspect) 표현을 설명한다. 템플릿 채우기 과제를 소개한다.
**키워드**: `relation extraction`, `event extraction`, `temporal analysis`, `distant supervision`, `template filling`
**상세**: → `Speech and Language Processing, 3rd Ed_jan26_full.md` Ch 20 (line 903)

### Ch 21: Semantic Role Labeling (pp. 481-500)
**핵심**: 의미역(thematic roles)과 태도 교체(diathesis alternation)를 설명한다. PropBank과 FrameNet의 구조를 비교하고, 신경망 기반 SRL 시스템을 소개한다. 선택 제약과 술어 분해도 다룬다.
**키워드**: `semantic roles`, `PropBank`, `FrameNet`, `SRL`, `selectional restrictions`
**상세**: → `Speech and Language Processing, 3rd Ed_jan26_full.md` Ch 21 (line 940)

### Ch 22: Lexicons for Sentiment, Affect, and Connotation (pp. 501-520)
**핵심**: 감정의 정의(기본 감정, 차원 모델)와 감성/정서 사전을 소개한다. 인간 레이블링, 반지도/지도 학습을 통한 사전 구축 방법을 설명한다. 사전 기반 감성/정서 인식과 함축 프레임(connotation frames)을 다룬다.
**키워드**: `sentiment lexicon`, `affect`, `connotation frames`, `emotion`, `opinion mining`
**상세**: → `Speech and Language Processing, 3rd Ed_jan26_full.md` Ch 22 (line 974)

### Ch 23: Coreference Resolution and Entity Linking (pp. 521-550)
**핵심**: 상호 참조 현상(대명사, 명사구 조응)의 언어학적 배경을 설명한다. 멘션 검출, 신경망 기반 멘션 랭킹 알고리즘, 엔티티 링킹을 다룬다. 상호 참조에서의 성별 편향 문제와 위노그래드 스키마를 논의한다.
**키워드**: `coreference resolution`, `entity linking`, `mention ranking`, `Winograd schema`, `gender bias`
**상세**: → `Speech and Language Processing, 3rd Ed_jan26_full.md` Ch 23 (line 1021)

### Ch 24: Discourse Coherence (pp. 551-572)
**핵심**: 담화 일관성 관계(수사 구조 이론 등)와 담화 구조 파싱을 설명한다. 센터링 이론과 엔티티 기반 일관성, 표현 학습 기반 지역/전역 일관성 모델을 다룬다.
**키워드**: `discourse coherence`, `RST`, `centering theory`, `entity-based coherence`
**상세**: → `Speech and Language Processing, 3rd Ed_jan26_full.md` Ch 24 (line 1065)

### Ch 25: Conversation and its Structure (pp. 573-580)
**핵심**: 인간 대화의 속성(턴 테이킹, 인접 쌍, 기반 형성)을 분석한다. 대화 행위(dialog acts)와 대화 코퍼스를 소개한다.
**키워드**: `dialog acts`, `turn-taking`, `adjacency pairs`, `grounding`, `conversation structure`
**상세**: → `Speech and Language Processing, 3rd Ed_jan26_full.md` Ch 25 (line 1101)
