---
name: "DAMA-DMBOK: Data Management Body of Knowledge, 2nd Edition"
type: book-summary
authors: "DAMA International"
year: 2017
total_pages: 628
language: en
keywords: [data-management, data-governance, data-architecture, data-quality, metadata, master-data, data-security, data-warehousing, data-integration, data-modeling]
sources:
  - file: "DAMA-DMBOK_marker_full.md"
    tool: Marker
---

# DAMA-DMBOK: Data Management Body of Knowledge (2nd Edition) — Summary

> DAMA International (2017), 628 pages, 17 chapters
> 데이터 관리의 11개 지식 영역과 조직·변화 관리를 체계적으로 정리한 표준 프레임워크이다.

## Contents

- Preface
- Ch 1: Data Management
- Ch 2: Data Handling Ethics
- Ch 3: Data Governance
- Ch 4: Data Architecture
- Ch 5: Data Modeling and Design
- Ch 6: Data Storage and Operations
- Ch 7: Data Security
- Ch 8: Data Integration and Interoperability
- Ch 9: Document and Content Management
- Ch 10: Reference and Master Data
- Ch 11: Data Warehousing and Business Intelligence
- Ch 12: Metadata Management
- Ch 13: Data Quality
- Ch 14: Big Data and Data Science
- Ch 15: Data Management Maturity Assessment
- Ch 16: Data Management Organization and Role Expectations
- Ch 17: Data Management and Organizational Change Management

---

## Chapter Summaries

> Marker 원본: `DAMA-DMBOK_marker_full.md` | 총 ~14,348 라인 | `L:숫자`로 직접 접근 가능


### Ch 1: Data Management (pp. 17-46)
**핵심**: 데이터, 정보, 조직 자산으로서의 데이터 개념을 정의한다. 데이터 관리 원칙과 과제를 제시하고, 데이터 관리 전략 수립 방법을 설명한다. Strategic Alignment Model, Amsterdam Information Model, DAMA-DMBOK Framework, DMBOK Pyramid 등 주요 프레임워크를 소개하고 비교한다.
**키워드**: `data-management-principles`, `DAMA-framework`, `strategic-alignment`, `data-as-asset`
**상세**: → `DAMA-DMBOK_marker_full.md` Ch 1 (L:728)
DAMA-DMBOK 제1장은 데이터, 정보, 지식의 관계를 정의하고 데이터를 조직의 자산으로 관리해야 하는 이유를 설명한다. 데이터 관리의 핵심 원칙으로 데이터 품질, 메타데이터, 데이터 보호의 중요성을 제시한다. Strategic Alignment Model과 Amsterdam Information Model을 통해 비즈니스 전략과 IT 전략의 정렬 방법을 설명한다. DAMA Wheel(DAMA-DMBOK Framework)은 데이터 거버넌스를 중심에 두고 11개 지식 영역을 배치한 프레임워크이다. 각 지식 영역의 Context Diagram은 SIPOC 개념을 기반으로 정의, 목표, 활동(P/D/C/O), 입력, 산출물, 역할, 도구, 기법, 메트릭을 체계적으로 구조화한다. Peter Aiken의 DMBOK Pyramid는 조직이 데이터 관리 성숙도를 단계적으로 구축하는 과정을 4단계로 설명한다. Sue Geuens의 프레임워크는 지식 영역 간 의존 관계를 시각화하여 BI와 분석 기능이 다른 모든 데이터 관리 기능에 의존함을 보여준다. DAMA Data Management Framework Evolved는 데이터 생명주기 관리, 기반 활동(메타데이터, 품질, 아키텍처), 거버넌스의 관계를 계층적으로 표현한다. DMBOK은 CDMP 자격 시험의 기본 참조 가이드로서 데이터 관리 전문가를 위한 공통 어휘와 모범 사례를 제공한다. 데이터 윤리, 빅데이터, 성숙도 평가, 조직 변화 관리 등 지식 영역 외 추가 주제도 다루어 데이터 관리의 전체적인 맥락을 제공한다.

**Marker 세부 목차** (`DAMA-DMBOK_marker_full.md`):
- 1. Introduction `L:728`
- 1.2 Data Architecture Outcomes and Practices (p.103) `L:2614`
- 1.3 Essential Concepts (p.129) `L:3109`
- 1.1 Business Drivers (p.273) `L:6279`
- 1.3.2.6 Taxonomies `L:7101`
- 1.3.7 Search Engine `L:7270`
- 1.3.10 Unstructured Data `L:7292`
- 1.3.2 Data Warehouse `L:8733`
- 1.3.15 Data Visualization91 (p.513) `L:11466`
- 1.3.1 Assessment Levels and Characteristics `L:12067`
- 1.3.3 Existing DMMA Frameworks98 (p.540) `L:12117`
- 1.3.3.2 EDM Council DCAM100 (p.541) `L:12136`


### Ch 2: Data Handling Ethics (pp. 49-65)
**핵심**: 데이터에 대한 윤리 원칙(비밀유지, 투명성, 동의 등)을 정의하고, 데이터 프라이버시 법률의 원칙을 설명한다. 온라인 데이터의 윤리적 맥락, 비윤리적 데이터 처리의 위험, 윤리적 데이터 문화 구축 방법을 다루고, 데이터 윤리와 거버넌스의 관계를 정리한다.
**키워드**: `data-ethics`, `privacy-law`, `ethical-culture`, `consent`, `transparency`
**상세**: → `DAMA-DMBOK_marker_full.md` Ch 2 (L:1803)
데이터 거버넌스(DG)는 데이터 자산에 대한 권한과 통제(계획, 모니터링, 집행)의 행사로 정의된다. DG의 범위에는 전략 정의, 정책 수립, 표준과 품질 관리, 감독(스튜어드십), 규제 준수, 이슈 관리, 데이터 관리 프로젝트 후원, 데이터 자산 가치 평가가 포함된다. 규제 준수와 고급 분석이 DG의 가장 일반적인 비즈니스 동인이며, 마스터 데이터 관리(MDM) 필요성에서 DG로 이어지는 경우가 빈번하다. DG 프로그램은 지속 가능성, 임베디드 운영, 측정 가능성을 갖추어야 하며, 리더십과 전략, 비즈니스 주도, 공유 책임, 다층 구조, 프레임워크 기반, 원칙 기반의 6가지 기본 원칙을 따른다. DG 조직은 운영위원회, 거버넌스 위원회(DGC), 거버넌스 사무국(DGO), 데이터 스튜어드십 팀, 지역 거버넌스 위원회로 구성되며 중앙형, 복제형, 연합형 운영 모델로 분류된다. 데이터 스튜어드는 Chief, Executive, Enterprise, Business, Technical, Coordinating 등 유형으로 구분되며 핵심 메타데이터 관리, 규칙·표준 문서화, 품질 이슈 관리, 운영 거버넌스 활동을 수행한다. 주요 활동으로 준비도 평가, 비즈니스 정렬, 전략 개발, 운영 프레임워크 정의, 목표·정책 개발, 이슈 관리, 규제 준수 평가, 비즈니스 용어사전 개발, 아키텍처 그룹 조정, 데이터 자산 가치 평가가 있다. 데이터 정책은 데이터 생성·취득·무결성·보안·품질·사용에 대한 기본 규칙을 성문화하며, 표준·절차와 구분된다. 조직 변화 관리(OCM)는 DG의 핵심 성공 요인으로, 데이터 자산 가치 홍보, 피드백 모니터링, 교육 실시, 인센티브 재정렬을 포함한다.

**Marker 세부 목차** (`DAMA-DMBOK_marker_full.md`):
- 2. Essential Concepts `L:763`
- 2.2 Data and Information (p.23) `L:791`
- 2.3 Data as an Organizational Asset (p.23) `L:801`
- 2.4 Data Management Principles (p.24) `L:815`
- 2.5.1 Data Differs from Other Assets6 (p.26) `L:870`
- 2.5.3 Data Quality `L:906`
- 2. Business Drivers `L:1459`
- 2. Activities `L:2147`
- 2.3 Perform Discovery and Business Alignment (p.83) `L:2168`
- 2.6 Define the DG Operating Framework `L:2202`
- 2.8 Underwrite Data Management Projects (p.87) `L:2234`
- 2.1 Establish Data Architecture Practice (p.113) `L:2805`
- 2.2 Build the Data Model (p.156) `L:3692`
- 2.3 Review the Data Models (p.161) `L:3801`
- 2.1 Manage Database Technology (p.197) `L:4571`
- 2.2.3.5 Load Data `L:4746`
- 2. Data Integration Activities `L:6571`
- 2.2 Design Data Integration Solutions (p.292) `L:6638`
- 2.2 Manage the Lifecycle (p.329) `L:7373`
- 2.1.4 Model Master Data `L:8401`
- 2.4 Populate the Data Warehouse (p.400) `L:8975`
- 2.1 Define High Quality Data (p.476) `L:10730`
- 2.3 Identify Critical Data and Business Rules (p.477) `L:10769`
- 2.6 Define Goals for Data Quality Improvement (p.480) `L:10813`
- 2.7.4 Establish Data Quality Service Level Agreements `L:10946`
- 2.2 Choose Data Sources `L:11497`
- 2.3 Acquire and Ingest Data Sources (p.516) `L:11519`
- 2.4 Develop Data Hypotheses and Methods (p.517) `L:11531`
- 2.5 Integrate / Align Data for Analysis (p.517) `L:11537`
- 2.1.5 Plan Communications `L:12207`
- 2. Understand Existing Organization and Cultural Norms (p.554) `L:12451`
- 2. Laws of Change `L:12931`


