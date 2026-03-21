---
name: "AI Engineering: Building Applications with Foundation Models"
type: book-summary
source_file: "Huyen-AIEngineering_full.md"
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

### Ch 1: Introduction to Building AI Applications with Foundation Models (pp. 1-47)
**핵심**: 언어 모델에서 대규모 언어 모델(LLM), 파운데이션 모델로의 발전 과정을 추적한다. 코딩, 이미지/비디오 생성, 작문, 교육, 대화형 봇, 정보 집계, 데이터 정리, 워크플로 자동화 등 주요 활용 사례를 분류한다. AI 엔지니어링 스택의 3계층 구조를 제시하고, ML 엔지니어링 및 풀스택 엔지니어링과의 차이를 명확히 구분한다. 활용 사례 평가, 기대치 설정, 마일스톤 계획, 유지보수까지 AI 애플리케이션 기획 전 과정을 안내한다.
**키워드**: `foundation-models`, `AI-engineering-stack`, `use-case-evaluation`, `milestone-planning`
**상세**: → `AI_ENGINEERING_BUILDING_APPLICATIONS_WITH_FOUNDATION_MODELS_BY_C_full.md` Ch 1 (line 187)

### Ch 2: Understanding Foundation Models (pp. 49-111)
**핵심**: 학습 데이터(다국어 모델, 도메인 특화 모델), 모델 아키텍처(인코더/디코더/인코더-디코더), 모델 크기의 스케일링 법칙을 분석한다. SFT(지도 파인튜닝)와 선호도 파인튜닝(RLHF)을 포함한 포스트-트레이닝 과정을 설명한다. 샘플링 기본 원리와 전략(temperature, top-k, top-p), 테스트 타임 컴퓨트, 구조화된 출력 생성, AI의 확률적 특성을 상세히 다룬다.
**키워드**: `model-architecture`, `post-training`, `SFT`, `RLHF`, `sampling`, `structured-outputs`
**상세**: → `AI_ENGINEERING_BUILDING_APPLICATIONS_WITH_FOUNDATION_MODELS_BY_C_full.md` Ch 2 (line 215)

### Ch 3: Evaluation Methodology (pp. 113-156)
**핵심**: 파운데이션 모델 평가의 고유한 어려움을 분석하고, 엔트로피·크로스 엔트로피·비트-퍼-바이트·퍼플렉시티 등 언어 모델 메트릭을 설명한다. 기능 정확성·유사도 측정(BLEU, ROUGE 등)을 포함한 정확 평가와 임베딩 개념을 소개한다. AI-as-a-Judge 접근법의 사용법, 한계, 적합 모델을 논의하고, 비교 평가를 통한 모델 랭킹 방법을 제시한다.
**키워드**: `perplexity`, `exact-evaluation`, `AI-judge`, `comparative-evaluation`, `embedding`
**상세**: → `AI_ENGINEERING_BUILDING_APPLICATIONS_WITH_FOUNDATION_MODELS_BY_C_full.md` Ch 3 (line 235)

### Ch 4: Evaluate AI Systems (pp. 159-208)
**핵심**: 도메인 특화 역량, 생성 역량(환각 포함), 지시 따르기 역량, 비용·지연시간 등 평가 기준을 정의한다. 모델 선택 워크플로와 모델 build vs. buy 의사결정 프레임워크를 제시한다. 공개 벤치마크의 활용법과 한계를 분석하고, 시스템 전체 컴포넌트 평가·평가 가이드라인 작성·평가 방법 및 데이터 정의의 3단계 평가 파이프라인을 설계한다.
**키워드**: `model-selection`, `benchmarks`, `evaluation-pipeline`, `hallucination`, `cost-latency`
**상세**: → `AI_ENGINEERING_BUILDING_APPLICATIONS_WITH_FOUNDATION_MODELS_BY_C_full.md` Ch 4 (line 263)

### Ch 5: Prompt Engineering (pp. 211-251)
**핵심**: 제로샷·퓨샷 인컨텍스트 학습, 시스템/사용자 프롬프트 구분, 컨텍스트 길이와 효율성을 다룬다. 명확한 지시 작성, 충분한 맥락 제공, 복잡한 작업 분해, 사고 시간 부여 등 모범 사례를 정리한다. 프롬프트 반복·도구 평가·버전 관리를 설명하고, 프롬프트 리버스 엔지니어링, 탈옥·인젝션 공격, 정보 추출 위험과 방어 전략을 다룬다.
**키워드**: `zero-shot`, `few-shot`, `prompt-injection`, `jailbreaking`, `defensive-prompting`
**상세**: → `AI_ENGINEERING_BUILDING_APPLICATIONS_WITH_FOUNDATION_MODELS_BY_C_full.md` Ch 5 (line 279)

