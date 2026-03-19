---
name: BOOK_SOURCE_GUIDE
type: reference
version: 1.0
description: 교재 기반 블로그 작성 시 소스 파일 참조 규칙
scope: docs/book/
parent: AGENT_GUIDE.md
book_sources:
  - group: statistics
    path: docs/book/statistics/
    authors: Casella & Berger
  - group: linear_algebra
    path: docs/book/linear_algebra/
    authors: Strang, Magnus, Matrix Cookbook
  - group: glm
    path: docs/book/glm/
    authors: McCullagh & Nelder, Faraway
  - group: mixed_model
    path: docs/book/mixed_model/
    authors: Hedeker & Gibbons
  - group: survival
    path: docs/book/survival/
    authors: Kleinbaum, Hosmer, Klein, Collett
  - group: epidemiology
    path: docs/book/epidemiology/
    authors: Hernan, Woodward, Schulz, Maxwell, Buisson
  - group: bayesian
    path: docs/book/bayesian/
    authors: Gelman, Downey
  - group: fda
    path: docs/book/fda/
    authors: Ramsay, Kokoszka
---

# Book Source Guide — 블로그 작성용 교재 레퍼런스

## 목적

이 폴더의 md 파일들은 AI Agent가 블로그 포스트 작성 시 **교과서 기반 근거**로 활용하는 소스이다.
Quarto 렌더링 대상이 아니며(`_quarto.yml`에서 제외됨), agent가 참조 자료로만 사용한다.

## 사용 규칙

### 1. 참조 방식
- 블로그 포스트 작성 시 개념 설명의 근거로 이 소스를 참조한다.
- 직접 복사하지 않고, 내용을 이해한 뒤 블로그 스타일(한다 체)로 재작성한다.
- 출처를 명시할 때는 아래 형식을 사용한다:
  ```
  (Casella & Berger, 2002, Ch.5)
  (Hernan & Robins, 2020, Ch.3)
  ```

### 2. 블로그 포스트 작성 시 참조 흐름
```
1. 사용자가 주제를 지정 (예: "mixed model 정리해줘")
2. 해당 그룹의 소스 파일을 읽는다
3. 교과서 내용을 기반으로 개념을 정리한다
4. 씨젠 실무 맥락에 맞는 예시를 추가한다
5. AGENT_GUIDE.md의 .qmd 작성 규칙을 따라 포스트를 생성한다
```

### 3. 수식 처리
- 소스의 LaTeX 수식은 Quarto에서 그대로 사용 가능하다.
- 인라인: `$수식$`, 블록: `$$수식$$`
- Document Intelligence로 변환된 수식 중 깨진 것이 있을 수 있으므로, 의미가 불명확한 수식은 교과서 맥락에서 재구성한다.

### 4. 금지 사항
- 소스 md 파일을 직접 수정하지 않는다.
- 소스 내용을 그대로 복붙하지 않는다 (저작권).
- 소스에 없는 내용을 소스에서 나온 것처럼 인용하지 않는다.

## 소스 목록

### 통계 기초 (`statistics/`)
| 파일 | 저자 | 인용 약어 | 활용 |
|---|---|---|---|
| Casella & Berger (1).md | Casella & Berger | (Casella & Berger, 2002) | 수리통계 전반: 분포, 추정, 검정, 수렴 |
| Casella & Berger (2).md | Casella & Berger | (Casella & Berger, 2002) | 위 책의 후반부 |

### 선형대수 (`linear_algebra/`)
| 파일 | 저자 | 인용 약어 | 활용 |
|---|---|---|---|
| Gilbert Strang Introduction to Linear Algebra | Strang | (Strang, 2009) | 벡터공간, 고유값, SVD 직관적 설명 |
| Gilbert Strang Linear Algebra and Its Applications | Strang | (Strang, 2006) | 공학/응용 관점 선형대수 |
| Magnus & Neudecker Matrix Differential Calculus | Magnus & Neudecker | (Magnus & Neudecker, 1999) | 행렬 미분, REML/최적화 수학적 근거 |
| matrixcookbook.md | Petersen & Pedersen | (Petersen & Pedersen, 2012) | 행렬 미분 공식 빠른 참조 |

### GLM/회귀 (`glm/`)
| 파일 | 저자 | 인용 약어 | 활용 |
|---|---|---|---|
| McCullagh & Nelder | McCullagh & Nelder | (McCullagh & Nelder, 1989) | GLM 이론: 링크함수, 편차, 모형 선택 |
| Faraway | Faraway | (Faraway, 2016) | GLM + Mixed + Nonparametric, R코드 |