### Ch 3: Data Governance (pp. 67-93)
**핵심**: 데이터 거버넌스의 비즈니스 동인, 목표·원칙, 핵심 개념을 정의한다. 거버넌스 조직 정의, 준비도 평가, 비즈니스 정렬, 운영 프레임워크 개발, 정책·표준 수립, 비즈니스 용어사전 개발, 이슈 관리, 규제 준수 평가 등 17개 활동을 체계적으로 설명한다.
**키워드**: `data-governance`, `stewardship`, `business-glossary`, `policy`, `compliance`
**상세**: → `DAMA-DMBOK_marker_full.md` Ch 3 (L:2614)
데이터 아키텍처는 비즈니스 전략과 기술 실행 사이의 다리 역할을 하며, 조직의 데이터 요구를 식별하고 충족하기 위한 마스터 블루프린트를 설계·유지한다. 엔터프라이즈 아키텍처의 네 도메인(비즈니스, 데이터, 애플리케이션, 기술) 내에서 데이터 아키텍처는 데이터 모델, 정의, 매핑 명세, 데이터 흐름, 구조화된 API를 포함한다. Zachman Framework는 6x6 매트릭스로 커뮤니케이션 질문(What, How, Where, Who, When, Why)과 구현 수준(식별, 정의, 표현, 명세, 구성, 인스턴스화)을 교차시켜 엔터프라이즈 아키텍처의 전체 모델 세트를 기술한다. 엔터프라이즈 데이터 모델(EDM)은 구현 독립적인 개념적·논리적 데이터 모델로서 주제 영역 모델, 논리 모델, 물리 모델 간 수직·수평 연결을 통해 추적 가능성을 제공한다. 데이터 흐름 설계는 애플리케이션, 데이터 저장소, 네트워크 세그먼트, 비즈니스 역할, 위치 간 데이터 이동을 매핑하며 매트릭스 또는 다이어그램으로 표현한다. 주요 활동은 품질 지향(기존 아키텍처 개선)과 혁신 지향(신기술·비즈니스 변혁) 두 가지 관점에서 수행되며, 프로젝트 데이터 요구사항 정의, 설계 검토, 리니지 영향 분석, 복제 통제, 표준 시행을 포함한다. 로드맵은 비즈니스 기능 간 데이터 의존성 분석을 기반으로 3-5년 개발 경로를 제시하며, 독립적 기능(마스터 데이터)에서 의존적 기능(트랜잭션 데이터)순으로 구현한다. 도구로 데이터 모델링 도구, 자산 관리 소프트웨어, 그래픽 디자인 애플리케이션을 사용하며, 라이프사이클 프로젝션과 다이어그래밍 명확성이 핵심 기법이다. 거버넌스 활동에는 프로젝트 감독, 아키텍처 설계·생명주기·도구 관리, 표준 정의, 데이터 관련 산출물 생성이 포함된다. 메트릭은 아키텍처 표준 준수율, 구현 추세(재사용/교체/은퇴), 비즈니스 가치(민첩성·품질·운영 효율·환경 개선)로 측정한다.

**Marker 세부 목차** (`DAMA-DMBOK_marker_full.md`):
- 3. Data Management Frameworks `L:1069`
- 3. Essential Concepts `L:1469`
- 3.3 Online Data in an Ethical Context (p.59) `L:1576`
- 3.5 Establishing an Ethical Data Culture (p.63) `L:1660`
- 3.6 Data Ethics and Governance `L:1729`
- 3. Tools and Techniques `L:2406`
- 3.4 Document Management Tools (p.96) `L:2436`
- 3. Tools `L:2890`
- 3.2 Lineage Tools (p.162) `L:3817`
- 3.1 Anti-Virus Software / Security Software (p.259) `L:5981`
- 3.3 Identity Management Technology (p.260) `L:5989`
- 3.7 Data Masking/Encryption (p.261) `L:6009`
- 3.1 Data Transformation Engine/ETL Tool (p.297) `L:6740`
- 3.4 Business Rules Engine (p.298) `L:6760`
- 3.6 Data Profiling Tool (p.298) `L:6768`
- 3.3 Controlled Vocabulary and Metadata Tools (p.336) `L:7557`
- 3.5 E-discovery Technology `L:7622`
- 3.1 Data Profiling Tools (p.488) `L:10984`
- 3. Data Management Organizational Constructs `L:12482`
- 3.3 Centralized Operating Model (p.558) `L:12512`
- 3.4 Hybrid Operating Model (p.559) `L:12524`
- 3.7 DMO Alternatives and Design Considerations (p.561) `L:12558`
- 3. Not Managing a Change: Managing a Transition `L:12945`


### Ch 4: Data Architecture (pp. 97-120)
**핵심**: 데이터 아키텍처의 비즈니스 동인, 성과·실천 방안, 핵심 개념을 설명한다. 데이터 아키텍처 실무 수립과 엔터프라이즈 아키텍처와의 통합 활동을 다룬다. 데이터 모델링 도구, 자산 관리 소프트웨어, 그래픽 디자인 애플리케이션 등 도구와 기법을 소개한다.
**키워드**: `data-architecture`, `enterprise-architecture`, `data-flow`, `as-is-to-be`
**상세**: → `DAMA-DMBOK_marker_full.md` Ch 4 (L:3068)
데이터 모델링은 데이터 요구사항을 발견·분석·범위화하고 데이터 모델이라는 정밀한 형식으로 표현·소통하는 과정이다. 6가지 주요 모델링 스킴(관계형, 차원형, 객체지향, 팩트기반, 시간기반, NoSQL)이 있으며, 각 스킴은 고유한 다이어그래밍 표기법을 사용한다. 데이터 모델의 구성요소는 엔터티(Who, What, When, Where, Why, How 범주), 관계(카디널리티와 외래키로 비즈니스 규칙 표현), 속성(식별자와 비식별 속성), 도메인(데이터 타입, 포맷, 리스트, 범위, 규칙 기반)이다. 개념적 모델(CDM)은 핵심 비즈니스 엔터티와 관계를 고수준으로 포착하고, 논리적 모델(LDM)은 속성을 추가하고 정규화를 적용하여 상세 요구사항을 표현하며, 물리적 모델(PDM)은 특정 기술 환경에 맞게 비정규화·인덱싱·파티셔닝을 적용한다. 정규화는 1NF(원자성·반복그룹 제거)부터 5NF까지 중복을 제거하고 데이터 무결성을 보장하는 규칙을 단계적으로 적용한다. 포워드 엔지니어링은 CDM→LDM→PDM 순으로 모델을 구축하고, 리버스 엔지니어링은 기존 데이터베이스에서 PDM→LDM→CDM 순으로 문서화한다. 명명 규칙은 ISO 11179 표준을 따르며 논리적 이름은 비즈니스 사용자에게 의미 있는 완전한 단어를, 물리적 이름은 DBMS 제한에 맞는 약어를 사용한다. 데이터베이스 설계 모범 사례는 PRISM(Performance, Reusability, Integrity, Security, Maintainability)으로 요약된다. Data Model Scorecard는 요구사항 충족, 완전성, 스킴 적합성, 구조적 건전성, 일반화 활용, 명명 표준, 가독성, 정의 품질, 엔터프라이즈 일관성, 메타데이터-데이터 일치의 10개 범주로 모델 품질을 100점 만점으로 평가한다. 거버넌스는 모델링·설계 표준 개발, 설계 리뷰 수행, 버전 관리·통합을 포함한다.