### Ch 6: RAG and Agents (pp. 253-305)
**핵심**: RAG 아키텍처와 검색 알고리즘(키워드·시맨틱·하이브리드)을 분석하고 검색 최적화 전략을 제시한다. 텍스트 이외의 RAG 활용을 포함한다. 에이전트 개요, 도구 사용, 계획 수립(반성, 함수 호출, 코드 생성 등 다양한 접근법)을 설명한다. 에이전트의 실패 모드와 평가 방법, 단기·장기 메모리 관리를 다룬다.
**키워드**: `RAG`, `retrieval-algorithms`, `agents`, `tool-use`, `planning`, `memory`
**상세**: → `AI_ENGINEERING_BUILDING_APPLICATIONS_WITH_FOUNDATION_MODELS_BY_C_full.md` Ch 6 (line 299)

### Ch 7: Finetuning (pp. 307-361)
**핵심**: 파인튜닝의 이유(도메인 적응, 성능 개선)와 하지 않아야 할 이유(비용, 데이터 부족)를 정리하고, 파인튜닝과 RAG의 관계를 설명한다. 역전파와 학습 가능 파라미터, 메모리 계산, 수치 표현(FP32/FP16/BF16), 양자화(INT8/INT4)로 인한 메모리 병목을 분석한다. LoRA 등 파라미터 효율적 파인튜닝(PEFT), 모델 병합, 멀티태스크 파인튜닝 기법을 다룬다.
**키워드**: `PEFT`, `LoRA`, `quantization`, `model-merging`, `memory-optimization`
**상세**: → `AI_ENGINEERING_BUILDING_APPLICATIONS_WITH_FOUNDATION_MODELS_BY_C_full.md` Ch 7 (line 320)

### Ch 8: Dataset Engineering (pp. 363-403)
**핵심**: 데이터 품질, 커버리지, 수량의 관점에서 데이터 큐레이션을 설명한다. 데이터 획득·어노테이션 방법론과 전통적 데이터 합성 기법 및 AI 기반 데이터 합성(모델 증류 포함)을 비교한다. 데이터 검사, 중복 제거, 클리닝·필터링, 포맷팅으로 구성된 데이터 처리 파이프라인을 정리한다.
**키워드**: `data-quality`, `data-synthesis`, `model-distillation`, `data-curation`, `annotation`
**상세**: → `AI_ENGINEERING_BUILDING_APPLICATIONS_WITH_FOUNDATION_MODELS_BY_C_full.md` Ch 8 (line 337)

### Ch 9: Inference Optimization (pp. 405-447)
**핵심**: 추론 과정의 개요와 성능 메트릭(지연시간, 처리량, 비용)을 정의하고 AI 가속기(GPU, TPU 등)의 특성을 소개한다. 모델 수준 최적화(양자화, 가지치기, 지식 증류)와 추론 서비스 수준 최적화(배칭, 캐싱, 병렬화)를 구분하여 실무 적용 방법을 설명한다.
**키워드**: `inference-latency`, `AI-accelerators`, `model-optimization`, `batching`, `parallelism`
**상세**: → `AI_ENGINEERING_BUILDING_APPLICATIONS_WITH_FOUNDATION_MODELS_BY_C_full.md` Ch 9 (line 364)

### Ch 10: AI Engineering Architecture and User Feedback (pp. 449-492)
**핵심**: 컨텍스트 강화 → 가드레일 → 모델 라우터/게이트웨이 → 캐시 → 에이전트 패턴의 5단계 아키텍처를 제시한다. 모니터링·관찰 가능성 체계와 AI 파이프라인 오케스트레이션을 다룬다. 대화형 피드백 추출, 피드백 UI 설계, 피드백의 한계를 포함하는 사용자 피드백 루프로 지속적 개선 체계를 설명한다.
**키워드**: `guardrails`, `model-router`, `caching`, `monitoring`, `user-feedback`, `observability`
**상세**: → `AI_ENGINEERING_BUILDING_APPLICATIONS_WITH_FOUNDATION_MODELS_BY_C_full.md` Ch 10 (line 374)
