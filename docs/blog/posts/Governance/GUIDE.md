# Governance 카테고리 작성 가이드

> 이 문서는 `AGENT_GUIDE.md`의 공통 규칙을 보충하는 **Governance 전용 가이드**이다.
> 공통 규칙(YAML 헤더, 한다 체, index.qmd 패턴 등)은 `AGENT_GUIDE.md`를 따른다.

---

## 카테고리 특성

- **업무 프로세스 중심**: 기술적 구현보다 거버넌스 체계, 절차, 표준을 다룬다
- **순차적 학습 경로**: 기초(1) → 업무절차(2) → 아키텍처(3) → 데이터 모델(4) → 표준화(5) → 등록/검토(6) → 규칙(7) → 품질(8) 순서
- **실무 문서 스타일**: 정책 문서, 가이드라인, 체크리스트 형태가 많다
- **커스텀 레이아웃**: `sidebar: 200px, body: 1150px, margin: 300px` 설정을 사용한다
- **파일명 패턴**: `번호.토픽명.qmd` (예: `4-0.data_model.qmd`, `5-0-0.data_standard.qmd`)

---

## 포스트 콘텐츠 구조

### 1. 정의 (Definition)

- 거버넌스 용어의 공식 정의를 제시한다
- 관련 표준/프레임워크(DAMA, ISO 등)에서의 정의를 인용한다

```markdown
::: {.callout-note}
## 정의: 데이터 표준화 (Data Standardization)

데이터 표준화는 조직 내 데이터의 명칭, 형식, 도메인, 코드를 일관된 규칙으로 정의하고
관리하는 활동이다.

- 범위: 표준 용어 → 표준 단어 → 표준 도메인 → 표준 코드
- 목적: 데이터 일관성 확보, 시스템 간 상호운용성 보장
- 참조: DAMA-DMBOK2 Chapter 13
:::
```

### 2. 개념 및 원리 (Concept & Principles)

- 거버넌스 프레임워크 내에서의 위치를 설명한다
- 구성 요소(조직, 프로세스, 기술, 정책)를 분해한다
- 선행/후행 활동과의 관계를 명시한다

### 3. 직관적 설명 (Intuitive Explanation)

- 조직 관점에서 왜 이 활동이 필요한지 비유로 설명한다

```markdown
> **직관**: 데이터 표준화는 "조직의 공용어 사전"을 만드는 것이다.
> 부서마다 같은 개념을 다른 이름으로 부르면(매출/수익/Revenue) 보고서가 맞지 않고,
> 시스템 통합 시 데이터 매핑에 막대한 비용이 든다.
```

### 4. 왜 필요한가 (Why It Matters)

- 거버넌스 부재 시 발생하는 구체적 비용과 리스크를 제시한다
- 규제 준수(compliance) 관점을 포함한다

### 5. 응용 분야 (Applications)

```markdown
| 분야 | 거버넌스 활동 | 구체적 예시 |
|---|---|---|
| 금융 | 데이터 리니지 관리 | 규제 보고(Basel III) 데이터 추적 |
| 의료 | 용어 표준화 | HL7 FHIR 기반 의료 데이터 교환 |
| 제조 | 마스터 데이터 관리 | 제품 코드 통합 (ERP ↔ MES) |
| 공공 | 데이터 카탈로그 | 공공데이터 포털 메타데이터 관리 |
```

### 6. 예시 (Examples)

- 실제 거버넌스 산출물(용어 사전, 데이터 모델, 코드표)의 예시를 제시한다
- Before/After 비교로 효과를 보여준다

### 7. 코드/도구 예시 (Code/Tool Examples)

- SQL DDL, ERD, 메타데이터 관리 스크립트를 포함한다
- 도구: ERD 모델링 도구, 데이터 카탈로그 도구

```markdown
```sql
-- 표준 도메인 정의 예시
CREATE DOMAIN 사용자ID AS VARCHAR(20)
    CHECK (VALUE ~ '^[A-Z]{2}[0-9]{6}$')
    COMMENT '표준 사용자 식별자: 부서코드(2자리) + 일련번호(6자리)';

-- 표준 코드 테이블
CREATE TABLE std_code (
    code_group_id   VARCHAR(10)  NOT NULL,
    code_id         VARCHAR(10)  NOT NULL,
    code_name_kr    VARCHAR(100) NOT NULL,
    code_name_en    VARCHAR(100),
    sort_order      INT,
    use_yn          CHAR(1) DEFAULT 'Y',
    PRIMARY KEY (code_group_id, code_id)
);
```
```

### 8. 관련 주제 (Related Topics)

- 포스트 끝에 관련 개념과 블로그 내 링크를 목록으로 제시한다
- 선행 지식(prerequisite)과 후속 주제(next)를 구분한다
- **파일이 아직 존재하지 않더라도 논리적으로 필요한 주제는 placeholder 링크로 포함한다.** 이를 통해 향후 채워야 할 콘텐츠를 체계적으로 파악할 수 있다. Placeholder 링크는 경로를 미리 지정하되, 해당 파일이 생성되면 자연스럽게 연결된다.

```markdown
## 관련 주제

**카테고리 내 연결**

- [데이터 모델링](./4-0.data_model.qmd)
- [데이터 표준화](./5-0-0.data_standard.qmd)
- [데이터 품질 측정](./8-0.data_quality_measures.qmd)

**다른 카테고리 연결**

- [데이터 모델링 (System)](../Engineering/System/Archi_Design/data_modeling/)
- [데이터 파이프라인](../Engineering/Data_Engineering/airflow/)
```

---

## YAML 헤더 특이사항

Governance 카테고리는 커스텀 레이아웃을 사용한다. 새 포스트에도 동일하게 적용한다:

```yaml
---
title: "제목"
subtitle: "부제목"
description: "설명"
author: Kwangmin Kim
categories:
  - Data Governance
date: MM/DD/YYYY
format:
  html:
    number-depth: 3
    grid:
      sidebar-width: 200px
      body-width: 1150px
      margin-width: 300px
---
```