**Marker 세부 목차** (`DAMA-DMBOK_marker_full.md`):
- 4. DAMA and the DMBOK `L:1223`
- 4. Works Cited / Recommended `L:1735`
- 4. Implementation Guidelines `L:2444`
- 4.1 Organization and Culture (p.96) `L:2448`
- 4. Techniques `L:2904`
- 4.1 Lifecycle Projections (p.119) `L:2906`
- 4.2 Diagramming Clarity `L:2921`
- 4. Best Practices `L:3839`
- 4.1 Best Practices in Naming Conventions (p.164) `L:3841`
- 4.1 Test in Lower Environments (p.213) `L:4923`
- 4.1 CRUD Matrix Usage (p.261) `L:6017`
- 4.2 Immediate Security Patch Deployment (p.261) `L:6021`
- 4.4 Metrics (p.262) `L:6029`
- 4.1 Litigation Response Playbook (p.339) `L:7628`
- 4.1 Adhere to Master Data Architecture (p.379) `L:8461`
- 4.3 Manage Reference Data Change `L:8476`
- 4.1 Prototypes to Drive Requirements (p.410) `L:9146`
- 4.3 Audit Data that can be Queried (p.411) `L:9162`
- 4.2 Metadata for Big Data Ingest (p.446) `L:10022`
- 4.1 Preventive Actions (p.489) `L:11006`
- 4.1 Analytic Modeling (p.524) `L:11686`
- 4.2 DAMA-DMBOK Framework Use `L:12328`
- 4. Critical Success Factors `L:12579`
- 4.2 Clear Vision (p.562) `L:12598`
- 4.10 Evolution Not Revolution (p.564) `L:12648`
- 4. Kotter's Eight Errors of Change Management `L:13010`
- 4.1 Error #1: Allowing Too Much Complacency (p.580) `L:13014`
- 4.6 Error #6: Failing to Create Short-Term Wins (p.583) `L:13083`
- 4.7 Error #7: Declaring Victory Too Soon (p.584) `L:13095`


### Ch 5: Data Modeling and Design (pp. 123-166)
**핵심**: 데이터 모델링의 비즈니스 동인, 목표·원칙, 핵심 개념을 설명한다. 모델 계획, 구축, 검토, 유지보수의 활동 과정을 다룬다. 명명 규칙·데이터베이스 설계의 모범 사례, 모델 품질 관리와 메트릭, 라인에지 도구·프로파일링 도구·산업 데이터 모델 등을 소개한다.
**키워드**: `conceptual-model`, `logical-model`, `physical-model`, `naming-conventions`, `data-model-quality`
**상세**: → `DAMA-DMBOK_marker_full.md` Ch 5 (L:4068)
데이터 저장 및 운영은 저장된 데이터의 가치를 생명주기 전체에 걸쳐 극대화하기 위한 설계·구현·지원 활동이다. 데이터베이스 지원(데이터 생명주기 관리, 백업, 성능 모니터링·튜닝)과 데이터베이스 기술 지원(기술 요구사항 정의, 아키텍처 설계, 제품 설치·관리)의 두 가지 하위 활동으로 구성된다. DBA 역할은 프로덕션 DBA(운영 관리·가용성·복구), 애플리케이션 DBA(특정 DB 전담), 프로시저/개발 DBA(저장 프로시저·트리거·UDF), NSA(네트워크 스토리지) 네 가지로 세분화된다. 데이터베이스 아키텍처는 중앙형과 분산형(연합형·비연합형)으로 분류되며, 블록체인 데이터베이스와 클라우드(VM 이미지, DaaS, 관리형 호스팅)도 포함한다. 데이터베이스 처리 유형은 ACID(원자성·일관성·격리성·지속성)와 BASE(기본 가용·소프트 상태·최종 일관성)로 구분되며, CAP 정리는 분산 시스템에서 일관성·가용성·파티션 허용 중 최대 두 가지만 충족 가능함을 제시한다. 저장 매체는 디스크/SAN, 인메모리, 컬럼 압축, 플래시 메모리를 포함하며 사용 패턴과 비용에 따라 선택한다. 데이터베이스 환경은 프로덕션, 개발, 테스트(QA·통합·UAT·성능), 샌드박스로 구분되며, 프로덕션 데이터를 비프로덕션 환경에 이동 시 규제 준수를 확인해야 한다. 공통 프로세스로 아카이빙, 용량·성장 예측, CDC(변경 데이터 캡처), 퍼징, 복제(능동/수동, 미러링/로그 배송), 복원력·복구(즉각/중요/비중요), 보존, 샤딩이 있다. SLA는 데이터베이스 가용성·성능·복구 기대치를 규정하며, 가용성의 네 요소(관리성·복구성·신뢰성·서비스성)를 관리한다. 거버넌스에는 저장·성능·운영·서비스 메트릭 수집, 정보 자산 추적(라이선스·비용 감사), 데이터 감사·검증 활동이 포함된다.

**Marker 세부 목차** (`DAMA-DMBOK_marker_full.md`):
- 5. Works Cited / Recommended `L:1276`
- 5. Metrics `L:2465`
- 5. Implementation Guidelines `L:2933`
- 5. Data Model Governance `L:3864`
- 5.2 Organization and Cultural Change (p.214) `L:4948`
- 5.4 Data Security in an Outsourced World (p.267) `L:6142`
- 5.5 Data Security in Cloud Environments (p.268) `L:6172`
- 5. Organization and Cultural Change `L:8508`
- 5.4 Organization and Cultural Change (p.413) `L:9197`
- 5.4.1 Dedicated Team `L:9209`
- 5. Guidelines for a DMMA `L:12334`
- 5. Build the Data Management Organization `L:12652`
- 5.1 Identify Current Data Management Participants (p.565) `L:12654`
- 5.2 Identify Committee Participants (p.565) `L:12662`
- 5. Kotter's Eight Stage Process for Major Change `L:13135`
- 5.3 Developing a Vision and Strategy (p.593) `L:13323`
- 5.4.2 Keeping it Simple `L:13418`
- 5.4.4 Repetition, Repetition, Repetition `L:13434`


### Ch 6: Data Storage and Operations (pp. 169-214)
**핵심**: 데이터베이스 기술 관리와 데이터베이스 관리의 활동을 포괄적으로 다룬다. 관계형, NoSQL, 그래프 등 다양한 DBMS 유형의 특성을 설명한다. 테스트 환경, 물리적 명명 표준, 스크립트 기반 변경 관리 등 기법과 데이터 감사·검증, 정보 자산 추적을 포함한 거버넌스를 다룬다.
**키워드**: `DBMS`, `database-operations`, `backup-recovery`, `performance-tuning`, `data-audit`
**상세**: → `DAMA-DMBOK_marker_full.md` Ch 6 (L:5130)
데이터 보안은 데이터 자산에 대한 적절한 인증, 권한 부여, 접근, 감사를 제공하기 위한 보안 정책·절차의 계획·개발·실행이다. 리스크 감소와 비즈니스 성장이 주요 동인이며, 보안 자체가 전략적 자산으로서 경쟁 우위를 제공한다. 리스크 분류는 CRD(Critical Risk Data), HRD(High Risk Data), MRD(Moderate Risk Data)의 세 등급으로 구분되며, 데이터 민감도와 악의적 목적 추구 가능성에 따라 접근 권한을 결정한다. 보안 프로세스의 핵심은 4A+E(Access, Audit, Authentication, Authorization, Entitlement)이며, 모니터링(능동적·수동적)을 통해 보안 위반을 탐지한다. 암호화는 해시, 대칭키(DES, 3DES, AES), 공개키(RSA, Diffie-Hellman) 방식으로 분류되며, 데이터 마스킹은 영구적(인플라이트, 인플레이스)과 동적 마스킹으로 구분된다. 마스킹 기법에는 대체, 셔플링, 시간 변동, 값 변동, 널링/삭제, 무작위화, 암호화, 표현식 마스킹, 키 마스킹이 있다. 네트워크 보안 용어로 백도어, 봇/좀비, 쿠키, 방화벽, 경계(perimeter), DMZ, 슈퍼유저 계정, 키로거, 침투 테스트, VPN이 정의된다. 데이터 보안 유형은 시설 보안, 디바이스 보안, 자격증명 보안(ID 관리·싱글사인온·패스워드 표준·다중인증), 전자 통신 보안으로 세분화된다. 기밀성 등급은 일반 공개부터 등록 기밀까지 5단계이며, 규제 범주는 PII, 재무 민감 데이터, PHI, 교육 기록, PCI-DSS, 영업 비밀 등으로 분류된다. 시스템 보안 리스크에는 과도 권한 남용, 정당 권한 남용, 무단 권한 상승, 서비스/공유 계정 남용, 플랫폼 침입 공격이 포함되며, 최소 권한 원칙과 쿼리 수준 접근 통제로 대응한다.

