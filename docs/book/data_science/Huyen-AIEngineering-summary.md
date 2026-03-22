---
name: "AI Engineering: Building Applications with Foundation Models"
type: book-summary
authors: "Chip Huyen"
year: 2025
total_pages: 512
language: en
keywords: [foundation-models, LLM, prompt-engineering, RAG, agents, finetuning, inference-optimization, AI-engineering, evaluation, dataset-engineering]
---

# AI Engineering: Building Applications with Foundation Models — Summary

> Chip Huyen (2025), 512 pages, 10 chapters + Epilogue
> 파운데이션 모델 기반 AI 애플리케이션의 설계·배포·운영 전 과정을 체계적으로 다루는 실무 가이드이다.

## Contents

- Preface
- Ch 1: Introduction to Building AI Applications with Foundation Models
- Ch 2: Understanding Foundation Models
- Ch 3: Evaluation Methodology
- Ch 4: Evaluate AI Systems
- Ch 5: Prompt Engineering
- Ch 6: RAG and Agents
- Ch 7: Finetuning
- Ch 8: Dataset Engineering
- Ch 9: Inference Optimization
- Ch 10: AI Engineering Architecture and User Feedback
- Epilogue
- Index

---

## Chapter Summaries

> Marker 원본: `Huyen-AIEngineering_marker_full.md` | 총 ~9,884 라인 | `L:숫자`로 직접 접근 가능


### Ch 1: Introduction to Building AI Applications with Foundation Models (pp. 1-47)
**핵심**: 언어 모델에서 대규모 언어 모델(LLM), 파운데이션 모델로의 발전 과정을 추적한다. 코딩, 이미지/비디오 생성, 작문, 교육, 대화형 봇, 정보 집계, 데이터 정리, 워크플로 자동화 등 주요 활용 사례를 분류한다. AI 엔지니어링 스택의 3계층 구조를 제시하고, ML 엔지니어링 및 풀스택 엔지니어링과의 차이를 명확히 구분한다. 활용 사례 평가, 기대치 설정, 마일스톤 계획, 유지보수까지 AI 애플리케이션 기획 전 과정을 안내한다.
**키워드**: `foundation-models`, `AI-engineering-stack`, `use-case-evaluation`, `milestone-planning`
**상세**: → `Huyen-AIEngineering_marker_full.md` Ch 1 (L:520)
AI 모델의 스케일 확대가 두 가지 결과를 낳았다: (1) 더 많은 태스크를 수행할 수 있는 강력한 모델, (2) model-as-a-service의 등장으로 AI 애플리케이션 구축 진입 장벽 하락. 언어 모델(LM)에서 대규모 언어 모델(LLM), 파운데이션 모델로의 발전 과정을 추적하며, 자기지도학습(self-supervision)이 대규모 학습을 가능하게 한 핵심 기술임을 설명한다. masked language model(BERT)과 autoregressive language model(GPT)의 차이를 설명하고, 후자가 텍스트 생성에 주로 사용된다. "파운데이션 모델"이라는 용어는 2021년 Stanford HAI에서 제안되었으며, 하나의 모델이 다양한 태스크의 기반(foundation)이 됨을 의미한다. 주요 활용 사례를 8가지로 분류한다: 코딩(GitHub Copilot), 이미지/비디오 생성(Midjourney, DALL-E), 작문 보조, 교육(개인 튜터), 대화형 봇(고객 지원), 정보 집계(검색 증강), 데이터 정리/변환, 워크플로 자동화. AI 엔지니어링 스택은 3계층(모델 레이어, 도구/인프라 레이어, 애플리케이션 레이어)으로 구성되며, ML 엔지니어링이 모델 학습에 집중하는 것과 달리 AI 엔지니어링은 기존 모델 위에 애플리케이션을 구축하는 데 집중한다. AI 애플리케이션 기획 시 활용 사례 평가(가능성, 비용 대비 가치), 기대치 설정(AI의 한계 인식), 마일스톤 계획, 유지보수 전략을 체계적으로 수립해야 한다. 전통 ML과 AI 엔지니어링의 차이로, AI 엔지니어링은 학습 없이도 프롬프팅만으로 모델 사용이 가능하고 평가와 프롬프트 엔지니어링이 핵심 역량이 된다.

