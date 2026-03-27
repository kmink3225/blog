---
name: maintain-book
type: skill
description: >
  교재 소스(docs/book/) 유지보수. 새 교재 추가, 변환 품질 개선, 정기 점검 절차.
  사용자가 교재 관리를 요청할 때만 로드한다.
prerequisite: AGENT_GUIDE.md (공통 코어)
---

# Book Source 유지보수

교재 소스는 정적 자산이 아니라 지속적으로 관리해야 한다.

## 새 교재 추가 시

새 PDF 변환 파일(`_full.md`)이 `docs/book/`에 추가되면:
1. 해당 책의 `*-summary.md`를 생성한다 (YAML frontmatter + 챕터별 핵심/키워드/상세)
2. `sources:` 필드에 변환 파일 정보를 추가한다
3. Marker 변환본이 있으면 `## Marker 세부 목차` 섹션을 추가한다
4. 해당 카테고리의 `GUIDE.md`에 교재 레퍼런스를 추가한다

## 기존 교재의 변환 품질 개선 시

더 좋은 변환 도구로 재변환한 경우(예: Azure → Marker):
1. 새 `_full.md` 파일을 추가하고, summary의 `sources:`에 추가한다
2. 상세 요약의 라인 참조(`L:숫자`)를 새 파일 기준으로 업데이트한다
3. Marker 세부 목차를 추가/갱신한다

## 정기 점검

새 세션 시작 시 사용자가 요청하면, 다음을 확인한다:
- `_full.md`가 있지만 대응하는 `*-summary.md`가 없는 파일 (누락된 summary)
- `*-summary.md`의 `**상세**` 필드에 요약 텍스트가 없는 챕터 (미보강)
- `sources:` 필드가 누락된 summary