**Marker 세부 목차** (`DAMA-DMBOK_marker_full.md`):
- 6. Works Cited / Recommended `L:2486`
- 6. Data Architecture Governance `L:2979`
- 6. Data Storage and Operations Governance `L:4969`
- 6.3 Data Audits and Data Validation (p.216) `L:5012`
- 6. Data Security Governance `L:6184`
- 6. DII Governance `L:6806`
- 6. Documents and Content Governance `L:7707`
- 6.3 Govern for Quality Content (p.345) `L:7749`
- 6. Reference and Master Data Governance `L:8518`
- 6. DW/BI Governance `L:9215`
- 6.5 Metrics (p.416) `L:9260`
- 6. Metadata Governance `L:10056`
- 6.1 Process Controls (p.448) `L:10060`
- 6. Data Quality and Data Governance `L:11118`
- 6. Big Data and Data Science Governance `L:11768`
- 6.1 Visualization Channels Management `L:11780`
- 6.5 Data Quality (p.530) `L:11811`
- 6. Maturity Management Governance `L:12374`
- 6. Interactions Between the DMO and Other Data-oriented Bodies `L:12696`
- 6.5 Managing a Global Organization (p.570) `L:12767`
- 6. The Formula for Change `L:13483`


### Ch 7: Data Security (pp. 217-265)
**핵심**: 데이터 보안 요구사항 식별, 보안 정책·표준 정의 활동을 설명한다. 안티바이러스, HTTPS, 신원 관리, 침입 탐지/방지, 방화벽, 메타데이터 추적, 데이터 마스킹/암호화 등 도구를 소개한다. CRUD 매트릭스, 보안 패치, 메타데이터 보안 속성, 클라우드·아웃소싱 환경의 보안 등을 다룬다.
**키워드**: `access-control`, `encryption`, `data-masking`, `CRUD-matrix`, `cloud-security`
**상세**: → `DAMA-DMBOK_marker_full.md` Ch 7 (L:6250)
데이터 통합 및 상호운용성(DII)은 데이터 저장소, 애플리케이션, 조직 간 데이터의 이동과 통합에 관한 프로세스를 다룬다. DII의 핵심 기능에는 데이터 마이그레이션·변환, 허브·마트로의 데이터 통합, 벤더 패키지 통합, 애플리케이션 간·조직 간 데이터 공유, 아카이빙, 인터페이스 관리, 외부 데이터 수집이 포함된다. ETL(추출·변환·적재)은 모든 DII 영역의 기본 프로세스이며, 변환에는 포맷 변경, 구조 변경, 의미 변환, 중복 제거, 재정렬이 포함된다. 대기 시간(latency)에 따라 배치(고 대기), CDC(변경 데이터 캡처), 근실시간/이벤트 기반, 비동기, 실시간 동기, 저대기/스트리밍으로 처리 유형이 분류된다. 상호작용 모델은 점대점(소규모 적합, 인터페이스 수 폭증 위험), 허브앤스포크(데이터 허브 중심의 효율적 통합), 발행-구독(데이터 서비스 카탈로그 기반 자동 배포)의 세 가지이다. 캐노니컬 데이터 모델은 조직 전체의 표준 데이터 교환 형식을 정의하여 시스템 간 변환 수를 최소화하며, 3개 이상 시스템에서 비용 효과가 입증된다. 애플리케이션 커플링은 긴밀(동기·위험) 또는 느슨(비동기·독립)으로 구분되며, SOA와 ESB가 느슨한 결합의 대표적 패턴이다. 복제는 소스와 타깃 데이터를 동기화하는 방법으로, DB 관리 유틸리티의 로그 기반 복제가 운영 시스템에 미치는 영향을 최소화한다. DII는 데이터 거버넌스, 데이터 아키텍처, 데이터 보안, 메타데이터, 데이터 저장·운영, 데이터 모델링·설계 등 다른 데이터 관리 영역에 의존한다. 엔터프라이즈 관점의 DII 설계는 포인트 투 포인트 방식 대비 지원 비용과 복잡성을 획기적으로 줄이며, 규제 준수를 위한 코드 재사용과 검증을 가능케 한다.

**Marker 세부 목차** (`DAMA-DMBOK_marker_full.md`):
- 7. Works Cited / Recommended `L:3002`
- 7. Data Management Roles `L:12783`
- 7.1 Organizational Roles (p.571) `L:12789`
- 7.2 Individual Roles (p.571) `L:12797`
- 7. Diffusion of Innovations and Sustaining Change `L:13498`


### Ch 8: Data Integration and Interoperability (pp. 269-299)
**핵심**: 데이터 통합의 계획·분석, 설계, 개발, 구현·모니터링 활동을 체계적으로 다룬다. ETL 도구, 데이터 가상화 서버, 엔터프라이즈 서비스 버스, 비즈니스 규칙 엔진, 프로파일링 도구, 메타데이터 저장소 등 도구를 소개한다. 데이터 공유 협약, 데이터 리니지, 통합 메트릭을 포함한 거버넌스를 설명한다.
**키워드**: `ETL`, `data-virtualization`, `ESB`, `data-lineage`, `data-sharing-agreements`
**상세**: → `DAMA-DMBOK_marker_full.md` Ch 8 (L:6921)
문서 및 콘텐츠 관리는 관계형 데이터베이스 외부에 저장된 데이터와 정보의 캡처, 저장, 접근, 사용을 통제하는 활동이다. 주요 비즈니스 동인은 규제 준수, 소송 및 e-디스커버리 대응, 업무 연속성, 운영 효율성 향상이다. ARMA International의 GARP 원칙(책임성, 무결성, 보호, 준수, 가용성, 보존, 처분, 투명성)이 기록 관리의 기본 프레임워크를 제공한다. 콘텐츠는 문서 내부의 데이터와 정보를 의미하며, 콘텐츠 관리는 정보 자원을 조직·분류·구조화하여 저장·발행·재사용하는 프로세스를 포함한다. 콘텐츠 메타데이터는 포맷, 검색 가능성, 자기 문서화, 기존 패턴, 콘텐츠 주제, 요구사항에 기반하여 설계된다. 콘텐츠 전달 방식은 푸시(RSS 등 신디케이션), 풀(온라인 소매 등), 인터랙티브(EPOS, 고객 대면 웹사이트)로 분류된다. 제어 어휘(controlled vocabulary)는 단순 용어 리스트부터 동의어 링, 시소러스, 온톨로지까지 복잡도에 따라 다양하며, ANSI/NISO Z39.19 표준이 관리 지침을 제공한다. 택소노미는 평면형, 계층형, 다중계층형, 패싯형, 네트워크형으로 구분되며, 콘텐츠 분류와 다면적 내비게이션을 지원한다. 온톨로지는 택소노미의 확장으로, 개방 세계 가정(OWA)에 기반하여 개념 간 관계를 추론할 수 있으며 시맨틱 웹의 핵심 지식 표현 수단이다. 문서는 절차, 프로토콜, 방법, 사양 등 지식 공유 수단이며, 기록(records)은 조직 활동과 규제 준수의 증거로서 공식적으로 관리된다. 문서 관리는 전자 및 종이 문서의 저장, 인벤토리, 통제를 포괄하며 현재 생성되는 문서의 90% 이상이 전자 형태이다.

**Marker 세부 목차** (`DAMA-DMBOK_marker_full.md`):
- 8. Works Cited / Recommended `L:12842`
- 8. Sustaining Change `L:13579`
- 8.1 Sense of Urgency / Dissatisfaction (p.607) `L:13587`