### Ch 2: Understanding Foundation Models (pp. 49-111)
**핵심**: 학습 데이터(다국어 모델, 도메인 특화 모델), 모델 아키텍처(인코더/디코더/인코더-디코더), 모델 크기의 스케일링 법칙을 분석한다. SFT(지도 파인튜닝)와 선호도 파인튜닝(RLHF)을 포함한 포스트-트레이닝 과정을 설명한다. 샘플링 기본 원리와 전략(temperature, top-k, top-p), 테스트 타임 컴퓨트, 구조화된 출력 생성, AI의 확률적 특성을 상세히 다룬다.
**키워드**: `model-architecture`, `post-training`, `SFT`, `RLHF`, `sampling`, `structured-outputs`
**상세**: → `Huyen-AIEngineering_marker_full.md` Ch 2 (L:1077)
파운데이션 모델의 학습 데이터는 모델의 역량을 결정하며, 다국어 데이터로 학습하면 다국어 모델이, 코드 데이터를 포함하면 코드 생성이 가능해진다. 모델 아키텍처를 인코더(BERT, 양방향 문맥 이해), 디코더(GPT, 자기회귀 생성), 인코더-디코더(T5, 번역/요약)로 분류하며, 현재 대부분의 LLM은 디코더 전용 아키텍처를 사용한다. Transformer 기반 모델의 스케일링 법칙(Chinchilla 법칙)을 설명하며, 모델 크기와 학습 데이터 양의 최적 비율을 분석한다. 포스트-트레이닝(post-training) 과정으로 SFT(지도 파인튜닝, instruction-response 쌍으로 학습)와 선호도 파인튜닝(RLHF: 인간 피드백 기반 강화학습, DPO: 직접 선호도 최적화)을 설명한다. 추론 시 샘플링 전략으로 greedy decoding, temperature scaling(분포 뾰족함 조절), top-k(상위 k개 후보), top-p/nucleus sampling(누적 확률 기반 동적 후보 선정)을 비교한다. 테스트 타임 컴퓨트(test-time compute)는 추론 시 더 많은 연산을 투자하여 성능을 향상시키는 기법으로, chain-of-thought, self-consistency, tree-of-thought 등이 포함된다. 구조화된 출력(structured outputs) 생성을 위해 JSON 모드, 함수 호출, 문법 기반 제약(constrained decoding)을 사용한다. AI의 확률적 특성으로 인해 동일 프롬프트에도 매번 다른 출력이 생성될 수 있으며, 이를 제어하기 위한 seed 설정과 temperature 조절을 설명한다.