### Mixed Model (`mixed_model/`)
| 파일 | 저자 | 인용 약어 | 활용 |
|---|---|---|---|
| Hedeker & Gibbons | Hedeker & Gibbons | (Hedeker & Gibbons, 2006) | 종단 데이터, 반복측정, random effects |

### Survival Analysis (`survival/`)
| 파일 | 저자 | 인용 약어 | 활용 |
|---|---|---|---|
| Kleinbaum & Klein | Kleinbaum & Klein | (Kleinbaum & Klein, 2012) | Survival 입문, Kaplan-Meier, Cox 기초 |
| Klein & Moeschberger | Klein & Moeschberger | (Klein & Moeschberger, 2003) | Censoring/truncation 이론, counting process |
| Hosmer et al. | Hosmer, Lemeshow & May | (Hosmer et al., 2008) | Cox model 실무, 모형 진단 |
| Collett | Collett | (Collett, 2015) | 의료 데이터 survival 분석 |

### 역학/실험설계 (`epidemiology/`)
| 파일 | 저자 | 인용 약어 | 활용 |
|---|---|---|---|
| Hernan & Robins | Hernan & Robins | (Hernan & Robins, 2020) | 인과추론, DAG, IPW, g-formula |
| Woodward | Woodward | (Woodward, 2014) | 역학 study design, OR/RR/HR 해석 |
| Schulz & Grimes | Schulz & Grimes | (Schulz & Grimes, 2018) | RCT 설계/평가, 바이어스 |
| Maxwell & Delaney | Maxwell & Delaney | (Maxwell & Delaney, 2004) | 실험설계, ANOVA, 검정력, 효과크기 |
| Buisson | Buisson | (Buisson, 2021) | AB test 실무, Python/R 코드 |

### Bayesian (`bayesian/`)
| 파일 | 저자 | 인용 약어 | 활용 |
|---|---|---|---|
| Gelman et al. | Gelman et al. | (Gelman et al., 2013) | Bayesian 이론, hierarchical model, MCMC |
| Downey | Downey | (Downey, 2021) | Bayesian 입문, Beta 분포, 업데이트 |

### Functional Data Analysis (`fda/`)
| 파일 | 저자 | 인용 약어 | 활용 |
|---|---|---|---|
| Ramsay & Silverman (1997) | Ramsay & Silverman | (Ramsay & Silverman, 1997) | FDA 이론: 기저함수, 스무딩, FPCA |
| Ramsay & Silverman (2002) | Ramsay & Silverman | (Ramsay & Silverman, 2002) | FDA 응용 사례 |
| Kokoszka & Reimherr (2017) | Kokoszka & Reimherr | (Kokoszka & Reimherr, 2017) | 최신 FDA 입문, 검정/추론 |

## 주제별 참조 우선순위

블로그 포스트 주제에 따라 어떤 소스를 먼저 참조할지 가이드:

| 블로그 주제 | 1순위 | 2순위 | 보충 |
|---|---|---|---|
| 확률/분포/추정/검정 | Casella & Berger | - | - |
| 선형대수/행렬 | Strang (Intro) | Matrix Cookbook | Magnus |
| 회귀분석/GLM | McCullagh & Nelder | Faraway | - |
| Mixed Model | Hedeker | Faraway | - |
| Survival Analysis | Kleinbaum (개념) | Hosmer (실무) | Klein (이론) |
| AB Test/실험설계 | Buisson (코드) | Maxwell (이론) | Hernan (인과) |
| 인과추론 | Hernan & Robins | - | Woodward |
| 역학/Study Design | Woodward | Schulz & Grimes | - |
| Bayesian | Gelman | Downey (입문) | - |
| FDA/PCR Curve | Kokoszka (최신) | Ramsay 1997 (이론) | Ramsay 2002 (사례) |

## 실무 맥락

블로그 작성 시 다음 맥락을 반영하여 예시를 구성한다:
- **PCR 데이터**: 96-well plate, well당 멀티플렉스 10채널 시계열 신호
- **Experimentation**: AB test, 배치/플레이트 효과 분석
- **FDA 적용**: PCR amplification curve를 함수형 데이터로 분석
- **Mixed Model**: well/plate/batch 랜덤 효과 모델링
- **Survival**: time-to-positive 분석, 진단 성능 평가