### Ch 9: Document and Content Management (pp. 303-344)
**핵심**: 콘텐츠 생명주기 관리 계획, 생명주기 관리, 콘텐츠 발행·전달 활동을 설명한다. ECM 시스템, 협업 도구, 제어 어휘·메타데이터 도구, 표준 마크업/교환 형식, e-디스커버리 기술을 소개한다. 소송 대응 플레이북·데이터 맵, 정보 거버넌스 프레임워크, 콘텐츠 품질 관리를 다룬다.
**키워드**: `ECM`, `content-lifecycle`, `e-discovery`, `taxonomy`, `records-management`
**상세**: → `DAMA-DMBOK_marker_full.md` Ch 9 (L:7841)
참조 데이터와 마스터 데이터 관리는 조직 목표 달성, 데이터 중복 리스크 감소, 품질 향상, 통합 비용 절감을 위해 공유 데이터를 관리하는 활동이다. 참조 데이터는 다른 데이터를 특성화·분류하거나 조직 외부 정보와 연결하는 데 사용되며, 코드-설명 쌍, 교차참조 리스트, 택소노미, 온톨로지 형태로 구조화된다. 마스터 데이터는 비즈니스 트랜잭션에 맥락을 제공하는 핵심 엔터티(당사자, 제품/서비스, 재무 구조, 위치)에 대한 권위 있는 데이터이다. Chisholm의 6계층 데이터 분류 체계는 메타데이터, 참조 데이터, 기업 구조 데이터, 트랜잭션 구조 데이터, 트랜잭션 활동 데이터, 트랜잭션 감사 데이터로 구분한다. MDM의 핵심 처리 단계는 데이터 모델 관리, 데이터 수집, 검증·표준화·보강, 엔터티 해결(매칭·아이덴티티 해결), 스튜어드십·공유이다. 엔터티 해결은 결정론적 알고리즘(패턴·규칙 기반)과 확률론적 알고리즘(통계적 유사도 분석)을 사용하며, 위양성(서로 다른 엔터티를 동일 ID로 연결)과 위음성(동일 엔터티에 별도 ID 부여) 리스크를 관리한다. 시스템 오브 레코드(SoR)는 데이터가 생성·유지되는 권위 있는 시스템이고, 시스템 오브 레퍼런스(SoRef)는 신뢰할 수 있는 데이터를 소비자에게 제공하는 시스템이다. 골든 레코드는 가장 정확한 엔터티 인스턴스 데이터를 의미하지만, 신뢰 소스(Trusted Source)라는 표현이 "현재 보유한 최선의 버전"이라는 의미에서 더 적절하다. 매칭 워크플로는 중복 식별(리뷰 후 수동 조치), 매치-링크(교차참조만 생성), 매치-머지(단일 통합 레코드 생성)로 구분되며, 매치-머지의 복잡성과 역전 비용이 가장 높다. 글로벌 ID와 교차참조(X-Ref) 관리는 MDM 솔루션이 유일한 식별자를 생성·유지하고 소스 ID와의 매핑 이력을 보존하여 언머지-리머지 상황에 대응한다. 당사자(Party), 재무, 법무, 제품(PLM, PDM, ERP, MES, CRM), 위치 등 다양한 도메인별 마스터 데이터 특성과 관리 방법을 설명한다.

**Marker 세부 목차** (`DAMA-DMBOK_marker_full.md`):
- 9. Communicating Data Management Value `L:13617`


### Ch 10: Reference and Master Data (pp. 347-379)
**핵심**: 마스터 데이터 관리(MDM) 활동과 참조 데이터 활동을 구분하여 설명한다. MDM 아키텍처 준수, 데이터 이동 모니터링, 참조 데이터 변경 관리, 데이터 공유 협약 등 구현 지침을 제시한다. 골든 레코드 구축과 참조/마스터 데이터 거버넌스 메트릭을 다룬다.
**키워드**: `MDM`, `reference-data`, `golden-record`, `data-sharing`, `master-data-architecture`
**상세**: → `DAMA-DMBOK_marker_full.md` Ch 10 (L:8610)
데이터 웨어하우스(DW)와 비즈니스 인텔리전스(BI)는 의사결정 지원 데이터를 제공하기 위한 기술 환경과 프로세스의 계획·구현·통제를 다룬다. Bill Inmon의 Corporate Information Factory(CIF)와 Ralph Kimball의 차원 모델링이라는 두 가지 주요 접근법이 있으며, 둘 다 원천 시스템의 데이터를 통합·조직하여 분석에 활용 가능하게 한다는 공통 원칙을 공유한다. DW 아키텍처 구성요소에는 원천 시스템, 데이터 통합(ETL), 스테이징 영역, 중앙 웨어하우스, ODS, 데이터 마트, OLAP 큐브가 포함된다. 데이터 적재 처리 유형으로 히스토리 로드, 배치 변경 데이터 캡처(CDC), 준실시간·실시간 처리(트리클 피드, 메시징, 스트리밍)가 있다. 요구사항 수집 시 비즈니스 목표와 전략에서 출발하여 핵심 성과 지표와 계산 규칙을 도출해야 한다. DW/BI 아키텍처 정의 시 데이터의 출처, 목적지, 이동 시점과 방법을 명확히 기술해야 한다. BI 포트폴리오 구현은 운영 보고, 비즈니스 성과 관리(BPM), 기술적·셀프서비스 분석으로 구분되며, 사용자 그룹별 적합한 도구를 매칭해야 한다. OLAP 도구는 슬라이스, 다이스, 드릴다운/업, 롤업, 피봇 등의 다차원 분석 기능을 제공한다. 릴리스 관리를 통해 점진적으로 웨어하우스를 발전시키되, 비즈니스 수용과 검증 가능한 데이터 리니지 확보가 핵심 성공 요인이다. 거버넌스 측면에서 SLA 정의, 보고 전략 수립, 사용 메트릭·주제 영역 커버리지·응답 성능 메트릭 관리가 필요하다.

**Marker 세부 목차** (`DAMA-DMBOK_marker_full.md`):
- 10. Works Cited / Recommended `L:13730`


### Ch 11: Data Warehousing and Business Intelligence (pp. 381-414)
**핵심**: 요구사항 이해, DW/BI 아키텍처 정의·유지, 데이터 웨어하우스·데이터 마트 개발, 데이터 적재, BI 포트폴리오 구현, 데이터 제품 유지보수 활동을 설명한다. 프로토타입 기반 요구사항 도출, 셀프서비스 BI, 감사 가능 데이터 기법을 다룬다. SLA, 보고 전략 등 거버넌스를 포함한다.
**키워드**: `data-warehouse`, `business-intelligence`, `dimensional-modeling`, `self-service-BI`, `SLA`
**상세**: → `DAMA-DMBOK_marker_full.md` Ch 11 (L:9394)
메타데이터 관리는 고품질·통합 메타데이터에 대한 접근을 가능케 하는 계획·구현·통제 활동이다. 메타데이터는 비즈니스, 기술, 운영 메타데이터의 세 가지 유형으로 분류되며, 각각 데이터의 의미와 맥락, 시스템 구조와 처리 정보, 처리 이력과 접근 패턴을 기술한다. 메타데이터 없이는 조직이 보유 데이터, 데이터의 의미, 출처, 시스템 간 이동 경로, 접근 권한, 품질 기준을 파악할 수 없다. 메타데이터 아키텍처는 중앙집중형, 분산형, 하이브리드, 양방향 네 가지 접근 방식이 있으며, 각각 가용성·최신성·유지비용 측면에서 장단점을 가진다. 주요 활동으로 메타데이터 전략 정의, 요구사항 파악, 메타모델 생성, 표준 적용, 저장소 관리, 메타데이터 통합·배포, 쿼리·보고·분석이 있다. 비즈니스 용어집은 용어·정의·관계를 관리하며 비즈니스 사용자, 데이터 스튜어드, 기술 사용자 세 핵심 대상에게 서비스한다. 데이터 리니지와 영향 분석은 데이터가 시스템 간 이동하며 변환되는 과정을 추적하여 변경 영향 분석과 근본 원인 조사를 지원한다. ISO/IEC 11179 메타데이터 레지스트리 표준은 데이터 요소의 정확한 정의에 기반한 메타데이터 기반 데이터 교환 프레임워크를 제공한다. 빅데이터 환경에서는 데이터 수집 시 메타데이터 태그를 적용하여 데이터 레이크 내 콘텐츠 식별과 민감 정보 보호를 지원해야 한다. 메타데이터 거버넌스는 프로세스 통제, 문서화, 표준·가이드라인, 메트릭(저장소 완전성, 스튜어드 대표성, 사용률, 문서 품질)을 포함한다.