### Ch 3: Evaluation Methodology (pp. 113-156)
**핵심**: 파운데이션 모델 평가의 고유한 어려움을 분석하고, 엔트로피·크로스 엔트로피·비트-퍼-바이트·퍼플렉시티 등 언어 모델 메트릭을 설명한다. 기능 정확성·유사도 측정(BLEU, ROUGE 등)을 포함한 정확 평가와 임베딩 개념을 소개한다. AI-as-a-Judge 접근법의 사용법, 한계, 적합 모델을 논의하고, 비교 평가를 통한 모델 랭킹 방법을 제시한다.
**키워드**: `perplexity`, `exact-evaluation`, `AI-judge`, `comparative-evaluation`, `embedding`
**상세**: → `Huyen-AIEngineering_marker_full.md` Ch 3 (L:2389)
파운데이션 모델 평가가 전통 ML 평가보다 어려운 이유를 분석한다: 개방형 생성 태스크의 정답이 불명확하고, 평가 기준이 주관적이며, 모델의 능력 범위가 광범위하다. 언어 모델 메트릭으로 엔트로피(불확실성 측정), 크로스 엔트로피(모델 분포와 실제 분포의 차이), 비트-퍼-바이트(BPB, 토크나이저 독립적 비교), 퍼플렉시티(perplexity = exp(cross-entropy), 모델이 "혼란스러워하는" 정도)를 단계적으로 설명한다. 정확 평가(exact evaluation)로 기능 정확성(패턴 매칭, 정규표현식 기반), 유사도 측정(BLEU-n-gram 정밀도, ROUGE-재현율 기반, BERTScore-의미적 유사도)을 다룬다. 임베딩(embedding)의 개념과 활용을 소개하며, 문장/문서 임베딩을 통한 의미적 유사도 측정, 벡터 공간에서의 거리 계산(코사인 유사도, 유클리드 거리)을 설명한다. AI-as-a-Judge 접근법은 LLM을 활용하여 다른 LLM의 출력을 평가하는 방법으로, 평가 프롬프트 설계, 점수 스케일(1-5 vs. 1-10), 루브릭 기반 평가를 다룬다. AI-as-a-Judge의 한계로 위치 편향(첫 번째 답변 선호), 자기 편향(같은 모델 계열 선호), 장문 편향(긴 답변 선호)을 분석하고, 이를 완화하는 전략을 제시한다. 비교 평가(comparative evaluation)에서 ELO 레이팅 시스템과 pairwise comparison을 통한 모델 랭킹 방법을 설명한다.

### Ch 4: Evaluate AI Systems (pp. 159-208)
**핵심**: 도메인 특화 역량, 생성 역량(환각 포함), 지시 따르기 역량, 비용·지연시간 등 평가 기준을 정의한다. 모델 선택 워크플로와 모델 build vs. buy 의사결정 프레임워크를 제시한다. 공개 벤치마크의 활용법과 한계를 분석하고, 시스템 전체 컴포넌트 평가·평가 가이드라인 작성·평가 방법 및 데이터 정의의 3단계 평가 파이프라인을 설계한다.
**키워드**: `model-selection`, `benchmarks`, `evaluation-pipeline`, `hallucination`, `cost-latency`
**상세**: → `Huyen-AIEngineering_marker_full.md` Ch 4 (L:3165)
평가 기준을 4가지 범주로 체계화한다: (1) 도메인 특화 역량(의료, 법률 등 전문 지식), (2) 생성 역량(유창성, 일관성, 환각 감지), (3) 지시 따르기 역량(형식 준수, 길이 제한, 안전성), (4) 비용·지연시간(토큰당 비용, TTFT, 처리량). 환각(hallucination)을 두 유형으로 구분한다: context hallucination(주어진 문맥과 모순되는 출력)과 knowledge hallucination(사실과 다른 출력). 모델 선택 워크플로를 제시하며, 요구사항 정의 → 후보 모델 식별 → 벤치마크 평가 → 실제 태스크 평가 → 비용-성능 트레이드오프 분석의 단계를 설명한다. 모델 build vs. buy 결정 프레임워크로 데이터 프라이버시, 커스터마이징 필요성, 비용 구조, 레이턴시 요구사항을 고려한다. 공개 벤치마크(MMLU, HumanEval, HellaSwag, TruthfulQA 등)의 유용성과 한계(데이터 오염, 태스크 특화성 부족, 벤치마크 해킹)를 분석한다. 시스템 전체 평가를 위한 3단계 파이프라인을 설계한다: (1) 각 컴포넌트별 평가 기준 정의, (2) 평가 가이드라인 작성(루브릭, 예시 포함), (3) 평가 방법(자동/수동/AI-Judge)과 평가 데이터 구성. A/B 테스트와 shadow deployment를 통한 온라인 평가 방법도 소개한다.

