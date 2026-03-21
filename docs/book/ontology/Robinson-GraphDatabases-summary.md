---
name: "Graph Databases: New Opportunities for Connected Data"
type: book-summary
source_file: "Robinson-GraphDatabases_full.md"
authors: "Ian Robinson, Jim Webber, Emil Eifrem"
year: 2015
total_pages: 220
language: en
keywords: [graph-database, Neo4j, Cypher, property-graph, data-modeling, connected-data, graph-theory, Dijkstra, social-network, recommendation]
---

# Graph Databases — Summary

> Ian Robinson, Jim Webber, Emil Eifrem (2015), 2nd Edition, ~220pp, 7 chapters + Appendix
> 그래프 데이터베이스의 개념·모델링·구축·실무 적용을 Neo4j 중심으로 다룬다

## Contents

- Ch 1: Introduction (pp. 1-10)
- Ch 2: Options for Storing Connected Data (pp. 11-24)
- Ch 3: Data Modeling with Graphs (pp. 25-64)
- Ch 4: Building a Graph Database Application (pp. 65-104)
- Ch 5: Graphs in the Real World (pp. 105-147)
- Ch 6: Graph Database Internals (pp. 149-170)
- Ch 7: Predictive Analysis with Graph Theory (pp. 171-190)
- Appendix A: NOSQL Overview (pp. 193-210)

---

## Chapter Summaries

### Ch 1: Introduction (pp. 1-10)
**핵심**: 그래프란 무엇인지 정의하고, 그래프 공간의 개요(graph databases vs graph compute engines)를 제시한다. 그래프 데이터베이스의 3가지 강점—성능(연결된 데이터 쿼리 시 일정 시간 탐색), 유연성(스키마 변경 용이), 민첩성(반복적 개발 지원)—을 설명한다.
**키워드**: `graph`, `graph-database`, `performance`, `flexibility`, `agility`
**상세**: → `Graph_Databases_OReilly_full.md` Ch 1 (line 78)

### Ch 2: Options for Storing Connected Data (pp. 11-24)
**핵심**: 관계형 데이터베이스와 NOSQL 데이터베이스가 연결된 데이터를 다루는 데 부적합한 이유를 분석한다. JOIN 폭발 문제, 비정규화의 한계를 보이고, 그래프 데이터베이스가 관계(relationships)를 일급 시민으로 다루는 방식의 우위를 설명한다.
**키워드**: `relational-limitations`, `NOSQL`, `JOIN-explosion`, `index-free-adjacency`
**상세**: → `Graph_Databases_OReilly_full.md` Ch 2 (line 91)

### Ch 3: Data Modeling with Graphs (pp. 25-64)
**핵심**: 레이블 속성 그래프 모델(labeled property graph)을 정의한다. Cypher 쿼리 언어의 철학과 기본 절(MATCH, RETURN, WHERE, CREATE)을 소개한다. 관계형 모델링과 그래프 모델링을 시스템 관리 도메인에서 비교한다. Shakespeare 그래프 사례, 이메일 출처 추적 모델링, 일반적 모델링 함정과 안티패턴을 다룬다.
**키워드**: `property-graph`, `Cypher`, `MATCH`, `data-modeling`, `anti-patterns`
**상세**: → `Graph_Databases_OReilly_full.md` Ch 3 (line 97)

### Ch 4: Building a Graph Database Application (pp. 65-104)
**핵심**: 데이터 모델링 원칙(노드는 사물, 관계는 구조), 세분화된 vs 일반적 관계, 팩트를 노드로 모델링, 시간 모델링을 다룬다. 애플리케이션 아키텍처(임베디드 vs 서버), 클러스터링, 부하 분산을 설명한다. 테스트 주도 개발, 성능 테스트, 용량 계획, 데이터 임포트/벌크 로딩을 다룬다.
**키워드**: `application-architecture`, `TDD`, `clustering`, `load-balancing`, `bulk-import`
**상세**: → `Graph_Databases_OReilly_full.md` Ch 4 (line 128)

### Ch 5: Graphs in the Real World (pp. 105-147)
**핵심**: 그래프 데이터베이스의 일반적 사용 사례(소셜, 추천, 지리, 마스터 데이터 관리, 네트워크 관리, 권한/접근 제어)를 소개한다. 전문 소셜 네트워크의 추천 시스템, 통신 분야 권한 관리, 물류 분야 지리공간 문제의 실제 구현 사례를 상세히 다룬다.
**키워드**: `social`, `recommendation`, `access-control`, `logistics`, `use-cases`
**상세**: → `Graph_Databases_OReilly_full.md` Ch 5 (line 161)

### Ch 6: Graph Database Internals (pp. 149-170)
**핵심**: 네이티브 그래프 처리(index-free adjacency)와 네이티브 그래프 스토리지의 내부 구조를 설명한다. 프로그래밍 API(Kernel API, Core API, Traversal Framework)와 비기능적 특성(트랜잭션, 복구 가능성, 가용성, 확장성)을 다룬다.
**키워드**: `native-graph-processing`, `native-storage`, `transactions`, `availability`, `scale`
**상세**: → `Graph_Databases_OReilly_full.md` Ch 6 (line 176)

### Ch 7: Predictive Analysis with Graph Theory (pp. 171-190)
**핵심**: 깊이/너비 우선 탐색, Dijkstra 알고리즘과 A* 알고리즘을 이용한 경로 탐색을 설명한다. 그래프 이론의 예측 모델링 활용: 삼자 폐합(triadic closures), 구조적 균형(structural balance), 지역 교량(local bridges)을 통한 관계 예측을 다룬다.
**키워드**: `Dijkstra`, `A-star`, `triadic-closure`, `structural-balance`, `path-finding`
**상세**: → `Graph_Databases_OReilly_full.md` Ch 7 (line 190)