### Ch 12: Metadata Management (pp. 417-448)
**핵심**: 메타데이터 전략 정의, 요구사항 파악, 아키텍처 정의, 메타데이터 생성·유지, 쿼리·보고·분석 활동을 설명한다. 메타데이터 저장소 관리 도구를 소개하고, 데이터 리니지와 영향 분석, 빅데이터 수집을 위한 메타데이터 기법을 다룬다. 프로세스 통제, 문서화, 표준·가이드라인, 메트릭을 포함한 거버넌스를 정리한다.
**키워드**: `metadata-strategy`, `metadata-repository`, `data-lineage`, `impact-analysis`
**상세**: → `DAMA-DMBOK_marker_full.md` Ch 12 (L:10161)
데이터 품질 관리는 데이터가 소비자의 요구에 적합하도록 품질 관리 기법을 적용하는 계획·구현·통제 활동이다. 비즈니스 동인에는 조직 데이터의 가치 증대, 저품질 데이터 관련 비용·리스크 절감, 조직 효율성 향상, 평판 보호가 포함된다. 데이터 품질 차원(accuracy, completeness, consistency, integrity, reasonability, timeliness, uniqueness, validity)은 품질 요구사항 정의와 측정의 어휘를 제공한다. Strong-Wang 프레임워크는 15개 차원을 내재적·맥락적·표현적·접근성 DQ 네 범주로 분류하고, Redman은 데이터 모델·값·표현에 걸친 2개 이상의 차원을 제시하며, English는 내재적·실용적 특성으로 구분한다. 데이터 품질 개선 생명주기는 Shewhart/Deming 사이클(Plan-Do-Check-Act)에 기반하며, 핵심 데이터 식별부터 근본 원인 분석, 개선 우선순위 도출, 운영 배포까지 체계적 단계를 따른다. 예방적 조치(데이터 입력 통제, 생산자 교육, 규칙 정의·시행)와 교정적 조치(자동화·수동 지시·수동 교정)를 구분하여 적용한다. 통계적 공정 관리(SPC)는 공정 결과의 예측 가능성을 측정하며, 관리도를 사용하여 공통 원인과 특수 원인 변동을 구분한다. 데이터 품질 메트릭은 측정 가능성, 비즈니스 관련성, 수용 가능성, 책임성, 통제 가능성, 추세 분석 특성을 갖추어야 한다. 데이터 품질 SLA는 비즈니스 기대치에 대한 데이터 적합도를 모니터링하고 에스컬레이션 프로세스를 포함한다. 데이터 거버넌스 프로그램 내에서 DQ를 운영하면 리스크·보안 담당자, 비즈니스 프로세스 엔지니어, 데이터 스튜어드와 협력하여 효과를 극대화할 수 있다.

### Ch 13: Data Quality (pp. 449-494)
**핵심**: 고품질 데이터 정의, 품질 전략 수립, 핵심 데이터·비즈니스 규칙 식별, 초기 품질 평가, 개선 우선순위 도출, 품질 목표 설정, 품질 운영 개발·배포 활동을 체계적으로 설명한다. 예방적·교정적 조치, 품질 메트릭, 통계적 공정 관리(SPC), 근본 원인 분석 기법을 다루고, 프로파일링·ETL·메타데이터 저장소 도구를 소개한다.
**키워드**: `data-quality-dimensions`, `SPC`, `root-cause-analysis`, `data-profiling`, `quality-metrics`
**상세**: → `DAMA-DMBOK_marker_full.md` Ch 13 (L:11237)
빅데이터와 데이터 과학은 분석 시작 시점에 알 수 없는 질문에 대한 답과 인사이트를 찾기 위해 다양한 유형의 데이터를 수집·분석하는 영역이다. 빅데이터는 Volume(규모), Velocity(속도), Variety(다양성)의 3V로 정의되었으나 Viscosity(사용 난이도), Volatility(변동성), Veracity(신뢰성)까지 확장되었다. 데이터 과학은 과학적 방법론을 적용하여 가설을 수립하고 대규모 과거 데이터를 분석하여 예측 모델을 개발·검증하는 과정이다. 전통적 BI가 과거 추세를 분석하는 '백미러' 관점이라면, 데이터 과학은 예측·처방적 분석을 통해 '전방 시야'를 제공한다. 데이터 레이크는 대규모 다양한 형식의 데이터를 수집·저장·분석할 수 있는 환경이며, 메타데이터 관리 없이는 데이터 늪(swamp)이 될 위험이 있다. 머신러닝은 지도학습, 비지도학습, 강화학습의 세 유형으로 분류되며, 감정 분석(NLP 기반), 데이터·텍스트 마이닝(프로파일링·연관·클러스터링), 예측·처방적 분석이 주요 기법이다. DW와 빅데이터의 핵심 차이는 ETL 대 ELT 접근 방식이며, 빅데이터는 적재 후 변환하므로 메타데이터 관리가 더욱 중요하다. MPP 공유-무(shared-nothing) 아키텍처, Hadoop 같은 분산 파일 시스템, 인-데이터베이스 알고리즘이 빅데이터 분석의 핵심 기술이다. 거버넌스 측면에서 소싱, 공유, 메타데이터, 보강, 접근에 대한 비즈니스 및 기술 통제가 필요하며, 시각화 채널 관리, 데이터 과학 표준, 보안, 품질 메트릭을 포함한다.

### Ch 14: Big Data and Data Science (pp. 497-528)
**핵심**: 빅데이터 전략 정의, 데이터 소스 선택, 데이터 수집·적재, 가설·방법론 개발, 분석용 데이터 통합, 모델 탐색, 배포·모니터링 활동을 설명한다. MPP 아키텍처, 분산 파일 기반 데이터베이스, 인-데이터베이스 알고리즘, 클라우드 솔루션, 통계 컴퓨팅 언어, 시각화 도구를 소개한다. 분석 모델링과 빅데이터 모델링 기법을 다룬다.
**키워드**: `big-data`, `data-science`, `MPP`, `distributed-database`, `analytics-modeling`
**상세**: → `DAMA-DMBOK_marker_full.md` Ch 14 (L:11952)
데이터 관리 성숙도 평가(DMMA)는 조직의 데이터 관리 현황을 평가하고 개선을 위한 로드맵을 수립하는 방법론이다. 성숙도 모델은 Level 0(역량 부재)부터 Level 5(최적화)까지 단계적 진행을 정의하며, 각 수준은 프로세스 자동화, 정책 통제, 도구 표준화, 성과 측정의 특성을 포함한다. 평가 기준은 활동·도구·표준·인력의 네 범주로 구성되며, DAMA-DMBOK 지식 영역의 컨텍스트 다이어그램 카테고리에 매핑할 수 있다. 주요 DMMA 프레임워크로 CMMI-DMM, EDM Council DCAM, IBM Data Governance Council 모델, Stanford Data Governance Maturity Model, Gartner EIM 모델이 있다. 평가 활동은 계획 수립(목표 정의, 프레임워크 선택, 범위 정의, 커뮤니케이션 계획)과 평가 수행(정보 수집, 평가 실시, 결과 해석)으로 나뉜다. 평가 결과 보고서에는 비즈니스 동인, 주제별 등급과 격차, 강점·위험·투자 옵션, 개선 로드맵이 포함된다. 로드맵은 순차적 개선 활동, 구현 타임라인, 예상 DMMA 등급 향상, 감독 활동을 담아야 한다. 재평가는 정기적으로 수행하여 지속적 개선 사이클을 유지하며, 기준선 대비 추세를 추적한다. DAMA-DMBOK 자체를 평가 기준 수립이나 체크리스트로 활용할 수 있어 빠르게 격차와 개선 포인트를 식별할 수 있다. 거버넌스 측면에서 DMMA 프로세스 감독은 데이터 거버넌스 팀이 담당하고, DMMA 등급·자원 활용률·리스크 노출·지출 관리·변화 속도 등의 메트릭을 관리한다.

### Ch 15: Data Management Maturity Assessment (pp. 531-549)
**핵심**: 성숙도 평가 활동(계획, 평가 수행, 결과 해석, 개선 프로그램 수립, 재평가)을 설명한다. DMM 프레임워크 선택과 DAMA-DMBOK 프레임워크 활용 기법을 소개한다. 준비도 평가, 조직·문화 변화, 성숙도 관리 거버넌스와 메트릭을 다룬다.
**키워드**: `maturity-assessment`, `DMM-framework`, `readiness-assessment`, `continuous-improvement`
**상세**: → `DAMA-DMBOK_marker_full.md` Ch 15 (L:12451)
데이터 관리 조직 설계는 기존 조직·문화 규범을 이해하고 적합한 운영 모델을 선정하는 것에서 출발한다. 운영 모델은 분산형(비공식적, 라인별 정렬), 네트워크형(RACI 매트릭스 기반 책임 명확화), 중앙집중형(단일 DM 리더 아래 모든 기능 통합), 하이브리드형(중앙 CoE + 분산 비즈니스 유닛), 연합형(대규모 글로벌 기업용 다층 구조)의 다섯 가지로 구분된다. 조직에 적합한 모델 선정 시 현재의 의사결정 방식, 조직 계층, 부문 간 독립성 수준을 평가해야 한다. 10가지 핵심 성공 요인은 경영진 후원, 명확한 비전, 선제적 변화 관리, 리더십 정렬, 커뮤니케이션, 이해관계자 참여, 교육·훈련, 채택 측정, 지도 원칙 준수, 혁명이 아닌 진화이다. CDO(최고데이터책임자)는 비즈니스와 기술 간 간극을 연결하고 전사적 데이터 전략을 수립·추진하며, 데이터 거버넌스 오피스와 긴밀히 협력한다. 데이터 품질 관리는 종종 DMO의 출발점이 되며, 단일 비즈니스 라인에서 시작하여 전사적 CoE로 성장하는 경향이 있다. 데이터 아키텍트, 데이터 모델러, DBA, 데이터 보안 관리자, 데이터 통합 전문가, BI 아키텍트 등 IT 역할과 데이터 스튜어드 등 비즈니스 역할이 정의된다. 데이터 품질 분석가, 메타데이터 전문가 등 비즈니스와 기술 지식을 모두 요구하는 하이브리드 역할도 중요하다. 글로벌 조직은 국가별 법규, 분산 인력, 시간대·언어 차이에 특별히 주의해야 하며, 네트워크형 또는 연합형 모델이 적합하다.