### Ch 5: Prompt Engineering (pp. 211-251)
**핵심**: 제로샷·퓨샷 인컨텍스트 학습, 시스템/사용자 프롬프트 구분, 컨텍스트 길이와 효율성을 다룬다. 명확한 지시 작성, 충분한 맥락 제공, 복잡한 작업 분해, 사고 시간 부여 등 모범 사례를 정리한다. 프롬프트 반복·도구 평가·버전 관리를 설명하고, 프롬프트 리버스 엔지니어링, 탈옥·인젝션 공격, 정보 추출 위험과 방어 전략을 다룬다.
**키워드**: `zero-shot`, `few-shot`, `prompt-injection`, `jailbreaking`, `defensive-prompting`
**상세**: → `Huyen-AIEngineering_marker_full.md` Ch 5 (L:4095)
프롬프트 엔지니어링의 기본 개념으로 제로샷(예시 없이 지시만), 퓨샷(소수 예시 제공), 인컨텍스트 학습(프롬프트 내 정보로 모델 행동 조절)을 설명한다. 시스템 프롬프트(모델의 전반적 행동 규칙 정의)와 사용자 프롬프트(구체적 요청)의 구분과 각각의 역할을 다룬다. 컨텍스트 길이(context window)의 제약과 효율성 문제를 분석하며, 긴 프롬프트는 비용 증가와 "중간 상실(lost in the middle)" 현상을 유발할 수 있다. 프롬프트 작성 모범 사례를 체계화한다: 명확하고 구체적인 지시 작성, 충분한 맥락 제공, 복잡한 작업의 하위 작업으로 분해, 모델에 "사고 시간" 부여(chain-of-thought). Chain-of-thought(CoT) 프롬프팅은 모델이 단계별로 추론하도록 유도하며, "Let's think step by step" 같은 트리거 문구 또는 명시적 추론 단계 예시로 구현한다. 프롬프트 반복(iteration) 과정에서 체계적 실험, A/B 테스트, 평가 데이터셋 기반 비교의 중요성을 강조한다. 프롬프트 보안 위협으로 탈옥(jailbreaking: 안전 가드레일 우회), 프롬프트 인젝션(사용자 입력이 시스템 프롬프트를 오버라이드), 정보 추출(시스템 프롬프트 유출)을 분류한다. 방어 전략으로 입력 필터링, 출력 검증, 가드레일 모델 적용, 프롬프트 격리(시스템/사용자 프롬프트 분리), 레드팀 테스트를 제시한다. 프롬프트 버전 관리와 재현 가능성 확보를 위한 프롬프트 관리 시스템의 필요성을 설명한다.

### Ch 6: RAG and Agents (pp. 253-305)
**핵심**: RAG 아키텍처와 검색 알고리즘(키워드·시맨틱·하이브리드)을 분석하고 검색 최적화 전략을 제시한다. 텍스트 이외의 RAG 활용을 포함한다. 에이전트 개요, 도구 사용, 계획 수립(반성, 함수 호출, 코드 생성 등 다양한 접근법)을 설명한다. 에이전트의 실패 모드와 평가 방법, 단기·장기 메모리 관리를 다룬다.
**키워드**: `RAG`, `retrieval-algorithms`, `agents`, `tool-use`, `planning`, `memory`
**상세**: → `Huyen-AIEngineering_marker_full.md` Ch 6 (L:5138)
RAG(Retrieval-Augmented Generation)는 모델의 지식을 외부 데이터로 보강하여 환각을 줄이고 최신 정보를 제공하는 아키텍처이다. RAG 파이프라인은 인덱싱(문서 청킹 → 임베딩 → 벡터 DB 저장), 검색(쿼리와 유사한 문서 검색), 생성(검색 결과를 컨텍스트로 포함하여 응답 생성)의 3단계로 구성된다. 검색 알고리즘을 키워드 기반(BM25, TF-IDF), 시맨틱(임베딩 유사도, ANN 검색), 하이브리드(키워드 + 시맨틱 결합)로 분류하며, 각각의 장단점을 비교한다. 검색 최적화 전략으로 쿼리 재작성(query rewriting), 재순위화(re-ranking, cross-encoder 사용), 청킹 전략(고정 크기, 문장 단위, 의미 단위)을 다룬다. 에이전트(agent)는 LLM이 외부 도구를 사용하고 자율적으로 계획을 수립하여 복잡한 태스크를 수행하는 시스템이다. 에이전트의 핵심 구성요소로 계획 수립(반성/reflection, 함수 호출, 코드 생성), 도구 사용(API 호출, 검색, 계산), 메모리(단기: 대화 히스토리, 장기: 외부 저장소)를 설명한다. 에이전트의 실패 모드로 무한 루프, 잘못된 도구 선택, 도구 실행 오류, 과도한 비용 소모를 분석하고, 각각의 완화 전략을 제시한다. 에이전트 평가의 어려움과 엔드-투-엔드 평가(최종 결과 평가) vs. 단계별 평가(각 스텝의 정확성 평가) 접근법을 비교한다. 멀티 에이전트 시스템에서 에이전트 간 협력과 오케스트레이션 패턴을 소개한다.

### Ch 7: Finetuning (pp. 307-361)
**핵심**: 파인튜닝의 이유(도메인 적응, 성능 개선)와 하지 않아야 할 이유(비용, 데이터 부족)를 정리하고, 파인튜닝과 RAG의 관계를 설명한다. 역전파와 학습 가능 파라미터, 메모리 계산, 수치 표현(FP32/FP16/BF16), 양자화(INT8/INT4)로 인한 메모리 병목을 분석한다. LoRA 등 파라미터 효율적 파인튜닝(PEFT), 모델 병합, 멀티태스크 파인튜닝 기법을 다룬다.
**키워드**: `PEFT`, `LoRA`, `quantization`, `model-merging`, `memory-optimization`
**상세**: → `Huyen-AIEngineering_marker_full.md` Ch 7 (L:6244)
파인튜닝을 해야 하는 경우(도메인 적응, 성능 개선, 모델 크기 축소, 레이턴시 감소)와 하지 않아야 하는 경우(데이터 부족, 빈번한 업데이트 필요, 비용 제약)를 체계적으로 정리한다. 파인튜닝과 RAG의 관계를 설명하며, 두 기법은 상호 배타적이 아니라 보완적이고, RAG로 시작한 후 파인튜닝으로 성능을 추가 향상시키는 전략을 제안한다. 역전파(backpropagation)와 학습 가능 파라미터의 개념을 복습하며, 파인튜닝 시 모델의 모든 파라미터 또는 일부만 업데이트하는 전략을 비교한다. 메모리 병목을 분석하며, 7B 모델의 전체 파인튜닝에 필요한 메모리를 계산한다: 모델 파라미터(FP32: 28GB), gradient(28GB), optimizer state(Adam: 56GB), 활성화 메모리 등. 수치 표현 형식으로 FP32(32비트), FP16(16비트, 동적 범위 제한), BF16(16비트, 넓은 동적 범위), TF32를 비교한다. 양자화(quantization)로 INT8, INT4, NF4(Normal Float 4)를 다루며, QLoRA(양자화 + LoRA)가 메모리 효율적 파인튜닝의 표준이 되고 있다. LoRA(Low-Rank Adaptation)는 가중치 업데이트를 저랭크 행렬 분해(A×B)로 근사하여 학습 파라미터를 대폭 줄이며, rank, alpha, target modules가 핵심 하이퍼파라미터이다. 모델 병합(model merging)은 여러 파인튜닝 모델의 가중치를 결합하여 다중 능력을 가진 단일 모델을 만드는 기법으로, TIES-Merging, DARE 등의 방법을 소개한다. 멀티태스크 파인튜닝은 여러 태스크의 데이터를 혼합하여 단일 모델을 학습시키며, 태스크 간 가중치 조절이 핵심이다.