### Ch 16: Data Management Organization and Role Expectations (pp. 551-571)
**핵심**: 기존 조직·문화 규범 파악, 분산형·네트워크형·중앙형·하이브리드·연합형 운영 모델을 비교하고 조직에 적합한 모델 선정 방법을 제시한다. 경영진 후원, 비전 명확화, 변화 관리, 이해관계자 참여 등 10가지 핵심 성공 요인과 조직·개인 수준의 데이터 관리 역할을 정리한다.
**키워드**: `DMO`, `operating-model`, `CDO`, `data-steward`, `organizational-roles`
**상세**: → `DAMA-DMBOK_marker_full.md` Ch 16 (L:12931)
데이터 관리와 조직 변화 관리는 데이터 관리 실무 개선을 위해 사람들의 협업 방식과 데이터 역할 인식을 변화시키는 구조적 접근이다. 변화의 다섯 가지 법칙에 따르면 조직이 아니라 사람이 변하고, 사람은 변화 자체가 아니라 변화를 강요당하는 것에 저항하며, 현상은 역사적 이유가 있고, 추진력 없이는 현상이 유지되며, 변화의 어려움은 결국 사람에게서 비롯된다. William Bridges는 전환(transition)을 종료(Ending)→중립 지대(Neutral Zone)→새로운 시작(New Beginning)의 세 단계로 정의하며, 종료 단계의 관리 실패가 변화 실패의 가장 큰 원인이라고 강조한다. Kotter의 8가지 변화 관리 오류는 안일함 방치, 불충분한 지도 연합, 비전의 힘 과소평가, 비전 소통 부족, 장애물 방치, 단기 승리 미창출, 조기 승리 선언, 기업 문화 정착 실패이다. Kotter의 8단계 주요 변화 프로세스는 긴급성 확립, 지도 연합 구성, 비전·전략 개발, 비전 소통, 임파워먼트, 단기 승리 창출, 성과 공고화, 문화 정착이다. Gleicher 공식(C = D × V × F > R)은 변화가 현 상태 불만족, 미래 비전, 실행 가능한 첫 단계의 곱이 저항을 초과할 때 발생한다고 설명한다. Everett Rogers의 혁신 확산 이론은 혁신자(2.5%)→초기 수용자(13.5%)→초기 다수(34%)→후기 다수(34%)→지체자(16%)의 채택 곡선을 제시한다. 변화 지속을 위해서는 긴급성을 유지하고 프로젝트 범위와 변화 비전을 구분하며, 지도 연합을 가장 직접적 이해관계자 너머로 확장해야 한다. 데이터 관리 가치 커뮤니케이션은 이해관계자 분석 기반의 맞춤형 메시지, 다양한 채널, 반복적 전달을 통해 조직 전체의 데이터 관리 인식과 행동 변화를 이끌어야 한다.

### Ch 17: Data Management and Organizational Change Management (pp. 573-581)
**핵심**: 변화의 법칙과 변화가 아닌 전환(transition)의 관리를 설명한다. Kotter의 변화 관리 8가지 오류(안일함, 불충분한 연합, 비전 과소소통, 장애물 방치, 단기 승리 실패, 조기 승리 선언, 기업 문화 정착 실패)를 분석한다. Kotter의 8단계 주요 변화 프로세스를 데이터 관리 맥락에 적용한다.
**키워드**: `change-management`, `Kotter`, `organizational-transition`, `cultural-change`
**상세**: → `DAMA-DMBOK_marker_full.md` Ch 17 (L:1459)
데이터 윤리는 데이터 처리의 의도된 결과와 실제 결과가 윤리적이며 신뢰를 침해하거나 인간 존엄성을 훼손하지 않도록 적절한 거버넌스와 통제를 수립하는 것을 다룬다. 생명윤리의 벨몬트 원칙(인격 존중, 선행, 정의)을 데이터 관리에 적용하여 개인 데이터의 자율성, 해악 최소화, 공정한 처우를 보장해야 한다. EU GDPR은 공정성·합법성·투명성, 목적 제한, 데이터 최소화, 정확성, 보관 제한, 무결성·기밀성, 책임성의 7대 원칙을 규정한다. 비윤리적 데이터 취급의 위험으로 타이밍 조작, 오도하는 시각화, 불명확한 정의나 무효한 비교, 편향(사전 결정된 결과를 위한 수집, 편향된 표본 방법론, 문화적 맥락), 데이터 변환·통합 시 출처 불명과 품질 미달, 난독화·삭제의 한계가 있다. 프라이버시 법의 기저 원칙은 OECD 공정 정보 처리 원칙에서 출발하며, 캐나다 PIPEDA와 미국 FTC 보고서가 각국의 접근 방식을 보여준다. 윤리적 데이터 문화 수립을 위해 현행 취급 관행 검토, 원칙·실무·위험 요인 식별, 윤리적 데이터 취급 전략·로드맵 수립, 사회적 책임을 고려한 윤리적 리스크 모델 채택이 필요하다. 데이터 과학과 BI 프로젝트에서는 연구 대상 모집단 선정, 데이터 수집 방식, 분석 초점, 결과 접근 방식 각 단계에서 윤리적 위험을 평가해야 한다. 대규모 데이터셋의 재결합(recombination) 위험으로 익명화된 데이터도 개인 식별이 가능해질 수 있어 강력한 거버넌스가 필수적이다. 데이터 거버넌스는 법률 자문과 함께 윤리적 데이터 취급의 감독 책임을 지며, DAMA International은 CDMP 인증을 통해 데이터 관리 전문가의 윤리 강령 준수를 요구한다.


### 기타 섹션 (Marker)

- DATA MANAGEMENT BODY OF KNOWLEDGE** SECOND EDITION `L:9`
- Dedicated to the memory of `L:15`
- Patricia Cupoli, MLS, MBA, CCP, CDMP `L:17`
- Federated User View Location A Location B Location C map map map `L:4195`
- Data Warehousing and Business Intelligence (p.384) `L:8596`
- Big Data and Data Science (p.500) `L:11215`
- Data Management Organization and Role Expectations (p.554) `L:12443`
- Data Management and Organizational Change Management (p.576) `L:12910`

---

## Marker 세부 목차

> `L:숫자`는 `DAMA-DMBOK_marker_full.md`의 라인 번호.

- DATA MANAGEMENT BODY OF KNOWLEDGE** SECOND EDITION `L:9`
- Dedicated to the memory of `L:15`
- Patricia Cupoli, MLS, MBA, CCP, CDMP `L:17`
- 1. Introduction `L:728`
- 2. Essential Concepts `L:763`
  - 2.2 Data and Information (p.23) `L:791`