### Ch 8: Dataset Engineering (pp. 363-403)
**핵심**: 데이터 품질, 커버리지, 수량의 관점에서 데이터 큐레이션을 설명한다. 데이터 획득·어노테이션 방법론과 전통적 데이터 합성 기법 및 AI 기반 데이터 합성(모델 증류 포함)을 비교한다. 데이터 검사, 중복 제거, 클리닝·필터링, 포맷팅으로 구성된 데이터 처리 파이프라인을 정리한다.
**키워드**: `data-quality`, `data-synthesis`, `model-distillation`, `data-curation`, `annotation`
**상세**: → `Huyen-AIEngineering_marker_full.md` Ch 8 (L:7240)
데이터 큐레이션의 3가지 축을 정의한다: 품질(정확성, 일관성, 최신성), 커버리지(태스크/도메인/언어별 분포), 수량(양이 많을수록 성능 향상, 단 수확체감). 데이터 획득 방법으로 공개 데이터셋 활용, 웹 크롤링, 내부 데이터 수집, 사용자 피드백 기반 수집을 비교하며, 각 방법의 품질-비용 트레이드오프를 분석한다. 어노테이션(annotation) 방법론으로 전문가 어노테이션(고품질, 고비용), 크라우드소싱(대규모, 품질 관리 필요), AI 보조 어노테이션(LLM 기반 사전 라벨링 + 인간 검증)을 비교한다. 전통적 데이터 합성 기법으로 규칙 기반 생성, 템플릿 기반 변형, 시뮬레이션을 설명하고, AI 기반 데이터 합성으로 LLM을 활용한 instruction 생성(Self-Instruct), 응답 생성, 피드백 생성을 다룬다. 모델 증류(model distillation)는 강한 teacher 모델의 출력을 학습 데이터로 사용하여 작은 student 모델을 학습시키는 기법으로, 비용 효율적이지만 teacher 모델의 이용 약관 준수가 필요하다. 데이터 처리 파이프라인은 데이터 검사(형식 검증, 이상치 탐지) → 중복 제거(exact/near-duplicate 감지, MinHash) → 클리닝/필터링(노이즈 제거, PII 마스킹, 유해 콘텐츠 필터링) → 포맷팅(모델 입력 형식으로 변환)의 단계로 구성된다. 데이터 품질 관리에서 inter-annotator agreement(Fleiss' kappa, Cohen's kappa), 골드 스탠다드 데이터셋, 데이터 버저닝의 중요성을 강조한다.

### Ch 9: Inference Optimization (pp. 405-447)
**핵심**: 추론 과정의 개요와 성능 메트릭(지연시간, 처리량, 비용)을 정의하고 AI 가속기(GPU, TPU 등)의 특성을 소개한다. 모델 수준 최적화(양자화, 가지치기, 지식 증류)와 추론 서비스 수준 최적화(배칭, 캐싱, 병렬화)를 구분하여 실무 적용 방법을 설명한다.
**키워드**: `inference-latency`, `AI-accelerators`, `model-optimization`, `batching`, `parallelism`
**상세**: → `Huyen-AIEngineering_marker_full.md` Ch 9 (L:7974)
LLM 추론 과정을 prefill(프롬프트 처리, 병렬 가능)과 decode(토큰 순차 생성, 메모리 바운드)의 2단계로 구분하며, 각 단계의 연산 특성이 다름을 설명한다. 핵심 성능 메트릭으로 TTFT(Time to First Token), TPOT(Time Per Output Token), throughput(초당 토큰 수), 비용(토큰당 달러)을 정의한다. AI 가속기로 GPU(NVIDIA A100, H100), TPU(Google), 커스텀 칩(AWS Inferentia, Groq LPU)의 특성을 비교하며, 메모리 대역폭이 LLM 추론의 주요 병목임을 분석한다. 모델 수준 최적화로 양자화(INT8/INT4로 메모리와 연산 감소), 가지치기(구조적/비구조적 파라미터 제거), 지식 증류(큰 모델 → 작은 모델), 스펙트럼 프루닝을 다룬다. KV 캐시 최적화가 추론 효율의 핵심이며, MHA(Multi-Head Attention) → MQA(Multi-Query Attention, 모든 head가 KV 공유) → GQA(Grouped Query Attention, 그룹별 KV 공유)의 발전을 설명한다. 추론 서비스 수준 최적화로 연속 배칭(continuous batching, 완료된 요청 즉시 교체), 프리픽스 캐싱(공통 시스템 프롬프트 캐싱), 스펙룰레이티브 디코딩(작은 draft 모델로 후보 생성 후 큰 모델이 검증)을 소개한다. 병렬화 전략으로 텐서 병렬(단일 레이어를 여러 GPU에 분산), 파이프라인 병렬(레이어를 순차적으로 분배), 시퀀스 병렬(긴 시퀀스를 분할 처리)을 설명한다. FlashAttention은 GPU의 SRAM을 활용하여 attention 연산의 메모리 접근을 최적화하는 기법으로, 학습과 추론 모두에서 속도 향상을 제공한다.

### Ch 10: AI Engineering Architecture and User Feedback (pp. 449-492)
**핵심**: 컨텍스트 강화 → 가드레일 → 모델 라우터/게이트웨이 → 캐시 → 에이전트 패턴의 5단계 아키텍처를 제시한다. 모니터링·관찰 가능성 체계와 AI 파이프라인 오케스트레이션을 다룬다. 대화형 피드백 추출, 피드백 UI 설계, 피드백의 한계를 포함하는 사용자 피드백 루프로 지속적 개선 체계를 설명한다.
**키워드**: `guardrails`, `model-router`, `caching`, `monitoring`, `user-feedback`, `observability`
**상세**: → `Huyen-AIEngineering_marker_full.md` Ch 10 (L:8517)
AI 애플리케이션의 프로덕션 아키텍처를 5단계 패턴으로 제시한다: (1) 컨텍스트 강화(RAG, 프롬프트 구성), (2) 가드레일(입력/출력 필터링, 안전성 검증), (3) 모델 라우터/게이트웨이(복수 모델 간 요청 라우팅, 비용-성능 최적화), (4) 캐시(동일/유사 요청에 대한 응답 캐싱, 의미적 캐싱), (5) 에이전트 패턴(복잡한 워크플로 오케스트레이션). 모니터링과 관찰 가능성(observability) 체계를 설명하며, 시스템 메트릭(레이턴시, 에러율, 처리량)과 ML 메트릭(출력 품질, 환각률, 사용자 만족도)을 모두 추적해야 한다. AI 파이프라인 오케스트레이션으로 LangChain, LlamaIndex 등의 프레임워크와 DAG 기반 워크플로 관리를 소개하며, 복잡도 관리의 중요성을 강조한다. 사용자 피드백 루프는 AI 시스템의 지속적 개선을 위한 핵심 메커니즘으로, 명시적 피드백(좋아요/싫어요, 평점)과 암묵적 피드백(사용 패턴, 이탈률)을 수집한다. 대화형 피드백 추출에서 자연스러운 대화 흐름 내에서 피드백을 수집하는 방법과, 피드백 UI 설계 시 사용자 경험을 해치지 않으면서 유용한 데이터를 얻는 균형을 다룬다. 피드백의 한계로 선택 편향(만족/불만족 극단만 피드백), 정량화 어려움, 노이즈를 분석한다. 수집된 피드백을 파인튜닝 데이터, 프롬프트 개선, 가드레일 업데이트에 활용하는 closed-loop 시스템을 설계한다. A/B 테스트, 카나리 배포, 섀도우 모드를 통한 모델 업데이트 전략과 롤백 메커니즘을 설명한다.


### 기타 섹션 (Marker)

- Introduction to Building AI Applications with Foundation Models (p.24) `L:520`
- Challenges of Evaluating Foundation Models `L:2389`
- AI Engineering Architecture and User Feedback (p.472) `L:8517`