- 2.3 Data as an Organizational Asset (p.23) `L:801`
- 2.4 Data Management Principles (p.24) `L:815`
- 2.5.1 Data Differs from Other Assets6 (p.26) `L:870`
- 2.5.3 Data Quality `L:906`
- 3. Data Management Frameworks `L:1069`
- 4. DAMA and the DMBOK `L:1223`
- 5. Works Cited / Recommended `L:1276`
- 2. Business Drivers `L:1459`
- 3. Essential Concepts `L:1469`
- 3.3 Online Data in an Ethical Context (p.59) `L:1576`
- 3.5 Establishing an Ethical Data Culture (p.63) `L:1660`
- 3.6 Data Ethics and Governance `L:1729`
- 4. Works Cited / Recommended `L:1735`
- 2. Activities `L:2147`
- 2.3 Perform Discovery and Business Alignment (p.83) `L:2168`
- 2.6 Define the DG Operating Framework `L:2202`
- 2.8 Underwrite Data Management Projects (p.87) `L:2234`
- 3. Tools and Techniques `L:2406`
- 3.4 Document Management Tools (p.96) `L:2436`
- 4. Implementation Guidelines `L:2444`
- 4.1 Organization and Culture (p.96) `L:2448`
- 5. Metrics `L:2465`
- 6. Works Cited / Recommended `L:2486`
- 1.2 Data Architecture Outcomes and Practices (p.103) `L:2614`
- 2.1 Establish Data Architecture Practice (p.113) `L:2805`
- 3. Tools `L:2890`
- 4. Techniques `L:2904`
- 4.1 Lifecycle Projections (p.119) `L:2906`
- 4.2 Diagramming Clarity `L:2921`
- 5. Implementation Guidelines `L:2933`
- 6. Data Architecture Governance `L:2979`
- 7. Works Cited / Recommended `L:3002`
- 1.3 Essential Concepts (p.129) `L:3109`
- 2.2 Build the Data Model (p.156) `L:3692`
- 2.3 Review the Data Models (p.161) `L:3801`
- 3.2 Lineage Tools (p.162) `L:3817`
- 4. Best Practices `L:3839`
- 4.1 Best Practices in Naming Conventions (p.164) `L:3841`
- 5. Data Model Governance `L:3864`
- Federated User View Location A Location B Location C map map map `L:4195`
- 2.1 Manage Database Technology (p.197) `L:4571`
- 2.2.3.5 Load Data `L:4746`
- 4.1 Test in Lower Environments (p.213) `L:4923`
- 5.2 Organization and Cultural Change (p.214) `L:4948`
- 6. Data Storage and Operations Governance `L:4969`
- 6.3 Data Audits and Data Validation (p.216) `L:5012`
- 3.1 Anti-Virus Software / Security Software (p.259) `L:5981`
- 3.3 Identity Management Technology (p.260) `L:5989`
- 3.7 Data Masking/Encryption (p.261) `L:6009`
- 4.1 CRUD Matrix Usage (p.261) `L:6017`
- 4.2 Immediate Security Patch Deployment (p.261) `L:6021`
- 4.4 Metrics (p.262) `L:6029`
- 5.4 Data Security in an Outsourced World (p.267) `L:6142`
- 5.5 Data Security in Cloud Environments (p.268) `L:6172`
- 6. Data Security Governance `L:6184`
- 1.1 Business Drivers (p.273) `L:6279`
- 2. Data Integration Activities `L:6571`
- 2.2 Design Data Integration Solutions (p.292) `L:6638`
- 3.1 Data Transformation Engine/ETL Tool (p.297) `L:6740`
- 3.4 Business Rules Engine (p.298) `L:6760`
- 3.6 Data Profiling Tool (p.298) `L:6768`
- 6. DII Governance `L:6806`
- 1.3.2.6 Taxonomies `L:7101`
- 1.3.7 Search Engine `L:7270`
- 1.3.10 Unstructured Data `L:7292`
- 2.2 Manage the Lifecycle (p.329) `L:7373`
- 3.3 Controlled Vocabulary and Metadata Tools (p.336) `L:7557`
- 3.5 E-discovery Technology `L:7622`
- 4.1 Litigation Response Playbook (p.339) `L:7628`
- 6. Documents and Content Governance `L:7707`
- 6.3 Govern for Quality Content (p.345) `L:7749`
  - 2.1.4 Model Master Data `L:8401`
  - 4.1 Adhere to Master Data Architecture (p.379) `L:8461`
- 4.3 Manage Reference Data Change `L:8476`
- 5. Organization and Cultural Change `L:8508`
- 6. Reference and Master Data Governance `L:8518`
- Data Warehousing and Business Intelligence (p.384) `L:8596`
- 1.3.2 Data Warehouse `L:8733`
- 2.4 Populate the Data Warehouse (p.400) `L:8975`
- 4.1 Prototypes to Drive Requirements (p.410) `L:9146`
- 4.3 Audit Data that can be Queried (p.411) `L:9162`
- 5.4 Organization and Cultural Change (p.413) `L:9197`
- 5.4.1 Dedicated Team `L:9209`
- 6. DW/BI Governance `L:9215`
- 6.5 Metrics (p.416) `L:9260`
- 4.2 Metadata for Big Data Ingest (p.446) `L:10022`
- 6. Metadata Governance `L:10056`
- 6.1 Process Controls (p.448) `L:10060`
- 2.1 Define High Quality Data (p.476) `L:10730`
- 2.3 Identify Critical Data and Business Rules (p.477) `L:10769`
- 2.6 Define Goals for Data Quality Improvement (p.480) `L:10813`
- 2.7.4 Establish Data Quality Service Level Agreements `L:10946`
- 3.1 Data Profiling Tools (p.488) `L:10984`
- 4.1 Preventive Actions (p.489) `L:11006`
- 6. Data Quality and Data Governance `L:11118`
- Big Data and Data Science (p.500) `L:11215`
- 1.3.15 Data Visualization91 (p.513) `L:11466`
- 2.2 Choose Data Sources `L:11497`
- 2.3 Acquire and Ingest Data Sources (p.516) `L:11519`
- 2.4 Develop Data Hypotheses and Methods (p.517) `L:11531`
- 2.5 Integrate / Align Data for Analysis (p.517) `L:11537`
- 4.1 Analytic Modeling (p.524) `L:11686`
- 6. Big Data and Data Science Governance `L:11768`
- 6.1 Visualization Channels Management `L:11780`
- 6.5 Data Quality (p.530) `L:11811`
- 1.3.1 Assessment Levels and Characteristics `L:12067`
- 0 1 2 3 4 5 Governance Architecture Modeling Storage & Ops Security D&C DII R&MD DW&BI Metadata DQ **DMM Assessment Chart** Desired rank Current Rank `L:12113`
- 1.3.3 Existing DMMA Frameworks98 (p.540) `L:12117`
- 1.3.3.2 EDM Council DCAM100 (p.541) `L:12136`
- 2.1.5 Plan Communications `L:12207`
- 4.2 DAMA-DMBOK Framework Use `L:12328`
- 5. Guidelines for a DMMA `L:12334`
- 6. Maturity Management Governance `L:12374`
- Data Management Organization and Role Expectations (p.554) `L:12443`
- 2. Understand Existing Organization and Cultural Norms (p.554) `L:12451`
- 3. Data Management Organizational Constructs `L:12482`
- 3.3 Centralized Operating Model (p.558) `L:12512`
- 3.4 Hybrid Operating Model (p.559) `L:12524`
- 3.7 DMO Alternatives and Design Considerations (p.561) `L:12558`
- 4. Critical Success Factors `L:12579`
- 4.2 Clear Vision (p.562) `L:12598`
- 4.10 Evolution Not Revolution (p.564) `L:12648`
- 5. Build the Data Management Organization `L:12652`
- 5.1 Identify Current Data Management Participants (p.565) `L:12654`
- 5.2 Identify Committee Participants (p.565) `L:12662`
- 6. Interactions Between the DMO and Other Data-oriented Bodies `L:12696`
- 6.5 Managing a Global Organization (p.570) `L:12767`
- 7. Data Management Roles `L:12783`
- 7.1 Organizational Roles (p.571) `L:12789`
- 7.2 Individual Roles (p.571) `L:12797`
- 8. Works Cited / Recommended `L:12842`
- Data Management and Organizational Change Management (p.576) `L:12910`
- 2. Laws of Change `L:12931`
- 3. Not Managing a Change: Managing a Transition `L:12945`
- 4. Kotter's Eight Errors of Change Management `L:13010`
- 4.1 Error #1: Allowing Too Much Complacency (p.580) `L:13014`
- 4.6 Error #6: Failing to Create Short-Term Wins (p.583) `L:13083`
- 4.7 Error #7: Declaring Victory Too Soon (p.584) `L:13095`
- 5. Kotter's Eight Stage Process for Major Change `L:13135`
- 5.3 Developing a Vision and Strategy (p.593) `L:13323`
  - 5.4.2 Keeping it Simple `L:13418`
- 5.4.4 Repetition, Repetition, Repetition `L:13434`
- 6. The Formula for Change `L:13483`
- 7. Diffusion of Innovations and Sustaining Change `L:13498`
- 8. Sustaining Change `L:13579`
- 8.1 Sense of Urgency / Dissatisfaction (p.607) `L:13587`
- 9. Communicating Data Management Value `L:13617`
- 10. Works Cited / Recommended `L:13730`
